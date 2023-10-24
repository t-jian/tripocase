from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from selenium.common.exceptions import TimeoutException
import elementdavid

POLL_FREQUENCY = 0.5  # How long to sleep in between calls to the method
IGNORED_EXCEPTIONS = (NoSuchElementException,)  # exceptions ignored during calls to the method




class WebDriverWaitDavid(WebDriverWait):
    def untilmyself(self, method, message=''):
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.

        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None

        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    # print("通过了")
                    return value
            # except InvalidSelectorException as e:
            #    raise e
            except:
                # print("超时")
                exc = self._ignored_exceptions
                screen = getattr(exc, 'screen', None)
                stacktrace = getattr(exc, 'stacktrace', None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
        raise TimeoutException(message, screen, stacktrace)

    def untilmyself1(self, method):
        while True:
            try:
                method
                break
            except:
                time.sleep(0.5)
                continue
                # print("超时")
