# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LogicalDeviceMeterAccountChildDTO(Model):
    """LogicalDeviceMeterAccountChildDTO.

    :param account_meter_id: The MeterAccount meter identifier
    :type account_meter_id: int
    :param account_id: The MeterAccount identifier for this MeterAccount meter
    :type account_id: int
    :param account_code: The code of the MeterAccount for this MeterAccount
     meter
    :type account_code: str
    :param account_info: The info of the MeterAccount for this MeterAccount
     meter
    :type account_info: str
    :param active: Indicates whether the Account is active or inactive
    :type active: bool
    :param vendor: The account vendor
    :type vendor: ~energycap.sdk.models.VendorsVendorChildDTO
    :param meter_general_ledger: The general ledger assigned to the meter
    :type meter_general_ledger:
     ~energycap.sdk.models.BillsGeneralLedgerChildDTO
    :param account_general_ledger: The general ledger assigned to the account
    :type account_general_ledger:
     ~energycap.sdk.models.BillsGeneralLedgerChildDTO
    :param vendor_type: The vendor type. Vendors may assume different types on
     different account meters
    :type vendor_type: ~energycap.sdk.models.AccountsVendorTypeChildDTO
    :param start_date: The beginning date and time for this MeterAccount meter
     relationship
    :type start_date: datetime
    :param end_date: The ending date and time for this MeterAccount meter
     relationship
    :type end_date: datetime
    """

    _attribute_map = {
        'account_meter_id': {'key': 'accountMeterId', 'type': 'int'},
        'account_id': {'key': 'accountId', 'type': 'int'},
        'account_code': {'key': 'accountCode', 'type': 'str'},
        'account_info': {'key': 'accountInfo', 'type': 'str'},
        'active': {'key': 'active', 'type': 'bool'},
        'vendor': {'key': 'vendor', 'type': 'VendorsVendorChildDTO'},
        'meter_general_ledger': {'key': 'meterGeneralLedger', 'type': 'BillsGeneralLedgerChildDTO'},
        'account_general_ledger': {'key': 'accountGeneralLedger', 'type': 'BillsGeneralLedgerChildDTO'},
        'vendor_type': {'key': 'vendorType', 'type': 'AccountsVendorTypeChildDTO'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
    }

    def __init__(self, account_meter_id=None, account_id=None, account_code=None, account_info=None, active=None, vendor=None, meter_general_ledger=None, account_general_ledger=None, vendor_type=None, start_date=None, end_date=None):
        super(LogicalDeviceMeterAccountChildDTO, self).__init__()
        self.account_meter_id = account_meter_id
        self.account_id = account_id
        self.account_code = account_code
        self.account_info = account_info
        self.active = active
        self.vendor = vendor
        self.meter_general_ledger = meter_general_ledger
        self.account_general_ledger = account_general_ledger
        self.vendor_type = vendor_type
        self.start_date = start_date
        self.end_date = end_date
