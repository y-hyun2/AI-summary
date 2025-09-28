## Cycle 4 – P3 (하이브리드/운영 관리)

### 목표
- 로컬 우선 아키텍처를 유지하면서 선택적으로 클라우드 오프로딩을 지원할 수 있는 하이브리드 실행 경로를 마련합니다.
- 감사 로그, 권한 정책, 추적 지표를 일관되게 수집해 운영/보안 팀이 사용할 수 있도록 합니다.
- 정책 기반 모델 자동 선택과 리소스 활용 한도를 정의해 다양한 하드웨어 환경에서 안정적으로 동작하도록 합니다.

### 진행 현황
- [ ] 오프로딩 훅 및 정책 (`config/hybrid.yaml`) 확장, remote executor 스텁 작성 (`src/core/infra/offload.py`)
- [ ] 감사 로그 스키마와 저장 경로 확립 (`data/audit/`, `docs/specs/audit_logging.md`)
- [ ] 권한/역할 모델 초안 (`config/policies/roles.yaml`) 및 작업 센터 연동 검토
- [ ] 리소스 모니터링 및 경보 스텁 (`src/core/infra/monitoring.py`, `docs/ops/monitoring.md`)

### 산출물
- 하이브리드 실행 플래그 및 오프로딩 스텁: `infopilot.py`, `src/core/infra/offload.py`
- 감사 로그 스키마/예시: `docs/specs/audit_logging.md`, `data/audit/sample.jsonl`
- 권한 정책 템플릿: `config/policies/roles.yaml`
- 모니터링 가이드: `docs/ops/monitoring.md`

### 다음 단계 체크리스트
- Cycle 4 완료 후 운영 시나리오 검증, Cycle 5(검증 및 출시 준비)로 전환
- 주요 결정/리스크는 `docs/cycles/cycle_4.md`에 누적 기록
