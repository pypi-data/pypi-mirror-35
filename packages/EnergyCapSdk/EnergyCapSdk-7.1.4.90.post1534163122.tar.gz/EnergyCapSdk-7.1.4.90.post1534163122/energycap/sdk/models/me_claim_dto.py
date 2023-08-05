# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeClaimDto(Model):
    """MeClaimDto.

    :param claim_type:
    :type claim_type: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'claim_type': {'key': 'claimType', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, claim_type=None, value=None):
        super(MeClaimDto, self).__init__()
        self.claim_type = claim_type
        self.value = value
