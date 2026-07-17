"""PyInstaller hook para cffi — recolecta el .pyd compilado (_cffi_backend).

Sin esto, pythonnet → clr_loader → cffi falla con:
    ModuleNotFoundError: No module named 'cffi'

Porque hiddenimports=['cffi'] solo importa el paquete Python pero NO el .pyd
(_cffi_backend.*.pyd) que es el motor C compilado.
"""
from PyInstaller.utils.hooks import (
    collect_submodules,
    collect_data_files,
    collect_dynamic_libs,
)

hiddenimports = collect_submodules('cffi')
hiddenimports.append('_cffi_backend')
datas = collect_data_files('cffi')
binaries = collect_dynamic_libs('cffi')
