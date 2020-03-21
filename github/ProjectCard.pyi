from datetime import datetime
from typing import Any, Dict, Optional, Union

from github.GithubObject import _NotSetType
from github.Issue import Issue
from github.NamedUser import NamedUser
from github.PullRequest import PullRequest

class ProjectCard:
    def _repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def archived(self) -> bool: ...
    @property
    def column_url(self) -> str: ...
    @property
    def content_url(self) -> Optional[str]: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def creator(self) -> NamedUser: ...
    def get_content(
        self, content_type: Union[_NotSetType, str] = ...
    ) -> Optional[Union[PullRequest, Issue]]: ...
    @property
    def id(self) -> int: ...
    @property
    def node_id(self) -> str: ...
    @property
    def note(self) -> str: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
