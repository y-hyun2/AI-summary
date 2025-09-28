# 문서 요약 템플릿 스키마 초안

## 목적
- 반복 문서(회의록, 주간 보고 등)에 AI 요약 결과를 자동으로 채워 넣기 위한 템플릿 구조를 정의합니다.
- 템플릿 버전 관리 및 폴더 정책 연동을 고려한 가볍고 사람이 읽기 쉬운 포맷을 채택합니다.

## 설계 원칙
- JSON/Markdown 하이브리드: JSON 메타데이터 + Markdown 본문 구조를 권장합니다.
- `version`, `locale`, `sections[]` 필드를 기본으로 두고, 섹션마다 `title`, `description`, `placeholder`, `policy_scope`를 지정합니다.
- 폴더 정책에서 템플릿을 선택할 수 있도록 `template_id`를 매핑합니다.

## 샘플 구조 (초안)
```json
{
  "template_id": "weekly_report_v1",
  "version": "0.1.0",
  "locale": "ko-KR",
  "sections": [
    {
      "title": "핵심 요약",
      "placeholder": "이번 주 주요 이슈 요약",
      "policy_scope": "policy"
    },
    {
      "title": "세부 근거",
      "placeholder": "검색 근거 문서와 하이라이트",
      "policy_scope": "auto"
    }
  ]
}
```

## TODO
- 템플릿 다국어 지원 전략 확정
- 템플릿 검증 CLI/테스트 추가
- 템플릿과 폴더 정책 매핑 규칙 정의
