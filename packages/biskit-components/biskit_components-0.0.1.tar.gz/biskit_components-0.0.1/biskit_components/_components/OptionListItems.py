# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class OptionListItems(Component):
    """An OptionListItems component.
OptionListItems

Keyword arguments:

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

- searchKeyword (string; required)

- selectedValue (dict; required)

    `selectedValue` is a dict with keys:

    - description (string; optional)

    - id (string; required)

    - label (dict; required)

        `label` is a dict with keys:

        - en (string; required)

        - ko (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'OptionListItems'
    @_explicitize_args
    def __init__(self, options=Component.REQUIRED, onClick=Component.REQUIRED, searchKeyword=Component.REQUIRED, selectedValue=Component.REQUIRED, **kwargs):
        self._prop_names = ['options', 'searchKeyword', 'selectedValue']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['options', 'searchKeyword', 'selectedValue']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['options', 'searchKeyword', 'selectedValue']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(OptionListItems, self).__init__(**args)
