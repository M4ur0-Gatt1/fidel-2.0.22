; Instalador de LOW — editor de diseño/animación con agente IA
; Compilar (desde build_exe.py): python build_exe.py release
;   → genera dist/LOW.exe (onefile) y Output/LOWSetup-<ver>.exe
; Manual: ISCC.exe /DAppVersion=3.19.0 low_installer.iss

#define AppName "LOW"
; /DAppVersion se pasa desde build_exe.py. Default solo para build manual.
#ifndef AppVersion
  #define AppVersion "0.0.0-dev"
#endif
#define AppExe "LOW.exe"

[Setup]
AppId={{B7E3D9A4-2C51-4F8E-A6B0-3D94E71C5F28}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher=Mauro Gatti · Tropa Circa
DefaultDirName={localappdata}\Programs\{#AppName}
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
; instalación por usuario: no pide permisos de administrador
PrivilegesRequired=lowest
OutputDir=Output
OutputBaseFilename=LOWSetup-{#AppVersion}
SetupIconFile=low.ico
UninstallDisplayIcon={app}\{#AppExe}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
; En modo release (--onefile) el .exe es autónomo, no necesita DLLs ni carpetas extras.
Source: "dist\{#AppExe}"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppExe}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#AppExe}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#AppExe}"; Description: "{cm:LaunchProgram,{#AppName}}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
; Config e historial quedan en %APPDATA%\LOW por si reinstala.
Type: filesandordirs; Name: "{app}"
