# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ModalContent(Component):
    """A ModalContent component.
ModalContent component

Keyword arguments:

- id (string; required)

- content (string; optional)

- date (string; optional)

- fromClick (boolean; optional)

- title (string; required)

- type (a value equal to: 'failure', 'maintenance', 'notice', 'etc'; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'biskit_components'
    _type = 'ModalContent'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, title=Component.REQUIRED, content=Component.UNDEFINED, type=Component.UNDEFINED, date=Component.UNDEFINED, fromClick=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'content', 'date', 'fromClick', 'title', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'content', 'date', 'fromClick', 'title', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'title']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(ModalContent, self).__init__(**args)
