---
name: ui-theme-architect
description: TailwindCSS 기반의 테마(Theme) 교체 및 일관성 관리 시스템. Midnight Nebula, Clean Modern 등 프리셋 지원.
version: 1.0.0
author: Antigravity Core
usage: "User: 테마를 Clean Modern으로 바꿔줘 -> Agent: ui-theme-architect 실행"
---

# 🎨 UI Theme Architect

이 스킬은 프로젝트의 전체적인 Look & Feel을 담당합니다. CSS 변수(Variables)와 Tailwind Config를 조작하여 테마를 즉시 교체합니다.

## 🛠 Features
1. **Theme Swapper**: 미리 정의된 3가지 테마(Midnight, Clean, Brutal) 중 하나로 즉시 전환.
2. **Consistency Check**: 버튼, 카드, 입력창의 스타일이 테마 규칙을 따르는지 검사.
3. **Tailwind Injector**: `tailwind.config.js`가 없으면 자동 생성 및 최적화.

## 📦 Theme Presets

### 1. 🌌 Midnight Nebula (Default)
- **Concept**: Deep Space, Neon Glow, Glassmorphism
- **Colors**: `bg-slate-900`, `text-slate-100`, `accent-purple-500`
- **Vibe**: 신비로움, 몰입감, 개발자 친화적

### 2. 🍎 Clean Modern (Apple Style)
- **Concept**: Minimal, Whitespace, Soft Shadows
- **Colors**: `bg-white`, `text-gray-900`, `accent-blue-600`
- **Dark Mode**: `bg-gray-900` (Neutral)
- **Vibe**: 신뢰감, 전문성, 깔끔함

### 3. 🚧 Cyber Brutal (High Contrast)
- **Concept**: Raw Borders, Mono Typography, Vivid Colors
- **Colors**: `bg-yellow-50`, `text-black`, `border-black (2px)`
- **Vibe**: 트렌디, 강렬함, 가독성 최우선

## 📋 Execution Steps

### Step 1: Analyze & Backup
1. `index.html` (또는 메인 CSS)의 현재 스타일 분석.
2. `<head>` 내의 `<style>` 태그 또는 연결된 CSS 파일을 백업 (`styles.bak.css`).

### Step 2: Apply Theme (CSS Variables)
1. 사용자가 선택한 테마의 CSS 변수를 `:root`에 주입.
   ```css
   /* Example: Clean Modern */
   :root {
       --bg-primary: #ffffff;
       --text-primary: #111827;
       --accent: #2563eb;
       --radius: 0.5rem; /* Soft Round */
   }
   ```
2. Tailwind 클래스가 하드코딩된 경우(`bg-slate-900`), 정규식 치환을 통해 테마 클래스(`bg-primary`) 또는 변수 기반으로 리팩토링 제안.

### Step 3: Component Standardization
1. 버튼(`button`), 입력창(`input`), 카드(`div.card`) 요소를 찾아 공통 유틸리티 클래스(`btn-primary`, `input-field`) 적용.

## ⚠️ Notes
- 테마 변경 시 기존의 커스텀 스타일이 덮어씌워질 수 있음을 미리 경고할 것.
