# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RouteRouteMeterChildDTO(Model):
    """RouteRouteMeterChildDTO.

    :param meter_id:
    :type meter_id: int
    :param meter_code:
    :type meter_code: str
    :param meter_info:
    :type meter_info: str
    :param display_order:
    :type display_order: int
    :param commodity:
    :type commodity: ~energycap.sdk.models.CommoditiesCommodityChildDTO
    """

    _attribute_map = {
        'meter_id': {'key': 'meterId', 'type': 'int'},
        'meter_code': {'key': 'meterCode', 'type': 'str'},
        'meter_info': {'key': 'meterInfo', 'type': 'str'},
        'display_order': {'key': 'displayOrder', 'type': 'int'},
        'commodity': {'key': 'commodity', 'type': 'CommoditiesCommodityChildDTO'},
    }

    def __init__(self, meter_id=None, meter_code=None, meter_info=None, display_order=None, commodity=None):
        super(RouteRouteMeterChildDTO, self).__init__()
        self.meter_id = meter_id
        self.meter_code = meter_code
        self.meter_info = meter_info
        self.display_order = display_order
        self.commodity = commodity
