# 🌐 Configuración para Google Colab

Para usar esta agenda en Google Colab y guardar en Drive:

1. Ejecuta esto en una celda ANTES del código principal:
```python
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
```

2. Luego ejecuta el programa normalmente.

Los contactos se guardarán en: `MyDrive/AgendaContactos/contactos.json`
