"""Strangeworks SDK."""

import importlib.metadata

from .config import config
from .sw_client import SWClient

__version__ = importlib.metadata.version("strangeworks")

cfg = config.Config()
client = SWClient(cfg=cfg)  # instantiate a client on import by default

# strangeworks.(public method)
authenticate = client.authenticate
workspace_info = client.workspace_info
resources = client.resources
execute = client.execute
jobs = client.jobs
