#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dim.__version__ import __version__  # noqa: F401
from dim.dim import (load_data, fetch_data,  # noqa: F401
                     load_dim_json, load_dim_lock_json,
                     init, install, uninstall,
                     update, list, search)
