#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
import json

logger = logging.getLogger("uaa_client")
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


class UAAClient(object):
    def __init__(self, client, username: str, password: str, entrypoint: str):
        self.client = client
        self.username = username
        self.password = password
        self.entrypoint = entrypoint
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_token(self):
        status_code, response = self.client.post(self.entrypoint, headers=self.headers, json={
            'username': self.username,
            'password': self.password
        })
        logger.info("get token %s: [%d]", self.entrypoint, status_code)
        if status_code == 200:
            data = json.loads(response.content)
            return data['token']
        else:
            logger.info(response)
            return None


