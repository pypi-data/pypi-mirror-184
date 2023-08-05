# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class I18nContextProvider(Component):
    """An I18nContextProvider component.
I18nContextProvider description

Keyword arguments:

- children (a list of or a singular dash component, string or number; required):
    children.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- translations (dict; required):
    translations.

    `translations` is a dict with keys:
"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'I18nContextProvider'
    @_explicitize_args
    def __init__(self, children=None, translations=Component.REQUIRED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'translations']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'translations']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['translations']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(I18nContextProvider, self).__init__(children=children, **args)
