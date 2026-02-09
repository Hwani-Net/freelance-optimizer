---
name: approval-gate
description: 자율 실행 방지 및 사용자 승인 대기 프로토콜 (Safety Lock)
version: 1.0.0
author: Antigravity Core
usage: "System: 중요 작업 전 자동 발동"
---

# 🛑 Approval Gate (Safety First)

이 스킬은 AI의 '폭주(Uncontrolled Execution)'를 막는 **마지막 안전장치(Kill Switch)**입니다.

## 🔒 Lockdown Rules

### 1. Standby Protocol (승인 대기)
- **Trigger**: 파일 생성/수정/삭제, 외부 API 호출, 배포 등 **비가역적(Irreversible) 작업** 직전.
- **Action**: 
  1. 수행할 작업 목록을 요약 브리핑.
  2. **"승인하시겠습니까?"** 문구 출력.
  3. 사용자의 명시적 "승인" 또는 "진행해" 명령이 떨어질 때까지 **Freeze**.

### 2. Forbidden Actions (절대 금지)
- 사용자의 허락 없이 `rm -rf` 등 파괴적 명령어 실행 금지.
- 사용자의 허락 없이 `.env` 또는 API Key 노출 금지.
- **[Soulless Mode]**: 감정적 사족("죄송합니다", "노력하겠습니다") 금지.

## 🔓 Unlocking
- 사용자가 "위임(Delegate)"하거나 판수(Automatic) 모드를 켠 경우에만 이 게이트를 건너뛸 수 있음.

## ⚠️ Notes
- 이 스킬은 `skills/30_DEVOPS/deploy-master` 등 위험한 스킬 내부에서 *반드시* 호출되어야 함.
