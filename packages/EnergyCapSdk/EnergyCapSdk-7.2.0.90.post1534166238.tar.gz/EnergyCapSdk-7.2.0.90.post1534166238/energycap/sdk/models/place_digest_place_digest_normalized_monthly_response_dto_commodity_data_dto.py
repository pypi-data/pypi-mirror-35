# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestPlaceDigestNormalizedMonthlyResponseDTOCommodityDataDTO(Model):
    """PlaceDigestPlaceDigestNormalizedMonthlyResponseDTOCommodityDataDTO.

    :param commodity_code: The commodity code
    :type commodity_code: str
    :param commodity_info: The commodity info
    :type commodity_info: str
    :param commodity_id: The commodity identifier
    :type commodity_id: int
    :param common_use_unit: The common use unit of measure
    :type common_use_unit: ~energycap.sdk.models.UnitUnitChildDTO
    :param common_demand_unit: The common demand unit of measure
    :type common_demand_unit: ~energycap.sdk.models.UnitUnitChildDTO
    :param results: An array of commodity monthly data
    :type results:
     list[~energycap.sdk.models.PlaceDigestPlaceDigestNormalizedMonthlyResponseDTOCommodityResultsDTO]
    :param target_comparison: The target year info
    :type target_comparison:
     ~energycap.sdk.models.PlaceDigestPlaceDigestNormalizedCommodityTargetComparisonMonthlyDTO
    """

    _attribute_map = {
        'commodity_code': {'key': 'commodityCode', 'type': 'str'},
        'commodity_info': {'key': 'commodityInfo', 'type': 'str'},
        'commodity_id': {'key': 'commodityId', 'type': 'int'},
        'common_use_unit': {'key': 'commonUseUnit', 'type': 'UnitUnitChildDTO'},
        'common_demand_unit': {'key': 'commonDemandUnit', 'type': 'UnitUnitChildDTO'},
        'results': {'key': 'results', 'type': '[PlaceDigestPlaceDigestNormalizedMonthlyResponseDTOCommodityResultsDTO]'},
        'target_comparison': {'key': 'targetComparison', 'type': 'PlaceDigestPlaceDigestNormalizedCommodityTargetComparisonMonthlyDTO'},
    }

    def __init__(self, commodity_code=None, commodity_info=None, commodity_id=None, common_use_unit=None, common_demand_unit=None, results=None, target_comparison=None):
        super(PlaceDigestPlaceDigestNormalizedMonthlyResponseDTOCommodityDataDTO, self).__init__()
        self.commodity_code = commodity_code
        self.commodity_info = commodity_info
        self.commodity_id = commodity_id
        self.common_use_unit = common_use_unit
        self.common_demand_unit = common_demand_unit
        self.results = results
        self.target_comparison = target_comparison
