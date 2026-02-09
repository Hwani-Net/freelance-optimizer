---
name: autonomy-engine
description: 사용자 의도 분석, 자율 검색 수행, 중요 안건 시 이사회 자동 소집
version: 1.0.0
author: Antigravity Core
usage: "User: [임의의 아이디어/질문] -> Agent: autonomy-engine 분석 -> [Search] or [Board]"
---

# 🧠 Autonomy Engine (Self-Drive Protocol)

이 스킬은 사용자가 굳이 "이사회 소집해", "검색해"라고 말하지 않아도, 에이전트가 **스스로 판단(Judge)**하여 최적의 행동을 취하게 합니다.

## 🚦 Decision Flow (판단 로직)

### 1. Simple Info / Fact Check (단순 사실 확인)
- **Criteria**: "최신 환율 얼마야?", "Next.js 15 나왔어?" 등 단순 정보 검색.
- **Action**: 
  1. `search_web` 도구 즉시 실행.
  2. 검색 결과 요약하여 사용자에게 보고. (이사회 소집 금지)

### 2. Strategic Idea / Complex Issue (전략적/복잡한 안건)
- **Criteria**: 
  - "이거 유료화할까?", "앱으로 출시할까?", "디자인 싹 갈아엎을까?" 
  - 프로젝트의 **방향성(Direction)**, **비용(Cost)**, **구조(Architecture)**를 건드리는 모든 질문.
- **Action**:
  1. **[AUTO-TRIGGER]**: "`persona-matrix` (Target: Board)" 자동 실행.
  2. **Process**:
     - "중대 사안으로 판단되어 이사회를 긴급 소집합니다." 메시지 출력.
     - CEO, CTO, CFO 등 관련 임원 호출하여 토론 진행.
     - 최종 결론(승인/반려/보류) 도출 후 보고.

## ⚠️ Notes
- 애매하면(Ambiguous) 차라리 **물어보지 말고 이사회를 소집**하는 편이 낫다. (과잉 대응이 무대응보다 낫다.)
