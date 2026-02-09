---
name: growth-hacker
description: GA4, Clarity, SEO 메타태그 등 데이터 분석 및 성장 도구 원클릭 통합
version: 1.0.0
author: Antigravity Core
usage: "User: 분석 도구 심어줘 -> Agent: growth-hacker 실행"
---

# 📊 Growth Hacker (Analytics & SEO)

이 스킬은 웹사이트에 '성장의 눈(Data Analytics)'을 장착합니다. 구글 애널리틱스, MS Clarity, SEO 태그를 한 번에 심습니다.

## 🛠 Features
1. **Analytics Injector**: GA4 (Google Analytics 4) 및 MS Clarity 추적 코드 삽입.
2. **SEO Booster**: Open Graph(OG) 태그, Twitter Card, 메타 설명(Description) 자동 최적화.
3. **Sitemap Generator**: `sitemap.xml` 및 `robots.txt` 자동 생성.

## 📋 Execution Steps

### Step 1: Analytics Setup
1. 사용자에게 `GA4 Measurement ID` (G-XXXXXXXXXX)와 `Clarity Project ID` 요청.
2. `index.html`의 `<head>` 최상단에 스크립트 주입.
   - **Clarity Tip**: Clarity는 스크롤 히트맵과 클릭 무효 등을 보여주므로 GA4보다 직관적임.

### Step 2: SEO Meta Tags
1. `<title>`과 `<meta name="description">`이 비어있거나 짧으면, 페이지 내용을 요약하여 자동 생성.
2. 소셜 공유를 위한 Open Graph 태그 추가:
   ```html
   <meta property="og:title" content="..." />
   <meta property="og:image" content="./og-image.png" />
   ```

### Step 3: Accessibility & Robots
1. `robots.txt` 생성:
   ```
   User-agent: *
   Allow: /
   Sitemap: https://[도메인]/sitemap.xml
   ```
2. 모든 `<img>` 태그에 `alt` 속성이 있는지 검사하고, 없으면 파일명 기반으로라도 채워넣기 (SEO 점수 향상).

## ⚠️ Notes
- Analytics 코드는 반드시 `<head>` 태그 내에 위치해야 데이터 누락이 없음.
