# 🔌 Awesome MCP Tools

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> MCP (Model Context Protocol) 서버들의 큐레이션 목록

이 저장소는 AI 모델이 외부 도구 및 데이터 소스와 상호작용할 수 있게 해주는 **Model Context Protocol (MCP)** 서버들을 정리한 목록입니다.

## 📖 목차

- [MCP란?](#-mcp란)
- [카테고리](#-카테고리)
  - [Aggregators](#🔗-aggregators)
  - [Browser Automation](#🌐-browser-automation)
  - [Databases](#🗄️-databases)
  - [Developer Tools](#🛠️-developer-tools)
  - [File Systems](#📂-file-systems)
  - [Search](#🔎-search)
  - [Communication](#💬-communication)
  - [Payments](#💳-payments)
  - [Knowledge & Memory](#🧠-knowledge--memory)
  - [Cloud Platforms](#☁️-cloud-platforms)
  - [Monitoring](#📊-monitoring)
  - [Utilities](#🔧-utilities)
- [참조 링크](#-참조-링크)
- [기여하기](#-기여하기)

---

## 🤔 MCP란?

[MCP (Model Context Protocol)](https://modelcontextprotocol.io/)는 AI 모델이 표준화된 서버 구현을 통해 로컬 및 원격 리소스와 안전하게 상호작용할 수 있도록 하는 개방형 프로토콜입니다.

### 범례

| 아이콘 | 의미 |
|--------|------|
| 🎖️ | 공식 구현 |
| 📇 | TypeScript |
| 🐍 | Python |
| 🏎️ | Go |
| 🦀 | Rust |
| #️⃣ | C# |
| ☕ | Java |
| ☁️ | 클라우드 서비스 |
| 🏠 | 로컬 서비스 |
| 🔑 | API 키 필요 |

---

## 📂 카테고리

### 🔗 Aggregators

> 단일 MCP 서버를 통해 많은 앱과 도구에 접근하기 위한 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [1mcp/agent](https://github.com/1mcp-app/agent) | 여러 MCP 서버를 하나의 MCP 서버로 통합하는 통합 모델 컨텍스트 프로토콜 서버 구현 | 🔑 |
| [OpenMCP](https://github.com/wegotdocs/open-mcp) | 웹 API를 10초 만에 MCP 서버로 전환하고 오픈 소스 레지스트리에 추가할 수 있는 도구 | 🔑 |
| [mcgravity](https://github.com/tigranbs/mcgravity) | 여러 MCP 서버를 단일 연결 포인트로 통합하여 프록시하는 도구로, 요청 부하를 분산하여 AI 도구를 확장 | 🔑 |
| [MetaMCP (metatool-app)](https://github.com/metatool-ai/metatool-app) | GUI를 제공하여 여러 MCP 연결을 통합 관리하는 MetaMCP 미들웨어 서버 | 🔑 |
| [magg](https://github.com/sitbon/magg) | 서버 자동 탐색 및 오케스트레이션을 수행하는 범용 허브 역할의 Meta-MCP 서버 | 🔑 |
| [mcpx](https://github.com/TheLunarCompany/lunar) | 규모를 고려한 MCP 서버 관리를 위한 프로덕션급 게이트웨이. 접근 제어, 툴 탐색 등 기능 포함 | 🔑 |
| [pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy) | 여러 MCP 서버를 합쳐 하나의 인터페이스로 제공하며, 가시성(Visibility) 기능을 포함한 프록시 서버 | 🔑 |
| [Pipedream](https://github.com/PipedreamHQ/pipedream) | 약 2,500개의 API들과 8,000+ 도구를 연결 가능하며, 사용자 앱을 위한 서버 관리 기능 포함 | 🔑 |
| [mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates) | 단일 플랫폼에서 여러 앱/서비스를 뒤에 두고 통합 MCP 인터페이스 제공 | - |
| [roundtable](https://github.com/askbudi/roundtable) | 여러 AI 코딩 어시스턴트(Codex, Claude Code, Cursor, Gemini)를 자동 탐색하여 표준화된 MCP 인터페이스로 통합하는 Meta-MCP 서버 | 🔑 |
| [MCPJungle](https://github.com/duaraghav8/MCPJungle) | 엔터프라이즈 AI 에이전트를 위한 셀프호스팅 MCP 서버 레지스트리 | - |
| [mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) | 사용자 워크플로우 개선을 위해 사용 가능한 MCP 서버 목록을 제공 | - |
| [anyquery](https://github.com/julien040/anyquery) | 하나의 바이너리로 40개 이상의 앱을 SQL로 쿼리 가능, PostgreSQL/MySQL/SQLite 연결 지원, 로컬 우선 설계 | 🔑 |
| [mindsdb](https://github.com/mindsdb/mindsdb) | 다양한 플랫폼과 데이터베이스를 단일 MCP 서버로 연결 및 통합 | 🔑 |
| [ncp](https://github.com/portel-dev/ncp) | 지능형 discovery를 통해 전체 MCP 생태계를 조율하고 토큰 오버헤드를 제거하면서 높은 정확도 유지 | 🔑 |
| [MCPDiscovery](https://github.com/particlefuture/MCPDiscovery) | MCP 서버들의 중앙 허브로, 사용 가능한 MCP 서버를 발견하고 설치 및 사용 방법 안내 | - |
| [mcpbundles](https://github.com/thinkchainai/mcpbundles) | 도구 번들을 만들고 OAuth 또는 API 키로 제공자 연결, 수천 개 통합을 하나의 MCP 서버에서 관리 | 🔑 |
| [openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) | 이미지 생성/편집 기능을 제공하는 OpenAI GPT 기반 MCP 서버 | 🔑 |
| [imagen3-mcp](https://github.com/hamflx/imagen3-mcp) | Google Imagen 3.0 API를 통해 고품질 이미지 생성 기능을 제공하는 MCP 서버 | 🔑 |
| [mcp-access-point](https://github.com/sxhxliang/mcp-access-point) | 웹 서비스를 코드 변경 없이 한 번의 명령으로 MCP 서버로 변환해주는 도구 | - |
| [WayStation](https://github.com/WayStation-ai/mcp) | Claude Desktop 등 MCP 호스트들과 여러 앱(Notion, Slack, Airtable 등)을 90초 내로 쉽게 연결 | 🔑 |
| [Zapier MCP](https://zapier.com/mcp) | 8,000개 이상의 앱을 즉시 연결할 수 있는 자동화/통합 플랫폼을 MCP 서버로 활용 | 🔑 |
### 🌐 Browser Automation

> AI 앱이 브라우저를 제어하고 웹 상호작용을 자동화하기 위한 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [Browser MCP](https://github.com/browsermcp/mcp) | 로컬 Chrome 브라우저를 자동화하는 MCP 서버. Chrome 확장 프로그램 포함, VS Code, Claude, Cursor 등에서 브라우저 제어 가능 | - |
| [Playwright MCP (Microsoft)](https://github.com/microsoft/playwright-mcp) | Microsoft 공식 MCP 서버. 웹 페이지와 상호작용하고 구조화된 접근성 스냅샷(accessibility snapshot) 기능 제공 | - |
| [mcp-server-playwright](https://github.com/automatalabs/mcp-server-playwright) | Playwright를 사용하여 브라우저 자동화 기능을 제공하는 MCP 서버 | - |
| [server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) | Puppeteer 기반 MCP 서버. 웹 스크래핑, 양식 자동 작성, 상호작용 제공 | - |
| [puppeteer-mcp-server](https://github.com/merajmehrabi/puppeteer-mcp-server) | Puppeteer를 사용하여 스크린샷, 클릭, 양식 작성 등 브라우저 자동화 기능 제공 | - |
| [browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) | browser-use 엔진을 패키징하여 MCP 서버로 제공. Chromium 도커 + VNC 포함 | 🔑 |
| [selenium-mcp-server](https://github.com/PhungXuanAnh/selenium-mcp-server) | Selenium WebDriver를 통해 웹 자동화 기능을 제공하는 MCP 서버 | - |
| [firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp) | WebDriver BiDi로 Firefox 자동화 지원. 스냅샷, 콘솔 캡처, 네트워크 모니터링, 스크린샷 등 | - |
| [mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) | Azure OpenAI + Playwright를 사용한 최소한(minimal) 서버/클라이언트 구현. 웹 브라우징 기능 제공 | 🔑 |
| [olostep-mcp-server](https://github.com/olostep/olostep-mcp-server) | 웹 스크래핑, 크롤링, 검색 API 제공. 동적 URL 배치 처리 및 Markdown/JSON 반환 지원 | - |
| [web-search (pskill9)](https://github.com/pskill9/web-search) | Google 검색 결과를 통해 무료 웹 검색 기능 제공. API 키 없이 작동 가능하도록 설계 | - |
### 🗄️ Databases

> 데이터베이스와 상호작용하기 위한 MCP 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) | PostgreSQL 데이터베이스와 상호작용하는 공식 MCP 서버 | - |
| [server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) | SQLite 데이터베이스와 상호작용하는 공식 MCP 서버 | - |
| [supabase-mcp-server](https://github.com/alexanderzuev/supabase-mcp-server) | Supabase 프로젝트에 AI 어시스턴트 연결, 테이블 관리 및 쿼리 실행 가능 | 🔑 |
| [mcp-aiven](https://github.com/Aiven-Open/mcp-aiven) | PostgreSQL, Kafka, ClickHouse, OpenSearch 등을 포함한 Aiven 클라우드 DB 서비스와 상호작용 | 🔑 |
| [mysql-mcp-server](https://github.com/benborber/mysql-mcp-server) | MySQL 데이터베이스와 상호작용하는 MCP 서버 | - |
| [mongodb-mcp-server](https://github.com/kiliczsh/mcp-mongo-server) | MongoDB 데이터베이스와 상호작용하는 MCP 서버 | - |
| [redis-mcp-server](https://github.com/redis/mcp-server) | Redis 데이터베이스와 상호작용하는 MCP 서버 | - |
### 🛠️ Developer Tools

> 개발 워크플로우를 향상시키기 위한 MCP 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) | GitHub API와 상호작용하는 공식 MCP 서버. 리포지토리, 이슈, PR 관리 | 🔑 |
| [server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) | GitLab API와 상호작용하는 MCP 서버 | 🔑 |
| [server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | Git 리포지토리와 상호작용하는 MCP 서버. 커밋, 브랜치, diff 등 | - |
| [docker-mcp](https://github.com/ckreiling/mcp-server-docker) | Docker 컨테이너와 이미지를 관리하는 MCP 서버 | - |
| [mcp-kubernetes](https://github.com/strowk/mcp-k8s-go) | Kubernetes 클러스터와 상호작용하는 MCP 서버 | - |
### 📂 File Systems

> 파일 및 디렉토리와 상호작용하기 위한 MCP 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | 로컬 파일 시스템과 상호작용하는 공식 MCP 서버 | - |
| [google-drive-mcp](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) | Google Drive와 상호작용하는 MCP 서버 | 🔑 |
| [dropbox-mcp](https://github.com/amidabuddha/mcp-dropbox-server) | Dropbox와 상호작용하는 MCP 서버 | 🔑 |
### 🔎 Search

> 웹 검색 및 데이터 검색을 위한 MCP 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) | Brave Search API를 통한 웹 검색 기능 제공 | 🔑 |
| [tavily-mcp](https://github.com/tavily-ai/tavily-mcp) | Tavily AI 검색 API를 통한 검색 기능 제공 | 🔑 |
| [exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) | Exa AI 검색 API를 통한 검색 기능 제공 | 🔑 |
| [google-search-mcp](https://github.com/adenot/mcp-server-google) | Google Custom Search API를 통한 검색 기능 제공 | 🔑 |
### 💬 Communication

> 이메일, 메시징 등 커뮤니케이션 도구와 상호작용하기 위한 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) | Slack 워크스페이스와 상호작용하는 공식 MCP 서버 | 🔑 |
| [discord-mcp](https://github.com/v-3/mcp-discord) | Discord 서버와 상호작용하는 MCP 서버 | 🔑 |
| [gmail-mcp](https://github.com/GongRzhe/Gmail-MCP-Server) | Gmail과 상호작용하는 MCP 서버 | 🔑 |
| [teams-mcp](https://github.com/aaronpowell/mcp-server-teams) | Microsoft Teams와 상호작용하는 MCP 서버 | 🔑 |
### 💳 Payments

> 에이전트의 결제 준비, 상태 및 영수증 조회를 위한 로컬 도구

| 이름 | 설명 | API |
|------|------|:---:|
| [Agent Payment Node](https://github.com/nuanu-ai/agent-payment-node) | Apple Silicon macOS·Node.js 24 전용 로컬 stdio 결제 도구: x402 제안 확인, 제한된 결제 준비, 상태·영수증 조회. 소유자 승인·정책 적용, 네트워크·서비스 수수료 별도 | - |
### 🧠 Knowledge & Memory

> 노트, 문서 관리 등 지식 관리 도구와 상호작용하기 위한 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) | 지식 그래프 기반 메모리 시스템을 제공하는 공식 MCP 서버 | - |
| [notion-mcp](https://github.com/makenotion/notion-mcp-server) | Notion 워크스페이스와 상호작용하는 MCP 서버 | 🔑 |
| [obsidian-mcp](https://github.com/smithery-ai/mcp-obsidian) | Obsidian 노트와 상호작용하는 MCP 서버 | - |
### ☁️ Cloud Platforms

> AWS, GCP, Azure 등 클라우드 서비스와 상호작용하기 위한 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [aws-mcp](https://github.com/aws-samples/mcp-server-aws) | AWS 서비스들과 상호작용하는 MCP 서버 | 🔑 |
| [gcp-mcp](https://github.com/GoogleCloudPlatform/mcp-server-gcp) | Google Cloud Platform 서비스들과 상호작용하는 MCP 서버 | 🔑 |
| [azure-mcp](https://github.com/Azure/azure-mcp) | Azure 서비스들과 상호작용하는 MCP 서버 | 🔑 |
| [cloudflare-mcp](https://github.com/cloudflare/mcp-server-cloudflare) | Cloudflare 서비스들과 상호작용하는 MCP 서버 | 🔑 |
### 📊 Monitoring

> 시스템 모니터링 및 관측을 위한 MCP 서버들

| 이름 | 설명 | API |
|------|------|:---:|
| [sentry-mcp](https://github.com/getsentry/sentry-mcp) | Sentry 에러 모니터링 서비스와 상호작용하는 MCP 서버 | 🔑 |
| [datadog-mcp](https://github.com/DataDog/mcp-server-datadog) | Datadog 모니터링 서비스와 상호작용하는 MCP 서버 | 🔑 |
### 🔧 Utilities

> MCP 개발 및 테스트를 위한 유틸리티 도구들

| 이름 | 설명 | API |
|------|------|:---:|
| [mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) | 예제 서버 및 MCP 클라이언트가 포함된 MCP stdio에서 HTTP SSE 전송 게이트웨이 | - |
| [mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client) | LangChain.js에서 MCP 제공 도구 사용 | - |
| [MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) | 기존의 모든 OpenAI 호환 클라이언트에서 MCP를 사용하기 위한 openAI 미들웨어 프록시 | - |
| [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) | MCP stdio에서 SSE 전송 게이트웨이 | - |
| [mcphost](https://github.com/mark3labs/mcphost) | LLM이 MCP를 통해 외부 도구와 상호작용할 수 있도록 하는 CLI 호스트 애플리케이션 | - |
| [mcp-chat](https://github.com/flux159/mcp-chat) | 모든 MCP 서버와 채팅하고 연결하는 CLI 기반 클라이언트. MCP 서버 개발 및 테스트 중 유용 | - |

---

## 📚 참조 링크

### 공식 리소스
- [Awesome MCP Servers (English)](https://github.com/punkpeye/awesome-mcp-servers)
- [Awesome MCP Servers (한국어)](https://github.com/punkpeye/awesome-mcp-servers/blob/main/README-ko.md)
- [Model Context Protocol 공식 사이트](https://modelcontextprotocol.io/)
- [MCP Servers Web Directory](https://glama.ai/mcp/servers)

### 공식 저장소
- [Model Context Protocol Organization](https://github.com/modelcontextprotocol)
- [MCP Servers (Official)](https://github.com/modelcontextprotocol/servers)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

### 커뮤니티
- [MCP Discord Server](https://glama.ai/mcp/discord)
- [MCP Subreddit](https://www.reddit.com/r/mcp/)
- [Awesome MCP Clients](https://github.com/punkpeye/awesome-mcp-clients)
- [Glama MCP Clients](https://glama.ai/mcp/clients)

### 튜토리얼
- [MCP Quick Start Guide](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
- [Claude Desktop SQLite Setup](https://youtu.be/wxCCzo9dGj0)

---

## 🤝 기여하기

새로운 MCP 서버를 발견하셨거나 정보 수정이 필요하시면 다음 파일을 수정해주세요:

1. `mcptools.yaml` - MCP 서버 목록
2. `reference.yaml` - 참조 소스 URL

README.md는 아래 스크립트로 자동 생성됩니다:

```bash
python scripts/generate_readme.py
```

---

## 📄 라이선스

MIT License

---

<p align="center">
  <i>이 목록은 <a href="https://github.com/punkpeye/awesome-mcp-servers">awesome-mcp-servers</a>를 참조하여 작성되었습니다.</i>
</p>

<!-- 
자동 생성됨: 2026-10-27 00:38:40
총 서버 수: 72개
-->
