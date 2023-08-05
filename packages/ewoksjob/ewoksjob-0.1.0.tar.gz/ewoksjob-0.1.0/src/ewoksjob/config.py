import os
import sys
import logging
import importlib
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse, ParseResult

from celery.loaders.base import BaseLoader
from celery import Celery

try:
    from blissdata.beacon.files import read_config as bliss_read_config
except ImportError:
    bliss_read_config = None

logger = logging.getLogger(__name__)


class EwoksLoader(BaseLoader):
    """Celery loader based on a configuration URI: python file, python module, yaml file, Beacon URL.

    Requires the environment variable CELERY_LOADER=ewoksjob.config.EwoksLoader
    """

    def __init__(self, app: Celery) -> None:
        self.app = app
        super().__init__(app)

    def read_configuration(self) -> Optional[dict]:
        config = read_configuration(get_cfg_uri())
        if config:
            return config
        return super().read_configuration()


def get_cfg_uri() -> str:
    """Returns the celery configuration URL based on environment variables."""
    cfg_uri = os.environ.get("CELERY_CONFIG_URI")
    if cfg_uri:
        return cfg_uri
    beacon_host = os.environ.get("BEACON_HOST", None)
    if beacon_host:
        return "beacon:///ewoks/config.yml"
    return ""


def read_configuration(cfg_uri: Optional[str] = None) -> Optional[dict]:
    """When the URI is not provided, we will assume it is the python module "celeryconfig"
    (or whatever module defined by the CELERY_CONFIG_MODULE environment variable).

    Different types of URI's are supported:

     - Python module:
        - myproject.config
     - Python file:
        - /tmp/ewoks/config.py
     - Yaml file:
        - /tmp/ewoks/config.yml
     - Beacon yaml file:
        - beacon:///ewoks/config.yml  (this requires the BEACON_HOST environment variable)
        - beacon://id22:25000/ewoks/config.yml
    """
    file_type = None
    if cfg_uri:
        presult = _parse_url(cfg_uri)
        if presult.scheme == "beacon":
            file_type = "yaml"
        elif presult.scheme in ("file", ""):
            cfg_uri = _url_to_filename(presult)
            if os.path.splitext(cfg_uri)[-1] == ".py":
                file_type = "python"
            else:
                file_type = "yaml"
    else:
        file_type = "python"

    logger.info(f"Loading celery configuration '{cfg_uri}' ({file_type})")

    if file_type == "yaml":
        config = _read_yaml_config(cfg_uri)
    elif file_type == "python":
        config = _read_py_config(cfg_uri)
    else:
        raise ValueError(f"Configuration URL '{cfg_uri}' is not supported")

    if config:
        if "celery" in config:
            config = config["celery"]
        elif "CELERY" in config:
            config = config["CELERY"]

    if not config:
        logger.warning(
            f"Celery configuration from '{cfg_uri}' is empty or could not be loaded. Fall back to celery's configuration discovery mechanism"
        )

    return config


def _parse_url(url: str) -> ParseResult:
    presult = urlparse(url)
    if presult.scheme == "beacon":
        # beacon:///path/to/file.yml
        # beacon://id00:25000/path/to/file.yml
        return presult
    elif presult.scheme in ("file", ""):
        # /path/to/file.yaml
        # file:///path/to/file.yaml
        return presult
    elif sys.platform == "win32" and len(presult.scheme) == 1:
        # c:\\path\\to\\file.yaml
        return urlparse(f"file://{url}")
    else:
        return presult


def _url_to_filename(presult: ParseResult) -> str:
    if presult.netloc and presult.path:
        # urlparse("file://c:/a/b")
        return presult.netloc + presult.path
    elif presult.netloc:
        # urlparse("file://c:\\a\\b")
        return presult.netloc
    else:
        return presult.path


def _read_yaml_config(resource: str) -> Optional[dict]:
    if bliss_read_config is None:
        logger.error(
            f"Cannot get celery configuration '{resource}' from Beacon: blissdata is not installed"
        )
        return
    try:
        return bliss_read_config(resource)
    except Exception as e:
        logger.error(f"Cannot get celery configuration '{resource}' from Beacon: {e}")


def _read_py_config(cfg_uri: Optional[str] = None) -> Optional[dict]:
    """Warning: this is not thread-safe and it has side-effects during execution"""
    sys_path, module = _get_config_module(cfg_uri)
    keep_sys_path = sys.path
    sys.path.insert(0, sys_path)
    try:
        try:
            config = vars(importlib.import_module(module))
        except ModuleNotFoundError:
            if cfg_uri:
                logger.error(
                    f"Celery configuration module '{module}' cannot be imported (Extra import path: {sys_path})"
                )
            return None
        mtype = type(os)
        config = {
            k: v
            for k, v in config.items()
            if not k.startswith("_") and not isinstance(v, mtype)
        }
        return config
    finally:
        sys.path = keep_sys_path


def _get_config_module(cfg_uri: Optional[str] = None) -> Tuple[str, str]:
    if not cfg_uri:
        cfg_uri = os.environ.get("CELERY_CONFIG_MODULE")
    if not cfg_uri:
        return os.getcwd(), "celeryconfig"
    path = Path(cfg_uri)
    if path.is_file():
        parent = str(path.parent.resolve())
        return parent, path.stem
    return os.getcwd(), cfg_uri
