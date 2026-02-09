---
name: context-sync
description: blueprint.md, 작업.md, task.md 등 프로젝트 상태(Context) 동기화 및 유지
version: 1.0.0
author: Antigravity Core
usage: "User: 작업 어디까지 했지? -> Agent: context-sync 실행"
---

# 🧱 Context Sync (The Memory)

이 스킬은 에이전트의 단기 기억(Short-term Memory) 한계를 극복하고, 프로젝트의 영속성(Persistence)을 보장합니다.

## 🛠 Features

### 1. Resume Protocol (이어하기)
- 대화 시작 시 `blueprint.md`와 `작업.md`를 **가장 먼저 스캔**.
- "지난번에 A를 하다가 멈췄군요. B부터 하면 됩니까?"라고 먼저 제안.

### 2. Blueprint Update (설계도 갱신)
- 주요 아키텍처 변경(예: 테마 교체, DB 변경) 발생 시, `blueprint.md`를 즉시 수정.
- *Rule*: "코드는 바뀌었는데 설계도는 그대로"인 상황을 절대 만들지 말 것.

### 3. Task Management (작업 관리)
- `작업.md`의 체크박스(`- [ ]`) 상태를 실시간 동기화.
- 완료된 작업은 `- [x]` 처리하고, 타임스탬프 또는 커밋 ID 기록.

## ⚠️ Notes
- 이 스킬은 '수동'이 아니라, **모든 주요 작업(Task) 완료 후 자동으로 트리거(Auto-trigger)** 되어야 함.
