# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackNewDistributionVersionManageDTO(Model):
    """<span class='property-internal'>Only one of VersionId, CopyVersionId is
    required</span>.

    :param version_id: Version id to update
     VersionId must exist on the account and meter relationship being updated
    :type version_id: int
    :param copy_version_id: An existing version id on this account meter to
     copy
     A new version will be created and all instructions will be copied to the
     new version
     CopyVersionId chargeback type must match the chargeback type begin managed
     (Either "Split" or "Calculation").
     CopyVersionId must exist on the account and meter relationship being
     updated
    :type copy_version_id: int
    :param name: Name given to the version
     Name must be unique for a particular account and meter <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 64 characters</span>
    :type name: str
    :param workflow_step_id: Workflow step this version will belong to
     The workflow step type must match the chargeback type begin managed
     (Either "Split" or "Calculation")
    :type workflow_step_id: int
    :param begin_period: Begin period for the version in the format YYYYMM
     Cannot overlap any existing versions on this account and meter for the
     chargeback type being managed <span
     class='property-internal'>Required</span>
    :type begin_period: int
    :param end_period: End period for the version in the format YYYYMM
     null value means continuing indefinately
     Cannot overlap any existing versions on this account and meter for the
     chargeback type being managed
    :type end_period: int
    """

    _validation = {
        'name': {'required': True, 'max_length': 64, 'min_length': 0},
        'begin_period': {'required': True},
    }

    _attribute_map = {
        'version_id': {'key': 'versionId', 'type': 'int'},
        'copy_version_id': {'key': 'copyVersionId', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'workflow_step_id': {'key': 'workflowStepId', 'type': 'int'},
        'begin_period': {'key': 'beginPeriod', 'type': 'int'},
        'end_period': {'key': 'endPeriod', 'type': 'int'},
    }

    def __init__(self, name, begin_period, version_id=None, copy_version_id=None, workflow_step_id=None, end_period=None):
        super(ChargebackNewDistributionVersionManageDTO, self).__init__()
        self.version_id = version_id
        self.copy_version_id = copy_version_id
        self.name = name
        self.workflow_step_id = workflow_step_id
        self.begin_period = begin_period
        self.end_period = end_period
