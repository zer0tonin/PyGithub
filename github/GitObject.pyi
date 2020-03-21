from typing import Dict

class GitObject:
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, str]) -> None: ...
    @property
    def sha(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def url(self) -> str: ...
