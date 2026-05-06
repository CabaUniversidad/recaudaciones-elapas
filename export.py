from pathlib import Path

ROOT_DIR = Path(".").resolve()
OUTPUT_FILE = ROOT_DIR / "codigo_proyecto.txt"

TARGETS = {
    "core": ROOT_DIR / "app" / "core",
    "db": ROOT_DIR / "app" / "db",
    "api": ROOT_DIR / "app" / "api",
    "endpoints": ROOT_DIR / "app" / "api" / "v1" / "endpoints",
    "models": ROOT_DIR / "app" / "models",
    "repositories": ROOT_DIR / "app" / "repositories",
    "schemas": ROOT_DIR / "app" / "schemas",
    "services": ROOT_DIR / "app" / "services",
}

EXCLUDED_DIRS = {
    "__pycache__",
    ".venv",
    "venv",
    ".git",
    ".idea",
    ".vscode",
    "node_modules",
    "dist",
    "build",
    ".pytest_cache",
    ".mypy_cache",
}

EXCLUDED_FILES = {
    ".DS_Store",
}

PROCESADOS = set()


def archivo_valido(path: Path):
    if not path.is_file():
        return False

    if path.suffix != ".py":
        return False

    if path.name in EXCLUDED_FILES:
        return False

    for part in path.parts:
        if part in EXCLUDED_DIRS:
            return False

    return True


def leer_archivo(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")
    except Exception as e:
        return f"ERROR AL LEER: {e}"


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for grupo, carpeta in TARGETS.items():
        if not carpeta.exists():
            continue

        f.write(f"\n[{grupo.upper()}]\n\n")

        archivos = sorted(
            [p for p in carpeta.rglob("*") if archivo_valido(p)]
        )

        for archivo in archivos:
            rel = archivo.relative_to(ROOT_DIR)

            if rel in PROCESADOS:
                continue

            PROCESADOS.add(rel)

            f.write(f"Archivo: {rel}\n")
            f.write("-" * 60 + "\n")
            f.write(leer_archivo(archivo))
            f.write("\n\n")

print(f"Generado: {OUTPUT_FILE}")