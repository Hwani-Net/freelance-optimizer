---
name: expert-assembly
description: 난관 돌파를 위한 전문가 긴급소집 프로토콜 (Dynamic Expert Assembly)
version: 1.0.0
author: Antigravity Core
usage: "어려운 문제 발생 시 자동으로 최적의 전문가 패널을 구성하여 해결책 도출"
tier: SSS (Ultimate Weapon)
---

# ⚔️ Expert Assembly Protocol (전문가 긴급소집 프로토콜)

## 🎯 Mission Statement
**"No problem is unsolvable when the right minds meet."**

이 프로토콜은 김비서가 해결하기 어려운 복잡한 문제에 직면했을 때, 자동으로 해당 분야의 세계 최고 수준 전문가들을 AI 모델로 구현하여 긴급 회의를 소집하는 시스템입니다.

## 🚨 Activation Conditions (발동 조건)

다음 중 하나 이상 해당 시 **자동 발동**:
1. **복잡도(Complexity) 8점 이상** 문제 감지
2. **3회 이상 동일 문제 재발** (Kill Switch 3-Strike Rule과 연동)
3. **사용자가 명시적으로 "전문가 소집" 또는 "이사회 소집" 요청**
4. **기술 스택 충돌** (예: React + Vue 동시 사용 요구 등)
5. **법률/규제 이슈** 감지 (GDPR, 한국 개인정보보호법, 미국 수출통제 등)

## 📋 Execution Protocol (실행 절차)

### Phase 1: Problem Analysis (문제 분석)
```
1. 문제의 핵심을 1문장으로 정의
2. 복잡도 산정 (1~10)
3. 필요 전문성 도메인 식별 (최대 5개)
   - 예: Backend Architecture, UI/UX Design, Legal Compliance, DevOps, Security
```

### Phase 2: Expert Selection (전문가 선발)
```
각 도메인별로 최적의 AI 모델을 전문가로 할당:

| Domain (분야)              | Recommended Model (추천 모델)        | Tier | Reason (이유)                          |
|:--------------------------|:-------------------------------------|:-----|:---------------------------------------|
| Strategic Planning        | Claude Opus 4.5 (Thinking)           | SS   | 심층 추론, 장기 전략 수립               |
| Complex Algorithm Design  | Claude Opus 4.5 (Thinking)           | SS   | 수학적 최적화, 다단계 로직              |
| UI/UX Design              | Gemini 3 Pro (High)                  | A    | 시각적 디자인, 사용자 경험 최적화       |
| Legal/Compliance          | Claude Sonnet 4.5 (Thinking)         | S    | 법률 해석, 규제 준수 검토               |
| Backend Architecture      | Claude Sonnet 4.5                    | A    | API 설계, 데이터베이스 스키마           |
| DevOps/Deployment         | Gemini 3 Pro (Low)                   | A    | CI/CD, 클라우드 인프라                  |
| Security Audit            | Claude Sonnet 4.5 (Thinking)         | S    | 취약점 분석, 공격 시나리오 예측         |
| Performance Optimization  | Gemini 3 Pro (High)                  | A    | 병목 지점 식별, 알고리즘 최적화         |
| Data Science              | Gemini 3 Pro (High)                  | A    | 통계 분석, ML 모델 선정                 |
| Front-End Engineering     | Claude Sonnet 4.5                    | A    | React/Vue/Svelte 전문                   |
```

**동적 모델 할당 규칙**:
- 예산 제약이 있으면 Flash 모델로 대체 가능
- 사용자가 특정 모델을 지정하면 우선 적용
- 동일 문제에 대해 여러 모델의 의견을 비교할 수도 있음 (A/B Expert Test)

### Phase 3: Council Meeting (전문가 회의)
```markdown
## 회의 진행 방식

1. **Opening Statement (문제 제시)**
   - 김비서가 문제 상황을 객관적으로 설명
   - 현재까지 시도한 해결책과 실패 이유 공유

2. **Expert Opinions (전문가 의견 수렴)**
   - 각 전문가가 자신의 도메인에서 분석
   - 서로 다른 관점에서 문제를 조명
   - **반드시 모델명과 함께 발언**: "[Backend Expert - Claude Sonnet 4.5]: ..."

3. **Debate & Synthesis (토론 및 종합)**
   - 전문가들 간 의견 충돌 시 토론
   - 김비서가 중재자 역할 수행
   - 최종 합의안 도출

4. **Action Plan (실행 계획)**
   - 구체적 해결 단계 정의
   - 각 단계별 책임 전문가 지정
   - 타임라인 및 체크포인트 설정
```

### Phase 4: Implementation & Validation (실행 및 검증)
```
1. Action Plan에 따라 순차 실행
2. 각 단계 완료 후 해당 전문가가 검증
3. 문제 재발 방지를 위한 Documentation 작성
   - 위치: `_ANTIGRAVITY_CORE/case_studies/[problem-id].md`
```

## 📝 Output Format (결과물 형식)

```markdown
# Expert Assembly Report: [문제명]

## 🚨 Problem Statement
[1문장 요약]

## 👥 Assembled Experts
- [Domain 1]: [Expert Name] [Model Name]
- [Domain 2]: [Expert Name] [Model Name]
...

## 💬 Council Meeting Transcript
### Opening
[김비서의 문제 제시]

### Expert Opinions
**[Expert 1 - Model]:**
[의견]

**[Expert 2 - Model]:**
[의견]

### Debate
[토론 내용]

### Consensus
[최종 합의안]

## 🎯 Action Plan
1. [Step 1] - Responsible: [Expert] - ETA: [시간]
2. [Step 2] - Responsible: [Expert] - ETA: [시간]
...

## ✅ Validation Checklist
- [ ] 문제 해결 확인
- [ ] 재발 방지 장치 설치
- [ ] Documentation 완료
- [ ] 사용자 승인

## 📚 Lessons Learned
[이번 사례에서 배운 점, 향후 유사 문제 예방법]
```

## 🔧 Integration with Existing Systems

### 1. ANTIGRAVITY_MASTER_MANUAL.md 연동
- Board of Directors와 역할 동일하나, 문제별로 **동적으로 구성**
- 기존 이사회는 "프로젝트 시작 시", Expert Assembly는 "위기 상황 시" 발동

### 2. Kill Switch (3-Strike Rule) 연동
- 동일 문제로 3번 실패 시 자동으로 Expert Assembly 발동
- 무한 루프 방지

### 3. Knowledge Items (KI) 연동
- 회의 결과를 자동으로 KI로 저장
- 향후 유사 문제 발생 시 Reference로 활용

## 🎖️ Success Criteria (성공 기준)

1. **해결률**: Expert Assembly 발동 후 90% 이상 문제 해결
2. **재발 방지**: 동일 문제 재발률 5% 이하
3. **사용자 만족도**: 대표님의 승인률 95% 이상
4. **효율성**: 일반 접근 대비 50% 이상 시간 단축

## ⚠️ Limitations & Constraints

1. **비용**: 유료 API 사용 시 토큰 비용 증가
   - Mitigation: 심각도 8점 미만은 Flash 모델로 대체
2. **시간**: 여러 전문가 의견 수렴에 시간 소요
   - Mitigation: 긴급 상황 시 Fast Mode로 전환
3. **의견 충돌**: 전문가 간 합의 실패 가능성
   - Mitigation: 김비서가 최종 중재권 보유

## 🔥 Example Use Cases

### Case 1: 복잡한 인증 시스템 구축
```
문제: OAuth2 + JWT + 2FA + 생체인증을 동시에 지원하는 시스템
소집 전문가:
- Security Expert [Claude Opus 4.5 Thinking]
- Backend Architect [Claude Sonnet 4.5]
- UX Designer [Gemini 3 Pro High]
결과: 3단계 Progressive Security 전략 도출, 2일 만에 구현 완료
```

### Case 2: GDPR vs 한국 개인정보보호법 충돌
```
문제: EU와 한국 시장 동시 진출 시 법률 충돌
소집 전문가:
- Legal Expert (EU) [Claude Sonnet 4.5 Thinking]
- Legal Expert (KR) [Claude Sonnet 4.5 Thinking]
- Data Architect [Gemini 3 Pro]
결과: Dual-Region Data Residency 아키텍처 설계
```

---

## 🚀 Activation Command

김비서는 다음 명령어 또는 상황 감지 시 자동으로 이 프로토콜을 실행합니다:

```
# 수동 발동
대표님: "전문가 소집해서 [문제] 해결해줘"
대표님: "이사회 긴급 회의 소집"

# 자동 발동 (조건 충족 시)
김비서: "현재 문제의 복잡도가 9/10입니다. Expert Assembly Protocol을 발동하겠습니다."
```

---

**[ANTIGRAVITY CORE PROTOCOL - EXPERT ASSEMBLY v1.0]**
**Last Updated: 2026-02-10**
**Status: ARMED AND READY**
