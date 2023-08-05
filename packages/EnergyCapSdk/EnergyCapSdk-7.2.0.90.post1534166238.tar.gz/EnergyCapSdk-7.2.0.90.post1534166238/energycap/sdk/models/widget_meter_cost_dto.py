# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class WidgetMeterCostDTO(Model):
    """WidgetMeterCostDTO.

    :param meter: Meter
    :type meter: ~energycap.sdk.models.LogicalDeviceMeterChildDTO
    :param place: Place
    :type place: ~energycap.sdk.models.PlacePlaceChildDTO
    :param total_cost: Total cost
    :type total_cost: float
    :param cost_unit: The cost unit of measure
    :type cost_unit: ~energycap.sdk.models.UnitUnitChildDTO
    """

    _attribute_map = {
        'meter': {'key': 'meter', 'type': 'LogicalDeviceMeterChildDTO'},
        'place': {'key': 'place', 'type': 'PlacePlaceChildDTO'},
        'total_cost': {'key': 'totalCost', 'type': 'float'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitUnitChildDTO'},
    }

    def __init__(self, meter=None, place=None, total_cost=None, cost_unit=None):
        super(WidgetMeterCostDTO, self).__init__()
        self.meter = meter
        self.place = place
        self.total_cost = total_cost
        self.cost_unit = cost_unit
