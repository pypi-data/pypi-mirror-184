# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tooltip(Component):
    """A Tooltip component.
tooltip의 위치를 기준 삼을 컴포넌트에 position: relatvie 적용해야 합니다.
상위 엘리먼트에서 .biskit__tooltip 으로 선택자를 잡아 컨트롤 합니다.

Keyword arguments:

- description (a list of or a singular dash component, string or number; required)

- position (a value equal to: 'top', 'topLeft', 'topRight', 'bottom', 'bottomLeft', 'bottomRight', 'left', 'right'; optional)

- title (a list of or a singular dash component, string or number; optional)"""
    _children_props = ['description', 'title']
    _base_nodes = ['description', 'title', 'children']
    _namespace = 'biskit_components'
    _type = 'Tooltip'
    @_explicitize_args
    def __init__(self, description=Component.REQUIRED, title=Component.UNDEFINED, position=Component.UNDEFINED, **kwargs):
        self._prop_names = ['description', 'position', 'title']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['description', 'position', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['description']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Tooltip, self).__init__(**args)
