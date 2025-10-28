# ParaBank Test Automation Framework

> ⚡ **Quick Summary for Recruiters**  
Modular test automation suite for the ParaBank demo banking app using Python, Pytest, and Playwright. Demonstrates clean architecture, CI/CD readiness, and real-world QA engineering practices.

<details>
  <summary>📄 Full Technical Overview</summary>

## Tech Stack

- Pytest for test orchestration and marker-based execution  
- Playwright for browser automation (headless/headed)  
- Page Object Model (POM) for maintainability  
- Custom assertions for readable and traceable validations  
- Environment variable handling via `.env` and `config.py`  

## Test Coverage

- **User registration and login** — validates successful onboarding and dashboard access  
- **Account overview** — checks account count, balances, and available funds  
- **Open new account** — creates a savings account and verifies UI updates  
- **Transfer funds** — moves money between accounts and confirms updated balances  
- **Dynamic data validation** — uses account numbers and balance checks across multiple views  

## CI/CD Integration

- Jenkins jobs triggered by GitHub commits  
- Parameterized test runs with environment control  
- Build history and job status visible in Jenkins dashboard (`Jenkins.jpg`)  

## Reporting

- Pytest generates HTML reports for each test run  
- Sample report and screenshots included (`report.html`, `report.jpg`)  
- Screenshot capture on failure can be added for deeper traceability  

## 📁 Project Structure

- `pages/` — Page Object Models  
  - `account_overview_page.py`  
  - `administration_page.py`  
  - `login_page.py`  
  - `main_page.py`  
  - `open_new_account_page.py`  
  - `register_page.py`  
  - `transfer_funds_page.py`  
- `tests/` — Pytest test cases  
  - `test_register_login.py`  
  - `test_account_overview.py`  
  - `test_open_new_account.py`  
  - `test_transfer_funds.py`  
  - `test_logout.py`  
- `utils/` — Helpers and shared methods  
- `.env` — Environment variables  
- `.gitignore` — Git exclusions  
- `config.py` — Runtime config loader  
- `pytest.ini` — Pytest config  
- `requirements.txt` — Python dependencies  
- `report.html` — Sample test report  
- `report.jpg` — Screenshot from test run  
- `README.md` — Project overview  

##  Author

**Ievgen** — QA-focused engineer with deep experience in Playwright, Pytest, and CI/CD pipelines. Passionate about clean architecture, traceable validations, and scalable test automation.

</details>