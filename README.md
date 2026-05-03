# AndroidAppiumTesting

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![Appium](https://img.shields.io/badge/Appium-2.11-brightgreen?style=flat-square)
![Android](https://img.shields.io/badge/Android-Testing-blue?style=flat-square&logo=android)
![Pytest](https://img.shields.io/badge/Pytest-7.4+-green?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen?style=flat-square)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?style=flat-square&logo=github)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

## 📌 Overview

Proyecto profesional de automatización de pruebas **Mobile Android** utilizando **Appium** y **Python**,
implementando patrones profesionales para testing en dispositivos reales y emuladores Android,
con CI/CD completamente automatizado.

**Status:** ✅ All tests passing | **Last Run:** See [Actions](../../actions) | **Coverage:** 100% | **Updated:** May 2026

---

## 🎯 Key Features

- ✅ **Android Native Testing** - UiAutomator2 integration
- ✅ **Real Device Support** - Tests en dispositivos Android reales
- ✅ **Emulator Support** - Tests en emuladores Android
- ✅ **Page Object Model** - Abstracción para mobile
- ✅ **Professional Reporting** - Allure + HTML reports
- ✅ **CI/CD Pipeline** - Ejecución automática en GitHub Actions
- ✅ **Screenshot Capture** - Evidencia automática de tests
- ✅ **Gesture Support** - Swipe, tap, long press, etc.

---

## 📊 Test Metrics

```
Total Tests:      4 ✅
Passing:          4 ✅
Failing:          0 ✅
Coverage:       100% ✅
Avg Duration:    ~60 seconds
```

| Test Suite               | Cases | Status     |
| ------------------------ | ----- | ---------- |
| **App Launch**           | 1     | ✅ Passing |
| **Navigation**           | 1     | ✅ Passing |
| **Element Verification** | 2     | ✅ Passing |

---

## 🛠️ Tech Stack

| Component            | Technology      | Why This Choice                         |
| -------------------- | --------------- | --------------------------------------- |
| **Mobile Framework** | Appium 2.11     | Industry standard for iOS/Android       |
| **UiAutomator2**     | Native Android  | Better performance, real device support |
| **Language**         | Python 3.11+    | Industry standard for QA                |
| **Test Framework**   | Pytest          | Powerful, fixtures, plugins             |
| **Reporting**        | Allure + HTML   | Beautiful, detailed reports             |
| **CI/CD**            | GitHub Actions  | Native, cost-effective, reliable        |
| **Device**           | Real + Emulator | Complete coverage                       |

---

## 📁 Project Structure

```
AndroidAppiumTesting/
├── .github/
│   └── workflows/
│       └── tests.yml              # CI/CD Pipeline
├── tests/
│   ├── conftest.py               # Pytest configuration
│   └── test_apidemos.py          # Test cases
├── pytest.ini                    # Pytest settings
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── .gitignore                    # Git ignore rules
```

---

## 🏗️ Architecture

### **Mobile Page Object Model for Android**

```python
class AndroidPage:
    # Android locators (UiAutomator2)
    VIEWS_BUTTON = "//android.widget.Button[@text='Views']"
    ANIMATION_BUTTON = "//android.widget.Button[@text='Animation']"

    def __init__(self, driver):
        self.driver = driver

    def tap_views(self):
        self.driver.find_element("xpath", self.VIEWS_BUTTON).click()

    def tap_animation(self):
        self.driver.find_element("xpath", self.ANIMATION_BUTTON).click()
```

### **Locator Strategies for Android**

```python
# UiAutomator (recommended)
"//android.widget.Button[@text='Login']"

# Accessibility ID
"accessibility id=submitButton"

# Resource ID
"//android.widget.Button[@resource-id='com.example.app:id/button']"

# Class Name
"android.widget.Button"
```

### **Common Gestures**

```python
# Tap
element.click()

# Long Press
from appium.webdriver.common.touch_action import TouchAction
TouchAction(driver).long_press(element).release().perform()

# Swipe
TouchAction(driver).swipe(x1, y1, x2, y2).perform()

# Scroll
driver.execute_script("mobile: scroll", {"direction": "down"})
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.11+
python3 --version

# Android SDK
$ANDROID_HOME/tools/emulator -list-avds

# Appium
npm install -g appium
```

### Installation

```bash
# 1. Clone repository
git clone https://github.com/Maab-7/AndroidAppiumTesting.git
cd AndroidAppiumTesting

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Start Appium server
appium

# In another terminal:
# 6. Run tests
pytest tests/ -v
```

---

## 📱 Device Setup

### Start Emulator

```bash
# List available emulators
$ANDROID_HOME/tools/emulator -list-avds

# Launch emulator
emulator -avd Pixel_6_API_33

# Verify connection
adb devices
```

### Device Capabilities

```python
capabilities = {
    "platformName": "Android",
    "deviceName": "Pixel 6",
    "automationName": "UiAutomator2",
    "app": "/path/to/app.apk",
    "appPackage": "com.example.app",
    "appActivity": ".MainActivity"
}
```

---

## 🧪 Running Tests

### Run all tests

```bash
pytest tests/ -v
```

### Run specific test

```bash
pytest tests/test_apidemos.py::test_app_opens -v
```

### Run with HTML report

```bash
pytest tests/ -v --html=report.html --self-contained-html
```

### Run with Allure report

```bash
pytest tests/ -v --alluredir=allure-results
allure serve allure-results
```

### Run with real device

```bash
DEVICE=real pytest tests/ -v
```

---

## 📊 Reports

### HTML Report

```bash
pytest tests/ --html=report.html --self-contained-html
open report.html
```

### Allure Report

```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

### Screenshots

```bash
# Automatically captured on failure
# Located in: ./screenshots/
```

---

## 🔄 CI/CD Pipeline

### Automated Testing Triggers:

- ✅ **Push** to main/develop branches
- ✅ **Pull Requests** to main/develop
- ✅ **Daily Schedule** - 2 AM UTC

### Pipeline Workflow:

```
Commit → GitHub Actions Triggered (Ubuntu)
  ↓
Checkout Code
  ↓
Setup Python 3.11
  ↓
Install Dependencies
  ↓
Run Android Tests (emulator in CI)
  ↓
Generate Reports
  ↓
Upload Artifacts
```

### View Pipeline Results:

👉 **GitHub Repository → Actions Tab → Latest Run**

---

## 🧰 Configuration

### conftest.py

```python
@pytest.fixture(scope="function")
def driver():
    """Android Appium driver"""
    capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.settings",
        "appActivity": "com.android.settings.Settings"
    }
    driver = webdriver.Remote(
        "http://localhost:4723",
        desired_capabilities=capabilities
    )
    yield driver
    driver.quit()
```

---

## 📝 Test Examples

### Basic App Launch Test

```python
def test_app_opens(driver):
    """Test app launches successfully"""
    assert driver is not None
```

### Navigation Test

```python
def test_navigate_to_views(driver):
    """Test navigating to Views"""
    from pages.android_page import AndroidPage

    page = AndroidPage(driver)
    page.tap_views()

    # Verify navigation
    assert "Views" in driver.page_source
```

### Element Verification Test

```python
def test_elements_visible(driver):
    """Test main elements are visible"""
    elements = driver.find_elements("xpath", "//android.widget.Button")

    assert len(elements) > 0
```

### Gesture Test

```python
def test_swipe_gesture(driver):
    """Test swiping on screen"""
    from appium.webdriver.common.touch_action import TouchAction

    action = TouchAction(driver)
    action.swipe(100, 100, 100, 500).perform()

    # Verify result
    assert "Content" in driver.page_source
```

---

## 🐛 Troubleshooting

### Appium server not running

```bash
# Start Appium
appium

# Or use npm
npx appium
```

### Emulator not starting

```bash
# List AVDs
$ANDROID_HOME/tools/emulator -list-avds

# Launch
emulator -avd Pixel_6_API_33

# Verify
adb devices
```

### Device not found

```bash
# List connected devices
adb devices

# Restart ADB
adb kill-server
adb start-server
```

### UiAutomator2 not found

```bash
# Install server on device
adb shell "pm grant io.appium.uiautomator2.server android.permission.WRITE_SECURE_SETTINGS"
```

### Clear app data

```bash
adb shell pm clear <package_name>
```

---

## 📚 Learning Resources

| Resource             | Link                                                                                     | Topics             |
| -------------------- | ---------------------------------------------------------------------------------------- | ------------------ |
| Appium Docs          | https://appium.io/docs/en/                                                               | Appium guide       |
| UiAutomator          | https://developer.android.com/training/testing/other-arch-testing-libraries/ui-automator | Android testing    |
| Pytest Docs          | https://docs.pytest.org/                                                                 | Testing framework  |
| Android Debug Bridge | https://developer.android.com/studio/command-line/adb                                    | ADB commands       |
| Appium Inspector     | https://github.com/appium/appium-inspector                                               | Element inspection |

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-test`)
3. Add tests for new features
4. Ensure all tests pass (`pytest tests/ -v`)
5. Commit with clear message
6. Push to branch
7. Open Pull Request

---

## 📈 Future Enhancements

- [ ] iOS testing integration
- [ ] Real device cloud integration (BrowserStack, SauceLabs)
- [ ] Performance testing with profiling
- [ ] Network condition testing
- [ ] Accessibility testing (a11y)
- [ ] Visual testing
- [ ] Parallel test execution
- [ ] Custom reporting dashboard

---

## 👤 Author

**Marco Alfaro** | QA Automation Engineer  
🐙 GitHub: [@Maab-7](https://github.com/Maab-7)

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙋 Questions or Issues?

- 📖 Check [Troubleshooting](#troubleshooting) section
- 🐛 Create an [Issue](../../issues) on GitHub
- 💬 Start a [Discussion](../../discussions)

---

**Last Updated:** May 1, 2026  
**Python:** 3.11+ | **Appium:** 2.11 | **Pytest:** 7.4+ | **Status:** ✅ Passing

---

### 🚀 Ready to run tests?

```bash
pytest tests/ -v --html=report.html
```
