from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `mytestsdk3.resources` module.

    This is used so that we can lazily import `mytestsdk3.resources` only when
    needed *and* so that users can just import `mytestsdk3` and reference `mytestsdk3.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("mytestsdk3.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
