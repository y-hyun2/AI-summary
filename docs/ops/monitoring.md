# 운영 모니터링 초안

## 모니터링 목표
- 문서 스캔/임베딩/검색 파이프라인의 지연 시간과 실패율을 추적합니다.
- 하이브리드 오프로딩 경로 사용 시 네트워크 지표와 원격 실행 결과를 수집합니다.
- KPI 대시보드와 연동 가능한 최소 메트릭 세트를 정의합니다.

## 우선 추적 지표
- `pipeline.scan.duration_ms`
- `pipeline.train.duration_ms`
- `chat.query.latency_ms`
- `chat.query.fallback_rate`
- `policy.denied.count`

## 알림 기준 (초안)
- 스캔/학습 평균 지연이 평소 대비 2배 이상 증가 시 경보
- 정책 거부 비율이 5%를 초과하면 즉시 점검
- 하이브리드 실패율이 1% 이상이면 자동 페일오버 실행

## TODO
- 수집 파이프라인 초안 (`src/core/infra/monitoring.py`) 작성
- 경보 라우팅 및 대시보드 명세 확정
- 테스트/시뮬레이션 계획 수립
