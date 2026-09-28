"""Importing this module registers every table on ``Base.metadata``."""

from bluemage.models.automation import AutomationLink
from bluemage.models.case import Tag, TestCase, TestCaseVersion, test_case_tags
from bluemage.models.plan import TestPlan, TestPlanCase
from bluemage.models.project import Project
from bluemage.models.run import Result, Run
from bluemage.models.run_job import RunJob
from bluemage.models.suite import Suite

__all__ = [
    "AutomationLink",
    "Project",
    "Result",
    "Run",
    "RunJob",
    "Suite",
    "Tag",
    "TestCase",
    "TestCaseVersion",
    "TestPlan",
    "TestPlanCase",
    "test_case_tags",
]
