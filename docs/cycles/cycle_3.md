## Cycle 3 – P2 (문서 자동화 & 협업 강화)

### 목표
- 문서 요약 결과를 반복 업무용 템플릿(회의록, 주간 보고 등)에 자동으로 채워 넣는 파이프라인을 설계하고 구현합니다.
- 검색/요약 결과를 작업 센터에서 공유·할당할 수 있도록 협업 흐름과 권한 체크를 확장합니다.
- 사용자 피드백(좋아요/수정 요청 등)을 수집해 순위 재학습 및 품질 지표로 활용할 준비를 마칩니다.

### 진행 현황
- [ ] 템플릿 정의/버전 관리를 위한 구조 설계 (`config/templates/`, `docs/specs/template_schema.md` 초안)
- [ ] 요약 엔진에서 템플릿 채우기 워크플로 구현 (`src/core/summarize/template_renderer.py`)
- [ ] 작업 센터 UX 확장(공유/할당 UI, 감사 로그) 및 API 설계 (`ui/` 전반, `docs/ux/work_center.md` 업데이트)
- [ ] 사용자 피드백 로깅 파이프라인과 분석 노트북 초안 (`data/feedback/`, `notebooks/feedback_insights.ipynb`)

### 산출물
- 템플릿 스키마 및 예시: `docs/specs/template_schema.md`, `config/templates/weekly_report.json`
- 템플릿 기반 요약 렌더러: `src/core/summarize/template_renderer.py`
- 협업 확장 API/UX 문서: `docs/ux/work_center.md`
- 피드백 로깅 스키마: `src/core/telemetry/feedback.py`, 결과 샘플 `data/feedback/sample.jsonl`

### 다음 단계 체크리스트
- Cycle 3 완료 후 템플릿/협업 플로 사용자 검증, Cycle 4(하이브리드/운영) 준비
- 주요 결정/리스크는 `docs/cycles/cycle_3.md`에 누적 기록
