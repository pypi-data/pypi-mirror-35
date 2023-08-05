# -*- coding: utf-8 -*-
"""
Run pytest --collect-only and generate XMLs.
"""

from __future__ import absolute_import, unicode_literals

import io
import json
import logging
import os
import subprocess
import sys

from cfme_testcases import consts
from cfme_testcases.exceptions import TestcasesException
from dump2polarion.requirements_exporter import RequirementExport
from dump2polarion.testcases_exporter import TestcaseExport
from dump2polarion.xunit_exporter import ImportedData, XunitExport

# pylint: disable=invalid-name
logger = logging.getLogger(__name__)


_JSON_FILES = (consts.TEST_CASE_JSON, consts.TEST_RUN_JSON)


def _check_environment():
    # check that launched in integration tests repo
    if not os.path.exists(consts.TESTS_PATH):
        raise TestcasesException("Not running in the integration tests repo")
    # check that running in virtualenv
    if not hasattr(sys, "real_prefix"):
        raise TestcasesException("Not running in virtual environment")


def _cleanup():
    for fname in _JSON_FILES:
        try:
            os.remove(fname)
        except OSError:
            pass


def _load_json(json_file):
    with io.open(json_file, encoding="utf-8") as input_json:
        return json.load(input_json)


def run_pytest():
    """Runs the pytest command."""
    pytest_retval = None
    _check_environment()
    _cleanup()

    args = [
        "miq-runtest",
        "-qq",
        "--collect-only",
        "--long-running",
        "--perf",
        "--runxfail",
        "--include-manual",
        "--disablemetaplugins",
        "blockers",
        "--use-provider",
        "complete",
        "--generate-jsons",
    ]

    logger.info("Generating the XMLs using '%s'", " ".join(args))
    with open(os.devnull, "w") as devnull:
        pytest_proc = subprocess.Popen(args, stdout=devnull, stderr=devnull)
        try:
            pytest_retval = pytest_proc.wait()
        # pylint: disable=broad-except
        except Exception:
            try:
                pytest_proc.terminate()
            except OSError:
                pass
            pytest_proc.wait()
            return None

    missing_files = []
    for fname in _JSON_FILES:
        if not os.path.exists(fname):
            missing_files.append(fname)
    if missing_files:
        raise TestcasesException(
            "The JSON files {} were not generated".format(" and ".join(missing_files))
        )

    return pytest_retval


def _resolve_requirements(requirements_mapping, testcases_data):
    for testcase_rec in testcases_data:
        requirement_name = testcase_rec.get("linked-items")
        if not requirement_name:
            continue
        if not requirements_mapping:
            del testcase_rec["linked-items"]
            continue

        requirement_id = requirements_mapping.get(requirement_name)
        if requirement_id:
            testcase_rec["linked-items"] = requirement_id
        else:
            del testcase_rec["linked-items"]


def gen_testcases_xml_str(testcases_json, requirements_mapping, config, transform_func=None):
    """Generates the testcases XML string."""
    try:
        testcases_data = _load_json(testcases_json)["results"]
    except KeyError:
        raise TestcasesException("Not valid testcases JSON.")
    _resolve_requirements(requirements_mapping, testcases_data)
    testsuite = TestcaseExport(testcases_data, config, transform_func)
    return testsuite.export()


def gen_testsuite_xml_str(testsuite_json, testrun_id, config, transform_func=None):
    """Generates the testcases XML string."""
    assert testrun_id
    try:
        results = _load_json(testsuite_json)["results"]
    except KeyError:
        raise TestcasesException("Not valid testsuite JSON.")
    testsuite_data = ImportedData(results, testrun_id)
    testsuite = XunitExport(testrun_id, testsuite_data, config, transform_func)
    return testsuite.export()


def gen_requirements_xml_str(requirements_data, config, transform_func=None):
    """Generates the requirements XML string."""
    requirements = RequirementExport(requirements_data, config, transform_func)
    return requirements.export()
