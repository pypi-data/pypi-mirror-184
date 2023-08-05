import os

import logging
from fnmatch import fnmatch

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import geckodriver_autoinstaller

__version__ = "0.0.3"

logging.basicConfig(level=logging.INFO)


class Sypter:
    """
    This is the base class for Frontend Testing Framework the Sypter

    It wraps selenium and adds testing functionalities
    """

    def __init__(self, source=None):
        """
        source could be one of three:
        - string HTML
        - url
        - local_file HTML
        """
        self._driver = None
        self.source = source
        self.source_type = None
        self._external_css = None

        self.config_driver()

        if source is not None:
            self.process_source(source)

        else:
            logging.warning("Initiated Sypter without source. Please use process_source() to process source later")

    def config_driver(self, **kwargs):
        """
        Configure driver
        """
        # Try to get Chrome driver
        try:
            from selenium.webdriver.chrome.options import Options

            chrome_options = Options()
            chrome_options.add_argument("--headless")
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(10)
        # if not installed try Firefox driver
        except Exception:
            # Check if the current version of geckodriver exists
            # and if it doesn't exist, download it automatically,
            # then add geckodriver to path
            # TODO: this should be done one time when the package is installed
            geckodriver_autoinstaller.install()

            from selenium.webdriver.firefox.options import Options

            firefox_options = Options()
            firefox_options.add_argument("--headless")
            self._driver = webdriver.Firefox(options=firefox_options)
            self._driver.implicitly_wait(10)

        for key, value in kwargs.items():
            self._driver.__setattr__(key, value)

    def process_source(self, source):
        """
        Process source and return source type
        """
        self.source = source
        self._get_source_type()

        if self.source_type == "url":
            self._driver.get(source)
        elif self.source_type == "file":
            self._driver.get(f"file://{source}")
        elif self.source_type == "html":
            self._driver.get(f"data:text/html;charset=utf-8,{source}")

    def _get_source_type(self):
        """
        Check if source is url, file or html
        """
        import re

        source = self.source.strip()
        url_regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            # domain...
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        # Check if source is url
        if re.match(url_regex, source):
            self.source_type = 'url'
        # else if source is a string containing html
        elif source.startswith('<') and source.endswith('>'):
            self.source_type = 'html'
        # else if source is a file
        elif os.path.isfile(source):
            # check if file exists
            if not os.path.exists(source):
                raise ValueError("File does not exist")
            elif os.path.isfile(source):
                self.source_type = "file"
            else:
                raise ValueError("Invalid source")

    @staticmethod
    def check_elements_quantity(elements, comparison_operator: str, numeric_value: int, verbose: bool = False) -> bool:
        """
        Check if elements quantity is valid
        :param elements: elements to check
        :param comparison_operator: comparison operator "<", ">", "<=", ">=", "==", "!="
        :param numeric_value: numeric value to compare with (second operand)
        :param verbose: if True, logging.debug the result
        :return:
        """
        number_of_elements = len(elements)  # first operand
        if verbose:
            logging.debug(f"comparing {number_of_elements} {comparison_operator} {numeric_value}")
        # write switch cases
        match comparison_operator:
            case "<":
                return number_of_elements < numeric_value
            case ">":
                return number_of_elements > numeric_value
            case "<=":
                return number_of_elements <= numeric_value
            case ">=":
                return number_of_elements >= numeric_value
            case "==":
                return number_of_elements == numeric_value
            case "!=":
                return number_of_elements != numeric_value
            case _:
                raise ValueError("Invalid comparison operator")

    @staticmethod
    def get_selector(selector_type: str, selector_value: str, verbose: bool = False) -> tuple:
        """
        Get selector type and selector value
        """
        selector_type = selector_type.lower()
        if verbose:
            logging.debug(f"selector_type: {selector_type} selector_value: {selector_value}")
        if selector_type == "id":
            return By.ID, selector_value
        elif selector_type == "class":
            return By.CLASS_NAME, selector_value
        elif selector_type == "tag":
            return By.TAG_NAME, selector_value
        elif selector_type == "css":
            return By.CSS_SELECTOR, selector_value
        elif selector_type == "xpath":
            return By.XPATH, selector_value
        else:
            raise ValueError("Invalid selector type")

    def test(self, selector_value: str, selector_type: str = "tag",
             comparison_operator: str = "==", numeric_value: int = 1,
             style_tests: list = None, attribute_tests: list = None,
             verbose=False) -> list:
        """
        Test HTML element
        """

        # get selector
        selector = self.get_selector(selector_type, selector_value, verbose)

        if verbose:
            logging.debug(f"selector: {selector}")

        # get elements
        try:
            elements = self._driver.find_elements(*selector)
        except NoSuchElementException:
            raise False

        if verbose:
            logging.debug(f"Found {len(elements)} elements: {elements}")

        # check if attributes need to be filtered
        if attribute_tests is not None:
            if isinstance(attribute_tests, list) and attribute_tests[0].get("attribute_name"):
                new_test = {}
                for attribute_test in attribute_tests:
                    value = attribute_test.get("attribute_value", None)
                    if value == '':
                        value = "*"  # if value is empty, use wildcard
                    key = attribute_test.get("attribute_name")
                    new_test[key] = value

                attribute_tests = new_test

            elements = self.filter_elements_by_attributes(elements, attribute_tests, verbose)

        # check if styles need to be filtered
        if style_tests is not None:
            logging.debug(style_tests, isinstance(style_tests, list), style_tests[0].get("attribute_name"))
            if isinstance(style_tests, list) and style_tests[0].get("attribute_name"):
                style_tests = {style_test["attribute_name"]: style_test["attribute_value"] for style_test in
                               style_tests}
            elements = self.filter_elements_by_style(elements, style_tests, verbose)

        return self.check_elements_quantity(elements, comparison_operator, numeric_value, verbose)

    @staticmethod
    def filter_elements_by_attributes(elements, attributes: dict, verbose) -> list:
        """
        Check if there are elements with given css selector and attributes
        """
        # filter list of elements to get only elements with given attributes
        result = []
        for attribute, value in attributes.items():
            for element in elements:
                # For whatever reason get_attribute returns None for some elements (e.g. <a> elements)
                if attribute == "href":
                    attribute_value = [attribute['value'] for attribute in element.get_property("attributes") if
                                       attribute['name'] == "href"][0]
                else:
                    attribute_value = element.get_attribute(attribute)

                match = fnmatch(element.get_attribute(attribute), value)

                if verbose:
                    logging.debug(f"element: {element}")
                    logging.debug(f"element.get_attribute({attribute}) = {attribute_value}")
                    logging.debug(f"nmatch({attribute_value}, {value}): {match}")

                if attribute_value and match:
                    result.append(element)
                    if verbose:
                        logging.debug("match")
                else:
                    if verbose:
                        logging.debug("no match")
        return result

    @staticmethod
    def filter_elements_by_style(elements, styles: dict, verbose=True) -> list:
        """
        Filter elements by css style attribute

        :param styles: dictionary of styles to filter by
        :param elements: list of elements to filter
        :return: list of elements
        """
        # filter list of elements to get only elements with given styles
        result = []
        for style, value in styles.items():
            for element in elements:

                css_value = element.value_of_css_property(style)
                if "rgba" in css_value:
                    # convert rgba to hex
                    css_value = css_value.replace("rgba(", "").replace(")", "")
                    css_value = "#" + "".join([hex(int(x))[2:].zfill(2) for x in css_value.split(",")[:-1]])
                elif "rgb" in css_value:
                    # convert rgb to hex
                    css_value = css_value.replace("rgb(", "").replace(")", "")
                    css_value = "#" + "".join([hex(int(x))[2:].zfill(2) for x in css_value.split(",")])

                match = fnmatch(css_value, value)

                if verbose:
                    logging.debug(f"element: {element.get_property('style')}")
                    logging.debug(f"element style ({style}): {element.value_of_css_property(style)}")
                    logging.debug(f"fnmatch({css_value}, {value}): {match}")

                if css_value and match:
                    if verbose:
                        logging.debug("match")
                    result.append(element)
                else:
                    if verbose:
                        logging.debug("no match")

        return result
