import requests
import json

URL = "https://raia-actualizar.jdomfer870.workers.dev/"
FILE_PATH = "censoPublico.json"

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; GitHubActions/1.0)",
    "Accept": "application/json"
}

print("🔄 Descargando datos desde RAIA...")
try:
    r = requests.get(URL, headers=headers, timeout=200)
    r.raise_for_status()
    data = r.json()

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Datos actualizados correctamente ({len(data)} registros).")

except requests.exceptions.RequestException as e:
    print(f"❌ Error al conectar con RAIA: {e}")

