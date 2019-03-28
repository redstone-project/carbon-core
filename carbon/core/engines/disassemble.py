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

from carbon.utils.logger import logger
from carbon.db.models import CarbonJobsModel
from carbon.db.constant import JobStatus
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
                row.status = JobStatus.READY
                row.save()
                self.split_job(payloads, job_id, job_type)

        logger.info("{} stop!".format(self.name))

    @staticmethod
    def split_job(payloads, job_id, job_type):
        """
        将job切分成task
        :param payloads:
        :param job_id:
        :param job_type:
        :return:
        """
        payloads = payloads.replace("\r", "\n")
        payloads = payloads.split("\n")

        for target in payloads:
            if is_url_target(target):
                pass
            elif is_ip_target(target):
                pass
            else:
                logger.warning("Unknown parse target type, value: {}".format(target))

