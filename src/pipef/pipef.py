"""The `pipef` class itself; see `pipef/__init__.py` for the public re-export"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterator


class _PipefMeta(type):
    """Lets a lazy chain start on the bare class, so `pipef | func` opens one without a call"""

    def __or__(cls, func: Callable[..., Any]) -> pipef:  # type: ignore[override]
        """Opens a lazy chain of `cls` and pipes `func` into it as the first step"""
        self = pipef.__new__(pipef)
        object.__setattr__(self, "args", ())
        object.__setattr__(self, "kwargs", {})
        object.__setattr__(self, "func_list", (func,))
        object.__setattr__(self, "eager", False)
        return self


@dataclass(frozen=True, init=False)
class pipef(metaclass=_PipefMeta):  # pylint: disable=invalid-name
    """
    Chains callables with `|`; calling `pipef(...)`, even with no arguments, pipes eagerly
    Only the bare class, never called, opens a lazy reusable chain — see USAGE.md for both modes
    """

    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    func_list: tuple[Callable[..., Any], ...]
    eager: bool

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Any direct call is eager, holding `args`/`kwargs` as the value to pipe through"""
        object.__setattr__(self, "args", args)
        object.__setattr__(self, "kwargs", kwargs)
        object.__setattr__(self, "func_list", ())
        object.__setattr__(self, "eager", True)

    def __or__(self, func: Callable[..., Any]) -> pipef:
        """Applies `func` now if eager, otherwise appends it to the lazy chain; both return a fresh `pipef`"""
        if self.eager:
            return pipef(func(*self.args, **self.kwargs))
        forked = pipef.__new__(pipef)
        object.__setattr__(forked, "args", ())
        object.__setattr__(forked, "kwargs", {})
        object.__setattr__(forked, "func_list", (*self.func_list, func))
        object.__setattr__(forked, "eager", False)
        return forked

    # Frozen dataclasses hash by field value by default, but `kwargs` is a dict, so hashing would
    # always blow up anyway — disable it outright rather than let that leak through as a surprise
    __hash__ = None  # type: ignore[assignment]

    @property
    def _value(self) -> Any:
        """The single value this eager pipef is holding, or `None` when it was given nothing at all"""
        if self.args:
            return self.args[0]
        if self.kwargs:
            raise TypeError("this pipef only holds keyword arguments — pipe them into a function first")
        return None

    def __iter__(self) -> Iterator[Any]:
        """Yields the held value, so an eager result can be unpacked with `result, =`"""
        if not self.eager:
            raise TypeError("a lazy pipef chain can't be unpacked — call it with a value instead")
        yield self._value

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Runs the lazy chain against `args`/`kwargs`, or with none, returns an eager result directly"""
        if self.eager:
            if args or kwargs:
                raise TypeError("an eager pipef takes no arguments — start a new pipef(value) instead")
            return self._value
        result = None
        for i, func in enumerate(self.func_list):
            result = func(*args, **kwargs) if i == 0 else func(result)
        return result

    def __repr__(self) -> str:
        """Shows the held value once eager, so a bare `pipef()` reads as `None`, not a raw dataclass repr"""
        if self.eager:
            if not self.args and self.kwargs:
                return f"pipef(**{self.kwargs!r})"
            return repr(self.args[0] if self.args else None)
        return f"<pipef lazy chain of {len(self.func_list)} step(s)>"
