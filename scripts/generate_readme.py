#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCP Tools README.md 자동 생성 스크립트

이 스크립트는 mcptools.yaml과 reference.yaml 파일을 읽어서
README.md 파일을 자동으로 생성합니다.

사용법:
    python scripts/generate_readme.py
"""

import sys
import io
import yaml
from pathlib import Path
from datetime import datetime

# Windows 콘솔 UTF-8 출력 설정
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# 프로젝트 루트 경로
PROJECT_ROOT = Path(__file__).parent.parent
MCPTOOLS_FILE = PROJECT_ROOT / "mcptools.yaml"
REFERENCE_FILE = PROJECT_ROOT / "reference.yaml"
README_FILE = PROJECT_ROOT / "README.md"

# 카테고리 메타데이터 (이름, 아이콘, 설명)
CATEGORY_META = {
    "aggregators": {
        "icon": "🔗",
        "title": "Aggregators",
        "description": "단일 MCP 서버를 통해 많은 앱과 도구에 접근하기 위한 서버들"
    },
    "browser_automation": {
        "icon": "🌐",
        "title": "Browser Automation",
        "description": "AI 앱이 브라우저를 제어하고 웹 상호작용을 자동화하기 위한 서버들"
    },
    "databases": {
        "icon": "🗄️",
        "title": "Databases",
        "description": "데이터베이스와 상호작용하기 위한 MCP 서버들"
    },
    "developer_tools": {
        "icon": "🛠️",
        "title": "Developer Tools",
        "description": "개발 워크플로우를 향상시키기 위한 MCP 서버들"
    },
    "file_systems": {
        "icon": "📂",
        "title": "File Systems",
        "description": "파일 및 디렉토리와 상호작용하기 위한 MCP 서버들"
    },
    "search": {
        "icon": "🔎",
        "title": "Search",
        "description": "웹 검색 및 데이터 검색을 위한 MCP 서버들"
    },
    "communication": {
        "icon": "💬",
        "title": "Communication",
        "description": "이메일, 메시징 등 커뮤니케이션 도구와 상호작용하기 위한 서버들"
    },
    "payments": {
        "icon": "💳",
        "title": "Payments",
        "description": "에이전트의 결제 준비, 상태 및 영수증 조회를 위한 로컬 도구"
    },
    "knowledge_memory": {
        "icon": "🧠",
        "title": "Knowledge & Memory",
        "description": "노트, 문서 관리 등 지식 관리 도구와 상호작용하기 위한 서버들"
    },
    "cloud_platforms": {
        "icon": "☁️",
        "title": "Cloud Platforms",
        "description": "AWS, GCP, Azure 등 클라우드 서비스와 상호작용하기 위한 서버들"
    },
    "monitoring": {
        "icon": "📊",
        "title": "Monitoring",
        "description": "시스템 모니터링 및 관측을 위한 MCP 서버들"
    },
    "utilities": {
        "icon": "🔧",
        "title": "Utilities",
        "description": "MCP 개발 및 테스트를 위한 유틸리티 도구들"
    }
}


def load_yaml(file_path: Path) -> dict:
    """YAML 파일을 로드합니다."""
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def generate_toc(categories: list[str]) -> str:
    """목차를 생성합니다."""
    lines = [
        "## 📖 목차\n",
        "- [MCP란?](#-mcp란)",
        "- [카테고리](#-카테고리)"
    ]
    
    for cat in categories:
        meta = CATEGORY_META.get(cat, {"icon": "📦", "title": cat.replace("_", " ").title()})
        anchor = meta["title"].lower().replace(" ", "-").replace("&", "")
        lines.append(f"  - [{meta['title']}](#{meta['icon'].replace(' ', '-')}-{anchor})")
    
    lines.extend([
        "- [참조 링크](#-참조-링크)",
        "- [기여하기](#-기여하기)"
    ])
    
    return "\n".join(lines)


def generate_category_section(category: str, servers: list[dict]) -> str:
    """카테고리 섹션을 생성합니다."""
    meta = CATEGORY_META.get(category, {
        "icon": "📦",
        "title": category.replace("_", " ").title(),
        "description": ""
    })
    
    lines = [
        f"### {meta['icon']} {meta['title']}\n",
        f"> {meta['description']}\n",
        "| 이름 | 설명 | API |",
        "|------|------|:---:|"
    ]
    
    for server in servers:
        name = server.get("name", "Unknown")
        description = server.get("description", "")
        url = server.get("url", "#")
        api_required = server.get("api_required", False)
        
        api_icon = "🔑" if api_required else "-"
        lines.append(f"| [{name}]({url}) | {description} | {api_icon} |")
    
    return "\n".join(lines)


def generate_references_section(reference_data: dict) -> str:
    """참조 링크 섹션을 생성합니다."""
    lines = [
        "## 📚 참조 링크\n",
        "### 공식 리소스"
    ]
    
    # Primary sources
    for source in reference_data.get("primary_sources", []):
        name = source.get("name", "")
        url = source.get("url", "")
        lines.append(f"- [{name}]({url})")
    
    # Official repositories
    lines.append("\n### 공식 저장소")
    for repo in reference_data.get("official_repositories", []):
        name = repo.get("name", "")
        url = repo.get("url", "")
        lines.append(f"- [{name}]({url})")
    
    # Community resources
    lines.append("\n### 커뮤니티")
    for resource in reference_data.get("community_resources", []):
        name = resource.get("name", "")
        url = resource.get("url", "")
        lines.append(f"- [{name}]({url})")
    
    # Tutorials
    lines.append("\n### 튜토리얼")
    for tutorial in reference_data.get("tutorials", []):
        name = tutorial.get("name", "")
        url = tutorial.get("url", "")
        lines.append(f"- [{name}]({url})")
    
    return "\n".join(lines)


def generate_readme(mcptools: dict, reference: dict) -> str:
    """전체 README.md 내용을 생성합니다."""
    
    # 카테고리 목록 (순서대로)
    category_order = [
        "aggregators", "browser_automation", "databases", "developer_tools",
        "file_systems", "search", "communication", "payments", "knowledge_memory",
        "cloud_platforms", "monitoring", "utilities"
    ]
    
    # 존재하는 카테고리만 필터링
    existing_categories = [cat for cat in category_order if cat in mcptools]
    
    # 통계 계산
    total_servers = sum(len(mcptools.get(cat, [])) for cat in existing_categories)
    
    # README 생성
    readme_parts = []
    
    # 헤더
    readme_parts.append("""# 🔌 Awesome MCP Tools

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> MCP (Model Context Protocol) 서버들의 큐레이션 목록

이 저장소는 AI 모델이 외부 도구 및 데이터 소스와 상호작용할 수 있게 해주는 **Model Context Protocol (MCP)** 서버들을 정리한 목록입니다.

""")
    
    # 목차
    readme_parts.append(generate_toc(existing_categories))
    
    # MCP 소개
    readme_parts.append("""

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

""")
    
    # 각 카테고리 섹션
    for category in existing_categories:
        servers = mcptools.get(category, [])
        if servers:
            readme_parts.append(generate_category_section(category, servers))
            readme_parts.append("\n")
    
    # 참조 링크
    readme_parts.append("\n---\n\n")
    readme_parts.append(generate_references_section(reference))
    
    # 기여 가이드
    readme_parts.append("""

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
자동 생성됨: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f"""
총 서버 수: {total_servers}개
-->
""")
    
    return "".join(readme_parts)


def main():
    """메인 함수"""
    print("📄 README.md 생성 스크립트 시작...")
    
    # YAML 파일 로드
    print(f"  - {MCPTOOLS_FILE} 로드 중...")
    mcptools = load_yaml(MCPTOOLS_FILE)
    
    print(f"  - {REFERENCE_FILE} 로드 중...")
    reference = load_yaml(REFERENCE_FILE)
    
    # README 생성
    print("  - README.md 생성 중...")
    readme_content = generate_readme(mcptools, reference)
    
    # 파일 저장
    print(f"  - {README_FILE} 저장 중...")
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # 통계 출력
    category_order = [
        "aggregators", "browser_automation", "databases", "developer_tools",
        "file_systems", "search", "communication", "payments", "knowledge_memory",
        "cloud_platforms", "monitoring", "utilities"
    ]
    
    total = 0
    print("\n📊 카테고리별 서버 수:")
    for cat in category_order:
        if cat in mcptools:
            count = len(mcptools[cat])
            total += count
            meta = CATEGORY_META.get(cat, {"icon": "📦", "title": cat})
            print(f"  {meta['icon']} {meta['title']}: {count}개")
    
    print(f"\n✅ 완료! 총 {total}개의 MCP 서버가 README.md에 생성되었습니다.")


if __name__ == "__main__":
    main()
