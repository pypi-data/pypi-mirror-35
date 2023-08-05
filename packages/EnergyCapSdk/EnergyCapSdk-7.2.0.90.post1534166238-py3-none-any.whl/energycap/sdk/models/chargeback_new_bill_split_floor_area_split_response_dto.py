# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackNewBillSplitFloorAreaSplitResponseDTO(Model):
    """ChargebackNewBillSplitFloorAreaSplitResponseDTO.

    :param destination_account: Destination account for bill split
    :type destination_account:
     ~energycap.sdk.models.AccountsAccountChildWithTypeDTO
    :param destination_meter: Destination meter for bill split
    :type destination_meter: ~energycap.sdk.models.LogicalDeviceMeterChildDTO
    :param destination_place: Parent place of destination meter for bill split
    :type destination_place:
     ~energycap.sdk.models.ChargebackNewBillSplitPlaceChildWithFloorAreaDTO
    :param weighting_factor: Weighting factor to apply in floor area bill
     split for this account and meter
    :type weighting_factor: float
    :param split_percentage: Fixed percentage to apply in bill split for this
     account and meter
    :type split_percentage: float
    """

    _attribute_map = {
        'destination_account': {'key': 'destinationAccount', 'type': 'AccountsAccountChildWithTypeDTO'},
        'destination_meter': {'key': 'destinationMeter', 'type': 'LogicalDeviceMeterChildDTO'},
        'destination_place': {'key': 'destinationPlace', 'type': 'ChargebackNewBillSplitPlaceChildWithFloorAreaDTO'},
        'weighting_factor': {'key': 'weightingFactor', 'type': 'float'},
        'split_percentage': {'key': 'splitPercentage', 'type': 'float'},
    }

    def __init__(self, destination_account=None, destination_meter=None, destination_place=None, weighting_factor=None, split_percentage=None):
        super(ChargebackNewBillSplitFloorAreaSplitResponseDTO, self).__init__()
        self.destination_account = destination_account
        self.destination_meter = destination_meter
        self.destination_place = destination_place
        self.weighting_factor = weighting_factor
        self.split_percentage = split_percentage
