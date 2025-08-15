# UI + API Automation Framework.

A robust, scalable Python framework for automated testing of both web UIs and APIs. Built with Playwright, Requests, and Pytest, it enables seamless end-to-end, UI, and API test automation with environment-based configuration and rich reporting.

---

## Features
- **Hybrid Testing:** Automate both UI (web) and API workflows, or combine them for end-to-end scenarios.
- **Playwright Integration:** Fast, reliable browser automation for modern web apps.
- **API Automation:** Use Requests for flexible, powerful API testing.
- **Configurable Environments:** Easily switch between environments (dev, qa, etc.) using JSON config files.
- **Parallel Execution:** Speed up test runs with pytest-xdist.
- **Allure Reporting:** Generate beautiful, interactive test reports.
- **Extensible Structure:** Modular codebase for easy maintenance and scaling.

---

## Technologies Used
- **Python 3.11+**
- **Pytest** (test runner)
- **Playwright** (UI automation)
- **Requests** (API automation)
- **pytest-xdist** (parallel test execution)
- **Allure-pytest** (reporting)
- **jsonschema** (API response validation)

---

## Project Structure
```
├── src/                # Framework source code
│   ├── api/            # API client, helpers
│   ├── ui/             # UI page objects, helpers
│   ├── utils/          # Config, utilities
│   └── __init__.py
├── tests/              # Test cases
│   ├── api/            # API tests
│   ├── ui/             # UI tests
│   └── e2e/            # End-to-end (hybrid) tests
├── config/             # Environment configs (dev.json, qa.json, ...)
├── scripts/            # Setup scripts
│   └── setup_playwright.ps1
├── conftest.py         # Pytest fixtures (config, API client, etc.)
├── requirements.txt    # Python dependencies
├── pytest.ini          # Pytest config & markers
└── README.md           # Project documentation
```

---

## Quickstart

### 1. Clone the Repository
```bash
git clone <REPO_URL>
cd hybrid-automation
```

### 2. Setup Python Virtual Environment
```bash
python -m venv .venv
# Windows:
. .venv/Scripts/activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies & Playwright Browsers
```bash
pip install -r requirements.txt
python -m playwright install
```
Or use the provided PowerShell script (Windows):
```powershell
scripts/setup_playwright.ps1
```

### 4. Set Environment
Set the environment variable to select config (e.g., dev, qa):
```bash
# Windows:
set ENV=dev
# macOS/Linux:
export ENV=dev
```

### 5. Run Tests
- **Smoke tests:**
  ```bash
  pytest -m smoke -n auto --alluredir=allure-results
  ```
- **UI tests:**
  ```bash
  pytest -m ui --headed
  ```
- **API tests:**
  ```bash
  pytest -m api
  ```
- **E2E tests:**
  ```bash
  pytest -m e2e
  ```

### 6. View Allure Report
```bash
allure serve allure-results
```

---

## Configuration
- Edit or add environment configs in `config/` (e.g., `dev.json`, `qa.json`).
- Sensitive data (tokens, etc.) can be set via environment variables or config files.

---

## Writing Tests
- Place new API tests in `tests/api/`, UI tests in `tests/ui/`, and hybrid tests in `tests/e2e/`.
- Use fixtures from `conftest.py` for config and API client access.
- Use Playwright’s page object model for UI automation.

---

## Markers
Defined in `pytest.ini`:
- `smoke`: Basic checks
- `ui`: UI tests
- `api`: API tests
- `e2e`: End-to-end (hybrid) tests

---

## Contributing
1. Fork the repo and create a feature branch.
2. Add/modify tests or framework code.
3. Ensure all tests pass and code is linted.
4. Submit a pull request with a clear description.

---

## Support
For questions or issues, open an issue on GitHub or contact the maintainer.
