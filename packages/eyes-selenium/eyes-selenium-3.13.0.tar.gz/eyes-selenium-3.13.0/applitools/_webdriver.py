from __future__ import absolute_import

import abc
import base64
import re
import math
import time
import typing as tp

from PIL import Image
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from . import _viewport_size, logger
from .common import StitchMode
from .errors import EyesError, OutOfBoundsError
from .geometry import Point, Region
from .utils import _image_utils, general_utils
from .utils.general_utils import cached_property
from .utils.compat import ABC

if tp.TYPE_CHECKING:
    from .eyes import Eyes
    from .scaling import ScaleProvider
    from .utils._custom_types import Num, ViewPort, FrameReference, AnyWebDriver, AnyWebElement


class EyesScreenshot(object):
    @staticmethod
    def create_from_base64(screenshot64, driver):
        """
        Creates an instance from the base64 data.

        :param screenshot64: The base64 representation of the png bytes.
        :param driver: The webdriver for the session.
        """
        return EyesScreenshot(driver, screenshot64=screenshot64)

    @staticmethod
    def create_from_image(screenshot, driver):
        # type: (PngImage, EyesWebDriver) -> EyesScreenshot
        """
        Creates an instance from the base64 data.

        :param screenshot: The screenshot image.
        :param driver: The webdriver for the session.
        """
        return EyesScreenshot(driver, screenshot=screenshot)

    def __init__(self, driver, screenshot=None, screenshot64=None,
                 is_viewport_screenshot=None, frame_location_in_screenshot=None):
        # type: (EyesWebDriver, PngImage, None, tp.Optional[bool], tp.Optional[Point]) -> None
        """
        Initializes a Screenshot instance. Either screenshot or screenshot64 must NOT be None.
        Should not be used directly. Use create_from_image/create_from_base64 instead.

        :param driver: EyesWebDriver instance which handles the session from which the screenshot
                    was retrieved.
        :param screenshot: image instance. If screenshot64 is None,
                                    this variable must NOT be none.
        :param screenshot64: The base64 representation of a png image. If screenshot
                                     is None, this variable must NOT be none.
        :param is_viewport_screenshot: Whether the screenshot object represents a
                                                viewport screenshot or a full screenshot.
        :param frame_location_in_screenshot: The location of the frame relative
                                                    to the top,left of the screenshot.
        :raise EyesError: If the screenshots are None.
        """
        self._screenshot64 = screenshot64
        if screenshot:
            self._screenshot = screenshot
        elif screenshot64:
            self._screenshot = _image_utils.image_from_bytes(base64.b64decode(screenshot64))
        else:
            raise EyesError("both screenshot and screenshot64 are None!")
        self._driver = driver
        self._viewport_size = driver.get_default_content_viewport_size()  # type: ViewPort

        self._frame_chain = driver.get_frame_chain()
        if self._frame_chain:
            chain_len = len(self._frame_chain)
            self._frame_size = self._frame_chain[chain_len - 1].size
        else:
            try:
                self._frame_size = driver.get_entire_page_size()
            except WebDriverException:
                # For Appium, we can't get the "entire page size", so we use the viewport size.
                self._frame_size = self._viewport_size
        # For native Appium Apps we can't get the scroll position, so we use (0,0)
        try:
            self._scroll_position = driver.get_current_position()
        except (WebDriverException, EyesError):
            self._scroll_position = Point(0, 0)
        if is_viewport_screenshot is None:
            is_viewport_screenshot = (self._screenshot.width <= self._viewport_size['width']
                                      and self._screenshot.height <= self._viewport_size['height'])
        self._is_viewport_screenshot = is_viewport_screenshot
        if frame_location_in_screenshot is None:
            if self._frame_chain:
                frame_location_in_screenshot = EyesScreenshot \
                    .calc_frame_location_in_screenshot(self._frame_chain, is_viewport_screenshot)
            else:
                # The frame is the default content
                frame_location_in_screenshot = Point(0, 0)
                if self._is_viewport_screenshot:
                    frame_location_in_screenshot.offset(-self._scroll_position.x,
                                                        -self._scroll_position.y)
        self._frame_location_in_screenshot = frame_location_in_screenshot
        self._frame_screenshot_intersect = Region(frame_location_in_screenshot.x,
                                                  frame_location_in_screenshot.y,
                                                  self._frame_size['width'],
                                                  self._frame_size['height'])
        self._frame_screenshot_intersect.intersect(Region(width=self._screenshot.width,
                                                          height=self._screenshot.height))

    @staticmethod
    def calc_frame_location_in_screenshot(frame_chain, is_viewport_screenshot):
        # type: (tp.List[EyesFrame], tp.Optional[bool]) -> Point
        """
        :param frame_chain: List of the frames.
        :param is_viewport_screenshot: Whether the viewport is a screenshot or not.
        :return: The frame location as it would be on the screenshot. Notice that this value
            might actually be OUTSIDE the screenshot (e.g, if this is a viewport screenshot and
            the frame is located outside the viewport). This is not an error. The value can also
            be negative.
        """
        first_frame = frame_chain[0]
        location_in_screenshot = Point(first_frame.location['x'], first_frame.location['y'])
        # We only need to consider the scroll of the default content if the screenshot is a
        # viewport screenshot. If this is a full page screenshot, the frame location will not
        # change anyway.
        if is_viewport_screenshot:
            location_in_screenshot.x -= first_frame.parent_scroll_position.x
            location_in_screenshot.y -= first_frame.parent_scroll_position.y
        # For inner frames we must calculate the scroll
        inner_frames = frame_chain[1:]
        for frame in inner_frames:
            location_in_screenshot.x += frame.location['x'] - frame.parent_scroll_position.x
            location_in_screenshot.y += frame.location['y'] - frame.parent_scroll_position.y
        return location_in_screenshot

    def get_frame_chain(self):
        # type: () -> tp.List[EyesFrame]
        """
        Returns a copy of the fram chain.

        :return: A copy of the frame chain, as received by the driver when the screenshot was
            created.
        """
        return [frame.clone() for frame in self._frame_chain]

    def get_base64(self):
        """
        Returns a base64 screenshot.

        :return: The base64 representation of the png.
        """
        if not self._screenshot64:
            self._screenshot64 = _image_utils.get_base64(self._screenshot)
        return self._screenshot64

    def get_bytes(self):
        # type: () -> bytes
        """
        Returns the bytes of the screenshot.

        :return: The bytes representation of the png.
        """
        return _image_utils.get_bytes(self._screenshot)

    def get_location_relative_to_frame_viewport(self, location):
        # type: (tp.Dict[tp.Text, Num]) -> tp.Dict[tp.Text, Num]
        """
        Gets the relative location from a given location to the viewport.

        :param location: A dict with 'x' and 'y' keys representing the location we want
            to adjust.
        :return: A location (keys are 'x' and 'y') adjusted to the current frame/viewport.
        """
        result = {'x': location['x'], 'y': location['y']}
        if self._frame_chain or self._is_viewport_screenshot:
            result['x'] -= self._scroll_position.x
            result['y'] -= self._scroll_position.y
        return result

    def get_element_region_in_frame_viewport(self, element):
        # type: (AnyWebElement) -> Region
        """
        Gets The element region in the frame.

        :param element: The element to get the region in the frame.
        :return: The element's region in the frame with scroll considered if necessary
        """
        location, size = element.location, element.size

        relative_location = self.get_location_relative_to_frame_viewport(location)

        x, y = relative_location['x'], relative_location['y']
        width, height = size['width'], size['height']
        # We only care about the part of the element which is in the viewport.
        if x < 0:
            diff = -x
            # IMPORTANT the diff is between the original location and the viewport's bounds.
            width -= diff
            x = 0
        if y < 0:
            diff = -y
            height -= diff
            y = 0

        if width <= 0 or height <= 0:
            raise OutOfBoundsError("Element's region is outside the viewport! [(%d, %d) %d x %d]" %
                                   (location['x'], location['y'], size['width'], size['height']))

        return Region(x, y, width, height)

    def get_intersected_region(self, region):
        # type: (Region) -> Region
        """
        Gets the intersection of the region with the screenshot image.

        :param region: The region in the frame.
        :return: The part of the region which intersects with
            the screenshot image.
        """
        region_in_screenshot = region.clone()
        region_in_screenshot.left += self._frame_location_in_screenshot.x
        region_in_screenshot.top += self._frame_location_in_screenshot.y
        region_in_screenshot.intersect(self._frame_screenshot_intersect)
        return region_in_screenshot

    def get_intersected_region_by_element(self, element):
        """
        Gets the intersection of the element's region with the screenshot image.

        :param element: The element in the frame.
        :return: The part of the element's region which intersects with
            the screenshot image.
        """
        element_region = self.get_element_region_in_frame_viewport(element)
        return self.get_intersected_region(element_region)

    def get_sub_screenshot_by_region(self, region):
        # type: (Region) -> EyesScreenshot
        """
        Gets the region part of the screenshot image.

        :param region: The region in the frame.
        :return: A screenshot object representing the given region part of the image.
        """
        sub_screenshot_region = self.get_intersected_region(region)
        if sub_screenshot_region.is_empty():
            raise OutOfBoundsError("Region {0} is out of bounds!".format(region))
        # If we take a screenshot of a region inside a frame, then the frame's (0,0) is in the
        # negative offset of the region..
        sub_screenshot_frame_location = Point(-region.left, -region.top)

        # FIXME Calculate relative region location? (same as the java version)

        screenshot = _image_utils.get_image_part(self._screenshot, sub_screenshot_region)
        return EyesScreenshot(self._driver, screenshot,
                              is_viewport_screenshot=self._is_viewport_screenshot,
                              frame_location_in_screenshot=sub_screenshot_frame_location)

    def get_sub_screenshot_by_element(self, element):
        # type: (EyesWebElement) -> EyesScreenshot
        """
        Gets the element's region part of the screenshot image.

        :param element: The element in the frame.
        :return: A screenshot object representing the element's region part of the
            image.
        """
        element_region = self.get_element_region_in_frame_viewport(element)
        return self.get_sub_screenshot_by_region(element_region)

    def get_viewport_screenshot(self):
        # type: () -> EyesScreenshot
        """
        Always return viewport size screenshot
        """
        # if screenshot if full page
        if not self._is_viewport_screenshot and not self._driver.is_mobile_device():
            return self.get_sub_screenshot_by_region(
                Region(top=self._scroll_position.y, height=self._viewport_size['height'],
                       width=self._viewport_size['width']))
        return self


class PositionProvider(ABC):
    """ Encapsulates page/element positioning """
    _JS_GET_CONTENT_ENTIRE_SIZE = """
        var scrollWidth = document.documentElement.scrollWidth;
        var bodyScrollWidth = document.body.scrollWidth;
        var totalWidth = Math.max(scrollWidth, bodyScrollWidth);
        var clientHeight = document.documentElement.clientHeight;
        var bodyClientHeight = document.body.clientHeight;
        var scrollHeight = document.documentElement.scrollHeight;
        var bodyScrollHeight = document.body.scrollHeight;
        var maxDocElementHeight = Math.max(clientHeight, scrollHeight);
        var maxBodyHeight = Math.max(bodyClientHeight, bodyScrollHeight);
        var totalHeight = Math.max(maxDocElementHeight, maxBodyHeight);
        return [totalWidth, totalHeight];";
    """

    def __init__(self, driver):
        # type: (AnyWebDriver) -> None
        self._driver = driver
        self._states = []  # type: tp.List[Point]

    def _execute_script(self, script):
        # type: (tp.Text) -> tp.List[int]
        return self._driver.execute_script(script)

    @abc.abstractmethod
    def get_current_position(self):
        # type: () -> tp.Optional[Point]
        """
        :return: The current position, or `None` if position is not available.
        """

    @abc.abstractmethod
    def set_position(self, location):
        # type: (Point) -> None
        """
        Go to the specified location.

        :param location: The position to set
        :return:
        """

    def get_entire_size(self):
        # type: () -> ViewPort
        """
        :return: The entire size of the container which the position is relative to.
        """
        try:
            width, height = self._driver.execute_script(self._JS_GET_CONTENT_ENTIRE_SIZE)
        except WebDriverException:
            raise EyesError('Failed to extract entire size!')
        return dict(width=width, height=height)

    def push_state(self):
        """
        Adds the current position to the states list.
        """
        self._states.append(self.get_current_position())

    def pop_state(self):
        """
        Sets the position to be the last position added to the states list.
        """
        self.set_position(self._states.pop())


class ScrollPositionProvider(PositionProvider):
    _JS_GET_CURRENT_SCROLL_POSITION = """
        var doc = document.documentElement;
        var x = window.scrollX || ((window.pageXOffset || doc.scrollLeft) - (doc.clientLeft || 0));
        var y = window.scrollY || ((window.pageYOffset || doc.scrollTop) - (doc.clientTop || 0));
        return [x, y]"""

    def set_position(self, location):
        scroll_command = "window.scrollTo({0}, {1})".format(location.x, location.y)
        logger.debug(scroll_command)
        self._execute_script(scroll_command)

    def get_current_position(self):
        try:
            x, y = self._execute_script(self._JS_GET_CURRENT_SCROLL_POSITION)
            if x is None or y is None:
                raise EyesError("Got None as scroll position! ({},{})".format(x, y))
        except WebDriverException:
            raise EyesError("Failed to extract current scroll position!")
        return Point(x, y)


class CSSTranslatePositionProvider(PositionProvider):
    _JS_TRANSFORM_KEYS = ["transform", "-webkit-transform"]

    def __init__(self, driver):
        super(CSSTranslatePositionProvider, self).__init__(driver)
        self._current_position = Point(0, 0)

    def _set_transform(self, transform_list):
        script = ''
        for key, value in transform_list.items():
            script += "document.documentElement.style['{}'] = '{}';".format(key, value)
        self._execute_script(script)

    def _get_current_transform(self):
        script = 'return {'
        for key in self._JS_TRANSFORM_KEYS:
            script += "'{0}': document.documentElement.style['{0}'],".format(key)
        script += ' }'
        return self._execute_script(script)

    def get_current_position(self):
        return self._current_position.clone()

    def _get_position_from_transform(self, transform):
        data = re.match(r"^translate\(\s*(\-?)([\d, \.]+)px,\s*(\-?)([\d, \.]+)px\s*\)", transform)
        if not data:
            raise EyesError("Can't parse CSS transition")

        x = float(data.group(2))
        y = float(data.group(4))
        minus_x, minus_y = data.group(1), data.group(3)
        if minus_x:
            x *= -1
        if minus_y:
            y *= -1

        return Point(float(x), float(y))

    def set_position(self, location):
        translate_command = "translate(-{}px, -{}px)".format(location.x, location.y)
        logger.debug(translate_command)
        transform_list = dict((key, translate_command) for key in self._JS_TRANSFORM_KEYS)
        self._set_transform(transform_list)
        self._current_position = location.clone()

    def push_state(self):
        """
        Adds the transform to the states list.
        """
        transforms = self._get_current_transform()
        if not all(transforms.values()):
            self._current_position = Point.create_top_left()
        else:
            point = Point(0, 0)
            for transform in transforms.values():
                point += self._get_position_from_transform(transform)
            self._current_position = point
        self._states.append(self._current_position)


class ElementPositionProvider(PositionProvider):

    def __init__(self, driver, element):
        # type: (AnyWebDriver, tp.Optional[AnyWebElement]) -> None
        super(ElementPositionProvider, self).__init__(driver)
        self._element = element

    def get_current_position(self):
        position = Point(self._element.get_scroll_left(), self._element.get_scroll_top())
        logger.info("Current position: {}".format(position))
        return position

    def set_position(self, location):
        logger.info("Scrolling element to {}".format(location))
        self._element.scroll_to(location)
        logger.info("Done scrolling element!")

    def get_entire_size(self):
        try:
            size = {'width': self._element.get_scroll_width(), 'height': self._element.get_scroll_height()}
        except WebDriverException:
            raise EyesError('Failed to extract entire size!')
        logger.info("ElementPositionProvider - Entire size: {}".format(size))
        return size


def build_position_provider_for(stitch_mode,  # type: tp.Text
                                driver,  # type: WebDriver
                                ):
    # type: (...) -> tp.Union[CSSTranslatePositionProvider, ScrollPositionProvider]
    if stitch_mode == StitchMode.Scroll:
        return ScrollPositionProvider(driver)
    elif stitch_mode == StitchMode.CSS:
        return CSSTranslatePositionProvider(driver)
    raise ValueError("Invalid stitch mode: {}".format(stitch_mode))


class EyesWebElement(object):
    """
    A wrapper for selenium web element. This enables eyes to be notified about actions/events for
    this element.
    """
    _METHODS_TO_REPLACE = ['find_element', 'find_elements']

    # Properties require special handling since even testing if they're callable "activates"
    # them, which makes copying them automatically a problem.
    _READONLY_PROPERTIES = ['tag_name', 'text', 'location_once_scrolled_into_view', 'size',
                            'location', 'parent', 'id', 'rect', 'screenshot_as_base64', 'screenshot_as_png',
                            'location_in_view', 'anonymous_children']
    _JS_GET_COMPUTED_STYLE_FORMATTED_STR = """
            var elem = arguments[0];
            var styleProp = '%s';
            if (window.getComputedStyle) {
                return window.getComputedStyle(elem, null)
                .getPropertyValue(styleProp);
            } else if (elem.currentStyle) {
                return elem.currentStyle[styleProp];
            } else {
                return null;
            }
    """
    _JS_GET_SCROLL_LEFT = "return arguments[0].scrollLeft;"
    _JS_GET_SCROLL_TOP = "return arguments[0].scrollTop;"
    _JS_GET_SCROLL_WIDTH = "return arguments[0].scrollWidth;"
    _JS_GET_SCROLL_HEIGHT = "return arguments[0].scrollHeight;"
    _JS_GET_OVERFLOW = "return arguments[0].style.overflow;"
    _JS_SET_OVERFLOW_FORMATTED_STR = "arguments[0].style.overflow = '%s'"
    _JS_GET_CLIENT_WIDTH = "return arguments[0].clientWidth;"
    _JS_GET_CLIENT_HEIGHT = "return arguments[0].clientHeight;"
    _JS_SCROLL_TO_FORMATTED_STR = """
            arguments[0].scrollLeft = {:d};
            arguments[0].scrollTop = {:d};
    """

    def __init__(self, element, eyes, driver):
        # type: (WebElement, Eyes, EyesWebDriver) -> None
        """
        Ctor.

        :param element: The element in the frame.
        :param eyes: The eyes sdk instance.
        :param driver: EyesWebDriver instance.
        """
        self.element = element
        self._eyes = eyes
        self._driver = driver  # type: AnyWebDriver
        # Replacing implementation of the underlying driver with ours. We'll put the original
        # methods back before destruction.
        self._original_methods = {}  # type: tp.Dict[tp.Text, tp.Callable]
        for method_name in self._METHODS_TO_REPLACE:
            self._original_methods[method_name] = getattr(element, method_name)
            setattr(element, method_name, getattr(self, method_name))

        # Copies the web element's interface
        general_utils.create_proxy_interface(self, element, self._READONLY_PROPERTIES)
        # Setting properties
        for attr in self._READONLY_PROPERTIES:
            setattr(self.__class__, attr, general_utils.create_proxy_property(attr, 'element'))

    @property
    def bounds(self):
        # type: () -> Region
        # noinspection PyUnresolvedReferences
        location = self._driver.location
        left, top = location['x'], location['y']
        width = height = 0  # Default

        # noinspection PyBroadException
        try:
            size = self.element.size
            width, height = size['width'], size['height']
        except Exception:
            # Not implemented on all platforms.
            pass
        if left < 0:
            left, width = 0, max(0, width + left)
        if top < 0:
            top, height = 0, max(0, height + top)
        return Region(left, top, width, height)

    def find_element(self, by=By.ID, value=None):
        """
        Returns a WebElement denoted by "By".

        :param by: By which option to search for (default is by ID).
        :param value: The value to search for.
        :return: WebElement denoted by "By".
        """
        # Get result from the original implementation of the underlying driver.
        result = self._original_methods['find_element'](by, value)
        # Wrap the element.
        if result:
            result = EyesWebElement(result, self._eyes, self._driver)
        return result

    def find_elements(self, by=By.ID, value=None):
        """
        Returns a list of web elements denoted by "By".

        :param by: By which option to search for (default is by ID).
        :param value: The value to search for.
        :return: List of web elements denoted by "By".
        """
        # Get result from the original implementation of the underlying driver.
        results = self._original_methods['find_elements'](by, value)
        # Wrap all returned elements.
        if results:
            updated_results = []
            for element in results:
                updated_results.append(EyesWebElement(element, self._eyes, self._driver))
            results = updated_results
        return results

    def click(self):
        """
        Clicks and element.
        """
        self._eyes.add_mouse_trigger_by_element('click', self)
        self.element.click()

    def send_keys(self, *value):
        """
        Sends keys to a certain element.

        :param value: The value to type into the element.
        """
        text = u''
        for val in value:
            if isinstance(val, int):
                val = val.__str__()
            text += val.encode('utf-8').decode('utf-8')
        self._eyes.add_text_trigger_by_element(self, text)
        self.element.send_keys(*value)

    def set_overflow(self, overflow, stabilization_time=None):
        """
        Sets the overflow of the current element.

        :param overflow: The overflow value to set. If the given value is None, then overflow will be set to
                         undefined.
        :param stabilization_time: The time to wait for the page to stabilize after overflow is set. If the value is
                                    None, then no waiting will take place. (Milliseconds)
        :return: The previous overflow value.
        """
        logger.debug("Setting overflow: %s" % overflow)
        if overflow is None:
            script = "var elem = arguments[0]; var origOverflow = elem.style.overflow; " \
                     "elem.style.overflow = undefined; " \
                     "return origOverflow;"
        else:
            script = "var elem = arguments[0]; var origOverflow = elem.style.overflow; " \
                     "elem.style.overflow = \"{0}\"; " \
                     "return origOverflow;".format(overflow)
        # noinspection PyUnresolvedReferences
        original_overflow = self._driver.execute_script(script, self.element)
        logger.debug("Original overflow: %s" % original_overflow)
        if stabilization_time is not None:
            time.sleep(stabilization_time / 1000)
        return original_overflow

    def hide_scrollbars(self):
        # type: () -> tp.Text
        """
        Hides the scrollbars of the current element.

        :return: The previous value of the overflow property (could be None).
        """
        logger.debug('EyesWebElement.HideScrollbars()')
        return self.set_overflow('hidden')

    def get_computed_style(self, prop_style):
        script = self._JS_GET_COMPUTED_STYLE_FORMATTED_STR % prop_style
        return self._driver.execute_script(script, self.element)

    def get_computed_style_int(self, prop_style):

        value = self.get_computed_style(prop_style)
        return int(round(float(value.replace('px', '').strip())))

    def get_scroll_left(self):
        return int(math.ceil(self._driver.execute_script(self._JS_GET_SCROLL_LEFT, self.element)))

    def get_scroll_top(self):
        return math.ceil(self._driver.execute_script(self._JS_GET_SCROLL_TOP, self.element))

    def get_scroll_width(self):
        return int(math.ceil(self._driver.execute_script(self._JS_GET_SCROLL_WIDTH, self.element)))

    def get_scroll_height(self):
        return int(math.ceil(self._driver.execute_script(self._JS_GET_SCROLL_HEIGHT, self.element)))

    def get_border_left_width(self):
        return self.get_computed_style_int('border-left-width')

    def get_border_right_width(self):
        return self.get_computed_style_int('border-right-width')

    def get_border_top_width(self):
        return self.get_computed_style_int('border-right-width')

    def get_border_bottom_width(self):
        return self.get_computed_style_int('border-right-width')

    def get_overflow(self):
        return self._driver.execute_script(self._JS_GET_OVERFLOW, self.element)

    def get_client_width(self):
        return int(math.ceil(float(self._driver.execute_script(self._JS_GET_CLIENT_WIDTH, self.element))))

    def get_client_height(self):
        return int(math.ceil(float(self._driver.execute_script(self._JS_GET_CLIENT_HEIGHT, self.element))))

    def scroll_to(self, location):
        # type: (Point) -> None
        """Scrolls to the specified location inside the element."""
        self._driver.execute_script(
            self._JS_SCROLL_TO_FORMATTED_STR.format(location.x, location.y), self.element)


class _EyesSwitchTo(object):
    """
    Wraps a selenium "SwitchTo" object, so we can keep track of switching between frames.
    """
    _READONLY_PROPERTIES = ['alert', 'active_element']
    PARENT_FRAME = 1

    def __init__(self, driver, switch_to):
        # type: (EyesWebDriver, SwitchTo) -> None
        """
        Ctor.

        :param driver: EyesWebDriver instance.
        :param switch_to: Selenium switchTo object.
        """
        self._switch_to = switch_to
        self._driver = driver  # type: AnyWebDriver
        general_utils.create_proxy_interface(self, switch_to, self._READONLY_PROPERTIES)

    def frame(self, frame_reference):
        # type: (FrameReference) -> None
        """
        Switch to a given frame.

        :param frame_reference: The reference to the frame.
        """
        # Find the frame's location and add it to the current driver offset
        if isinstance(frame_reference, str):
            frame_element = self._driver.find_element_by_name(frame_reference)
        elif isinstance(frame_reference, int):
            frame_elements_list = self._driver.find_elements_by_css_selector('frame, iframe')
            frame_element = frame_elements_list[frame_reference]
        else:
            # It must be a WebElement
            if isinstance(frame_reference, EyesWebElement):
                frame_reference = frame_reference.element
            frame_element = frame_reference
        # Calling the underlying "SwitchTo" object
        # noinspection PyProtectedMember
        self._driver._will_switch_to(frame_reference, frame_element)
        self._switch_to.frame(frame_reference)

    def frames(self, frame_chain):
        # type: (tp.List[EyesFrame]) -> None
        """
        Switches to the frames one after the other.

        :param frame_chain: A list of frames.
        """
        for frame in frame_chain:
            self._driver.scroll_to(frame.parent_scroll_position)
            self.frame(frame.reference)

    def default_content(self):
        # type: () -> None
        """
        Switch to default content.
        """
        # We should only do anything if we're inside a frame.
        if self._driver.get_frame_chain():
            # This call resets the driver's current frame location
            # noinspection PyProtectedMember
            self._driver._will_switch_to(None)
            self._switch_to.default_content()

    def parent_frame(self):
        """
        Switch to parent frame.
        """
        # IMPORTANT We implement switching to parent frame ourselves here, since it's not yet
        # implemented by the webdriver.

        # Notice that this is a COPY of the frames.
        frames = self._driver.get_frame_chain()
        if frames:
            frames.pop()

            # noinspection PyProtectedMember
            self._driver._will_switch_to(_EyesSwitchTo.PARENT_FRAME)

            self.default_content()
            self.frames(frames)

    def window(self, window_name):
        # type: (tp.Text) -> None
        """
        Switch to window.

        :param window_name: The window name to switch to.
        :return:The switched to window object.
        """
        # noinspection PyProtectedMember
        self._driver._will_switch_to(None)
        self._switch_to.window(window_name)


class EyesFrame(object):
    """
    Encapsulates data about frames.
    """

    @staticmethod
    def is_same_frame_chain(frame_chain1, frame_chain2):
        # type: (tp.List[EyesFrame], tp.List[EyesFrame]) -> bool
        """
        Checks whether the two frame chains are the same or not.

        :param frame_chain1: list of _EyesFrame instances, which represents a path to a frame.
        :param frame_chain2: list of _EyesFrame instances, which represents a path to a frame.
        :return: True if the frame chains ids are identical, otherwise False.
        """
        cl1, cl2 = len(frame_chain1), len(frame_chain2)
        if cl1 != cl2:
            return False
        for i in range(cl1):
            if frame_chain1[i].id_ != frame_chain2[i].id_:
                return False
        return True

    def __init__(self, reference, location, size, id_, parent_scroll_position):
        # type: (FrameReference, tp.Dict, tp.Dict, int, Point) -> None
        """
        Ctor.

        :param reference: The reference to the frame.
        :param location: The location of the frame.
        :param size: The size of the frame.
        :param id_: The id of the frame.
        :param parent_scroll_position: The parents' scroll position.
        """
        self.reference = reference
        self.location = location
        self.size = size
        self.id_ = id_
        self.parent_scroll_position = parent_scroll_position

    def clone(self):
        # type: () -> EyesFrame
        """
        Clone the EyesFrame object.

        :return: A cloned EyesFrame object.
        """
        return EyesFrame(self.reference, self.location.copy(), self.size.copy(), self.id_,
                         self.parent_scroll_position.clone())


class EyesWebDriver(object):
    """
    A wrapper for selenium web driver which creates wrapped elements, and notifies us about
    events / actions.
    """
    # Properties require special handling since even testing if they're callable "activates"
    # them, which makes copying them automatically a problem.
    _READONLY_PROPERTIES = ['application_cache', 'current_url', 'current_window_handle',
                            'desired_capabilities', 'log_types', 'name', 'page_source', 'title',
                            'window_handles', 'switch_to', 'mobile', 'current_context', 'context',
                            'current_activity', 'network_connection', 'available_ime_engines',
                            'active_ime_engine', 'device_time', 'w3c', 'contexts', 'current_package']
    _SETTABLE_PROPERTIES = ['orientation', 'file_detector']

    # This should pretty much cover all scroll bars (and some fixed position footer elements :) ).
    _MAX_SCROLL_BAR_SIZE = 50

    _MIN_SCREENSHOT_PART_HEIGHT = 10

    def __init__(self, driver, eyes, stitch_mode=StitchMode.Scroll):
        # type: (WebDriver, Eyes, tp.Text) -> None
        """
        Ctor.

        :param driver: remote WebDriver instance.
        :param eyes: A Eyes sdk instance.
        :param stitch_mode: How to stitch a page (default is with scrolling).
        """
        self.driver = driver
        self._eyes = eyes
        self._origin_position_provider = build_position_provider_for(StitchMode.Scroll, driver)
        self._position_provider = build_position_provider_for(stitch_mode, driver)
        # tp.List of frames the user switched to, and the current offset, so we can properly
        # calculate elements' coordinates
        self._frames = []  # type: tp.List[EyesFrame]
        self.driver_takes_screenshot = driver.capabilities.get('takesScreenshot', False)

        # Creating the rest of the driver interface by simply forwarding it to the underlying
        # driver.
        general_utils.create_proxy_interface(self, driver,
                                             self._READONLY_PROPERTIES + self._SETTABLE_PROPERTIES)

        for attr in self._READONLY_PROPERTIES:
            if not hasattr(self.__class__, attr):
                setattr(self.__class__, attr, general_utils.create_proxy_property(attr, 'driver'))
        for attr in self._SETTABLE_PROPERTIES:
            if not hasattr(self.__class__, attr):
                setattr(self.__class__, attr, general_utils.create_proxy_property(attr, 'driver', True))

    def get_display_rotation(self):
        # type: () -> int
        """
        Get the rotation of the screenshot.

        :return: The rotation of the screenshot we get from the webdriver in (degrees).
        """
        if self.platform_name == 'Android' and self.driver.orientation == "LANDSCAPE":
            return -90
        return 0

    def get_platform_name(self):
        return self.platform_name

    def get_platform_version(self):
        return self.platform_version

    @cached_property
    def platform_name(self):
        # type: () -> tp.Optional[tp.Text]
        return self.driver.desired_capabilities.get('platformName', None)

    @cached_property
    def platform_version(self):
        # type: () -> tp.Optional[tp.Text]
        return self.driver.desired_capabilities.get('platformVersion', None)

    @cached_property
    def browser_version(self):
        # type: () -> tp.Optional[float]
        caps = self.driver.capabilities
        version = caps.get('browserVersion', caps.get('version', None))
        if version:
            # convert version that has few dots in to float number (e.g. Edge 1.23.45)
            if version.find('.') != -1:
                version = float(version[:version.index('.') + 2])
            else:
                version = float(version)
        return version

    @cached_property
    def browser_name(self):
        # type: () -> tp.Optional[tp.Text]
        caps = self.driver.capabilities
        return caps.get('browserName', caps.get('browser', None))

    @cached_property
    def user_agent(self):
        try:
            user_agent = self.driver.execute_script("return navigator.userAgent")
            logger.info("user agent: {}".format(user_agent))
        except Exception as e:
            logger.info("Failed to obtain user-agent string")
            user_agent = None
        return user_agent

    def is_mobile_device(self):
        # type: () -> bool
        """
        Returns whether the platform running is a mobile device or not.

        :return: True if the platform running the test is a mobile platform. False otherwise.
        """
        return self.driver.capabilities.get('platformName') in ('Android', 'iOS')

    def get(self, url):
        # type: (tp.Text) -> tp.Optional[tp.Any]
        """
        Navigates the driver to the given url.

        :param url: The url to navigate to.
        :return: A driver that navigated to the given url.
        """
        # We're loading a new page, so the frame location resets
        self._frames = []  # type: tp.List[EyesFrame]
        return self.driver.get(url)

    def find_element(self, by=By.ID, value=None):
        # type: (tp.Text, tp.Text) -> EyesWebElement
        """
        Returns a WebElement denoted by "By".

        :param by: By which option to search for (default is by ID).
        :param value: The value to search for.
        :return: A element denoted by "By".
        """
        # Get result from the original implementation of the underlying driver.
        result = self.driver.find_element(by, value)
        # Wrap the element.
        if result:
            result = EyesWebElement(result, self._eyes, self)
        return result

    def find_elements(self, by=By.ID, value=None):
        # type: (tp.Text, tp.Text) -> tp.List[EyesWebElement]
        """
        Returns a list of web elements denoted by "By".

        :param by: By which option to search for (default is by ID).
        :param value: The value to search for.
        :return: List of elements denoted by "By".
        """
        # Get result from the original implementation of the underlying driver.
        results = self.driver.find_elements(by, value)
        # Wrap all returned elements.
        if results:
            updated_results = []
            for element in results:
                updated_results.append(EyesWebElement(element, self._eyes, self))
            results = updated_results
        return results

    def find_element_by_id(self, id_):
        # type: (tp.Text) -> EyesWebElement
        """
        Finds an element by id.

        :params id_: The id of the element to be found.
        """
        return self.find_element(by=By.ID, value=id_)

    def find_elements_by_id(self, id_):
        # type: (tp.Text) -> tp.List[EyesWebElement]
        """
        Finds multiple elements by id.

        :param id_: The id of the elements to be found.
        """
        return self.find_elements(by=By.ID, value=id_)

    def find_element_by_xpath(self, xpath):
        # type: (tp.Text) -> EyesWebElement
        """
        Finds an element by xpath.

        :param xpath: The xpath locator of the element to find.
        """
        return self.find_element(by=By.XPATH, value=xpath)

    def find_elements_by_xpath(self, xpath):
        # type: (tp.Text) -> tp.List[EyesWebElement]
        """
        Finds multiple elements by xpath.

        :param xpath: The xpath locator of the elements to be found.
        """
        return self.find_elements(by=By.XPATH, value=xpath)

    def find_element_by_link_text(self, link_text):
        # type: (tp.Text) -> EyesWebElement
        """
        Finds an element by link text.

        :param link_text: The text of the element to be found.
        """
        return self.find_element(by=By.LINK_TEXT, value=link_text)

    def find_elements_by_link_text(self, text):
        # type: (tp.Text) -> tp.List[EyesWebElement]
        """
        Finds elements by link text.

        :param text: The text of the elements to be found.
        """
        return self.find_elements(by=By.LINK_TEXT, value=text)

    def find_element_by_partial_link_text(self, link_text):
        # type: (tp.Text) -> EyesWebElement
        """
        Finds an element by a partial match of its link text.

        :param link_text: The text of the element to partially match on.
        """
        return self.find_element(by=By.PARTIAL_LINK_TEXT, value=link_text)

    def find_elements_by_partial_link_text(self, link_text):
        # type: (tp.Text) -> tp.List[EyesWebElement]
        """
        Finds elements by a partial match of their link text.

        :param link_text: The text of the element to partial match on.
        """
        return self.find_elements(by=By.PARTIAL_LINK_TEXT, value=link_text)

    def find_element_by_name(self, name):
        # type: (tp.Text) -> EyesWebElement
        """
        Finds an element by name.

        :param name: The name of the element to find.
        """
        return self.find_element(by=By.NAME, value=name)

    def find_elements_by_name(self, name):
        # type: (tp.Text) -> tp.List[EyesWebElement]
        """
        Finds elements by name.

        :param name: The name of the elements to find.
        """
        return self.find_elements(by=By.NAME, value=name)

    def find_element_by_tag_name(self, name):
        # type: (tp.Text) -> EyesWebElement
        """
        Finds an element by tag name.

        :param name: The tag name of the element to find.
        """
        return self.find_element(by=By.TAG_NAME, value=name)

    def find_elements_by_tag_name(self, name):
        # type: (tp.Text) -> tp.List[EyesWebElement]
        """
        Finds elements by tag name.

        :param name: The tag name to use when finding elements.
        """
        return self.find_elements(by=By.TAG_NAME, value=name)

    def find_element_by_class_name(self, name):
        # type: (tp.Text) -> EyesWebElement
        """
        Finds an element by class name.

        :param name: The class name of the element to find.
        """
        return self.find_element(by=By.CLASS_NAME, value=name)

    def find_elements_by_class_name(self, name):
        # type: (tp.Text) -> tp.List[EyesWebElement]
        """
        Finds elements by class name.

        :param name: The class name of the elements to find.
        """
        return self.find_elements(by=By.CLASS_NAME, value=name)

    def find_element_by_css_selector(self, css_selector):
        # type: (tp.Text) -> EyesWebElement
        """
        Finds an element by css selector.

        :param css_selector: The css selector to use when finding elements.
        """
        return self.find_element(by=By.CSS_SELECTOR, value=css_selector)

    def find_elements_by_css_selector(self, css_selector):
        # type: (tp.Text) -> tp.List[EyesWebElement]
        """
        Finds elements by css selector.

        :param css_selector: The css selector to use when finding elements.
        """
        return self.find_elements(by=By.CSS_SELECTOR, value=css_selector)

    def get_screenshot_as_base64(self):
        # type: () -> tp.Text
        """
        Gets the screenshot of the current window as a base64 encoded string
           which is useful in embedded images in HTML.
        """
        screenshot64 = self.driver.get_screenshot_as_base64()
        display_rotation = self.get_display_rotation()
        if display_rotation != 0:
            logger.info('Rotation required.')
            # num_quadrants = int(-(display_rotation / 90))
            logger.debug('Done! Creating image object...')
            screenshot = _image_utils.image_from_base64(screenshot64)

            # rotating
            if display_rotation == -90:
                screenshot64 = _image_utils.get_base64(screenshot.rotate(90))
            logger.debug('Done! Rotating...')

        return screenshot64

    def get_screesnhot_as_base64_from_main_frame(self, seconds_to_wait):
        # type: (Num) -> tp.Text
        """
        Make screenshot from main frame
        """
        original_frame = self.get_frame_chain()
        self.switch_to.default_content()
        self._wait_before_screenshot(seconds_to_wait)
        screenshot64 = self.get_screenshot_as_base64()
        self.switch_to.frames(original_frame)
        return screenshot64

    def extract_full_page_width(self):
        # type: () -> int
        """
        Extracts the full page width.

        :return: The width of the full page.
        """
        # noinspection PyUnresolvedReferences
        default_scroll_width = int(round(self.driver.execute_script(
            "return document.documentElement.scrollWidth")))
        body_scroll_width = int(round(self.driver.execute_script("return document.body.scrollWidth")))
        return max(default_scroll_width, body_scroll_width)

    def extract_full_page_height(self):
        # type: () -> int
        """
        Extracts the full page height.

        :return: The height of the full page.
        IMPORTANT: Notice there's a major difference between scrollWidth and scrollHeight.
        While scrollWidth is the maximum between an element's width and its content width,
        scrollHeight might be smaller(!) than the clientHeight, which is why we take the
        maximum between them.
        """
        # noinspection PyUnresolvedReferences
        default_client_height = int(round(self.driver.execute_script(
            "return document.documentElement.clientHeight")))
        # noinspection PyUnresolvedReferences
        default_scroll_height = int(round(self.driver.execute_script(
            "return document.documentElement.scrollHeight")))
        # noinspection PyUnresolvedReferences
        body_client_height = int(round(self.driver.execute_script("return document.body.clientHeight")))
        # noinspection PyUnresolvedReferences
        body_scroll_height = int(round(self.driver.execute_script("return document.body.scrollHeight")))
        max_document_element_height = max(default_client_height, default_scroll_height)
        max_body_height = max(body_client_height, body_scroll_height)
        return max(max_document_element_height, max_body_height)

    def get_current_position(self):
        # type: () -> Point
        """
        Extracts the current scroll position from the browser.

        :return: The scroll position.
        """
        return self._origin_position_provider.get_current_position()

    def scroll_to(self, point):
        # type: (Point) -> None
        """
        Commands the browser to scroll to a given position.

        :param point: The point to scroll to.
        """
        self._origin_position_provider.set_position(point)

    def get_entire_page_size(self):
        # type: () -> tp.Dict[tp.Text, int]
        """
        Extracts the size of the current page from the browser using Javascript.

        :return: The page width and height.
        """
        return {'width': self.extract_full_page_width(),
                'height': self.extract_full_page_height()}

    def set_overflow(self, overflow, stabilization_time=None):
        # type: (tp.Text, tp.Optional[int]) -> tp.Text
        """
        Sets the overflow of the current context's document element.

        :param overflow: The overflow value to set. If the given value is None, then overflow will be set to
                         undefined.
        :param stabilization_time: The time to wait for the page to stabilize after overflow is set. If the value is
                                    None, then no waiting will take place. (Milliseconds)
        :return: The previous overflow value.
        """
        logger.debug("Setting overflow: %s" % overflow)
        if overflow is None:
            script = "var origOverflow = document.documentElement.style.overflow; " \
                     "document.documentElement.style.overflow = undefined; " \
                     "return origOverflow;"
        else:
            script = "var origOverflow = document.documentElement.style.overflow; " \
                     "document.documentElement.style.overflow = \"{0}\"; " \
                     "return origOverflow;".format(overflow)
        # noinspection PyUnresolvedReferences
        original_overflow = self.driver.execute_script(script)
        logger.debug("Original overflow: %s" % original_overflow)
        if stabilization_time is not None:
            time.sleep(stabilization_time / 1000)
        return original_overflow

    def wait_for_page_load(self, timeout=3, throw_on_timeout=False):
        # type: (int, bool) -> None
        """
        Waits for the current document to be "loaded".

        :param timeout: The maximum time to wait, in seconds.
        :param throw_on_timeout: Whether to throw an exception when timeout is reached.
        """
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, timeout) \
                .until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        except Exception:
            logger.debug('Page load timeout reached!')
            if throw_on_timeout:
                raise

    def hide_scrollbars(self):
        # type: () -> tp.Text
        """
        Hides the scrollbars of the current context's document element.

        :return: The previous value of the overflow property (could be None).
        """
        logger.debug('HideScrollbars() called. Waiting for page load...')
        self.wait_for_page_load()
        logger.debug('About to hide scrollbars')
        return self.set_overflow('hidden')

    def get_frame_chain(self):
        """
        Gets the frame chain.

        :return: A list of EyesFrame instances which represents the path to the current frame.
            This can later be used as an argument to _EyesSwitchTo.frames().
        """
        return [frame.clone() for frame in self._frames]

    def get_viewport_size(self):
        # type: () -> ViewPort
        """
        Returns:
            The viewport size of the current frame.
        """
        return _viewport_size.get_viewport_size(self)

    def get_default_content_viewport_size(self):
        # type: () -> ViewPort
        """
        Gets the viewport size.

        :return: The viewport size of the most outer frame.
        """
        current_frames = self.get_frame_chain()
        # If we're inside a frame, then we should first switch to the most outer frame.
        self.switch_to.default_content()
        viewport_size = self.get_viewport_size()
        self.switch_to.frames(current_frames)
        return viewport_size

    def reset_origin(self):
        # type: () -> None
        """
        Reset the origin position to (0, 0).

        :raise EyesError: Couldn't scroll to position (0, 0).
        """
        self._origin_position_provider.push_state()
        self._origin_position_provider.set_position(Point(0, 0))
        current_scroll_position = self._origin_position_provider.get_current_position()
        if current_scroll_position.x != 0 or current_scroll_position.y != 0:
            self._origin_position_provider.pop_state()
            raise EyesError("Couldn't scroll to the top/left part of the screen!")

    def restore_origin(self):
        # type: () -> None
        """
        Restore the origin position.
        """
        self._origin_position_provider.pop_state()

    def save_position(self):
        """
        Saves the position in the _position_provider list.
        """
        self._position_provider.push_state()

    def restore_position(self):
        """
        Restore the position.
        """
        self._position_provider.pop_state()

    @staticmethod
    def _wait_before_screenshot(seconds):
        logger.debug("Waiting {} ms before taking screenshot..".format(int(seconds * 1000)))
        time.sleep(seconds)
        logger.debug("Finished waiting!")

    def get_full_page_screenshot(self, wait_before_screenshots, scale_provider):
        # type: (Num, ScaleProvider) -> Image.Image
        """
        Gets a full page screenshot.

        :param wait_before_screenshots: Seconds to wait before taking each screenshot.
        :return: The full page screenshot.
        """
        logger.info('getting full page screenshot..')

        # Saving the current frame reference and moving to the outermost frame.
        original_frame = self.get_frame_chain()
        self.switch_to.default_content()

        self.reset_origin()

        entire_page_size = self.get_entire_page_size()

        # Starting with the screenshot at 0,0
        EyesWebDriver._wait_before_screenshot(wait_before_screenshots)
        part64 = self.get_screenshot_as_base64()
        screenshot = _image_utils.image_from_bytes(base64.b64decode(part64))

        scale_provider.update_scale_ratio(screenshot.width)
        pixel_ratio = 1.0 / scale_provider.scale_ratio
        need_to_scale = True if pixel_ratio != 1.0 else False
        if need_to_scale:
            screenshot = _image_utils.scale_image(screenshot, 1.0 / pixel_ratio)

        # IMPORTANT This is required! Since when calculating the screenshot parts for full size,
        # we use a screenshot size which is a bit smaller (see comment below).
        if (screenshot.width >= entire_page_size['width']) and \
                (screenshot.height >= entire_page_size['height']):
            self.restore_origin()
            self.switch_to.frames(original_frame)

            return screenshot

        #  We use a smaller size than the actual screenshot size in order to eliminate duplication
        #  of bottom scroll bars, as well as footer-like elements with fixed position.
        screenshot_part_size = {'width': screenshot.width,
                                'height': max(screenshot.height - self._MAX_SCROLL_BAR_SIZE,
                                              self._MIN_SCREENSHOT_PART_HEIGHT)}

        logger.debug("Total size: {0}, Screenshot part size: {1}".format(entire_page_size,
                                                                         screenshot_part_size))

        entire_page = Region(0, 0, entire_page_size['width'], entire_page_size['height'])
        screenshot_parts = entire_page.get_sub_regions(screenshot_part_size)

        # Starting with the screenshot we already captured at (0,0).
        stitched_image = Image.new('RGBA', (entire_page.width, entire_page.height))
        stitched_image.paste(screenshot, box=(0, 0))
        self.save_position()

        for part in screenshot_parts:
            # Since we already took the screenshot for 0,0
            if part.left == 0 and part.top == 0:
                logger.debug('Skipping screenshot for 0,0 (already taken)')
                continue
            logger.debug("Taking screenshot for {0}".format(part))
            # Scroll to the part's top/left and give it time to stabilize.
            self.scroll_to(Point(part.left, part.top))
            EyesWebDriver._wait_before_screenshot(wait_before_screenshots)
            # Since screen size might cause the scroll to reach only part of the way
            current_scroll_position = self.get_current_position()
            logger.debug("Scrolled To ({0},{1})".format(current_scroll_position.x,
                                                        current_scroll_position.y))
            part64 = self.get_screenshot_as_base64()
            part_image = _image_utils.image_from_bytes(base64.b64decode(part64))

            if need_to_scale:
                part_image = _image_utils.scale_image(part_image, 1.0 / pixel_ratio)

            stitched_image.paste(part_image, box=(current_scroll_position.x, current_scroll_position.y))

        self.restore_position()
        self.restore_origin()
        self.switch_to.frames(original_frame)

        return stitched_image

    def get_stitched_screenshot(self, element, wait_before_screenshots, scale_provider):
        # type: (AnyWebElement, int, ScaleProvider) -> Image.Image
        """
        Gets a stitched screenshot for specific element

        :param wait_before_screenshots: Seconds to wait before taking each screenshot.
        :return: The full page screenshot.
        """
        logger.info('getting stitched element screenshot..')

        self._position_provider = ElementPositionProvider(self.driver, element)
        entire_size = self._position_provider.get_entire_size()

        #  We use a smaller size than the actual screenshot size in order to eliminate duplication
        #  of bottom scroll bars, as well as footer-like elements with fixed position.
        pl = element.location

        # TODO: add correct values for Safari
        # in the safari browser the returned size has absolute value but not relative as
        # in other browsers

        origin_overflow = element.get_overflow()
        element.set_overflow('hidden')

        element_width = element.get_client_width()
        element_height = element.get_client_height()

        border_left_width = element.get_computed_style_int('border-left-width')
        border_top_height = element.get_computed_style_int('border-top-width')

        element_region = Region(pl['x'] + border_left_width,
                                pl['y'] + border_top_height,
                                element_width, element_height)

        # Firefox 60 and above make a screenshot of the current frame when other browsers
        # make a screenshot of the viewport. So we scroll down to frame at _will_switch_to method
        # and add a left margin here.
        # TODO: Refactor code. Use EyesScreenshot
        if self._frames:
            if ((self.browser_name == 'firefox' and self.browser_version < 60.0)
                    or self.browser_name in ('chrome', 'MicrosoftEdge', 'internet explorer', 'safari')):
                element_region.left += int(self._frames[-1].location['x'])

        screenshot_part_size = {'width': element_region.width,
                                'height': max(element_region.height - self._MAX_SCROLL_BAR_SIZE,
                                              self._MIN_SCREENSHOT_PART_HEIGHT)}
        entire_element = Region(0, 0, entire_size['width'], entire_size['height'])

        screenshot_parts = entire_element.get_sub_regions(screenshot_part_size)
        viewport = self.get_viewport_size()
        screenshot = _image_utils.image_from_bytes(base64.b64decode(self.get_screenshot_as_base64()))
        scale_provider.update_scale_ratio(screenshot.width)
        pixel_ratio = 1 / scale_provider.scale_ratio
        need_to_scale = True if pixel_ratio != 1.0 else False

        # Starting with element region size part of the screenshot. Use it as a size template.
        stitched_image = Image.new('RGBA', (entire_element.width, entire_element.height))
        for part in screenshot_parts:
            logger.debug("Taking screenshot for {0}".format(part))
            # Scroll to the part's top/left and give it time to stabilize.
            self._position_provider.set_position(Point(part.left, part.top))
            EyesWebDriver._wait_before_screenshot(wait_before_screenshots)
            # Since screen size might cause the scroll to reach only part of the way
            current_scroll_position = self._position_provider.get_current_position()
            logger.debug("Scrolled To ({0},{1})".format(current_scroll_position.x,
                                                        current_scroll_position.y))
            part64 = self.get_screenshot_as_base64()
            part_image = _image_utils.image_from_bytes(base64.b64decode(part64))
            # Cut to viewport size the full page screenshot of main frame for some browsers
            if self._frames:
                if (self.browser_name == 'firefox' and self.browser_version < 60.0
                        or self.browser_name in ('internet explorer', 'safari')):
                    # TODO: Refactor this to make main screenshot only once
                    frame_scroll_position = int(self._frames[-1].location['y'])
                    part_image = _image_utils.get_image_part(part_image, Region(top=frame_scroll_position,
                                                                                height=viewport['height'],
                                                                                width=viewport['width']))
            if need_to_scale:
                part_image = _image_utils.scale_image(part_image, 1.0 / pixel_ratio)
            part_image = _image_utils.get_image_part(part_image, element_region)

            # first iteration
            if stitched_image is None:
                stitched_image = part_image
                continue
            stitched_image.paste(part_image, box=(current_scroll_position.x, current_scroll_position.y))

        if origin_overflow:
            element.set_overflow(origin_overflow)

        return stitched_image

    def _will_switch_to(self, frame_reference, frame_element=None):
        # type: (tp.Optional[FrameReference], AnyWebElement) -> None
        """
        Updates the current webdriver that a switch was made to a frame element.

        :param frame_reference: The reference to the frame.
        :param frame_element: The frame element instance.
        """
        if frame_element is not None:
            frame_location = frame_element.location
            frame_size = frame_element.size
            frame_id = frame_element.id
            parent_scroll_position = self.get_current_position()
            # Frame border can affect location calculation for elements.
            # noinspection PyBroadException
            try:
                frame_left_border_width = int(frame_element
                                              .value_of_css_property('border-left-width')
                                              .rstrip('px'))
                frame_top_border_width = int(frame_element.value_of_css_property('border-top-width')
                                             .rstrip('px'))
            except Exception:
                frame_left_border_width = 0
                frame_top_border_width = 0
            frame_location['x'] += frame_left_border_width
            frame_location['y'] += frame_top_border_width

            # We need to scroll position to top of the frame to be able to take a correct screenshot
            # in the get_stitched_screenshot  method
            self.scroll_to(Point(frame_location['x'], frame_location['y']))

            self._frames.append(EyesFrame(frame_reference, frame_location, frame_size, frame_id,
                                          parent_scroll_position))
        elif frame_reference == _EyesSwitchTo.PARENT_FRAME:
            self._frames.pop()
        else:
            # We moved out of the frames
            self._frames = []

    @property
    def switch_to(self):
        return _EyesSwitchTo(self, self.driver.switch_to)

    @property
    def current_offset(self):
        # type: () -> Point
        """
        Return the current offset of the context we're in (e.g., due to switching into frames)
        """
        x, y = 0, 0
        for frame in self._frames:
            x += frame.location['x']
            y += frame.location['y']
        return Point(x, y)
