"""Policy engine for smart folder configurations."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

from .loader import load_policy_file
from src.core.utils import get_logger, resolve_repo_root

LOGGER = get_logger("policy.engine")


def _normalize_path(path: Path) -> Path:
    """사용자 홈(~)과 상대 경로 등을 정규화해 정책 비교에 쓰기 좋게 만든다."""
    path = path.expanduser()
    try:
        return path.resolve(strict=False)
    except TypeError:  # Python 3.9 미만에서 strict 인자가 지원되지 않는다
        try:
            return path.resolve()
        except OSError:
            return path
    except OSError:
        return path


# 스마트 폴더 정책 한 건을 보관하는 데이터 클래스
@dataclass(frozen=True)
class SmartFolderPolicy:
    # 이 정책이 적용될 루트 폴더
    path: Path
    # 폴더에서 동작을 허용할 에이전트 집합 (예: knowledge_search)
    agents: frozenset[str]
    # 처리 모드, PII 필터 등 보안 관련 설정
    security: Dict[str, object]
    # 인덱싱 주기 및 스케줄러 힌트
    indexing: Dict[str, object]
    # 요약/캐시 보존 기간 등 저장 관련 정책
    retention: Dict[str, object]

    @classmethod
    def from_dict(cls, data: Dict[str, object], *, base: Path) -> "SmartFolderPolicy":
        """JSON 딕셔너리 형태의 정책 정의를 SmartFolderPolicy 인스턴스로 변환한다."""
        if "path" not in data or not data.get("path"):
            raise ValueError("Smart folder policy requires a 'path' key")
        raw_path = Path(str(data.get("path")))
        if not raw_path.is_absolute():
            raw_path = base / raw_path
        normalized_path = _normalize_path(raw_path)
        # 리스트/딕셔너리를 복사해 후속 코드가 안전하게 사용할 수 있도록 한다
        agents = frozenset(str(item) for item in data.get("agents", []) or [])
        security = dict(data.get("security", {}) or {})
        indexing = dict(data.get("indexing", {}) or {})
        retention = dict(data.get("retention", {}) or {})
        # 필드들을 dataclass 생성자에 전달해 불변 객체로 반환한다
        return cls(
            path=normalized_path,
            agents=agents,
            security=security,
            indexing=indexing,
            retention=retention,
        )

    @property
    def indexing_mode(self) -> str:
        """인덱싱 모드를 소문자로 정규화하고, 알 수 없는 값은 realtime으로 처리한다."""
        mode = str(self.indexing.get("mode", "realtime") or "realtime").lower()
        if mode not in {"realtime", "scheduled", "manual"}:
            return "realtime"
        return mode

    def allows_agent(self, agent: str) -> bool:
        """특정 에이전트가 이 폴더에서 동작 가능한지 확인한다."""
        if not self.agents:
            return True
        return agent in self.agents


# 여러 스마트 폴더 정책을 관리하고 조회하는 엔진
class PolicyEngine:
    def __init__(self, policies: Sequence[SmartFolderPolicy], *, source: Optional[Path] = None) -> None:
        """정책 목록을 받아 우선순위 정렬 후 엔진 인스턴스를 초기화한다."""
        # 경로 길이가 긴(보다 구체적인) 정책부터 검사하도록 정렬한다
        self._policies = sorted(policies, key=lambda p: len(p.path.parts), reverse=True)
        self.source = source

    @classmethod
    def empty(cls) -> "PolicyEngine":
        """정책이 전혀 없는 빈 엔진을 생성한다."""
        return cls((), source=None)

    @classmethod
    def from_file(cls, path: Path) -> "PolicyEngine":
        """정책 파일을 로드해 엔진을 생성한다."""
        repo_root = resolve_repo_root()
        if not path.is_absolute():
            path = (repo_root / path).resolve()
        if not path.exists():
            LOGGER.info("Policy file not found at %s; continuing without policies", path)
            return cls.empty()
        raw_policies = load_policy_file(path)
        policies = [SmartFolderPolicy.from_dict(entry, base=path.parent) for entry in raw_policies]
        LOGGER.info("Loaded %d smart folder policies from %s", len(policies), path)
        return cls(policies, source=path)

    def __len__(self) -> int:
        """등록된 정책 수를 반환한다."""
        return len(self._policies)

    @property
    def has_policies(self) -> bool:
        """정책 존재 여부를 True/False로 알려준다."""
        return bool(self._policies)

    def roots_for_agent(self, agent: str, *, include_manual: bool = True) -> List[Path]:
        """해당 에이전트가 처리할 수 있는 폴더 루트 목록을 반환한다."""
        if not self._policies:
            return []
        roots: List[Path] = []
        for policy in self._policies:
            # 각 정책이 요청한 에이전트를 허용하는지 확인한다
            if not policy.allows_agent(agent):
                continue
            if not include_manual and policy.indexing_mode == "manual":
                continue
            roots.append(policy.path)
        # 순서를 유지한 채 중복 폴더를 제거한다
        seen = set()
        unique: List[Path] = []
        for root in roots:
            key = str(root)
            if key in seen:
                continue
            seen.add(key)
            unique.append(root)
        return unique

    def iter_policies(self) -> Sequence[SmartFolderPolicy]:
        """현재 보유 중인 정책을 튜플 형태로 반환한다."""
        return tuple(self._policies)

    def policy_for_path(self, path: Path) -> Optional[SmartFolderPolicy]:
        """지정된 경로에 가장 구체적으로 매칭되는 정책을 찾는다."""
        if not self._policies:
            return None
        normalized = _normalize_path(path)
        for policy in self._policies:
            try:
                normalized.relative_to(policy.path)
                return policy
            except ValueError:
                continue
        return None

    def allows(self, path: Path, *, agent: str, include_manual: bool = True) -> bool:
        """현재 정책에서 특정 경로를 해당 에이전트가 처리할 수 있는지 검사한다."""
        if not self._policies:
            return True
        policy = self.policy_for_path(path)
        if policy is None:
            return False
        if not policy.allows_agent(agent):
            return False
        if not include_manual and policy.indexing_mode == "manual":
            return False
        return True

    def filter_records(
        self,
        records: Iterable[Dict[str, object]],
        *,
        agent: str,
        include_manual: bool = True,
    ) -> List[Dict[str, object]]:
        """스캔 결과 중 정책에 허용된 경로만 남긴다."""
        if not self._policies:
            return list(records)
        filtered: List[Dict[str, object]] = []
        for record in records:
            # 스캔 결과가 딕셔너리 형태라고 가정하고 경로를 추출한다
            path_str = record.get("path") if isinstance(record, dict) else None
            if not path_str:
                continue
            # 허용된 경로라면 결과 목록에 포함시킨다
            if self.allows(Path(str(path_str)), agent=agent, include_manual=include_manual):
                filtered.append(record)
        return filtered
