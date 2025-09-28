## Cycle 5 – P4 (검증 및 출시 준비)

### 목표
- KPI 자동화와 대용량/PII 회귀 테스트를 정비해 안정적인 릴리스 기준을 마련합니다.
- 설치 마법사, 작업 센터, CLI 가이드를 다듬어 실제 배포 환경에서도 일관된 UX를 제공합니다.
- 릴리스 체크리스트와 배포 스크립트를 최신화해 운영팀 핸드오프를 준비합니다.

### 진행 현황
- [ ] KPI 스냅샷 및 리포트 자동화 (`scripts/release_prepare.py`, `artifacts/kpi_summary.md`)
- [ ] 대용량/PII 회귀 테스트 확장 (`tests/regression/`, `tests/test_pii_scrubber.py` 강화)
- [ ] 설치 마법사 & 작업 센터 폴리싱 (`ui/`, `docs/ux/improvements.md` 업데이트)
- [ ] 릴리스 체크리스트/가이드 개정 (`docs/release_checklist.md`, `docs/release_notes_draft.md`)

### 산출물
- 자동화된 KPI 리포트 산출물: `artifacts/kpi.json`, `artifacts/kpi_summary.md`
- 확장된 회귀 테스트와 테스트 결과 요약: `tests/regression/`, `docs/cycles/cycle_5.md`
- 최신 릴리스 체크리스트 및 사용자 가이드: `docs/release_checklist.md`, `README.md`

### 다음 단계 체크리스트
- Cycle 5 완료 후 출시 후보 빌드 검증, Cycle 6(지속 확장 준비)로 전환
- 결정 사항/리스크는 `docs/cycles/cycle_5.md`에 누적 기록
