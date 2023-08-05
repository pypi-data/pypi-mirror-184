from .scale import Scale
from .utils import config


class ScaleFabric(object):
    @classmethod
    def create_scale(cls, name: str = None, **kwargs: dict):
        if name is None:
            return Scale()
        elif name in config["default_scales"]:
            return Scale(**config["default_scales"][name]["values"])
        else:
            return Scale(**kwargs)
