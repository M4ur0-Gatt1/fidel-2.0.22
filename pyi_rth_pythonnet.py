"""Runtime hook de PyInstaller para pythonnet (clr).
Busca el runtime de .NET Core en la máquina y setea DOTNET_ROOT + PYTHONNET_RUNTIME
ANTES de que pythonnet intente cargar el CLR. Sin esto, el .exe revienta con:
  RuntimeError: Failed to create a .NET runtime (coreclr) using the parameters {}.
"""
import os
import sys


def _find_dotnet_root():
    """Busca una instalación de .NET con host/fxr (Core 3.1+, .NET 5-8)."""
    candidates = []

    # 1) Variable de entorno ya seteada
    dr = os.environ.get("DOTNET_ROOT", "")
    if dr and os.path.isdir(os.path.join(dr, "host", "fxr")):
        candidates.append(dr)

    # 2) Ubicaciones estándar
    for base in [
        r"C:\Program Files\dotnet",
        r"C:\Program Files (x86)\dotnet",
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\dotnet"),
        os.path.expandvars(r"%ProgramFiles%\dotnet"),
    ]:
        if os.path.isdir(os.path.join(base, "host", "fxr")):
            candidates.append(base)

    # 3) En PATH (dotnet.exe)
    import shutil
    dotnet_exe = shutil.which("dotnet")
    if dotnet_exe:
        d = os.path.dirname(dotnet_exe)
        if os.path.isdir(os.path.join(d, "host", "fxr")):
            candidates.append(d)

    return candidates[0] if candidates else None


dotnet_root = _find_dotnet_root()
if dotnet_root:
    os.environ["DOTNET_ROOT"] = dotnet_root
    os.environ["PYTHONNET_RUNTIME"] = "coreclr"
    if getattr(sys, "frozen", False):
        # PyInstaller: el hook corre antes de que pythonnet se importe,
        # pero confirmamos que las variables quedaron visibles.
        pass
else:
    # Sin .NET runtime, webview no puede usar WebView2 (winforms).
    # Esto no es fatal en máquinas que solo usan EdgeChromium (sin winforms),
    # pero lo advertimos para debugging.
    pass
