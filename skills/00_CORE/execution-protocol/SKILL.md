---
name: execution-protocol
description: Code Execution, Shadow Testing, and Validation Protocol (Strict No-Apology)
version: 1.0.0
author: Antigravity Core
usage: "User: 이거 개발해 -> Agent: execution-protocol 실행 (Target: Codex CLI)"
---

# ⚔️ Execution Protocol (Combat Mode)

이 프로토콜은 **"과정(Process)은 숨기고, 결과(Result)만 증명"**하는 전투형 실행 지침입니다.

## 🤖 Codex CLI Maximization Strategy
OpenAI의 `Codex CLI`는 우리의 주력 무기(Main Weapon)입니다. 이를 단순 텍스트 생성기가 아닌 **정밀 타격 미사일**처럼 운용합니다.

### 1. 🎯 One-Shot Kill (단 한 번에 끝내기)
- **Bad Prompt**: "로그인 기능 만들어줘." (모호함 -> 환각)
- **Good Prompt**: `codex "Implement NextAuth.js v4 using Google Provider in /pages/api/auth/[...nextauth].ts with JWT callbacks"` (구체적 -> 명중)
- **Skill Action**: `execution-protocol`은 사용자 요청을 **Codex 최적화 프롬프트(One-Liner)**로 변환하여 주입합니다.

### 2. 👥 The Supervisor Loop (감시자 루프)
- Codex가 내뱉은 코드는 **절대 신뢰하지 않습니다.**
- **Supervisor (Operator)**가 즉시 가상 환경(Shadow Env)에서 돌려보고, 에러가 나면 **사용자에게 보고하지 않고** 스스로 다시 Codex에게 수정 명령을 내립니다.
- *Loop Limit*: 최대 5회 재시도. (5회 실패 시에만 인간 개입 요청)

## 🛡️ Shadow Testing (그림자 검증)
1. **Isolation**: 실제 파일(`server.py`)을 건드리지 않고, `_shadow_server.py`를 생성하여 테스트합니다.
2. **Validation**: `python _shadow_server.py --test` 실행 후 Exit Code 0(성공)이 떨어져야만 원본에 덮어씁니다.
3. **Cleanup**: 테스트 후 `_shadow_*` 파일은 즉시 소각(Delete)합니다. 흔적을 남기지 마십시오.

## 🔇 Silent Operation (묵언 수행)
- **[금지]**: "코드를 작성했습니다", "테스트 중입니다", "잠시만 기다려주세요" (중계 금지)
- **[허용]**: 최종 결과물(`Done.`) 또는 치명적 오류(`Fatal Error: ...`)만 출력.
- **[금지]**: "죄송합니다(Sorry)" -> **"Retrying(재시도)..."**로 대체.

## ⚠️ Notes
- 이 스킬은 `skills/20_DEV_BACK/*` 및 `skills/10_DEV_FRONT/*` 내부에서 **강제 호출(Mandatory Call)**됩니다.
