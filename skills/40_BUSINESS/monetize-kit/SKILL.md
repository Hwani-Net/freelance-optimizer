---
name: monetize-kit
description: Google AdSense 승인 및 수익화를 위한 필수 법적 문서(Privacy, Terms)와 태그 자동 생성 키트
version: 1.0.0
author: Antigravity Core
usage: "User: 수익화 준비해줘 -> Agent: monetize-kit 실행"
---

# 💰 Monetize Kit (AdSense & Compliance)

이 스킬은 웹사이트의 수익화 승인(Google AdSense) 확률을 높이고, 필수 법적 준수 사항을 자동으로 해결합니다.

## 🛠 Features
1. **Legal Docs Generator**: `privacy.html`, `terms.html`가 없으면 표준 양식(Standard Template)으로 자동 생성.
2. **AdSense Tagger**: `index.html` <head>에 AdSense 승인 코드(`ca-pub-XXX`) 자동 삽입.
3. **Ads.txt Manager**: 루트 디렉토리에 `ads.txt` 생성 및 검증.

## 📋 Execution Steps

### Step 1: Legal Documents Check
1. 프로젝트 루트에 `privacy.html`과 `terms.html`이 있는지 확인.
2. 없다면, `templates/privacy_template.html` 내용을 복사하여 생성.
   - **Template**: "이 약관은 [서비스명]의 서비스 이용에..." (표준 약관 사용)
3. `index.html` Footer 영역에 "개인정보처리방침 | 이용약관" 링크가 있는지 확인하고 없으면 추가.

### Step 2: AdSense Verification
1. 사용자에게 `Publisher ID` (예: `pub-1234567890`)를 요청하거나 `.env`에서 확인.
2. `index.html`의 `<head>` 태그 내에 다음 스크립트 주입:
   ```html
   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-YOUR_ID" crossorigin="anonymous"></script>
   ```

### Step 3: Ads.txt Creation
1. `ads.txt` 파일 존재 여부 확인.
2. 없다면 생성 후 내용 작성: `google.com, pub-YOUR_ID, DIRECT, f08c47fec0942fa0`

## ⚠️ Notes
- 생성된 문서는 '표준 양식'이므로, 실제 서비스 배포 전 대표자의 검토가 필요함을 고지할 것.
