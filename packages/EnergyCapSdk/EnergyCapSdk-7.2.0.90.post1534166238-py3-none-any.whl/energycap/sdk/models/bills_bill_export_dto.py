# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillsBillExportDTO(Model):
    """BillsBillExportDTO.

    :param bill_ids:  <span class='property-internal'>Cannot be Empty</span>
     <span class='property-internal'>NULL Valid</span>
    :type bill_ids: list[int]
    :param export_mode:  <span class='property-internal'>Required</span> <span
     class='property-internal'>One of ap, gl </span>
    :type export_mode: str
    :param mark_as_exported:  <span class='property-internal'>Required</span>
    :type mark_as_exported: bool
    :param export_note: Optional note/comment.
    :type export_note: str
    """

    _validation = {
        'bill_ids': {'required': True},
        'export_mode': {'required': True},
        'mark_as_exported': {'required': True},
    }

    _attribute_map = {
        'bill_ids': {'key': 'billIds', 'type': '[int]'},
        'export_mode': {'key': 'exportMode', 'type': 'str'},
        'mark_as_exported': {'key': 'markAsExported', 'type': 'bool'},
        'export_note': {'key': 'exportNote', 'type': 'str'},
    }

    def __init__(self, bill_ids, export_mode, mark_as_exported, export_note=None):
        super(BillsBillExportDTO, self).__init__()
        self.bill_ids = bill_ids
        self.export_mode = export_mode
        self.mark_as_exported = mark_as_exported
        self.export_note = export_note
