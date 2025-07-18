# 🧪 Selenium Cross-Browser Testing with GitHub Actions

Este proyecto ejecuta pruebas automatizadas en múltiples navegadores (Chrome, Firefox, Safari y Brave) usando Selenium, Pytest y GitHub Actions. Las pruebas verifican contenido clave en la página de GitHub y generan reportes HTML para cada navegador.

---

## 🚀 Tecnologías utilizadas

- 🐍 Python 3.12
- ✅ Pytest + pytest-html
- 🌐 Selenium WebDriver
- 💻 Navegadores:
  - Chrome
  - Firefox
  - Safari (solo en macOS)
  - Brave
- 🔄 GitHub Actions (CI/CD)

---

## 📂 Estructura del proyecto

```
.
├── .github/
│   └── workflows/
│       └── pytest.yml            # CI/CD para ejecución de pruebas
├── test_cross_browser_github.py  # Script principal de pruebas
├── requirements.txt              # Dependencias de Python
└── README.md                     # Este archivo
```

---

## 📋 Requisitos

- Python 3.12+
- Navegadores instalados localmente si se ejecutan las pruebas fuera de CI
- ChromeDriver y GeckoDriver disponibles en el sistema o configurados por Selenium Manager

---

## 📦 Instalación

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🧪 Ejecutar pruebas localmente

Por defecto ejecuta con Chrome:

```bash
pytest test_cross_browser_github.py --html=report.html --self-contained-html
```

Ejecutar con otro navegador (ejemplo: Firefox):

```bash
BROWSER=firefox pytest test_cross_browser_github.py --html=report_firefox.html --self-contained-html
```

Valores válidos para `BROWSER`: `chrome`, `firefox`, `brave`, `safari`

> ⚠️ Para Brave, asegúrate que esté instalado y accesible en `/usr/bin/brave-browser`.

---

## 🛠️ GitHub Actions

El proyecto incluye un flujo de trabajo (`.github/workflows/pytest.yml`) que:

- Instala Python, Chrome y Firefox
- Ejecuta pruebas con diferentes navegadores
- Genera y sube reportes HTML como artefactos

---

## 📊 Reportes

Los reportes se generan con `pytest-html` y están disponibles como artefactos de GitHub Actions en cada run.

---

## ✍️ Autor

Luis Sánchez  
📫 [hlcxpl@gmaill.com]

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT.
