# agenda_crud_json.py - VERSIÓN PARA GOOGLE COLAB + DRIVE
import json
import os
from datetime import datetime

# ==========================================
# CONFIGURACIÓN PARA GOOGLE COLAB
# ==========================================

# Detectar si estamos en Colab
try:
    from google.colab import drive
    EN_COLAB = True
    print("🌐 Ejecutando en Google Colab")
except ImportError:
    EN_COLAB = False
    print("💻 Ejecutando en entorno local")

# Montar Google Drive si estamos en Colab
if EN_COLAB:
    print("\n📂 Montando Google Drive...")
    try:
        drive.mount('/content/drive')
        RUTA_DRIVE = '/content/drive/MyDrive/AgendaContactos'

        # Crear carpeta si no existe
        if not os.path.exists(RUTA_DRIVE):
            os.makedirs(RUTA_DRIVE)
            print(f"✅ Carpeta creada: {RUTA_DRIVE}")

        ARCHIVO_CONTACTOS = os.path.join(RUTA_DRIVE, 'contactos.json')
        print(f"✅ Drive montado correctamente")
        print(f"📍 Los contactos se guardarán en: {ARCHIVO_CONTACTOS}")
    except Exception as e:
        print(f"⚠️  Error al montar Drive: {e}")
        print(f"📍 Usando ubicación temporal: /content/contactos.json")
        ARCHIVO_CONTACTOS = '/content/contactos.json'
else:
    # En local, usar el directorio actual
    ARCHIVO_CONTACTOS = 'contactos.json'

contactos = []

# ==========================================
# FUNCIONES DE VALIDACIÓN
# ==========================================

def validar_telefono(telefono):
    """Valida que el teléfono tenga al menos 10 dígitos"""
    telefono = telefono.strip().replace("-", "").replace(" ", "")
    return telefono.isdigit() and len(telefono) >= 10


def validar_correo(correo):
    """Validación básica de correo electrónico"""
    return "@" in correo and "." in correo.split("@")[1]


def validar_pageweb(pageweb):
    """Validación básica de página web"""
    return "." in pageweb and " " not in pageweb


# ==========================================
# FUNCIONES DE PERSISTENCIA (JSON)
# ==========================================

def cargar_contactos():
    """Carga los contactos desde un archivo JSON"""
    global contactos
    try:
        if os.path.exists(ARCHIVO_CONTACTOS):
            with open(ARCHIVO_CONTACTOS, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                if isinstance(datos, list):
                    contactos = datos
                elif isinstance(datos, dict) and 'contactos' in datos:
                    contactos = datos['contactos']
                else:
                    contactos = []
            print(f"✅ {len(contactos)} contacto(s) cargado(s)")
        else:
            print(f"📁 No hay contactos guardados. Comenzando nueva agenda.")
            contactos = []
    except json.JSONDecodeError:
        print(f"⚠️  Error al leer el archivo. Iniciando nueva agenda.")
        contactos = []
    except Exception as e:
        print(f"❌ Error: {e}")
        contactos = []


def guardar_contactos():
    """Guarda los contactos en un archivo JSON"""
    try:
        with open(ARCHIVO_CONTACTOS, "w", encoding="utf-8") as archivo:
            json.dump(contactos, archivo, indent=4, ensure_ascii=False)
        print(f"💾 Guardado en: {ARCHIVO_CONTACTOS}")

        # Verificar que se guardó correctamente
        if os.path.exists(ARCHIVO_CONTACTOS):
            tamaño = os.path.getsize(ARCHIVO_CONTACTOS)
            print(f"✅ Confirmado ({tamaño} bytes)")
            return True
        else:
            print(f"⚠️  No se pudo verificar el guardado")
            return False
    except Exception as e:
        print(f"❌ Error al guardar: {e}")
        return False


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("        📇 AGENDA DE CONTACTOS")
    if EN_COLAB:
        print("        🌐 Modo: Google Colab + Drive")
    print("="*50)
    print("1. 👤 Agregar contacto")
    print("2. 📋 Listar contactos")
    print("3. 🔍 Buscar contacto")
    print("4. ✏️  Editar contacto")
    print("5. 🗑️  Eliminar contacto")
    print("6. 📊 Estadísticas")
    print("7. 💾 Guardar y salir")
    print("="*50)

    while True:  # ← ESTO ES CLAVE
        opcion = input("Selecciona (1-7): ").strip()
        if opcion in ["1", "2", "3", "4", "5", "6", "7"]:
            return opcion
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")




# ==========================================
# CRUD: CREATE (Añadir)
# ==========================================

def anadir_contacto():
    """Añade un nuevo contacto a la agenda"""
    print("\n" + "="*50)
    print("👤 Agregar nuevo contacto")
    print("="*50)

    # Nombre completo (requerido)
    while True:
        nombre = input("\n📛 Nombre completo: ").strip()
        if nombre:
            break
        print("⚠️ El nombre no puede estar vacío.")


    # Nombre favorito (opcional)
    nombre_favorito = input("💝 Nombre favorito (Enter para omitir): ").strip()

    # Teléfono (opcional)
    telefono = ""
    while True:
        telefono = input("📱 Teléfono (Enter para omitir): ").strip()
        if not telefono:
            break
        if validar_telefono(telefono):
            break
        print("⚠️ El teléfono debe tener al menos 10 dígitos")

    # Correo (opcional)
    correo = ""
    while True:
        correo = input("📧 Correo electrónico (Enter para omitir): ").strip()
        if not correo:
            break
        if validar_correo(correo):
            break
        print("⚠️ Formato de correo inválido")

    # Página web (opcional)
    pageweb = ""
    while True:
        pageweb = input("🌐 Página web (Enter para omitir): ").strip()
        if not pageweb:
            break
        if validar_pageweb(pageweb):
            break
        print("⚠️ Formato inválido (ej: ejemplo.com)")

    # Al menos uno debe existir
    if not telefono and not correo:
        print("\n⚠️  Debes ingresar al menos teléfono o correo")
        while not telefono and not correo:
            telefono = input("📱 Teléfono: ").strip()
            if telefono and not validar_telefono(telefono):
                print("⚠️ Teléfono inválido")
                telefono = ""
                continue

            if not telefono:
                correo = input("📧 Correo electrónico: ").strip()
                if correo and not validar_correo(correo):
                    print("⚠️ Correo inválido")
                    correo = ""

    # Campos opcionales
    cumples = input("🎂 Cumpleaños (Enter para omitir): ").strip()
    foco = input("🎯 Categoría (Enter para omitir): ").strip()
    nota = input("📝 Nota (Enter para omitir): ").strip()

    # Crear contacto
    contacto = {
        'nombre': nombre,
        'nombre_favorito': nombre_favorito,
        'telefono': telefono,
        'correo': correo,
        'pageweb': pageweb,
        'cumples': cumples,
        'foco': foco,
        'nota': nota,
        'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    contactos.append(contacto)
    guardar_contactos()  # Auto-guardar
    print(f"\n✅ {nombre} agregado exitosamente")


# ==========================================
# CRUD: READ (Listar y Buscar)
# ==========================================

def ver_contactos():
    """Muestra todos los contactos"""
    print("\n" + "="*50)
    print("        📋 LISTA DE CONTACTOS")
    print("="*50)

    if len(contactos) == 0:
        print("📭 No hay contactos registrados")
        return

    for i, contacto in enumerate(contactos):
        print(f"\n{i + 1}. {contacto['nombre']}")
        if contacto.get('nombre_favorito'):
            print(f"   💝 Apodo: {contacto['nombre_favorito']}")
        if contacto.get('telefono'):
            print(f"   📱 Teléfono: {contacto['telefono']}")
        if contacto.get('correo'):
            print(f"   📧 Email: {contacto['correo']}")
        if contacto.get('pageweb'):
            print(f"   🌐 Web: {contacto['pageweb']}")
        if contacto.get('cumples'):
            print(f"   🎂 Cumpleaños: {contacto['cumples']}")
        if contacto.get('foco'):
            print(f"   🎯 Foco: {contacto['foco']}")
        if contacto.get('nota'):
            print(f"   📝 Nota: {contacto['nota']}")


def buscar_contacto():
    """Busca un contacto por nombre, teléfono o correo"""
    print("\n" + "="*50)
    print("        🔍 BUSCAR CONTACTO")
    print("="*50)

    buscar = input("\nBuscar por nombre/teléfono/correo: ").strip().lower()

    encontrados = []
    for contacto in contactos:
        nombre_match = buscar in contacto['nombre'].lower()
        telefono_match = buscar in contacto.get('telefono', '')
        correo_match = buscar in contacto.get('correo', '').lower()

        if nombre_match or telefono_match or correo_match:
            encontrados.append(contacto)

    if len(encontrados) == 0:
        print("⚠️ No se encontraron contactos")
    else:
        print(f"\n✅ {len(encontrados)} contacto(s) encontrado(s):")
        for contacto in encontrados:
            info = contacto['nombre']
            if contacto.get('telefono'):
                info += f" - 📱 {contacto['telefono']}"
            if contacto.get('correo'):
                info += f" - 📧 {contacto['correo']}"
            print(f"   • {info}")


# ==========================================
# CRUD: UPDATE (Editar)
# ==========================================

def editar_contacto():
    """Edita un contacto existente"""
    print("\n" + "="*50)
    print("        ✏️  EDITAR CONTACTO")
    print("="*50)

    if len(contactos) == 0:
        print("📭 No hay contactos registrados")
        return

    ver_contactos()

    try:
        entrada = input("\nNúmero (o 'c' para cancelar): ").strip()

        if entrada.lower() == 'c':  # ← CANCELAR
            print("⚠️ Operación cancelada")
            return

        indice = int(entrada) - 1

        if indice < 0 or indice >= len(contactos):
            print("⚠️ Número inválido")
            return

        contacto = contactos[indice]
        print(f"\n✏️  Editando: {contacto['nombre']}")
        print("💡 Tip: Escribe 'c' para cancelar")

        # Nombre
        print(f"\nNombre: {contacto['nombre']}")
        nuevo = input("Nuevo (Enter=mantener, c=cancelar): ").strip()
        if nuevo.lower() == 'c':
            print("⚠️ Edición cancelada")
            return
        if nuevo:
            contacto['nombre'] = nuevo

        # Teléfono
        print(f"\nTeléfono: {contacto.get('telefono', 'Sin teléfono')}")
        nuevo = input("Nuevo (Enter=mantener, c=cancelar): ").strip()
        if nuevo.lower() == 'c':
            print("⚠️ Edición cancelada")
            return
        if nuevo and validar_telefono(nuevo):
            contacto['telefono'] = nuevo

        # Correo
        print(f"\nCorreo: {contacto.get('correo', 'Sin correo')}")
        nuevo = input("Nuevo (Enter=mantener, c=cancelar): ").strip()
        if nuevo.lower() == 'c':
            print("⚠️ Edición cancelada")
            return
        if nuevo and validar_correo(nuevo):
            contacto['correo'] = nuevo

        # Página web
        print(f"\nWeb: {contacto.get('pageweb', 'Sin web')}")
        nuevo = input("Nueva (Enter=mantener, c=cancelar): ").strip()
        if nuevo.lower() == 'c':
            print("⚠️ Edición cancelada")
            return
        if nuevo and validar_pageweb(nuevo):
            contacto['pageweb'] = nuevo

        guardar_contactos()
        print(f"\n✅ Contacto actualizado")

    except ValueError:
        print("⚠️ Número inválido")



# ==========================================
# CRUD: DELETE (Eliminar)
# ==========================================

def eliminar_contacto():
    """Elimina un contacto existente"""
    print("\n" + "="*50)
    print("        🗑️  ELIMINAR CONTACTO")
    print("="*50)

    if len(contactos) == 0:
        print("📭 No hay contactos registrados")
        return

    ver_contactos()

    try:
        entrada = input ("\nNumero de contacto a eliminar (o 'c' para cancelar):").strip()
        if entrada.lower() == 'c':
            print("⚠️ Operación cancelada")
            return
        indice = int(entrada) - 1
        if indice < 0 or indice >= len(contactos):
            print("⚠️ Número inválido")
            return

        contacto = contactos[indice]
        confirmar = input(f"\n⚠️  ¿Eliminar a {contacto['nombre']}? (s/n): ")

        if confirmar.lower() == 's':
            contactos.pop(indice)
            guardar_contactos()  # Auto-guardar
            print(f"✅ Contacto eliminado")
        else:
            print("⚠️ Operación cancelada")

    except ValueError:
        print("⚠️ Debes ingresar un número válido")


# ==========================================
# ESTADÍSTICAS
# ==========================================

def mostrar_estadisticas():
    """Muestra estadísticas de la agenda"""
    print("\n" + "="*50)
    print("        📊 ESTADÍSTICAS DE LA AGENDA")
    print("="*50)

    if len(contactos) == 0:
        print("📭 No hay contactos")
        return

    print(f"\n📇 Total: {len(contactos)}")
    print(f"📱 Con teléfono: {sum(1 for c in contactos if c.get('telefono'))}")
    print(f"📧 Con correo: {sum(1 for c in contactos if c.get('correo'))}")
    print(f"🌐 Con web: {sum(1 for c in contactos if c.get('pageweb'))}")  # ← FALTABA
    print(f"🎂 Con cumpleaños: {sum(1 for c in contactos if c.get('cumples'))}")
    print(f"📝 Con notas: {sum(1 for c in contactos if c.get('nota'))}")

    # Categorías
    focos = {}
    for contacto in contactos:
        foco = contacto.get('foco', '')
        if foco:
            focos[foco] = focos.get(foco, 0) + 1

    if focos:
        print(f"\n🎯 Categorías:")
        for foco, cant in sorted(focos.items(), key=lambda x: x[1], reverse=True):
            print(f"   • {foco}: {cant}")

# ==========================================
# FUNCIÓN PRINCIPAL
# ==========================================

def main():
    """Función principal"""
    print("\n" + "🌟"*25)
    print("  ¡Bienvenido a la Agenda de Contactos!")
    if EN_COLAB:
        print("  🌐 Versión para Google Colab + Drive")
    print("🌟"*25)

    cargar_contactos()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            anadir_contacto()
        elif opcion == "2":
            ver_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            editar_contacto()
        elif opcion == "5":
            eliminar_contacto()
        elif opcion == "6":
            mostrar_estadisticas()
        elif opcion == "7":
            print("\n💾 Guardando...")
            guardar_contactos()
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida")

        input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()

