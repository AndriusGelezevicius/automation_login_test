
# Login Form Test Automation

This project automates the testing of the login functionality on the [Practice Test Automation](https://practicetestautomation.com/practice-test-login/) page using:
- `pytest` for test structure and execution
- `Selenium WebDriver` for browser automation
- `Page Object Model (POM)` for code clarity and reuse
- `Qase` for test case documentation and traceability

##  How to Run Tests

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

2. **Run all tests:**

```bash
pytest
```

3. **Run a specific test file:**
```bash
pytest tests/test_negative_username.py
```

## Test Cases Documentation
All test cases are documented in Qase:

Qase – [automation_login_test](https://app.qase.io/project/ALT)

Each automated test corresponds to a test case ID, e.g. ALT-1,ALT-3, ALT-4.

### Requirements
- Python 3.10+
- Google Chrome
- ChromeDriver (compatible with your browser version)


### Contacts  
Author: Andrius Geleževičius  
Project goal: learning Python, Pytest, Selenium and Qase platform
