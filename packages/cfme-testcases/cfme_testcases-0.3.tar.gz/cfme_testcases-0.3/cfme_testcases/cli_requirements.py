# -*- coding: utf-8 -*-
"""
Create missing requirements and create list of requirements names and IDs.
"""

from __future__ import absolute_import, unicode_literals

import logging
import os

from cfme_testcases import cli_utils, gen_xmls, parselog, parsereq
from cfme_testcases.exceptions import TestcasesException
from dump2polarion import properties, submit
from dump2polarion import utils as d2p_utils

# pylint: disable=invalid-name
logger = logging.getLogger(__name__)


def get_req_logname(args):
    """Returns filename of the message bus log file."""
    req_log = "req-job-{}.log".format(cli_utils.get_filename_str(args))
    req_log = os.path.join(args.output_dir or "", req_log)
    return req_log


def gen_requirements_xml_str(config):
    """Generates the requirements XML string."""
    requirements_data = parsereq.get_requirements()
    return gen_xmls.gen_requirements_xml_str(requirements_data, config)


def get_requirements_xml_root(config):
    """Gets the requirements XML root."""
    req_xml_str = gen_requirements_xml_str(config)
    return d2p_utils.get_xml_root_from_str(req_xml_str)


def submit_requirements_xml(submit_args, config, req_xml_root, log):
    """Submits the pre-generated requirements file to the importer."""
    properties.remove_response_property(req_xml_root)

    if not submit.submit_and_verify(
        xml_root=req_xml_root, config=config, log_file=log, **submit_args
    ):
        raise TestcasesException("Failed to do the requirements submit")


def update_requirements(args, submit_args, req_xml_root, config):
    """Updates the requirements in Polarion."""
    if args.no_submit:
        return None

    req_logname = get_req_logname(args)
    submit_requirements_xml(submit_args, config, req_xml_root, req_logname)
    return req_logname


def get_requirements_from_log(req_logname):
    """Generates the requirements JSON using importer log file."""
    if req_logname:
        req_logname = os.path.expanduser(req_logname)
    if not (req_logname and os.path.isfile(req_logname)):
        logger.warning("No requirements log file supplied, skipping requirements generation.")
        return None
    return parselog.get_requirements(req_logname)


def get_requirements_mapping(args, submit_args, config, req_xml_root):
    """Generates the requirements mapping."""
    if args.no_requirements:
        return None

    req_logname = update_requirements(args, submit_args, req_xml_root, config)
    return get_requirements_from_log(req_logname)
