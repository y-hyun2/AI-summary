# 감사 로그 스키마 초안

## 목표
- 하이브리드/운영 환경에서 검색 및 요약 작업의 감사 추적을 가능하게 하는 공통 스키마를 정의합니다.
- 개인정보 및 민감 정보 유출을 방지하기 위해 최소 수집 원칙을 준수합니다.

## 필드 제안
- `event_id` (UUID)
- `timestamp` (ISO8601)
- `actor` (user id / service id)
- `action` (scan, train, chat, export 등)
- `resource` (폴더/문서 경로 해시 또는 정책 id)
- `policy_scope` (local_only, hybrid 등)
- `result` (success, denied, error)
- `metadata` (선택: 에러 메시지, 요약 길이 등)

## 보존 및 접근 제어
- 기본 보존 기간 180일, 정책에 따라 조정 가능
- 민감 폴더 이벤트는 별도 암호화 저장소에 보관
- 감사 로그는 읽기 전용 권한을 가진 운영자만 접근

## TODO
- 암호화/서명 전략 확정
- 감사 로그 뷰어 CLI/대시보드 요구사항 정의
- `data/audit/` 저장 경로 구조화 및 회전 정책 문서화
