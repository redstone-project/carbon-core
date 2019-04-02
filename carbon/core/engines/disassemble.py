#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    carbon.core.engines.disassemble
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Convert job to task

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2019 lightless. All rights reserved
"""

from silex.engines.thread import ThreadEngine

from carbon.db.constant.job import JobScanTypes
from carbon.utils.logger import logger
from carbon.db.models import CarbonJobsModel, CarbonTasksModel
from carbon.db.constant import JobStatus, JobType
from carbon.utils.target_parser import is_ip_target, is_url_target


class DisassembleEngine(ThreadEngine):
    def __init__(self, app_ctx, name):
        super(DisassembleEngine, self).__init__(app_ctx, name)

    def _worker(self):
        logger.info("{} start!".format(self.name))

        while self.is_running():

            rows = CarbonJobsModel.instance.filter(status=JobStatus.READY).all()
            if not rows:
                self.ev.wait(1)
                continue

            for row in rows:
                payloads = row.payloads
                job_id = row.id
                job_type = row.job_type
                scan_type = row.scan_types

                row.status = JobStatus.PREPARE
                row.save()

                self.split_job(payloads, job_id, job_type, scan_type)

        logger.info("{} stop!".format(self.name))

    def split_job(self, payloads, job_id, job_type, scan_type):
        """
        将job切分成task
        :param payloads:
        :param job_id:
        :param job_type:
        :param scan_type:
        :return:
        """
        payloads = payloads.replace("\r", "\n")
        payloads = payloads.split("\n")

        scan_types = scan_type.split(",")

        if job_type == JobType.ONCE:
            task_type_prefix = "ONCE_"
        elif job_type == JobType.DAILY:
            task_type_prefix = "DAILY_"
        else:
            logger.error("Unknown job_type: {}".format(job_type))
            return

        for target in payloads:
            if is_url_target(target):
                self.add_url_task(target)
                pass
            elif is_ip_target(target):
                pass
            else:
                logger.warning("Unknown parse target type, value: {}".format(target))

    def add_url_task(self, target, scan_types):
        for scan_type in scan_types:
            if scan_type == JobScanTypes.ATTACK:
                pass
            elif scan_type == JobScanTypes.PORT:
                pass
            elif scan_type == JobScanTypes.SPIDER:
                pass
            elif scan_type == JobScanTypes.BRUTE_DIR:
                pass
            elif scan_type == JobScanTypes.SUB_DOMAIN:
                pass
            else:
                pass

    def add_ip_task(self):
        pass
