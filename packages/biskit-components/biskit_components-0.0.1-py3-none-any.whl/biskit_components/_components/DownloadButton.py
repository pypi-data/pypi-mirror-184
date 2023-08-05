# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DownloadButton(Component):
    """A DownloadButton component.
Component description

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- disabled (boolean; optional)

- key (string; optional)

- label (string; required):
    Children.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional)

- n_clicks (number; optional)

- n_clicks_timestamp (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'DownloadButton'
    @_explicitize_args
    def __init__(self, label=Component.REQUIRED, disabled=Component.UNDEFINED, key=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, loading_state=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'disabled', 'key', 'label', 'loading_state', 'n_clicks', 'n_clicks_timestamp']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'disabled', 'key', 'label', 'loading_state', 'n_clicks', 'n_clicks_timestamp']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DownloadButton, self).__init__(**args)
