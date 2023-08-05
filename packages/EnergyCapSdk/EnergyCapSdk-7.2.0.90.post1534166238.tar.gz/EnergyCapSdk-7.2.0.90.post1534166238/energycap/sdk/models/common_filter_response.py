# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommonFilterResponse(Model):
    """CommonFilterResponse.

    :param available_operator:
    :type available_operator: list[str]
    :param caption:
    :type caption: str
    :param query_parameter_name:
    :type query_parameter_name: str
    :param field_id:
    :type field_id: int
    :param data_field_id:
    :type data_field_id: int
    :param data_type:
    :type data_type: ~energycap.sdk.models.UnitDataTypeResponseDTO
    :param operator:
    :type operator: str
    :param value:
    :type value: str
    :param required:
    :type required: bool
    :param recommended:
    :type recommended: bool
    """

    _attribute_map = {
        'available_operator': {'key': 'availableOperator', 'type': '[str]'},
        'caption': {'key': 'caption', 'type': 'str'},
        'query_parameter_name': {'key': 'queryParameterName', 'type': 'str'},
        'field_id': {'key': 'fieldId', 'type': 'int'},
        'data_field_id': {'key': 'dataFieldId', 'type': 'int'},
        'data_type': {'key': 'dataType', 'type': 'UnitDataTypeResponseDTO'},
        'operator': {'key': 'operator', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'required': {'key': 'required', 'type': 'bool'},
        'recommended': {'key': 'recommended', 'type': 'bool'},
    }

    def __init__(self, available_operator=None, caption=None, query_parameter_name=None, field_id=None, data_field_id=None, data_type=None, operator=None, value=None, required=None, recommended=None):
        super(CommonFilterResponse, self).__init__()
        self.available_operator = available_operator
        self.caption = caption
        self.query_parameter_name = query_parameter_name
        self.field_id = field_id
        self.data_field_id = data_field_id
        self.data_type = data_type
        self.operator = operator
        self.value = value
        self.required = required
        self.recommended = recommended
