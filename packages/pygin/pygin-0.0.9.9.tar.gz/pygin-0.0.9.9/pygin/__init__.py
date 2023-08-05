import sys
import os


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


blockPrint()
from .collider import Collider
from .color import Color
from .component import Component
from .draw import Draw
from .engine import Engine
from .game_object import GameObject
from .geometry import Geometry
from .input import Input
from .key_frame import KeyFrame
from .material import Material
from .mesh import Mesh
from .scene import Scene
from .time import Time
from .components.physics import Physics
from .components.animation import Animation
from .components.circle_collider import CircleCollider
from .components.animator import Animator
from .components.circle_mesh import CircleMesh
from .components.particle_system import ParticleSystem
from .components.physics import Physics
from .components.polygon_collider import PolygonCollider
from .components.polygon_mesh import PolygonMesh
from .components.text_mesh import TextMesh
from .components.transform import Transform
from .basic_objects.basic_circle import BasicCircle
from .basic_objects.basic_particle_circ import BasicParticleCirc
from .basic_objects.basic_rectangle import BasicRectangle
from .basic_objects.text import Text
enablePrint()
