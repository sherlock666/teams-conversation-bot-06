#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "35506354-62bd-4c0b-a4f8-7f103c6404c2")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "_z@lfJPIbvSb53M8n0cKFMSm-HgGMkK]")
