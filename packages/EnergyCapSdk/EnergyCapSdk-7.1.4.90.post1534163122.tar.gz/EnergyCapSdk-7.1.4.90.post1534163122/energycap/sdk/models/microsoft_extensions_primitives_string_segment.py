# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MicrosoftExtensionsPrimitivesStringSegment(Model):
    """MicrosoftExtensionsPrimitivesStringSegment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar buffer:
    :vartype buffer: str
    :ivar offset:
    :vartype offset: int
    :ivar length:
    :vartype length: int
    :ivar value:
    :vartype value: str
    :ivar has_value:
    :vartype has_value: bool
    """

    _validation = {
        'buffer': {'readonly': True},
        'offset': {'readonly': True},
        'length': {'readonly': True},
        'value': {'readonly': True},
        'has_value': {'readonly': True},
    }

    _attribute_map = {
        'buffer': {'key': 'buffer', 'type': 'str'},
        'offset': {'key': 'offset', 'type': 'int'},
        'length': {'key': 'length', 'type': 'int'},
        'value': {'key': 'value', 'type': 'str'},
        'has_value': {'key': 'hasValue', 'type': 'bool'},
    }

    def __init__(self):
        super(MicrosoftExtensionsPrimitivesStringSegment, self).__init__()
        self.buffer = None
        self.offset = None
        self.length = None
        self.value = None
        self.has_value = None
