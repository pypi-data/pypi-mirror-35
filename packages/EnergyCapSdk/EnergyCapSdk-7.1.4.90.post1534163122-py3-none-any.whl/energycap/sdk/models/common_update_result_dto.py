# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommonUpdateResultDTO(Model):
    """CommonUpdateResultDTO.

    :param selected:
    :type selected: int
    :param updated:
    :type updated: int
    """

    _attribute_map = {
        'selected': {'key': 'selected', 'type': 'int'},
        'updated': {'key': 'updated', 'type': 'int'},
    }

    def __init__(self, selected=None, updated=None):
        super(CommonUpdateResultDTO, self).__init__()
        self.selected = selected
        self.updated = updated
