# coding: utf-8

# flake8: noqa
"""
    Detection On Demand

    FireEye offers a best-in-class virtual execution engine in many of its core products, including our Network Security, Email Security, and File Analysis solutions. Now our customers can interact with and consume those capabilities directly via a scalable and performant web service. Use the new RESTful API to submit files for malware analysis, search hash values for past analysis results, get full reports for your file submissions, and integrate into your existing toolsets and workflows.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: developers@fireeye.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from feye_detection.models.forbidden import Forbidden
from feye_detection.models.inline_object import InlineObject
from feye_detection.models.internal_server_error import InternalServerError
from feye_detection.models.rate_limit_exceeded import RateLimitExceeded
from feye_detection.models.report_extended import ReportExtended
from feye_detection.models.report_extended_engine_results import ReportExtendedEngineResults
from feye_detection.models.report_extended_engine_results_av_lookup import ReportExtendedEngineResultsAvLookup
from feye_detection.models.report_extended_engine_results_avs_lookup import ReportExtendedEngineResultsAvsLookup
from feye_detection.models.report_extended_engine_results_dti_lookup import ReportExtendedEngineResultsDtiLookup
from feye_detection.models.report_extended_engine_results_dynamic_analysis import ReportExtendedEngineResultsDynamicAnalysis
from feye_detection.models.report_extended_engine_results_dynamic_analysis_analysis_info import ReportExtendedEngineResultsDynamicAnalysisAnalysisInfo
from feye_detection.models.report_extended_engine_results_dynamic_analysis_analysis_info_analysis_objects import ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjects
from feye_detection.models.report_extended_engine_results_dynamic_analysis_analysis_info_chk_sum import ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoChkSum
from feye_detection.models.report_extended_engine_results_dynamic_analysis_analysis_info_network_anomaly import ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoNetworkAnomaly
from feye_detection.models.report_extended_engine_results_dynamic_analysis_analysis_info_os_changes import ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges
from feye_detection.models.report_extended_engine_results_dynamic_analysis_analysis_info_os_changes_correlation_results import ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesCorrelationResults
from feye_detection.models.report_extended_engine_results_dynamic_analysis_analysis_info_os_changes_vm_results import ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesVmResults
from feye_detection.models.report_extended_engine_results_dynamic_analysis_analysis_info_work_orders import ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoWorkOrders
from feye_detection.models.report_extended_engine_results_fireml import ReportExtendedEngineResultsFireml
from feye_detection.models.report_not_extended import ReportNotExtended
from feye_detection.models.unauthorized import Unauthorized