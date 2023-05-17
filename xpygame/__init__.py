__all__ = [
    "draw",
    "display",
    "mixer",
    "font",
    "Vec2",
    "Vec3",
    "init"
]


import os


os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


from pygame import Vector2, Vector3, draw as _draw, display as _disp, mixer as _mixer, font as _font, init as _init

class draw:
    circle = _draw.circle
    rect = _draw.rect
    polygon = _draw.polygon
    line = _draw.line

    @staticmethod
    def arrow(sc,cl,ps,xl=10,
              angle=45,vec=None):
        if len(ps) < 2:
            raise ValueError("arrow should have at least two keypoints")
        for n in range(len(ps)):
            ps[n] = Vec2(ps[n])
        for n in range(len(ps)-1):
            draw.line(sc,cl,ps[n],ps[n+1])
        if not vec:
            vec = (Vector2(ps[-1])-Vector2(ps[-2])).\
            normalize()

        vec1 = vec.rotate(180-angle/2)
        vec2 = vec.rotate(-180+angle/2)
        px1 = Vector2(ps[-1])+vec1*xl
        px2 = Vector2(ps[-1])+vec2*xl
        draw.polygon(sc,cl,(ps[-1],px1,px2),0)


class display:
    set_caption = _disp.set_caption
    set_icon = _disp.set_icon
    get_surface = _disp.get_surface
    quit = _disp.quit
    flags = 0

    @staticmethod
    def set_mode(size, flags=0):
        _disp.set_mode(tuple(int(s) for s in size), flags|HWACCEL|HWPALETTE|HWSURFACE|DOUBLEBUF)
        display.flags = flags

    @staticmethod
    def resize(size):
        size = Vec2(size)
        display.set_mode(size, display.flags)


class mixer(_mixer):
    ...


class font:
    get_fonts = _font.get_fonts
    from_file = _font.Font
    from_system = _font.SysFont

    @staticmethod
    def new_font(families,size):
        found = None
        fp = 0
        for file in os.listdir("."):
            if file.endswith(".ttf"):
                for f in families.split("  "):
                    if file.removesuffix(".ttf") == f:
                        found = file
                        fp = 1
                    if found:
                        break
            if found:
                break
        if not found:
            for f in families.split("  "):
                if f in _font.get_fonts():
                    found = f
        if fp:
            return _font.Font(found, size)
        else:
            return _font.sysfont(found, size)

    @staticmethod
    def is_installed(family):
        found = None
        fp = 0
        for file in os.listdir("."):
            if file.endswith(".ttf"):
                for f in families.split("  "):
                    if file.removesuffix(".ttf") == f:
                        found = file
                        fp = 1
                    if found:
                        break
            if found:
                break
        if not found:
            for f in families.split("  "):
                if f in _font.get_fonts():
                    found = f
        return found


class Vec2(Vector2):
    ...


class Vec3(Vector3):
    ...


def init():
    _disp.init()
    _font.init()
    _mixer.init()
    _init()
