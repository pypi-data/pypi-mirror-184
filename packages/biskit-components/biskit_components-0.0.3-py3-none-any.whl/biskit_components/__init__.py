"""Bootstrap themed components for use in Plotly Dash"""
import os

from biskit_components import _components
from biskit_components._components import *  # noqa
from biskit_components._version import __version__


__all__ = _components.__all__

_current_path = os.path.dirname(os.path.abspath(__file__))
_METADATA_PATH = os.path.join(_current_path, "_components", "metadata.json")

_js_dist = [
    {
        "relative_package_path": (
            "_components/biskit_components.min.js"
        ),
        "namespace": "biskit_components",
    }
]

_css_dist = []


for _component_name in _components.__all__:
    _component = getattr(_components, _component_name)
    _component._js_dist = _js_dist
    _component._css_dist = _css_dist
