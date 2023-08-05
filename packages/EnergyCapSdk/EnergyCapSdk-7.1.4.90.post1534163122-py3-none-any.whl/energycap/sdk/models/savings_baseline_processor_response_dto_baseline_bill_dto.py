# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SavingsBaselineProcessorResponseDTOBaselineBillDTO(Model):
    """SavingsBaselineProcessorResponseDTOBaselineBillDTO.

    :param bill_id: The bill identifier
    :type bill_id: int
    :param avg_cooling_degree_days: The average cooling degree days
    :type avg_cooling_degree_days: float
    :param avg_heating_degree_days: The average heating degree days
    :type avg_heating_degree_days: float
    :param begin_date: The bill's begin date
    :type begin_date: datetime
    :param end_date: The bill's end date
    :type end_date: datetime
    :param is_excluded: Indicates if the bill is excluded from the baseline
     regression
    :type is_excluded: bool
    :param is_outlier: Indicates if the bill is an outlier
    :type is_outlier: bool
    :param native_use: The native use
    :type native_use: float
    :param days: The number of days in the bill
    :type days: int
    :param period_name: Calendar Period Name
    :type period_name: str
    :param calendar_period: Calendar period
    :type calendar_period: int
    :param calendar_year: Calendar year
    :type calendar_year: int
    :param fiscal_period: Fiscal period
    :type fiscal_period: int
    :param fiscal_year: Fiscal year
    :type fiscal_year: int
    """

    _attribute_map = {
        'bill_id': {'key': 'billId', 'type': 'int'},
        'avg_cooling_degree_days': {'key': 'avgCoolingDegreeDays', 'type': 'float'},
        'avg_heating_degree_days': {'key': 'avgHeatingDegreeDays', 'type': 'float'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'is_excluded': {'key': 'isExcluded', 'type': 'bool'},
        'is_outlier': {'key': 'isOutlier', 'type': 'bool'},
        'native_use': {'key': 'nativeUse', 'type': 'float'},
        'days': {'key': 'days', 'type': 'int'},
        'period_name': {'key': 'periodName', 'type': 'str'},
        'calendar_period': {'key': 'calendarPeriod', 'type': 'int'},
        'calendar_year': {'key': 'calendarYear', 'type': 'int'},
        'fiscal_period': {'key': 'fiscalPeriod', 'type': 'int'},
        'fiscal_year': {'key': 'fiscalYear', 'type': 'int'},
    }

    def __init__(self, bill_id=None, avg_cooling_degree_days=None, avg_heating_degree_days=None, begin_date=None, end_date=None, is_excluded=None, is_outlier=None, native_use=None, days=None, period_name=None, calendar_period=None, calendar_year=None, fiscal_period=None, fiscal_year=None):
        super(SavingsBaselineProcessorResponseDTOBaselineBillDTO, self).__init__()
        self.bill_id = bill_id
        self.avg_cooling_degree_days = avg_cooling_degree_days
        self.avg_heating_degree_days = avg_heating_degree_days
        self.begin_date = begin_date
        self.end_date = end_date
        self.is_excluded = is_excluded
        self.is_outlier = is_outlier
        self.native_use = native_use
        self.days = days
        self.period_name = period_name
        self.calendar_period = calendar_period
        self.calendar_year = calendar_year
        self.fiscal_period = fiscal_period
        self.fiscal_year = fiscal_year
