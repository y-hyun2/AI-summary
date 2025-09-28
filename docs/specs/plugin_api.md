# 플러그인/에이전트 API 가이드 초안

## 목적
- 지식·검색 코어에 신규 에이전트나 파이프라인을 추가할 때 필요한 최소 인터페이스를 정의합니다.
- 코어 업데이트 시 플러그인 호환성을 유지하기 위한 버전 교차 전략을 제공합니다.

## 핵심 컴포넌트
- `AgentDescriptor`: 메타데이터(`id`, `capabilities`, `required_scopes`) 선언
- `AgentLifecycle`: `load(context)`, `handle(request)`, `shutdown()` 메서드 계약
- `PolicyAdapter`: 스마트 폴더 정책과 연계하기 위한 허용 스코프 질의 API

## 디렉터리 구조 제안
```
src/plugins/
  README.md
  knowledge_search/
    __init__.py
    descriptor.py
    pipeline.py
```

## 버저닝 전략
- `PLUGIN_API_VERSION` 상수를 `src/plugins/__init__.py`에 선언
- 메이저 변경 시 마이그레이션 가이드 제공 (`scripts/migrate_plugins.py`)

## TODO
- 샌드박스 실행 환경 정의
- 예제 플러그인(문서 요약 확장) 작성
- 자동 검증 테스트 케이스 추가 (`tests/plugins/`)
