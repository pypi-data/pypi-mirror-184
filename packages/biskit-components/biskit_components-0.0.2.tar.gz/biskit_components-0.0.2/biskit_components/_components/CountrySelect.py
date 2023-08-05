# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CountrySelect(Component):
    """A CountrySelect component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- key (string; optional)

- options (list of dicts; required)

    `options` is a list of dicts with keys:

    - countries (list of dicts; required)

        `countries` is a list of dicts with keys:

        - description (string; optional)

        - id (string; required)

        - label (dict; required)

            `label` is a dict with keys:

            - en (string; required)

            - ko (string; required)

    - depthOrder (number; required)

    - id (string; required)

    - label (dict; optional)

        `label` is a dict with keys:

        - en (string; required)

        - ko (string; required)

- searchPlaceholder (string; required)

- value (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'CountrySelect'
    @_explicitize_args
    def __init__(self, options=Component.REQUIRED, value=Component.UNDEFINED, searchPlaceholder=Component.REQUIRED, key=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'options', 'searchPlaceholder', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'options', 'searchPlaceholder', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['options', 'searchPlaceholder']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(CountrySelect, self).__init__(**args)
