# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackNewCalculatedBillCalculatedBillCostRequestDTO(Model):
    """Defines how use is calculated for a calculated bill distribution <span
    class='property-internal'>Only one of UseCurrentMetersRateSchedule,
    FixedUnitCost, UnitCostMeterId, FixedAmount, CopyCostFromMeter,
    CostCalculation is required</span>.

    :param use_current_meters_rate_schedule: Apply the meter's current rate
     when calculating bill cost
     "true" is the only valid value for this property <span
     class='property-internal'>One of True </span>
    :type use_current_meters_rate_schedule: bool
    :param fixed_unit_cost: Fixed amount per unit to apply during bill
     calculation
    :type fixed_unit_cost:
     ~energycap.sdk.models.ChargebackNewCalculatedBillFixedUnitCostRequestDTO
    :param unit_cost_meter_id: MeterId from where to get the unit cost
    :type unit_cost_meter_id: int
    :param fixed_amount: Use a fixed amount for bill cost <span
     class='property-info'>Max precision of 2</span> <span
     class='property-info'>>NULL Valid</span>
    :type fixed_amount: float
    :param copy_cost_from_meter: Copy aggregated cost from another meter
    :type copy_cost_from_meter:
     ~energycap.sdk.models.ChargebackNewCalculatedBillCopyMeterRequestDTO
    :param cost_calculation: Add and subtract cost from meters and meter
     groups
    :type cost_calculation:
     ~energycap.sdk.models.ChargebackNewCalculatedBillCalculationRequestDTO
    """

    _attribute_map = {
        'use_current_meters_rate_schedule': {'key': 'useCurrentMetersRateSchedule', 'type': 'bool'},
        'fixed_unit_cost': {'key': 'fixedUnitCost', 'type': 'ChargebackNewCalculatedBillFixedUnitCostRequestDTO'},
        'unit_cost_meter_id': {'key': 'unitCostMeterId', 'type': 'int'},
        'fixed_amount': {'key': 'fixedAmount', 'type': 'float'},
        'copy_cost_from_meter': {'key': 'copyCostFromMeter', 'type': 'ChargebackNewCalculatedBillCopyMeterRequestDTO'},
        'cost_calculation': {'key': 'costCalculation', 'type': 'ChargebackNewCalculatedBillCalculationRequestDTO'},
    }

    def __init__(self, use_current_meters_rate_schedule=None, fixed_unit_cost=None, unit_cost_meter_id=None, fixed_amount=None, copy_cost_from_meter=None, cost_calculation=None):
        super(ChargebackNewCalculatedBillCalculatedBillCostRequestDTO, self).__init__()
        self.use_current_meters_rate_schedule = use_current_meters_rate_schedule
        self.fixed_unit_cost = fixed_unit_cost
        self.unit_cost_meter_id = unit_cost_meter_id
        self.fixed_amount = fixed_amount
        self.copy_cost_from_meter = copy_cost_from_meter
        self.cost_calculation = cost_calculation
