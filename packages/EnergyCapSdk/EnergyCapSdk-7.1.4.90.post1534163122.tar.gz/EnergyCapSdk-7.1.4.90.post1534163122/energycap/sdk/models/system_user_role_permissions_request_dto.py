# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SystemUserRolePermissionsRequestDTO(Model):
    """SystemUserRolePermissionsRequestDTO.

    :param accounting_settings:
    :type accounting_settings:
     ~energycap.sdk.models.SystemUserRoleAccountingSettings
    :param accounts:
    :type accounts: ~energycap.sdk.models.SystemUserRoleAccounts
    :param accounts_module:
    :type accounts_module: ~energycap.sdk.models.SystemUserRoleAccountsModule
    :param accrual_settings:
    :type accrual_settings:
     ~energycap.sdk.models.SystemUserRoleAccrualSettings
    :param cost_centers:
    :type cost_centers: ~energycap.sdk.models.SystemUserRoleCostCenters
    :param move_accounts_between_vendors:
    :type move_accounts_between_vendors:
     ~energycap.sdk.models.SystemUserRoleMoveAccountsBetweenVendors
    :param application_settings:
    :type application_settings:
     ~energycap.sdk.models.SystemUserRoleApplicationSettings
    :param approve_bills:
    :type approve_bills: ~energycap.sdk.models.SystemUserRoleApproveBills
    :param bill_audit_groups:
    :type bill_audit_groups:
     ~energycap.sdk.models.SystemUserRoleBillAuditGroups
    :param bill_audits:
    :type bill_audits: ~energycap.sdk.models.SystemUserRoleBillAudits
    :param bill_entry_templates:
    :type bill_entry_templates:
     ~energycap.sdk.models.SystemUserRoleBillEntryTemplates
    :param bill_workflow_settings:
    :type bill_workflow_settings:
     ~energycap.sdk.models.SystemUserRoleBillWorkflowSettings
    :param bills_and_batches:
    :type bills_and_batches:
     ~energycap.sdk.models.SystemUserRoleBillsAndBatches
    :param export_bills:
    :type export_bills: ~energycap.sdk.models.SystemUserRoleExportBills
    :param export_hold:
    :type export_hold: ~energycap.sdk.models.SystemUserRoleExportHold
    :param move_existing_bills:
    :type move_existing_bills:
     ~energycap.sdk.models.SystemUserRoleMoveExistingBills
    :param bill_audit_results_and_alerts:
    :type bill_audit_results_and_alerts:
     ~energycap.sdk.models.SystemUserRoleBillAuditResultsAndAlerts
    :param shared_bill_lists:
    :type shared_bill_lists:
     ~energycap.sdk.models.SystemUserRoleSharedBillLists
    :param unit_system_settings:
    :type unit_system_settings:
     ~energycap.sdk.models.SystemUserRoleUnitSystemSettings
    :param update_approved_bills:
    :type update_approved_bills:
     ~energycap.sdk.models.SystemUserRoleUpdateApprovedBills
    :param update_units_on_existing_bills:
    :type update_units_on_existing_bills:
     ~energycap.sdk.models.SystemUserRoleUpdateUnitsOnExistingBills
    :param budgets_and_budget_versions:
    :type budgets_and_budget_versions:
     ~energycap.sdk.models.SystemUserRoleBudgetsAndBudgetVersions
    :param chargebacks_module:
    :type chargebacks_module:
     ~energycap.sdk.models.SystemUserRoleChargebacksModule
    :param chargeback_distributions:
    :type chargeback_distributions:
     ~energycap.sdk.models.SystemUserRoleChargebackDistributions
    :param chargeback_reversals:
    :type chargeback_reversals:
     ~energycap.sdk.models.SystemUserRoleChargebackReversals
    :param submeter_routes:
    :type submeter_routes: ~energycap.sdk.models.SystemUserRoleSubmeterRoutes
    :param meter_savings_settings:
    :type meter_savings_settings:
     ~energycap.sdk.models.SystemUserRoleMeterSavingsSettings
    :param savings_adjustments:
    :type savings_adjustments:
     ~energycap.sdk.models.SystemUserRoleSavingsAdjustments
    :param manually_adjust_savings:
    :type manually_adjust_savings:
     ~energycap.sdk.models.SystemUserRoleManuallyAdjustSavings
    :param savings_engine:
    :type savings_engine: ~energycap.sdk.models.SystemUserRoleSavingsEngine
    :param baseline_engine:
    :type baseline_engine: ~energycap.sdk.models.SystemUserRoleBaselineEngine
    :param global_cost_avoidance_settings:
    :type global_cost_avoidance_settings:
     ~energycap.sdk.models.SystemUserRoleGlobalCostAvoidanceSettings
    :param dashboard_and_maps_module:
    :type dashboard_and_maps_module:
     ~energycap.sdk.models.SystemUserRoleDashboardAndMapsModule
    :param dashboard_administrator:
    :type dashboard_administrator:
     ~energycap.sdk.models.SystemUserRoleDashboardAdministrator
    :param public_dashboards_or_maps:
    :type public_dashboards_or_maps:
     ~energycap.sdk.models.SystemUserRolePublicDashboardsOrMaps
    :param shared_dashboards_or_maps:
    :type shared_dashboards_or_maps:
     ~energycap.sdk.models.SystemUserRoleSharedDashboardsOrMaps
    :param buildings_and_meters_module:
    :type buildings_and_meters_module:
     ~energycap.sdk.models.SystemUserRoleBuildingsAndMetersModule
    :param groups_and_benchmarks_module:
    :type groups_and_benchmarks_module:
     ~energycap.sdk.models.SystemUserRoleGroupsAndBenchmarksModule
    :param building_and_meter_groups:
    :type building_and_meter_groups:
     ~energycap.sdk.models.SystemUserRoleBuildingAndMeterGroups
    :param buildings_and_organizations:
    :type buildings_and_organizations:
     ~energycap.sdk.models.SystemUserRoleBuildingsAndOrganizations
    :param interval_data:
    :type interval_data: ~energycap.sdk.models.SystemUserRoleIntervalData
    :param interval_data_analysis:
    :type interval_data_analysis:
     ~energycap.sdk.models.SystemUserRoleIntervalDataAnalysis
    :param energystar_submissions:
    :type energystar_submissions:
     ~energycap.sdk.models.SystemUserRoleENERGYSTARSubmissions
    :param facility_projects:
    :type facility_projects:
     ~energycap.sdk.models.SystemUserRoleFacilityProjects
    :param greenhouse_gas_administrator:
    :type greenhouse_gas_administrator:
     ~energycap.sdk.models.SystemUserRoleGreenhouseGasAdministrator
    :param interval_data_rollup:
    :type interval_data_rollup:
     ~energycap.sdk.models.SystemUserRoleIntervalDataRollup
    :param meters:
    :type meters: ~energycap.sdk.models.SystemUserRoleMeters
    :param normalization_settings:
    :type normalization_settings:
     ~energycap.sdk.models.SystemUserRoleNormalizationSettings
    :param weather_settings:
    :type weather_settings:
     ~energycap.sdk.models.SystemUserRoleWeatherSettings
    :param reports_module:
    :type reports_module: ~energycap.sdk.models.SystemUserRoleReportsModule
    :param distributed_reports_settings:
    :type distributed_reports_settings:
     ~energycap.sdk.models.SystemUserRoleDistributedReportsSettings
    :param install_or_update_reports:
    :type install_or_update_reports:
     ~energycap.sdk.models.SystemUserRoleInstallOrUpdateReports
    :param report_groups:
    :type report_groups: ~energycap.sdk.models.SystemUserRoleReportGroups
    :param shared_reports:
    :type shared_reports: ~energycap.sdk.models.SystemUserRoleSharedReports
    :param reset_user_passwords:
    :type reset_user_passwords:
     ~energycap.sdk.models.SystemUserRoleResetUserPasswords
    :param users_and_roles:
    :type users_and_roles: ~energycap.sdk.models.SystemUserRoleUsersAndRoles
    :param vendors_and_rates_module:
    :type vendors_and_rates_module:
     ~energycap.sdk.models.SystemUserRoleVendorsAndRatesModule
    :param rate_schedules:
    :type rate_schedules: ~energycap.sdk.models.SystemUserRoleRateSchedules
    :param vendors:
    :type vendors: ~energycap.sdk.models.SystemUserRoleVendors
    """

    _attribute_map = {
        'accounting_settings': {'key': 'accountingSettings', 'type': 'SystemUserRoleAccountingSettings'},
        'accounts': {'key': 'accounts', 'type': 'SystemUserRoleAccounts'},
        'accounts_module': {'key': 'accountsModule', 'type': 'SystemUserRoleAccountsModule'},
        'accrual_settings': {'key': 'accrualSettings', 'type': 'SystemUserRoleAccrualSettings'},
        'cost_centers': {'key': 'costCenters', 'type': 'SystemUserRoleCostCenters'},
        'move_accounts_between_vendors': {'key': 'moveAccountsBetweenVendors', 'type': 'SystemUserRoleMoveAccountsBetweenVendors'},
        'application_settings': {'key': 'applicationSettings', 'type': 'SystemUserRoleApplicationSettings'},
        'approve_bills': {'key': 'approveBills', 'type': 'SystemUserRoleApproveBills'},
        'bill_audit_groups': {'key': 'billAuditGroups', 'type': 'SystemUserRoleBillAuditGroups'},
        'bill_audits': {'key': 'billAudits', 'type': 'SystemUserRoleBillAudits'},
        'bill_entry_templates': {'key': 'billEntryTemplates', 'type': 'SystemUserRoleBillEntryTemplates'},
        'bill_workflow_settings': {'key': 'billWorkflowSettings', 'type': 'SystemUserRoleBillWorkflowSettings'},
        'bills_and_batches': {'key': 'billsAndBatches', 'type': 'SystemUserRoleBillsAndBatches'},
        'export_bills': {'key': 'exportBills', 'type': 'SystemUserRoleExportBills'},
        'export_hold': {'key': 'exportHold', 'type': 'SystemUserRoleExportHold'},
        'move_existing_bills': {'key': 'moveExistingBills', 'type': 'SystemUserRoleMoveExistingBills'},
        'bill_audit_results_and_alerts': {'key': 'billAuditResultsAndAlerts', 'type': 'SystemUserRoleBillAuditResultsAndAlerts'},
        'shared_bill_lists': {'key': 'sharedBillLists', 'type': 'SystemUserRoleSharedBillLists'},
        'unit_system_settings': {'key': 'unitSystemSettings', 'type': 'SystemUserRoleUnitSystemSettings'},
        'update_approved_bills': {'key': 'updateApprovedBills', 'type': 'SystemUserRoleUpdateApprovedBills'},
        'update_units_on_existing_bills': {'key': 'updateUnitsOnExistingBills', 'type': 'SystemUserRoleUpdateUnitsOnExistingBills'},
        'budgets_and_budget_versions': {'key': 'budgetsAndBudgetVersions', 'type': 'SystemUserRoleBudgetsAndBudgetVersions'},
        'chargebacks_module': {'key': 'chargebacksModule', 'type': 'SystemUserRoleChargebacksModule'},
        'chargeback_distributions': {'key': 'chargebackDistributions', 'type': 'SystemUserRoleChargebackDistributions'},
        'chargeback_reversals': {'key': 'chargebackReversals', 'type': 'SystemUserRoleChargebackReversals'},
        'submeter_routes': {'key': 'submeterRoutes', 'type': 'SystemUserRoleSubmeterRoutes'},
        'meter_savings_settings': {'key': 'meterSavingsSettings', 'type': 'SystemUserRoleMeterSavingsSettings'},
        'savings_adjustments': {'key': 'savingsAdjustments', 'type': 'SystemUserRoleSavingsAdjustments'},
        'manually_adjust_savings': {'key': 'manuallyAdjustSavings', 'type': 'SystemUserRoleManuallyAdjustSavings'},
        'savings_engine': {'key': 'savingsEngine', 'type': 'SystemUserRoleSavingsEngine'},
        'baseline_engine': {'key': 'baselineEngine', 'type': 'SystemUserRoleBaselineEngine'},
        'global_cost_avoidance_settings': {'key': 'globalCostAvoidanceSettings', 'type': 'SystemUserRoleGlobalCostAvoidanceSettings'},
        'dashboard_and_maps_module': {'key': 'dashboardAndMapsModule', 'type': 'SystemUserRoleDashboardAndMapsModule'},
        'dashboard_administrator': {'key': 'dashboardAdministrator', 'type': 'SystemUserRoleDashboardAdministrator'},
        'public_dashboards_or_maps': {'key': 'publicDashboardsOrMaps', 'type': 'SystemUserRolePublicDashboardsOrMaps'},
        'shared_dashboards_or_maps': {'key': 'sharedDashboardsOrMaps', 'type': 'SystemUserRoleSharedDashboardsOrMaps'},
        'buildings_and_meters_module': {'key': 'buildingsAndMetersModule', 'type': 'SystemUserRoleBuildingsAndMetersModule'},
        'groups_and_benchmarks_module': {'key': 'groupsAndBenchmarksModule', 'type': 'SystemUserRoleGroupsAndBenchmarksModule'},
        'building_and_meter_groups': {'key': 'buildingAndMeterGroups', 'type': 'SystemUserRoleBuildingAndMeterGroups'},
        'buildings_and_organizations': {'key': 'buildingsAndOrganizations', 'type': 'SystemUserRoleBuildingsAndOrganizations'},
        'interval_data': {'key': 'intervalData', 'type': 'SystemUserRoleIntervalData'},
        'interval_data_analysis': {'key': 'intervalDataAnalysis', 'type': 'SystemUserRoleIntervalDataAnalysis'},
        'energystar_submissions': {'key': 'energystarSubmissions', 'type': 'SystemUserRoleENERGYSTARSubmissions'},
        'facility_projects': {'key': 'facilityProjects', 'type': 'SystemUserRoleFacilityProjects'},
        'greenhouse_gas_administrator': {'key': 'greenhouseGasAdministrator', 'type': 'SystemUserRoleGreenhouseGasAdministrator'},
        'interval_data_rollup': {'key': 'intervalDataRollup', 'type': 'SystemUserRoleIntervalDataRollup'},
        'meters': {'key': 'meters', 'type': 'SystemUserRoleMeters'},
        'normalization_settings': {'key': 'normalizationSettings', 'type': 'SystemUserRoleNormalizationSettings'},
        'weather_settings': {'key': 'weatherSettings', 'type': 'SystemUserRoleWeatherSettings'},
        'reports_module': {'key': 'reportsModule', 'type': 'SystemUserRoleReportsModule'},
        'distributed_reports_settings': {'key': 'distributedReportsSettings', 'type': 'SystemUserRoleDistributedReportsSettings'},
        'install_or_update_reports': {'key': 'installOrUpdateReports', 'type': 'SystemUserRoleInstallOrUpdateReports'},
        'report_groups': {'key': 'reportGroups', 'type': 'SystemUserRoleReportGroups'},
        'shared_reports': {'key': 'sharedReports', 'type': 'SystemUserRoleSharedReports'},
        'reset_user_passwords': {'key': 'resetUserPasswords', 'type': 'SystemUserRoleResetUserPasswords'},
        'users_and_roles': {'key': 'usersAndRoles', 'type': 'SystemUserRoleUsersAndRoles'},
        'vendors_and_rates_module': {'key': 'vendorsAndRatesModule', 'type': 'SystemUserRoleVendorsAndRatesModule'},
        'rate_schedules': {'key': 'rateSchedules', 'type': 'SystemUserRoleRateSchedules'},
        'vendors': {'key': 'vendors', 'type': 'SystemUserRoleVendors'},
    }

    def __init__(self, accounting_settings=None, accounts=None, accounts_module=None, accrual_settings=None, cost_centers=None, move_accounts_between_vendors=None, application_settings=None, approve_bills=None, bill_audit_groups=None, bill_audits=None, bill_entry_templates=None, bill_workflow_settings=None, bills_and_batches=None, export_bills=None, export_hold=None, move_existing_bills=None, bill_audit_results_and_alerts=None, shared_bill_lists=None, unit_system_settings=None, update_approved_bills=None, update_units_on_existing_bills=None, budgets_and_budget_versions=None, chargebacks_module=None, chargeback_distributions=None, chargeback_reversals=None, submeter_routes=None, meter_savings_settings=None, savings_adjustments=None, manually_adjust_savings=None, savings_engine=None, baseline_engine=None, global_cost_avoidance_settings=None, dashboard_and_maps_module=None, dashboard_administrator=None, public_dashboards_or_maps=None, shared_dashboards_or_maps=None, buildings_and_meters_module=None, groups_and_benchmarks_module=None, building_and_meter_groups=None, buildings_and_organizations=None, interval_data=None, interval_data_analysis=None, energystar_submissions=None, facility_projects=None, greenhouse_gas_administrator=None, interval_data_rollup=None, meters=None, normalization_settings=None, weather_settings=None, reports_module=None, distributed_reports_settings=None, install_or_update_reports=None, report_groups=None, shared_reports=None, reset_user_passwords=None, users_and_roles=None, vendors_and_rates_module=None, rate_schedules=None, vendors=None):
        super(SystemUserRolePermissionsRequestDTO, self).__init__()
        self.accounting_settings = accounting_settings
        self.accounts = accounts
        self.accounts_module = accounts_module
        self.accrual_settings = accrual_settings
        self.cost_centers = cost_centers
        self.move_accounts_between_vendors = move_accounts_between_vendors
        self.application_settings = application_settings
        self.approve_bills = approve_bills
        self.bill_audit_groups = bill_audit_groups
        self.bill_audits = bill_audits
        self.bill_entry_templates = bill_entry_templates
        self.bill_workflow_settings = bill_workflow_settings
        self.bills_and_batches = bills_and_batches
        self.export_bills = export_bills
        self.export_hold = export_hold
        self.move_existing_bills = move_existing_bills
        self.bill_audit_results_and_alerts = bill_audit_results_and_alerts
        self.shared_bill_lists = shared_bill_lists
        self.unit_system_settings = unit_system_settings
        self.update_approved_bills = update_approved_bills
        self.update_units_on_existing_bills = update_units_on_existing_bills
        self.budgets_and_budget_versions = budgets_and_budget_versions
        self.chargebacks_module = chargebacks_module
        self.chargeback_distributions = chargeback_distributions
        self.chargeback_reversals = chargeback_reversals
        self.submeter_routes = submeter_routes
        self.meter_savings_settings = meter_savings_settings
        self.savings_adjustments = savings_adjustments
        self.manually_adjust_savings = manually_adjust_savings
        self.savings_engine = savings_engine
        self.baseline_engine = baseline_engine
        self.global_cost_avoidance_settings = global_cost_avoidance_settings
        self.dashboard_and_maps_module = dashboard_and_maps_module
        self.dashboard_administrator = dashboard_administrator
        self.public_dashboards_or_maps = public_dashboards_or_maps
        self.shared_dashboards_or_maps = shared_dashboards_or_maps
        self.buildings_and_meters_module = buildings_and_meters_module
        self.groups_and_benchmarks_module = groups_and_benchmarks_module
        self.building_and_meter_groups = building_and_meter_groups
        self.buildings_and_organizations = buildings_and_organizations
        self.interval_data = interval_data
        self.interval_data_analysis = interval_data_analysis
        self.energystar_submissions = energystar_submissions
        self.facility_projects = facility_projects
        self.greenhouse_gas_administrator = greenhouse_gas_administrator
        self.interval_data_rollup = interval_data_rollup
        self.meters = meters
        self.normalization_settings = normalization_settings
        self.weather_settings = weather_settings
        self.reports_module = reports_module
        self.distributed_reports_settings = distributed_reports_settings
        self.install_or_update_reports = install_or_update_reports
        self.report_groups = report_groups
        self.shared_reports = shared_reports
        self.reset_user_passwords = reset_user_passwords
        self.users_and_roles = users_and_roles
        self.vendors_and_rates_module = vendors_and_rates_module
        self.rate_schedules = rate_schedules
        self.vendors = vendors
