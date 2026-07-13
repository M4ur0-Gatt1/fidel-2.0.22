"""LOW Animation Studio — motor de animación 2D vectorial con IA.

Formato nativo: SVG (ilustración vectorial editable).
Animación: keyframes en JSON (timeline), interpolación con curvas-bezier.
Rigging: huesos sobre paths SVG.
Exportación: secuencia de PNG/JPG → video MP4, GIF, o SVG animado SMIL.

Integración IA:
  • generate_image / edit_image → diseño de personajes y escenas
  • animate_image / generate_video → aceleración de cuadros clave
  • ask_model → guiones, storyboard, asistente de animación

Referencia: Harmony/Toon Boom, OpenToonz, Moho, After Effects, Spine.
"""

from .core import AnimationEngine, Scene, Layer, Bone, Keyframe
from .timeline import Timeline, Track, EasingCurve
from .exporter import Exporter, RenderSettings
from .rigging import Rig, BoneSystem, IK_solver
from .ai_pipeline import AIPipeline, CharacterGenerator, PoseMaker, SceneComposer

__all__ = [
    "AnimationEngine", "Scene", "Layer", "Bone", "Keyframe",
    "Timeline", "Track", "EasingCurve",
    "Exporter", "RenderSettings",
    "Rig", "BoneSystem", "IK_solver",
    "AIPipeline", "CharacterGenerator", "PoseMaker", "SceneComposer",
]