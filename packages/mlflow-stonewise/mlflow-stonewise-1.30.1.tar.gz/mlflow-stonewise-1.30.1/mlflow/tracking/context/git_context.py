import logging

from mlflow.tracking.context.abstract_context import RunContextProvider
from mlflow.tracking.context.default_context import _get_main_file
from mlflow.utils.git_utils import get_git_commit, get_git_repo_url, get_git_commit_date
from mlflow.utils.mlflow_tags import MLFLOW_GIT_COMMIT, MLFLOW_GIT_REPO_URL, MLFLOW_GIT_COM_DATE

_logger = logging.getLogger(__name__)


def _get_source_version():
    main_file = _get_main_file()
    if main_file is not None:
        return get_git_commit(main_file)
    return None


def _get_source_url():
    main_file = _get_main_file()
    if main_file is not None:
        return get_git_repo_url(main_file)
    return None


def _get_source_committed_date():
    main_file = _get_main_file()
    if main_file is not None:
        return get_git_commit_date(main_file)
    return None


class GitRunContext(RunContextProvider):
    def __init__(self):
        self._cache = {}

    @property
    def _source_version(self):
        if "source_version" not in self._cache:
            self._cache["source_version"] = _get_source_version()
        return self._cache["source_version"]

    @property
    def _source_url(self):
        if "source_url" not in self._cache:
            self._cache["source_url"] = _get_source_url()
        return self._cache["source_url"]

    @property
    def _source_date(self):
        if "source_date" not in self._cache:
            self._cache["source_date"] = _get_source_committed_date()
        return self._cache["source_date"]

    def in_context(self):
        return self._source_version is not None or \
               self._source_url is not None or \
               self._source_date is not None

    def tags(self):
        return {MLFLOW_GIT_COMMIT: self._source_version,
                MLFLOW_GIT_REPO_URL: self._source_url,
                MLFLOW_GIT_COM_DATE: self._source_date}
