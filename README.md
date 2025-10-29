# ParaBank Test Automation Framework

>  **Overview**  
Compact PyTest suite for the ParaBank demo site. Focuses on transactional workflows (onboarding, transfers, balances) with POM design.

>  **Highlights**
- Transactional flows: onboarding, transfers, balances
- Page Object Model with parametrized negative cases
- HTML reporting and environment-based configuration
- CI-ready structure for PR and nightly runs

<details>
  <summary>📄 Full Technical Overview</summary>

## Tech Stack

- **Pytest** — orchestrates tests and supports marker-based execution  
- **Playwright** — handles browser automation (headless and headed modes)  
- **Page Object Model (POM)** — improves code maintainability and reuse  
- **Custom assertions** — ensures readable, traceable validations  
- **Environment config** — managed via `.env` and `config.py`  

## Test Coverage

- **User registration and login** — validates onboarding and dashboard access  
- **Account overview** — checks account count, balances, and available funds  
- **Open new account** — creates a savings account and verifies UI updates  
- **Transfer funds** — moves money between accounts and confirms updated balances  
- **Dynamic data validation** — uses account numbers and balance checks across multiple views  

## CI/CD Integration

- Jenkins jobs triggered automatically on GitHub commits  
- Supports parameterized test runs with environment control  
- Build history and job status visible in the Jenkins dashboard (`Jenkins.jpg`)  

## Reporting

- HTML reports generated via Pytest for each test run  
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
- `config.py` — Runtime configuration loader  
- `pytest.ini` — Pytest settings  
- `requirements.txt` — Python dependencies  
- `report.html` — Sample test report  
- `report.jpg` — Screenshot from test run  
- `README.md` — Project overview  

## 👤 Author

**Ievgen** — QA engineer with deep expertise in Playwright, Pytest, and CI/CD pipelines. Focused on building scalable, maintainable automation with clean architecture and traceable validations.

</details>
