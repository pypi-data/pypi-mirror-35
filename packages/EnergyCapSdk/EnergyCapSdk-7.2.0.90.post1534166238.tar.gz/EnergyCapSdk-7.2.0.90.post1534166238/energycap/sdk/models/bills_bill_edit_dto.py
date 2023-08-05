# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillsBillEditDTO(Model):
    """BillsBillEditDTO.

    :param account_id: The bill's account <span
     class='property-internal'>Required</span>
    :type account_id: int
    :param begin_date: The bill's begin date <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 12/31/1899 and 1/1/3000</span>
    :type begin_date: datetime
    :param end_date: The bill's end date <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 12/31/1899 and 1/1/3000</span>
    :type end_date: datetime
    :param billing_period: The bill's billing period <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 190001 and 209912</span>
    :type billing_period: int
    :param account_period: The bill's accounting period
     Depending on your settings you can have up to 13 accounting periods <span
     class='property-internal'>Must be between 190001 and 209913</span>
    :type account_period: int
    :param estimated: Indicates if the bill is estimated
    :type estimated: bool
    :param statement_date: The date and time of the bill statement <span
     class='property-internal'>Must be between 12/31/1899 and 1/1/3000</span>
    :type statement_date: datetime
    :param due_date: The date and time the bill is due <span
     class='property-internal'>Must be between 12/31/1899 and 1/1/3000</span>
    :type due_date: datetime
    :param next_reading: The date and time the next reading <span
     class='property-internal'>Must be between 12/31/1899 and 1/1/3000</span>
    :type next_reading: datetime
    :param control_code: The bill's control code <span
     class='property-internal'>Must be between 0 and 255 characters</span>
    :type control_code: str
    :param invoice_number: The bill's invoice number <span
     class='property-internal'>Must be between 0 and 32 characters</span>
    :type invoice_number: str
    :param set_to_unapproved: The bill's "approval change flag".
     If a bill is approved and the approval system is turned on:
     true = unapprove bill, false = don't change bill's approval status.
     If the approval system is not turned on:
     the bill's approval staus will not be changed regardless of this setting.
    :type set_to_unapproved: bool
    :param note: The bill note
    :type note: str
    :param meters: The meters with line items
    :type meters: list[~energycap.sdk.models.BillsBillMeterEditDTO]
    :param account_body_lines: The account line items
    :type account_body_lines:
     list[~energycap.sdk.models.BillsBillAccountBodyLineEditDTO]
    """

    _validation = {
        'account_id': {'required': True},
        'begin_date': {'required': True},
        'end_date': {'required': True},
        'billing_period': {'required': True, 'maximum': 209912, 'minimum': 190001},
        'account_period': {'maximum': 209913, 'minimum': 190001},
        'control_code': {'max_length': 255, 'min_length': 0},
        'invoice_number': {'max_length': 32, 'min_length': 0},
    }

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'int'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'billing_period': {'key': 'billingPeriod', 'type': 'int'},
        'account_period': {'key': 'accountPeriod', 'type': 'int'},
        'estimated': {'key': 'estimated', 'type': 'bool'},
        'statement_date': {'key': 'statementDate', 'type': 'iso-8601'},
        'due_date': {'key': 'dueDate', 'type': 'iso-8601'},
        'next_reading': {'key': 'nextReading', 'type': 'iso-8601'},
        'control_code': {'key': 'controlCode', 'type': 'str'},
        'invoice_number': {'key': 'invoiceNumber', 'type': 'str'},
        'set_to_unapproved': {'key': 'setToUnapproved', 'type': 'bool'},
        'note': {'key': 'note', 'type': 'str'},
        'meters': {'key': 'meters', 'type': '[BillsBillMeterEditDTO]'},
        'account_body_lines': {'key': 'accountBodyLines', 'type': '[BillsBillAccountBodyLineEditDTO]'},
    }

    def __init__(self, account_id, begin_date, end_date, billing_period, account_period=None, estimated=None, statement_date=None, due_date=None, next_reading=None, control_code=None, invoice_number=None, set_to_unapproved=None, note=None, meters=None, account_body_lines=None):
        super(BillsBillEditDTO, self).__init__()
        self.account_id = account_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.billing_period = billing_period
        self.account_period = account_period
        self.estimated = estimated
        self.statement_date = statement_date
        self.due_date = due_date
        self.next_reading = next_reading
        self.control_code = control_code
        self.invoice_number = invoice_number
        self.set_to_unapproved = set_to_unapproved
        self.note = note
        self.meters = meters
        self.account_body_lines = account_body_lines
