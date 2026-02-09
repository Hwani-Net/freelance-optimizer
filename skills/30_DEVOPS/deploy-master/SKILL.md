---
name: deploy-master
description: Cloudflare Pages 및 주요 플랫폼 배포 자동화 마스터
version: 1.0.0
author: Antigravity Core
usage: "User: 배포해줘 -> Agent: deploy-master 실행"
---

# ⚡ Deploy Master (Cloudflare Pages)

이 스킬은 현재 프로젝트를 분석하여 가장 최적화된 배포 경로를 제안하고 실행합니다. (Default: Cloudflare Pages)

## 🛠 Features
1. **Project Analyzer**: 정적 웹사이트(HTML)인지, 프레임워크(React/Next)인지 감지.
2. **Wrangler Config**: `wrangler.toml` 파일 자동 생성/검증.
3. **Direct Deploy**: CLI 명령어를 통한 즉시 배포 (Git 연동 없이도 가능).

## 📋 Execution Steps

### Step 1: Project Analysis
1. `package.json` 확인 -> Build Script 유무 확인.
2. `index.html`만 있는 경우 -> Static Site로 간주.

### Step 2: Cloudflare Wrangler Setup
1. `wrangler.toml` 파일 존재 여부 확인.
2. 없다면 생성 (Static Site 기준):
   ```toml
   name = "project-name"
   pages_build_output_dir = "./" 
   ```

### Step 3: Deployment Execution
1. 터미널 명령 실행:
   - **Login check**: `npx wrangler whoami`
   - **Deploy**: `npx wrangler pages deploy .` (현재 폴더 배포)
2. 배포 완료 후 나온 URL을 사용자에게 보고.

## ⚠️ Notes
- Cloudflare 계정 로그인이 안 되어 있을 경우, 브라우저 인증 절차를 안내할 것.
