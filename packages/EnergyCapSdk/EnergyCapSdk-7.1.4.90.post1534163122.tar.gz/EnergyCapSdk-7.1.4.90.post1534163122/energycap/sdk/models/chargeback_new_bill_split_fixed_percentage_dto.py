# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackNewBillSplitFixedPercentageDTO(Model):
    """ChargebackNewBillSplitFixedPercentageDTO.

    :param destination_account_id: Destination account ID
     There must be an existing relationship between the DestinationAccountId
     and DestinationMeterId <span class='property-internal'>Required</span>
     <span class='property-internal'>Topmost (CostCenter)</span>
    :type destination_account_id: int
    :param destination_meter_id: Destination meter ID
     There must be an existing relationship between the DestinationAccountId
     and DestinationMeterId <span class='property-internal'>Required</span>
     <span class='property-internal'>Topmost (LogicalDevice)</span>
    :type destination_meter_id: int
    :param split_percentage: Fixed percentage to apply in bill split for this
     account and meter
     Pass the percentage value
     For example 50.5% should be 50.5 <span class='property-info'>Max precision
     of 8</span> <span class='property-internal'>Required</span>
    :type split_percentage: float
    """

    _validation = {
        'destination_account_id': {'required': True},
        'destination_meter_id': {'required': True},
        'split_percentage': {'required': True},
    }

    _attribute_map = {
        'destination_account_id': {'key': 'destinationAccountId', 'type': 'int'},
        'destination_meter_id': {'key': 'destinationMeterId', 'type': 'int'},
        'split_percentage': {'key': 'splitPercentage', 'type': 'float'},
    }

    def __init__(self, destination_account_id, destination_meter_id, split_percentage):
        super(ChargebackNewBillSplitFixedPercentageDTO, self).__init__()
        self.destination_account_id = destination_account_id
        self.destination_meter_id = destination_meter_id
        self.split_percentage = split_percentage
