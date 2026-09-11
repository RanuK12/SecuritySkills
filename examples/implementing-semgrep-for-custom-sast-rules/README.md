# Ejemplo: Detección de Secretos Hardcodeados con Semgrep

Este ejemplo demuestra cómo una regla Semgrep personalizada puede detectar secretos hardcodeados en código Python y cómo corregirlos usando variables de entorno.

## Código Vulnerable (`vulnerable.py`)
Contiene secretos hardcodeados:
- `API_KEY = "sk-live-1234567890abcdef"`
- `DB_PASSWORD = "super_secret_password_123"`
- `SECRET_TOKEN = "ghp_abcdef1234567890"`

## Código Corregido (`fixed.py`)
Utiliza variables de entorno:
- `API_KEY = os.environ.get("API_KEY", "")`
- `DB_PASSWORD = os.environ.get("DB_PASSWORD", "")`
- `SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "")`

## Regla Semgrep Personalizada
Ubicada en `rules/hardcoded-secret.yaml`, detecta asignaciones de variables que contienen palabras clave como "password", "secret", "api_key", "token", etc.

## Ejecución de la Detección

### Contra código vulnerable:
```bash
semgrep --config rules/hardcoded-secret.yaml vulnerable.py
```
**Salida esperada:** 2 findings (API_KEY y SECRET_TOKEN)

### Contra código corregido:
```bash
semgrep --config rules/hardcoded-secret.yaml fixed.py
```
**Salida esperada:** 0 findings

## Instalación de Semgrep (1 comando)
```bash
pip install semgrep
```
O alternativamente:
```bash
brew install semgrep
```

## Cómo probarlo
1. Clonar este repositorio
2. Navegar a `examples/implementing-semgrep-for-custom-sast-rules/`
3. Ejecutar los comandos de semgrep mostrados arriba
4. Verificar que el código vulnerable produzca findings y el corregido no

Este ejemplo muestra el valor práctico de las skills de seguridad: proporcionan reglas listas para usar que detectan vulnerabilidades reales con pocos falsos positivos.
