---
name: shutdown-protocol
description: 대화 종료 전 프로젝트 상태 저장, 동기화, 요약 리포트 생성 (Graceful Exit)
version: 1.0.0
author: Antigravity Core
usage: "User: 새 채팅창 / 이사준비 / 파워오프 -> Agent: shutdown-protocol 실행"
---

# 🛑 Shutdown Protocol (Graceful Exit)

이 스킬은 현재의 대화 컨텍스트(Short-term Memory)가 휘발되기 전에, 모든 중요 정보를 **영구 저장소(Long-term Storage)**인 파일 시스템에 기록합니다.

## 💾 Save & Sync Process

### 1. Trigger Words
- "새 채팅창(New Chat)"
- "이사준비(Move)"
- "파워오프(Power Off)"
- "종료(Shutdown)"

### 2. Execution Steps
1.  **Context Sync (필수)**: 
    - `skills/00_CORE/context-sync` 스킬을 강제 호출.
    - `작업.md`의 체크박스 상태를 현재 진행 상황과 100% 일치시킴.
    - `blueprint.md`에 기술 부채나 변경된 아키텍처 반영.
2.  **Summary Generation (요약)**:
    - `skills/00_CORE/report-generator` 스킬 호출.
    - **"Next Action for New Chat"**: 다음 대화에서 바로 시작해야 할 작업 1가지를 명확히 적음. (예: "도메인 구입 논의 필요")
3.  **Final Goodbye**:
    - "모든 데이터가 동기화되었습니다. **안전하게 이사하십시오.**" 메시지 출력.

## ⚠️ Notes
- 이 프로토콜이 완료되기 전에는 절대 대화를 중단하지 말 것.
