<p align="center">
  <h1 align="center">0x-scan</h1>
  <p align="center">
    ⚡ Advanced Reconnaissance & Port Scanning Platform for Security Professionals
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" />
  <img src="https://img.shields.io/badge/platform-linux-lightgrey" />
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <img src="https://img.shields.io/badge/security-research-red" />
</p>

---

## 🚀 Overview

**0x-scan** is a modern, modular, high-performance reconnaissance platform designed for deep network and web intelligence gathering. Built in Python with asynchronous architecture, it goes beyond traditional port scanning to provide layered visibility into network services, infrastructure, web technologies, and OSINT data.

Unlike simple scanners, 0x-scan integrates:

- Network discovery
- Service fingerprinting
- Web intelligence
- Infrastructure detection
- OSINT analysis
- Persistent storage
- Background job processing
- Web dashboard interface

It is designed for:

- Security researchers
- Penetration testers
- Red team operators
- Network engineers
- Advanced system administrators

Linux-first, tested on Arch Linux and Kali Linux.

---

## ✨ Key Features

### 🔍 Network Reconnaissance
- High-speed asynchronous TCP port scanning
- UDP probing without raw sockets
- Banner grabbing for service identification
- Passive OS fingerprinting

### 🌐 Web Intelligence
- HTTP/HTTPS probing
- TLS certificate analysis
- Security header inspection
- Cookie security evaluation
- Technology fingerprinting
- Lightweight crawler

### ☁️ Infrastructure Detection
- CDN identification
- WAF detection
- Cloud provider inference

### 🌍 OSINT Modules
- DNS enumeration (A, AAAA, MX, NS, TXT, SOA)
- Subdomain discovery
- Reputation assessment

### 🗄️ Persistence & Automation
- PostgreSQL storage backend
- Scan history tracking
- Background workers
- Continuous monitoring capability

### 🖥️ Web UI
- React dashboard
- Scan management interface
- Result visualization

---

## 📸 Screenshots

> _Add screenshots of the dashboard, scan results, and API interface here._



Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ## 🧰 Installation Guide  ### ✅ Prerequisites  - Python 3.10+  - Node.js 18+  - PostgreSQL  - Linux (recommended)  - Git---###   🔧 Clone Repository  ```bash  git clone https://github.com/yourname/0x-scan.gitcd 0x-scan   `

### 🐍 Create Virtual Environment

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv venvsource venv/bin/activate   `

### 📦 Install Dependencies

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

### 🗄️ Configure Database

Create database:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   CREATE DATABASE recon;CREATE USER user WITH PASSWORD 'password';GRANT ALL PRIVILEGES ON DATABASE recon TO user;   `

Edit .env:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/recon   `

### 🏗️ Initialize Database

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m scripts.init_dbpython -m scripts.seed_db   `

### ▶️ Run Backend API

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   uvicorn app.main:app --reload   `

Access API:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://localhost:8000/docs   `

### 🛰️ Start Workers

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m scripts.run_worker   `

### 🖥️ Run Web UI

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd webuinpm installnpm run dev   `

Open:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://localhost:5173   `

📖 Usage Guide
--------------

### 🔹 Basic Scan (Quick)

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   POST /scan/quick{  "target": "example.com"}   `

### 🔹 Full Scan

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {  "target": "example.com",  "full_scan": true,  "ports": "common"}   `

### 🔹 Background Scan

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   POST /scan/start   `

Results processed asynchronously by workers.

### 🧪 Recommended Test Targets

*   scanme.nmap.org
    
*   testphp.vulnweb.com
    
*   Your local network devices
    

🧠 Feature Breakdown
--------------------

### TCP Scanning

*   Asynchronous socket connections
    
*   Configurable concurrency
    
*   Port state detection
    

### UDP Scanning

*   Safe application-level probes
    
*   No raw packet privileges required
    

### Service Detection

*   Banner analysis
    
*   Port-service mapping
    

### Banner Grabbing

*   Reads initial server response
    
*   Identifies software versions
    

### OS Fingerprinting

*   TTL-based heuristics
    
*   Service correlation
    

### Performance

*   Async I/O architecture
    
*   Concurrency controls
    

### Timeout Handling

*   Per-connection timeouts
    
*   Failure recovery
    

### Error Handling

*   Graceful network failure handling
    
*   Safe retries
    

🏗️ Architecture Overview
-------------------------

### High-Level Design

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Frontend → API → Scanner Engine → Analyzers → Database → Workers   `

### Data Flow

1.  User submits target
    
2.  API validates request
    
3.  Scan job created
    
4.  Worker executes modules
    
5.  Results stored
    
6.  UI retrieves output
    

### Module Responsibilities

LayerResponsibilityAPIRequest handlingScannerOrchestrationAnalyzersIntelligence gatheringDatabasePersistenceWorkersBackground executionServicesBusiness logic

📂 Directory Structure
----------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   0x-scan/├── app/│   ├── api/│   ├── analyzers/│   ├── scanner/│   ├── database/│   ├── workers/│   ├── services/│   └── main.py├── webui/├── scripts/├── requirements.txt├── docker-compose.yml└── README.md   `

🧩 Code Structure Explanation
-----------------------------

*   **api/** — REST endpoints
    
*   **scanner/** — Core scan orchestration
    
*   **analyzers/** — Intelligence modules
    
*   **database/** — ORM models & CRUD
    
*   **workers/** — Async background processing
    
*   **services/** — Business logic layer
    

⚙️ Configuration Options
------------------------

Configured via .env.

Key variables:

VariablePurposeAPI\_KEYAPI authenticationDATABASE\_URLDB connectionSCAN\_TIMEOUTNetwork timeoutRATE\_LIMITRequest limits

⚠️ Security & Ethical Use
-------------------------

This tool is intended for:

✔ Authorized testing✔ Research environments✔ Owned infrastructure

Unauthorized scanning may violate laws and policies.

⚡ Performance Considerations
----------------------------

*   Async networking enables high throughput
    
*   PostgreSQL ensures persistence scalability
    
*   Worker model supports large workloads
    
*   Can be distributed across nodes (future)
    

🔎 Comparison with Nmap
-----------------------

0x-scan is NOT a replacement for Nmap.

AspectNmap0x-scanRaw packet control✔❌Web intelligenceLimited✔AutomationLimited✔Database storage❌✔UI❌✔

Designed as a complementary modern platform.

📝 Logging System
-----------------

*   Structured console logging
    
*   Supports production integration
    
*   Can be extended to file or SIEM output
    

🧪 Extending the Project
------------------------

To add new features:

1.  Create analyzer module
    
2.  Integrate into scanner engine
    
3.  Update service layer
    
4.  Add API endpoint
    

🛠️ Troubleshooting
-------------------

### Database Connection Failed

*   Verify PostgreSQL is running
    
*   Check credentials
    
*   Confirm database exists
    

### Import Errors

Run scripts as modules:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m scripts.init_db   `

### Worker Issues

Ensure background workers are running.

🤝 Contributing
---------------

Contributions welcome.

Steps:

1.  Fork repository
    
2.  Create feature branch
    
3.  Submit pull request
    
4.  Follow coding standards
    

🗺️ Roadmap
-----------

*   Distributed scanning nodes
    
*   Real-time WebSocket updates
    
*   Authentication & RBAC
    
*   Advanced vulnerability detection
    
*   Passive intelligence integration
    
*   Kubernetes deployment support
    

📜 License
----------

MIT License — see LICENSE file.

👨‍💻 Author
------------

**0x-scan Project**

Security-focused open-source reconnaissance platform.


<p align="center"> <b>⚡ Built for serious cybersecurity professionals ⚡</b> </p>
