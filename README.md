# Hybrid UI + API Automation (Python)

[![CI](https://img.shields.io/github/actions/workflow/status/<USER>/<REPO>/ci.yml?label=CI&logo=github)](https://github.com/<USER>/<REPO>/actions/workflows/ci.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Live%20Report-1f6feb?logo=allure&logoColor=white)](https://<USER>.github.io/<REPO>/)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-8.x-0A9EDC?logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.47-2EAD33)

**Stack:** PyTest • Playwright • Requests • Allure • Pytest-xdist • GitHub Actions

---
## 🚀 Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install  # + --with-deps on Linux CI
export ENV=dev  # or set in your IDE/run config
pytest -m smoke -n auto --alluredir=allure-results
