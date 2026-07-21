"""Reemplaza TODOS los emojis del proyecto por iconos Font Awesome — v2 corregida."""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))

# ── Mapa emoji → (texto_python, fa_class, fa_unicode)
# fa_unicode se usa en CSS content
MAP = {
    # low_anim.py
    0x1F9B4: ('[Rig]', 'fa-bone', 'f5d7'),              # [Rig]
    0x1F4CB: ('[Storyboard]', 'fa-clipboard-list', 'f46d'),  # [Storyboard]
    0x1F4AC: ('[Dialogo]', 'fa-comment-dots', 'f4ad'),   # [Dialogo]
    # main.py / main_ctk.py
    0x1F464: ('[Personaje]', 'fa-user', 'f007'),          # [Personaje]
    0x1F9EC: ('[Variacion]', 'fa-dna', 'f471'),           # [Variacion]
    0x1F3AE: ('[App]', 'fa-gamepad', 'f11b'),            # [App]
    0x1F4E3: ('[Post]', 'fa-bullhorn', 'f0a1'),          # [Post]
    0x1F50C: ('[SSH]', 'fa-plug', 'f1e6'),               # [SSH]
    0x1F4E4: ('[Upload]', 'fa-upload', 'f093'),          # [Upload]
    0x1F22F: ('[Prompt]', 'fa-language', 'f1ab'),        # [Prompt]
    0x1F7E1: ('[Amarillo]', 'fa-circle', 'f111'),        # [Amarillo]
    0x1F3C6: ('[Ranking]', 'fa-trophy', 'f091'),         # [Ranking]
    0x1F50E: ('[Buscar]', 'fa-search', 'f002'),          # [Buscar]
    0x1F5A7: ('[Red]', 'fa-network-wired', 'f6ff'),      # [Red]
    0x1F9CA: ('[Assets]', 'fa-cube', 'f1b2'),            # [Assets]
    0x2712:  ('[Diseno]', 'fa-pen-fancy', 'f5ac'),       # [Diseno]
    0x25A6:  ('[Grid]', 'fa-th', 'f00a'),                # [Grid]
    0x1F512: ('[Bloqueado]', 'fa-lock', 'f023'),         # [Bloqueado]
    0x1F3A5: ('[Video]', 'fa-video', 'f03d'),            # [Video]
    0x1F3AD: ('[Diorama]', 'fa-masks-theater', 'f630'),  # [Diorama]
    0x1F9C5: ('[Onion]', 'fa-layer-group', 'f5fd'),      # [Onion]
    0x1F511: ('[Clave]', 'fa-key', 'f084'),               # [Clave]
    0x1F4F9: ('[Camara]', 'fa-camera-movie', 'f8a9'),    # [Camara]
    0x1FA9E: ('[Espejo]', 'fa-sync-alt', 'f2f1'),        # [Espejo]
    0x1F58C: ('[Pincel]', 'fa-paint-brush', 'f1fc'),     # [Pincel]
    0x1F3A6: ('[Film]', 'fa-film', 'f008'),              # [Film]
    0x23FA:  ('[Grabar]', 'fa-stop-circle', 'f28d'),     # [Grabar]
    0x1F3C3: ('[Run]', 'fa-running', 'f70c'),            # [Run]
    0x1F999: ('[Ollama]', 'fa-robot', 'f544'),           # [Ollama]
    0x1F4A1: ('[Idea]', 'fa-lightbulb', 'f0eb'),         # [Idea]
    0x26A1:  ('[Rapido]', 'fa-bolt', 'f0e7'),            # [Rapido]
    0x270F:  ('[Editar]', 'fa-pencil-alt', 'f303'),      # [Editar]
    0x1F4DD: ('[Nota]', 'fa-sticky-note', 'f249'),       # [Nota]
    0x1F4C1: ('[Carpeta]', 'fa-folder', 'f07b'),         # [Carpeta]
    0x1F4C4: ('[Archivo]', 'fa-file-alt', 'f15c'),       # [Archivo]
    0x1F4E5: ('[Download]', 'fa-download', 'f019'),      # [Download]
    0x1F4A5: ('[Error]', 'fa-exclamation-triangle', 'f071'), # [Error]
    0x2699:  ('[Config]', 'fa-cog', 'f013'),             # [Config]
    0x1F527: ('[Tools]', 'fa-wrench', 'f0ad'),           # [Tools]
    0x1F4C8: ('[Stats]', 'fa-chart-line', 'f201'),       # [Stats]
    0x23F0:  ('[Hora]', 'fa-clock', 'f017'),             # [Hora]
    0x1F514: ('[Alerta]', 'fa-bell', 'f0f3'),            # [Alerta]
    0x2705:  ('[OK]', 'fa-check-circle', 'f058'),        # [OK]
    0x274C:  ('[ERROR]', 'fa-times-circle', 'f057'),     # [ERROR]
    0x26A0:  ('[WARN]', 'fa-exclamation-triangle', 'f071'), # [WARN]
    0x2139:  ('[INFO]', 'fa-info-circle', 'f05a'),       # [INFO]
    0x1F6AB: ('[Prohibido]', 'fa-ban', 'f05e'),          # [Prohibido]
    0x1F44D: ('[Like]', 'fa-thumbs-up', 'f164'),         # [Like]
    0x1F44E: ('[Dislike]', 'fa-thumbs-down', 'f165'),    # [Dislike]
    0x1F389: ('[Festejo]', 'fa-glass-cheers', 'f79f'),   # [Festejo]
    0x1F4A8: ('[Rapido]', 'fa-wind', 'f72e'),            # [Rapido]
    0x1F680: ('[Rocket]', 'fa-rocket', 'f135'),          # [Rocket]
    0x2B50:  ('[Estrella]', 'fa-star', 'f005'),          # [Estrella]
    0x1F31F: ('[Destacado]', 'fa-star', 'f005'),         # [Destacado]
    0x1F525: ('[Fire]', 'fa-fire', 'f06d'),              # [Fire]
    0x1F48E: ('[Gema]', 'fa-gem', 'f3a5'),               # [Gema]
    0x1F3A8: ('[Paleta]', 'fa-palette', 'f53f'),         # [Paleta]
    0x1F4A3: ('[Bomba]', 'fa-bomb', 'f1e2'),             # [Bomba]
    0x1F4A2: ('[Explosion]', 'fa-burst', 'f7b6'),        # [Explosion]
}

def replace_in_file(fp, ext):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new = content
    count = 0
    
    for cp, (text, fa_class, fa_unicode) in MAP.items():
        ch = chr(cp)
        if ch not in new:
            continue
        
        if ext == '.py':
            # Python: texto descriptivo
            new = new.replace(ch, text)
            count += 1
        elif ext == '.css':
            # CSS: en content usar FA unicode, en comentarios eliminar
            # Para content: "[Camara]" → "\f8a9" y agregar font-family
            # Buscar patrones content: "X"
            pass  # se maneja abajo
        elif ext in ('.js', '.html'):
            # Frontend: usar <i> tag
            new = new.replace(ch, f'<i class="fas {fa_class}"></i>')
            count += 1
        elif ext == '.md':
            new = new.replace(ch, f'`{text}`')
            count += 1
    
    if ext == '.css':
        # Reemplazos especiales para CSS: emojis en comentarios y content
        for cp, (text, fa_class, fa_unicode) in MAP.items():
            ch = chr(cp)
            if ch not in new:
                continue
            # Si está en un comentario (/* ... */), simplemente eliminar o poner nombre
            # Si está en content: "X", reemplazar por código FA
            # Detectar si está dentro de content:
            lines = new.split('\n')
            new_lines = []
            for line in lines:
                if ch in line:
                    if 'content:' in line and ch in line:
                        # Reemplazar el emoji en content por código FA
                        line = line.replace(f'"{ch}"', f'"\\{fa_unicode}"')
                        # Agregar font-family si no existe
                        if 'font-family' not in line:
                            indent = line[:len(line) - len(line.lstrip())]
                            line = line.rstrip() + f'\n{indent}font-family: "Font Awesome 5 Free"; font-weight: 900;'
                    elif '/*' in line and '*/' in line:
                        # Comentario: eliminar emoji
                        line = line.replace(ch, text)
                    else:
                        line = line.replace(ch, text)
                new_lines.append(line)
            new = '\n'.join(new_lines)
            count += content.count(ch)
    
    if new != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
        return count
    return 0

# Procesar todos los archivos
FILES = [
    'main.py', 'main_ctk.py', 'low_anim.py', 'self_improvement.py',
    'config.py', 'build_exe.py', 'README.md',
    'ui/app.js', 'ui/app.css', 'ui/index.html', 'ui/diag-tablet.html',
    'low_installer.iss',
]

# Agregar providers y tools
for root, dirs, fs in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in ('.git','__pycache__','node_modules','dist','build','Output','social','animation_engine','code_runner','design_handoff_low_editor','docs')]
    for f in fs:
        if f.endswith(('.py','.js','.css','.html','.md','.iss')):
            FILES.append(os.path.relpath(os.path.join(root, f), BASE))

changed = 0
for rel in sorted(set(FILES)):
    fp = os.path.join(BASE, rel)
    if not os.path.exists(fp):
        continue
    ext = os.path.splitext(fp)[1]
    n = replace_in_file(fp, ext)
    if n:
        print(f'OK  {rel}  ({n} reemplazos)')
        changed += 1

print(f'\nTotal: {changed} archivos modificados')
