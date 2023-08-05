# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class SideBar(Component):
    """A SideBar component.
SideBar Component

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- dashboards (list of dicts; optional):
    Dashboard Item Array.

    `dashboards` is a list of dicts with keys:

    - iconURL (string; required)

    - id (string; required)

    - label (string; required)

    - menus (list of dicts; required)

        `menus` is a list of dicts with keys:

        - items (list of dicts; required)

            `items` is a list of dicts with keys:

            - disabled (boolean; optional)

            - label (string; required)

            - pages (list of strings; optional)

            - to (string; required)

        - label (string; required)

- languageSelect (a list of or a singular dash component, string or number; optional)"""
    _children_props = ['languageSelect']
    _base_nodes = ['languageSelect', 'children']
    _namespace = 'biskit_components'
    _type = 'SideBar'
    @_explicitize_args
    def __init__(self, dashboards=Component.UNDEFINED, languageSelect=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'dashboards', 'languageSelect']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'dashboards', 'languageSelect']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(SideBar, self).__init__(**args)
