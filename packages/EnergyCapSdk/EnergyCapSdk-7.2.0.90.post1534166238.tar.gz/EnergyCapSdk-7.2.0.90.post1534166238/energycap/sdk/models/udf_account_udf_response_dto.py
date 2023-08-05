# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UDFAccountUDFResponseDTO(Model):
    """UDFAccountUDFResponseDTO.

    :param account_id: The account identifier
    :type account_id: int
    :param account_code: The account code
    :type account_code: str
    :param account_info: The account info
    :type account_info: str
    :param udfs: An array of user-defined fields (UDFs)
    :type udfs: list[~energycap.sdk.models.UDFUDFFieldChildDTO]
    """

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'int'},
        'account_code': {'key': 'accountCode', 'type': 'str'},
        'account_info': {'key': 'accountInfo', 'type': 'str'},
        'udfs': {'key': 'udfs', 'type': '[UDFUDFFieldChildDTO]'},
    }

    def __init__(self, account_id=None, account_code=None, account_info=None, udfs=None):
        super(UDFAccountUDFResponseDTO, self).__init__()
        self.account_id = account_id
        self.account_code = account_code
        self.account_info = account_info
        self.udfs = udfs
