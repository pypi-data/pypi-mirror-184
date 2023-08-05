# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Layout(Component):
    """A Layout component.
Layout Component

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- Header (a list of or a singular dash component, string or number; required):
    Header Children.

- PageContent (a list of or a singular dash component, string or number; optional):
    pageContent Children.

- dashboards (list of dicts; required):
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

- languageSelect (a list of or a singular dash component, string or number; optional)

- translations (dict; required):
    translations Children.

    `translations` is a dict with keys:
"""
    _children_props = ['Header', 'PageContent', 'languageSelect']
    _base_nodes = ['Header', 'PageContent', 'languageSelect', 'children']
    _namespace = 'biskit_components'
    _type = 'Layout'
    @_explicitize_args
    def __init__(self, dashboards=Component.REQUIRED, Header=Component.REQUIRED, translations=Component.REQUIRED, PageContent=Component.UNDEFINED, languageSelect=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'Header', 'PageContent', 'dashboards', 'languageSelect', 'translations']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'Header', 'PageContent', 'dashboards', 'languageSelect', 'translations']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['Header', 'dashboards', 'translations']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Layout, self).__init__(**args)
