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

from carbon.db.constant import JobStatus, TaskType
from carbon.db.models import CarbonJobsModel, CarbonTasksModel
from carbon.utils.logger import logger
from carbon.utils.target_parser import is_ip_target, is_url_target


class SplitEngine(ThreadEngine):
    def __init__(self, app_ctx, name):
        super(SplitEngine, self).__init__(app_ctx, name)

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
                scan_type = row.scan_types
                cycle = row.cycle

                row.status = JobStatus.PREPARE
                row.save()

                self.split_job(payloads, job_id, cycle, scan_type)

        logger.info("{} stop!".format(self.name))

    def split_job(self, payloads, job_id, cycle, scan_types):
        """
        将job切分成task
        :param payloads:
        :param job_id:
        :param cycle:
        :param scan_types:
        :return:
        """

        # 将payload转换为list，并且去掉空串
        payloads = payloads.replace("\r", "\n")
        payloads = payloads.split("\n")
        payloads.remove("")

        # 将job的扫描类型转换为list
        scan_types = scan_types.split(",")

        # 循环处理每个payload
        for payload in payloads:
            if is_ip_target(payload):
                # 这里不需要考虑任务转换功能
                self._add_task(payload, scan_types, job_id, cycle, "ip")
            elif is_url_target(payload):
                # 添加url类型的任务
                self._add_task(payload, scan_types, job_id, cycle, "url")
            else:
                logger.warning("skipping unknown task: {}".format(payload))
                continue

    @staticmethod
    def _add_task(target, scan_types, job_id, cycle, _type):

        _task_types = {
            "ip": [
                TaskType.PORT,
                TaskType.ATTACK,
            ],
            "url": [
                TaskType.SUB_DOMAIN,
                TaskType.BRUTE_DIR,
                TaskType.WEB_SPIDER,
                TaskType.ATTACK,
            ]
        }

        for st in scan_types:
            if st in _task_types.get(_type, []):
                CarbonTasksModel.instance.create_task(
                    job_id, st, target, cycle
                )
