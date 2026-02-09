---
name: report-generator
description: 작업 결과에 대한 표준 보고 양식(Status, Self-Eval, Next Model) 생성
version: 1.0.0
author: Antigravity Core
usage: "User: 보고해 -> Agent: report-generator 실행"
---

# 📝 Report Generator (Standard Output)

이 스킬은 모든 작업의 끝맺음(Closing)을 담당합니다. 모호한 보고를 금지하고, 정량적/객관적 지표를 제시합니다.

## 📋 Report Structure (Mandatory)

### 1. Status (상태)
- ✅ Success / ⚠️ Warning / ❌ Failure
- 한 줄 요약 (예: "AdSense 태그 삽입 완료")

### 2. Self-Evaluation (자가 평가)
- **Score**: 0~100점
- **Breakdown**: 정확성, 효율성, 가독성, 심미성 등
- **Justification**: 왜 이 점수를 주었는가? (냉철한 자기 비판)

### 3. Next Model Recommendation (다음 모델 추천)
- **Tier**: SS(Oracle) | S(Deep) | A(Pro) | B(Flash)
- **Model**: 구체적 모델명 (예: Claude 3.5 Sonnet, Gemini 1.5 Pro)
- **Mode**: Planning (기획/생각) vs Fast (실행/속도)
- **Reason**: 왜 그 모델이 적합한가? (예: "다음은 창의적 작문이 필요하므로 Opus 추천")

## ⚠️ Notes
- 보고서는 개발자가 아닌 **'결정권자(User)'가 3초 만에 판단할 수 있도록** 작성할 것.
