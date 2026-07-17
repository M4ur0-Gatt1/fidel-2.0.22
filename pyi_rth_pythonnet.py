"""Runtime hook de PyInstaller para pythonnet (clr).

Busca el runtime de .NET en la máquina y setea las variables de entorno
ANTES de que pythonnet/clr_loader intente cargar el CLR. Sin esto, el .exe
revienta con:
  RuntimeError: Failed to create a .NET runtime (coreclr/netfx).

Estrategia:
- Si hay .NET Core/5+ → DOTNET_ROOT + PYTHONNET_RUNTIME=coreclr
- Si no → no tocamos nada: pythonnet usará netfx (.NET Framework 4.x de Windows)
- cffi DEBE estar incluido en el build (hidden import en el .spec)
"""
import os
import sys


def _find_dotnet_core():
    """Busca .NET Core/5+ (host/fxr). Devuelve el root o None."""
    candidates = []

    dr = os.environ.get("DOTNET_ROOT", "")
    if dr and os.path.isdir(os.path.join(dr, "host", "fxr")):
        candidates.append(dr)

    for base in [
        r"C:\Program Files\dotnet",
        r"C:\Program Files (x86)\dotnet",
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\dotnet"),
        os.path.expandvars(r"%ProgramFiles%\dotnet"),
    ]:
        if os.path.isdir(os.path.join(base, "host", "fxr")):
            candidates.append(base)

    import shutil
    dotnet_exe = shutil.which("dotnet")
    if dotnet_exe:
        d = os.path.dirname(dotnet_exe)
        if os.path.isdir(os.path.join(d, "host", "fxr")):
            candidates.append(d)

    return candidates[0] if candidates else None


dotnet_root = _find_dotnet_core()

if dotnet_root:
    # .NET Core encontrado → lo usamos
    os.environ["DOTNET_ROOT"] = dotnet_root
    os.environ["PYTHONNET_RUNTIME"] = "coreclr"
else:
    # Sin .NET Core → pythonnet usará netfx (el .NET Framework nativo de Windows).
    # No seteamos nada; pythonnet lo detecta automáticamente.
    # Solo advertimos si PYTHONNET_RUNTIME estaba forzado a coreclr sin DOTNET_ROOT.
    if os.environ.get("PYTHONNET_RUNTIME") == "coreclr":
        del os.environ["PYTHONNET_RUNTIME"]
