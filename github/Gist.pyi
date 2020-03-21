from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from github.GistComment import GistComment
from github.GistFile import GistFile
from github.GistHistoryState import GistHistoryState
from github.GithubObject import _NotSetType
from github.InputFileContent import InputFileContent
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList

class Gist:
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def comments(self) -> int: ...
    @property
    def comments_url(self) -> str: ...
    @property
    def commits_url(self) -> str: ...
    def create_comment(self, body: str) -> GistComment: ...
    def create_fork(self) -> Gist: ...
    @property
    def created_at(self) -> datetime: ...
    def delete(self) -> None: ...
    @property
    def description(self) -> Optional[str]: ...
    def edit(
        self,
        description: Union[_NotSetType, str] = ...,
        files: Union[_NotSetType, Dict[str, Optional[InputFileContent]]] = ...,
    ) -> None: ...
    @property
    def files(self) -> Dict[str, GistFile]: ...
    @property
    def fork_of(self) -> Optional[Gist]: ...
    @property
    def forks(self) -> List[Gist]: ...
    @property
    def forks_url(self) -> str: ...
    def get_comment(self, id: int) -> GistComment: ...
    def get_comments(self) -> PaginatedList: ...
    @property
    def git_pull_url(self) -> str: ...
    @property
    def git_push_url(self) -> str: ...
    @property
    def history(self) -> List[GistHistoryState]: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> str: ...
    def is_starred(self) -> bool: ...
    @property
    def owner(self) -> NamedUser: ...
    @property
    def public(self) -> bool: ...
    def reset_starred(self) -> None: ...
    def set_starred(self) -> None: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def user(self) -> Optional[NamedUser]: ...
