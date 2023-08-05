# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Translation(Component):
    """A Translation component.
Translation Component

Keyword arguments:

- translationKey (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'Translation'
    @_explicitize_args
    def __init__(self, translationKey=Component.REQUIRED, **kwargs):
        self._prop_names = ['translationKey']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['translationKey']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['translationKey']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Translation, self).__init__(**args)
