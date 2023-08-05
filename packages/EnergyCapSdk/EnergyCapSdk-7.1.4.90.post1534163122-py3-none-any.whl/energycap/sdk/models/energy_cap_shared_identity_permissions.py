# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EnergyCapSharedIdentityPermissions(Model):
    """EnergyCapSharedIdentityPermissions.

    :param license_feature_accounting_export:
    :type license_feature_accounting_export:
     ~energycap.sdk.models.EnergyCapSharedIdentityLicenseFeatureAccountingExport
    :param license_feature_accrual_bills:
    :type license_feature_accrual_bills:
     ~energycap.sdk.models.EnergyCapSharedIdentityLicenseFeatureAccrualBills
    :param license_feature_chargebacks:
    :type license_feature_chargebacks:
     ~energycap.sdk.models.EnergyCapSharedIdentityLicenseFeatureChargebacks
    :param license_feature_cost_avoidance:
    :type license_feature_cost_avoidance:
     ~energycap.sdk.models.EnergyCapSharedIdentityLicenseFeatureCostAvoidance
    :param license_feature_interval_data_analysis:
    :type license_feature_interval_data_analysis:
     ~energycap.sdk.models.EnergyCapSharedIdentityLicenseFeatureIntervalDataAnalysis
    :param license_feature_report_designer:
    :type license_feature_report_designer:
     ~energycap.sdk.models.EnergyCapSharedIdentityLicenseFeatureReportDesigner
    :param accounting_settings:
    :type accounting_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityAccountingSettings
    :param accounts:
    :type accounts: ~energycap.sdk.models.EnergyCapSharedIdentityAccounts
    :param accounts_module:
    :type accounts_module:
     ~energycap.sdk.models.EnergyCapSharedIdentityAccountsModule
    :param accrual_settings:
    :type accrual_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityAccrualSettings
    :param cost_centers:
    :type cost_centers:
     ~energycap.sdk.models.EnergyCapSharedIdentityCostCenters
    :param move_accounts_between_vendors:
    :type move_accounts_between_vendors:
     ~energycap.sdk.models.EnergyCapSharedIdentityMoveAccountsBetweenVendors
    :param application_settings:
    :type application_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityApplicationSettings
    :param approve_bills:
    :type approve_bills:
     ~energycap.sdk.models.EnergyCapSharedIdentityApproveBills
    :param bill_audit_groups:
    :type bill_audit_groups:
     ~energycap.sdk.models.EnergyCapSharedIdentityBillAuditGroups
    :param bill_audits:
    :type bill_audits: ~energycap.sdk.models.EnergyCapSharedIdentityBillAudits
    :param bill_entry_templates:
    :type bill_entry_templates:
     ~energycap.sdk.models.EnergyCapSharedIdentityBillEntryTemplates
    :param bill_workflow_settings:
    :type bill_workflow_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityBillWorkflowSettings
    :param bills_and_batches:
    :type bills_and_batches:
     ~energycap.sdk.models.EnergyCapSharedIdentityBillsAndBatches
    :param export_bills:
    :type export_bills:
     ~energycap.sdk.models.EnergyCapSharedIdentityExportBills
    :param export_hold:
    :type export_hold: ~energycap.sdk.models.EnergyCapSharedIdentityExportHold
    :param move_existing_bills:
    :type move_existing_bills:
     ~energycap.sdk.models.EnergyCapSharedIdentityMoveExistingBills
    :param bill_audit_results_and_alerts:
    :type bill_audit_results_and_alerts:
     ~energycap.sdk.models.EnergyCapSharedIdentityBillAuditResultsAndAlerts
    :param shared_bill_lists:
    :type shared_bill_lists:
     ~energycap.sdk.models.EnergyCapSharedIdentitySharedBillLists
    :param unit_system_settings:
    :type unit_system_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityUnitSystemSettings
    :param update_approved_bills:
    :type update_approved_bills:
     ~energycap.sdk.models.EnergyCapSharedIdentityUpdateApprovedBills
    :param update_units_on_existing_bills:
    :type update_units_on_existing_bills:
     ~energycap.sdk.models.EnergyCapSharedIdentityUpdateUnitsOnExistingBills
    :param budgets_and_budget_versions:
    :type budgets_and_budget_versions:
     ~energycap.sdk.models.EnergyCapSharedIdentityBudgetsAndBudgetVersions
    :param chargebacks_module:
    :type chargebacks_module:
     ~energycap.sdk.models.EnergyCapSharedIdentityChargebacksModule
    :param chargeback_distributions:
    :type chargeback_distributions:
     ~energycap.sdk.models.EnergyCapSharedIdentityChargebackDistributions
    :param chargeback_reversals:
    :type chargeback_reversals:
     ~energycap.sdk.models.EnergyCapSharedIdentityChargebackReversals
    :param submeter_routes:
    :type submeter_routes:
     ~energycap.sdk.models.EnergyCapSharedIdentitySubmeterRoutes
    :param meter_savings_settings:
    :type meter_savings_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityMeterSavingsSettings
    :param savings_adjustments:
    :type savings_adjustments:
     ~energycap.sdk.models.EnergyCapSharedIdentitySavingsAdjustments
    :param manually_adjust_savings:
    :type manually_adjust_savings:
     ~energycap.sdk.models.EnergyCapSharedIdentityManuallyAdjustSavings
    :param savings_engine:
    :type savings_engine:
     ~energycap.sdk.models.EnergyCapSharedIdentitySavingsEngine
    :param baseline_engine:
    :type baseline_engine:
     ~energycap.sdk.models.EnergyCapSharedIdentityBaselineEngine
    :param global_cost_avoidance_settings:
    :type global_cost_avoidance_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityGlobalCostAvoidanceSettings
    :param dashboard_and_maps_module:
    :type dashboard_and_maps_module:
     ~energycap.sdk.models.EnergyCapSharedIdentityDashboardAndMapsModule
    :param dashboard_administrator:
    :type dashboard_administrator:
     ~energycap.sdk.models.EnergyCapSharedIdentityDashboardAdministrator
    :param public_dashboards_or_maps:
    :type public_dashboards_or_maps:
     ~energycap.sdk.models.EnergyCapSharedIdentityPublicDashboardsOrMaps
    :param shared_dashboards_or_maps:
    :type shared_dashboards_or_maps:
     ~energycap.sdk.models.EnergyCapSharedIdentitySharedDashboardsOrMaps
    :param buildings_and_meters_module:
    :type buildings_and_meters_module:
     ~energycap.sdk.models.EnergyCapSharedIdentityBuildingsAndMetersModule
    :param groups_and_benchmarks_module:
    :type groups_and_benchmarks_module:
     ~energycap.sdk.models.EnergyCapSharedIdentityGroupsAndBenchmarksModule
    :param building_and_meter_groups:
    :type building_and_meter_groups:
     ~energycap.sdk.models.EnergyCapSharedIdentityBuildingAndMeterGroups
    :param buildings_and_organizations:
    :type buildings_and_organizations:
     ~energycap.sdk.models.EnergyCapSharedIdentityBuildingsAndOrganizations
    :param interval_data:
    :type interval_data:
     ~energycap.sdk.models.EnergyCapSharedIdentityIntervalData
    :param interval_data_analysis:
    :type interval_data_analysis:
     ~energycap.sdk.models.EnergyCapSharedIdentityIntervalDataAnalysis
    :param energystar_submissions:
    :type energystar_submissions:
     ~energycap.sdk.models.EnergyCapSharedIdentityENERGYSTARSubmissions
    :param facility_projects:
    :type facility_projects:
     ~energycap.sdk.models.EnergyCapSharedIdentityFacilityProjects
    :param greenhouse_gas_administrator:
    :type greenhouse_gas_administrator:
     ~energycap.sdk.models.EnergyCapSharedIdentityGreenhouseGasAdministrator
    :param interval_data_rollup:
    :type interval_data_rollup:
     ~energycap.sdk.models.EnergyCapSharedIdentityIntervalDataRollup
    :param meters:
    :type meters: ~energycap.sdk.models.EnergyCapSharedIdentityMeters
    :param normalization_settings:
    :type normalization_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityNormalizationSettings
    :param weather_settings:
    :type weather_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityWeatherSettings
    :param reports_module:
    :type reports_module:
     ~energycap.sdk.models.EnergyCapSharedIdentityReportsModule
    :param distributed_reports_settings:
    :type distributed_reports_settings:
     ~energycap.sdk.models.EnergyCapSharedIdentityDistributedReportsSettings
    :param install_or_update_reports:
    :type install_or_update_reports:
     ~energycap.sdk.models.EnergyCapSharedIdentityInstallOrUpdateReports
    :param report_groups:
    :type report_groups:
     ~energycap.sdk.models.EnergyCapSharedIdentityReportGroups
    :param shared_reports:
    :type shared_reports:
     ~energycap.sdk.models.EnergyCapSharedIdentitySharedReports
    :param reset_user_passwords:
    :type reset_user_passwords:
     ~energycap.sdk.models.EnergyCapSharedIdentityResetUserPasswords
    :param users_and_roles:
    :type users_and_roles:
     ~energycap.sdk.models.EnergyCapSharedIdentityUsersAndRoles
    :param vendors_and_rates_module:
    :type vendors_and_rates_module:
     ~energycap.sdk.models.EnergyCapSharedIdentityVendorsAndRatesModule
    :param rate_schedules:
    :type rate_schedules:
     ~energycap.sdk.models.EnergyCapSharedIdentityRateSchedules
    :param vendors:
    :type vendors: ~energycap.sdk.models.EnergyCapSharedIdentityVendors
    """

    _attribute_map = {
        'license_feature_accounting_export': {'key': 'licenseFeatureAccountingExport', 'type': 'EnergyCapSharedIdentityLicenseFeatureAccountingExport'},
        'license_feature_accrual_bills': {'key': 'licenseFeatureAccrualBills', 'type': 'EnergyCapSharedIdentityLicenseFeatureAccrualBills'},
        'license_feature_chargebacks': {'key': 'licenseFeatureChargebacks', 'type': 'EnergyCapSharedIdentityLicenseFeatureChargebacks'},
        'license_feature_cost_avoidance': {'key': 'licenseFeatureCostAvoidance', 'type': 'EnergyCapSharedIdentityLicenseFeatureCostAvoidance'},
        'license_feature_interval_data_analysis': {'key': 'licenseFeatureIntervalDataAnalysis', 'type': 'EnergyCapSharedIdentityLicenseFeatureIntervalDataAnalysis'},
        'license_feature_report_designer': {'key': 'licenseFeatureReportDesigner', 'type': 'EnergyCapSharedIdentityLicenseFeatureReportDesigner'},
        'accounting_settings': {'key': 'accountingSettings', 'type': 'EnergyCapSharedIdentityAccountingSettings'},
        'accounts': {'key': 'accounts', 'type': 'EnergyCapSharedIdentityAccounts'},
        'accounts_module': {'key': 'accountsModule', 'type': 'EnergyCapSharedIdentityAccountsModule'},
        'accrual_settings': {'key': 'accrualSettings', 'type': 'EnergyCapSharedIdentityAccrualSettings'},
        'cost_centers': {'key': 'costCenters', 'type': 'EnergyCapSharedIdentityCostCenters'},
        'move_accounts_between_vendors': {'key': 'moveAccountsBetweenVendors', 'type': 'EnergyCapSharedIdentityMoveAccountsBetweenVendors'},
        'application_settings': {'key': 'applicationSettings', 'type': 'EnergyCapSharedIdentityApplicationSettings'},
        'approve_bills': {'key': 'approveBills', 'type': 'EnergyCapSharedIdentityApproveBills'},
        'bill_audit_groups': {'key': 'billAuditGroups', 'type': 'EnergyCapSharedIdentityBillAuditGroups'},
        'bill_audits': {'key': 'billAudits', 'type': 'EnergyCapSharedIdentityBillAudits'},
        'bill_entry_templates': {'key': 'billEntryTemplates', 'type': 'EnergyCapSharedIdentityBillEntryTemplates'},
        'bill_workflow_settings': {'key': 'billWorkflowSettings', 'type': 'EnergyCapSharedIdentityBillWorkflowSettings'},
        'bills_and_batches': {'key': 'billsAndBatches', 'type': 'EnergyCapSharedIdentityBillsAndBatches'},
        'export_bills': {'key': 'exportBills', 'type': 'EnergyCapSharedIdentityExportBills'},
        'export_hold': {'key': 'exportHold', 'type': 'EnergyCapSharedIdentityExportHold'},
        'move_existing_bills': {'key': 'moveExistingBills', 'type': 'EnergyCapSharedIdentityMoveExistingBills'},
        'bill_audit_results_and_alerts': {'key': 'billAuditResultsAndAlerts', 'type': 'EnergyCapSharedIdentityBillAuditResultsAndAlerts'},
        'shared_bill_lists': {'key': 'sharedBillLists', 'type': 'EnergyCapSharedIdentitySharedBillLists'},
        'unit_system_settings': {'key': 'unitSystemSettings', 'type': 'EnergyCapSharedIdentityUnitSystemSettings'},
        'update_approved_bills': {'key': 'updateApprovedBills', 'type': 'EnergyCapSharedIdentityUpdateApprovedBills'},
        'update_units_on_existing_bills': {'key': 'updateUnitsOnExistingBills', 'type': 'EnergyCapSharedIdentityUpdateUnitsOnExistingBills'},
        'budgets_and_budget_versions': {'key': 'budgetsAndBudgetVersions', 'type': 'EnergyCapSharedIdentityBudgetsAndBudgetVersions'},
        'chargebacks_module': {'key': 'chargebacksModule', 'type': 'EnergyCapSharedIdentityChargebacksModule'},
        'chargeback_distributions': {'key': 'chargebackDistributions', 'type': 'EnergyCapSharedIdentityChargebackDistributions'},
        'chargeback_reversals': {'key': 'chargebackReversals', 'type': 'EnergyCapSharedIdentityChargebackReversals'},
        'submeter_routes': {'key': 'submeterRoutes', 'type': 'EnergyCapSharedIdentitySubmeterRoutes'},
        'meter_savings_settings': {'key': 'meterSavingsSettings', 'type': 'EnergyCapSharedIdentityMeterSavingsSettings'},
        'savings_adjustments': {'key': 'savingsAdjustments', 'type': 'EnergyCapSharedIdentitySavingsAdjustments'},
        'manually_adjust_savings': {'key': 'manuallyAdjustSavings', 'type': 'EnergyCapSharedIdentityManuallyAdjustSavings'},
        'savings_engine': {'key': 'savingsEngine', 'type': 'EnergyCapSharedIdentitySavingsEngine'},
        'baseline_engine': {'key': 'baselineEngine', 'type': 'EnergyCapSharedIdentityBaselineEngine'},
        'global_cost_avoidance_settings': {'key': 'globalCostAvoidanceSettings', 'type': 'EnergyCapSharedIdentityGlobalCostAvoidanceSettings'},
        'dashboard_and_maps_module': {'key': 'dashboardAndMapsModule', 'type': 'EnergyCapSharedIdentityDashboardAndMapsModule'},
        'dashboard_administrator': {'key': 'dashboardAdministrator', 'type': 'EnergyCapSharedIdentityDashboardAdministrator'},
        'public_dashboards_or_maps': {'key': 'publicDashboardsOrMaps', 'type': 'EnergyCapSharedIdentityPublicDashboardsOrMaps'},
        'shared_dashboards_or_maps': {'key': 'sharedDashboardsOrMaps', 'type': 'EnergyCapSharedIdentitySharedDashboardsOrMaps'},
        'buildings_and_meters_module': {'key': 'buildingsAndMetersModule', 'type': 'EnergyCapSharedIdentityBuildingsAndMetersModule'},
        'groups_and_benchmarks_module': {'key': 'groupsAndBenchmarksModule', 'type': 'EnergyCapSharedIdentityGroupsAndBenchmarksModule'},
        'building_and_meter_groups': {'key': 'buildingAndMeterGroups', 'type': 'EnergyCapSharedIdentityBuildingAndMeterGroups'},
        'buildings_and_organizations': {'key': 'buildingsAndOrganizations', 'type': 'EnergyCapSharedIdentityBuildingsAndOrganizations'},
        'interval_data': {'key': 'intervalData', 'type': 'EnergyCapSharedIdentityIntervalData'},
        'interval_data_analysis': {'key': 'intervalDataAnalysis', 'type': 'EnergyCapSharedIdentityIntervalDataAnalysis'},
        'energystar_submissions': {'key': 'energystarSubmissions', 'type': 'EnergyCapSharedIdentityENERGYSTARSubmissions'},
        'facility_projects': {'key': 'facilityProjects', 'type': 'EnergyCapSharedIdentityFacilityProjects'},
        'greenhouse_gas_administrator': {'key': 'greenhouseGasAdministrator', 'type': 'EnergyCapSharedIdentityGreenhouseGasAdministrator'},
        'interval_data_rollup': {'key': 'intervalDataRollup', 'type': 'EnergyCapSharedIdentityIntervalDataRollup'},
        'meters': {'key': 'meters', 'type': 'EnergyCapSharedIdentityMeters'},
        'normalization_settings': {'key': 'normalizationSettings', 'type': 'EnergyCapSharedIdentityNormalizationSettings'},
        'weather_settings': {'key': 'weatherSettings', 'type': 'EnergyCapSharedIdentityWeatherSettings'},
        'reports_module': {'key': 'reportsModule', 'type': 'EnergyCapSharedIdentityReportsModule'},
        'distributed_reports_settings': {'key': 'distributedReportsSettings', 'type': 'EnergyCapSharedIdentityDistributedReportsSettings'},
        'install_or_update_reports': {'key': 'installOrUpdateReports', 'type': 'EnergyCapSharedIdentityInstallOrUpdateReports'},
        'report_groups': {'key': 'reportGroups', 'type': 'EnergyCapSharedIdentityReportGroups'},
        'shared_reports': {'key': 'sharedReports', 'type': 'EnergyCapSharedIdentitySharedReports'},
        'reset_user_passwords': {'key': 'resetUserPasswords', 'type': 'EnergyCapSharedIdentityResetUserPasswords'},
        'users_and_roles': {'key': 'usersAndRoles', 'type': 'EnergyCapSharedIdentityUsersAndRoles'},
        'vendors_and_rates_module': {'key': 'vendorsAndRatesModule', 'type': 'EnergyCapSharedIdentityVendorsAndRatesModule'},
        'rate_schedules': {'key': 'rateSchedules', 'type': 'EnergyCapSharedIdentityRateSchedules'},
        'vendors': {'key': 'vendors', 'type': 'EnergyCapSharedIdentityVendors'},
    }

    def __init__(self, license_feature_accounting_export=None, license_feature_accrual_bills=None, license_feature_chargebacks=None, license_feature_cost_avoidance=None, license_feature_interval_data_analysis=None, license_feature_report_designer=None, accounting_settings=None, accounts=None, accounts_module=None, accrual_settings=None, cost_centers=None, move_accounts_between_vendors=None, application_settings=None, approve_bills=None, bill_audit_groups=None, bill_audits=None, bill_entry_templates=None, bill_workflow_settings=None, bills_and_batches=None, export_bills=None, export_hold=None, move_existing_bills=None, bill_audit_results_and_alerts=None, shared_bill_lists=None, unit_system_settings=None, update_approved_bills=None, update_units_on_existing_bills=None, budgets_and_budget_versions=None, chargebacks_module=None, chargeback_distributions=None, chargeback_reversals=None, submeter_routes=None, meter_savings_settings=None, savings_adjustments=None, manually_adjust_savings=None, savings_engine=None, baseline_engine=None, global_cost_avoidance_settings=None, dashboard_and_maps_module=None, dashboard_administrator=None, public_dashboards_or_maps=None, shared_dashboards_or_maps=None, buildings_and_meters_module=None, groups_and_benchmarks_module=None, building_and_meter_groups=None, buildings_and_organizations=None, interval_data=None, interval_data_analysis=None, energystar_submissions=None, facility_projects=None, greenhouse_gas_administrator=None, interval_data_rollup=None, meters=None, normalization_settings=None, weather_settings=None, reports_module=None, distributed_reports_settings=None, install_or_update_reports=None, report_groups=None, shared_reports=None, reset_user_passwords=None, users_and_roles=None, vendors_and_rates_module=None, rate_schedules=None, vendors=None):
        super(EnergyCapSharedIdentityPermissions, self).__init__()
        self.license_feature_accounting_export = license_feature_accounting_export
        self.license_feature_accrual_bills = license_feature_accrual_bills
        self.license_feature_chargebacks = license_feature_chargebacks
        self.license_feature_cost_avoidance = license_feature_cost_avoidance
        self.license_feature_interval_data_analysis = license_feature_interval_data_analysis
        self.license_feature_report_designer = license_feature_report_designer
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
