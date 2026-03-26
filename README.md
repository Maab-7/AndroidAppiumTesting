# Android Appium Testing

Proyecto de automatización de pruebas Mobile para Android utilizando Appium y Python.

## 🛠️ Tecnologías

- Python 3.11
- Appium 3.x
- Appium Python Client
- UiAutomator2
- Pytest
- Allure Reports
- Jenkins (CI/CD)
- Android Studio (Emulador Pixel 6 - API 33)

## 📁 Estructura del proyecto

```
AndroidAppiumTesting/
├── tests/
│   └── test_apidemos.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## ✅ Casos de prueba

| Test                         | Descripción                                        |
| ---------------------------- | -------------------------------------------------- |
| `test_app_opens`             | Verifica que la app abre correctamente             |
| `test_navigate_to_views`     | Verifica navegación a sección Views                |
| `test_navigate_to_animation` | Verifica navegación a sección Animation            |
| `test_main_elements_present` | Verifica elementos presentes en pantalla principal |

## 🚀 Prerequisitos

- Android Studio instalado
- Emulador Pixel 6 API 33 corriendo
- Appium 3.x instalado y corriendo
- ADB configurado

## 🔧 Instalación y ejecución

### 1. Iniciar emulador

Abrir Android Studio → Virtual Device Manager → Iniciar Pixel 6

### 2. Iniciar Appium

```bash
appium
```

### 3. Clonar el repositorio

```bash
git clone https://github.com/Maab-7/AndroidAppiumTesting.git
cd AndroidAppiumTesting
```

### 4. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar tests

```bash
pytest tests/test_apidemos.py -v
```

### 7. Ver reporte Allure

```bash
allure serve allure-results
```

## 📊 Allure Reports

El proyecto genera reportes detallados con Allure mostrando cada paso de los tests con duración y estado.

## 🔄 CI/CD

El proyecto está integrado con Jenkins para ejecución automática con generación de reportes Allure.

## 🏗️ App de prueba

Se utiliza **ApiDemos** — app oficial de demo de Android para testing.
