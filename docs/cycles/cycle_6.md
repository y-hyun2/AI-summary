## Cycle 6 – 지속 확장 준비

### 목표
- 플러그인/에이전트 개발을 위한 공용 API와 샌드박스 템플릿을 정리해 신규 기능을 안전하게 온보딩할 수 있도록 합니다.
- 정책/데이터 스키마 버저닝 전략을 수립해 장기 유지보수 시 스키마 변경을 유연하게 관리합니다.
- 우선순위 백로그를 정리하고 향후 사이클 후보(예: 외부 지식베이스 연결, 자동 시맨틱 태깅 등)를 정의합니다.

### 진행 현황
- [ ] 플러그인 가이드 및 샌드박스 템플릿 (`docs/specs/plugin_api.md`, `src/plugins/README.md`)
- [ ] 정책/데이터 스키마 버저닝 전략 문서화 (`docs/specs/schema_versioning.md`)
- [ ] 확장 백로그 및 의사결정 기록 (`docs/backlog/expansion.md`)

### 산출물
- 플러그인 API 가이드와 샌드박스 템플릿: `docs/specs/plugin_api.md`, `src/plugins/README.md`
- 스키마 버저닝 전략 및 마이그레이션 샘플: `docs/specs/schema_versioning.md`, `scripts/migrate_schemas.py`
- 확장 백로그와 의사결정 로그: `docs/backlog/expansion.md`

### 다음 단계 체크리스트
- Cycle 6 완료 후 신규 기능 개별 기획(외부 커넥터, 멀티모달 등)으로 분기
- 주요 결정/리스크는 `docs/cycles/cycle_6.md`에 누적 기록
