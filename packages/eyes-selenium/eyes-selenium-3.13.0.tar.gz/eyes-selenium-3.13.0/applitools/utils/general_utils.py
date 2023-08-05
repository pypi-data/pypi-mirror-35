"""
General purpose utilities.
"""
from __future__ import absolute_import

import json
import types
import typing as tp
from datetime import timedelta, tzinfo

from .compat import range

if tp.TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.remote.switch_to import SwitchTo

    from applitools._webdriver import EyesWebDriver, EyesWebElement, _EyesSwitchTo


class _UtcTz(tzinfo):
    """
    A UTC timezone class which is tzinfo compliant.
    """
    _ZERO = timedelta(0)

    def utcoffset(self, dt):
        return _UtcTz._ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return _UtcTz._ZERO


# Constant representing UTC
UTC = _UtcTz()


def to_json(obj):
    # type: (tp.Dict[str, tp.Any]) -> str
    """
    Returns an object's json representation (defaults to __getstate__ for user defined types).
    """
    return json.dumps(obj, default=lambda o: o.__getstate__(), indent=4)


def public_state_to_json(obj):
    """
    Returns an object's json representation, without(!) its private variables.
    DO NOT USE! This method has a problem with "datetime" objects (which have no __dict__
    attribute).
    """

    def get_public_state(o):
        return {key: value for key, value in o.__dict__.items()
                if not callable(value) and not key.startswith('_')}

    return json.dumps(obj, default=lambda o: get_public_state(o), indent=4)


def divide_to_chunks(l, chunk_size):
    """
    Divides a list into chunks.

    :param l: The list to divide.
    :param chunk_size: The size of each chunk
    :return: A list of lists. Each internal list has a maximum size of chunk_size (last item might be shorter).
    """
    result = []
    for i in range(0, len(l), chunk_size):
        result.extend([l[i:i + chunk_size]])
    return result


def join_chunks(l):
    """
    Joins a list of chunks into a single continuous list of values.

    :param l: The list of chunks to join.
    :return: A single composed the concatenated values of the chunks.
    """
    result = []
    for i in l:
        result.extend(i)
    return result


def create_proxy_property(property_name, target_name, is_settable=False):
    # type: (str, str, bool) -> property
    """
    Returns a property object which forwards "name" to target.

    :param property_name: The name of the property.
    :param target_name: The target to forward to.
    """

    # noinspection PyUnusedLocal
    def _proxy_get(self):
        # type: (tp.Any) -> tp.Dict[str, float]
        return getattr(getattr(self, target_name), property_name)

    # noinspection PyUnusedLocal
    def _proxy_set(self, val):
        return setattr(getattr(self, target_name), property_name, val)

    if not is_settable:
        return property(_proxy_get)
    else:
        return property(_proxy_get, _proxy_set)


def create_forwarded_method(from_,  # type: tp.Union[EyesWebDriver, EyesWebElement, _EyesSwitchTo]
                            to,  # type: tp.Union[WebDriver, WebElement, SwitchTo]
                            func_name,  # type: str
                            ):
    # type: (...) -> tp.Callable
    """
    Returns a method(!) to be set on 'from_', which activates 'func_name' on 'to'.

    :param from_: Source.
    :param to: Destination.
    :param func_name: The name of function to activate.
    :return: Relevant method.
    """

    # noinspection PyUnusedLocal
    def forwarded_method(self_, *args, **kwargs):
        # type: (EyesWebDriver, *tp.Any, **tp.Any) -> tp.Callable
        return getattr(to, func_name)(*args, **kwargs)

    return types.MethodType(forwarded_method, from_)


def create_proxy_interface(from_,  # type: tp.Union[EyesWebDriver, EyesWebElement, _EyesSwitchTo]
                           to,  # type: tp.Union[WebDriver, WebElement, SwitchTo]
                           ignore_list=None,  # type: tp.List[str]
                           override_existing=False,  # type: bool
                           ):
    # type: (...) -> None
    """
    Copies the public interface of the destination object, excluding names in the ignore_list,
    and creates an identical interface in 'src', which forwards calls to dst.

    :param from_: Source.
    :param to: Destination.
    :param ignore_list: List of names to ignore while copying.
    :param override_existing: If False, attributes already existing in 'src' will not be overridden.
    """
    if not ignore_list:
        ignore_list = []
    for attr_name in dir(to):
        if not attr_name.startswith('_') and attr_name not in ignore_list:
            if callable(getattr(to, attr_name)):
                if override_existing or not hasattr(from_, attr_name):
                    setattr(from_, attr_name, create_forwarded_method(from_, to, attr_name))


def cached_property(f):
    # type: (tp.Callable) -> tp.Any
    """
    Returns a cached property that is calculated by function f
    """
    def get(self):
        try:
            return self._property_cache[f]
        except AttributeError:
            self._property_cache = {}
            x = self._property_cache[f] = f(self)
            return x
        except KeyError:
            x = self._property_cache[f] = f(self)
            return x

    return property(get)
