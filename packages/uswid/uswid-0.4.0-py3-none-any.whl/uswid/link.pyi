from _typeshed import Incomplete
from enum import IntEnum
from typing import Optional

class uSwidLinkRel(IntEnum):
    LICENSE: int
    COMPILER: int
    ANCESTOR: int
    COMPONENT: int
    FEATURE: int
    INSTALLATIONMEDIA: int
    PACKAGEINSTALLER: int
    PARENT: int
    PATCHES: int
    REQUIRES: int
    SEE_ALSO: int
    SUPERSEDES: int
    SUPPLEMENTAL: int

class uSwidLink:
    href: Incomplete
    def __init__(self, href: Optional[str] = ..., rel: Optional[str] = ...) -> None: ...
    @property
    def rel(self) -> Optional[str]: ...
    @rel.setter
    def rel(self, rel: Optional[str]) -> None: ...
    @property
    def href_for_display(self) -> Optional[str]: ...
