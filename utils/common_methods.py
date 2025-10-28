import inspect
import os

from playwright.sync_api import Page, expect


def get_text_of_element(element):
    return element.inner_text()

def get_value_of_element(element):
    return element.input_value()

def element_loaded(element) -> bool:
    # Wait until breadcrumb is visible and return True if it appears
    expect(element.first).to_be_visible(timeout=5000)
    return True

def assert_is_true(actual_value, expected_value):
    if actual_value == expected_value:
        print(f"✅ Actual value: {actual_value}  -> EXP: {expected_value}")
        return True
    else:
        print(f"❌ Actual value: {actual_value}  <- EXP: {expected_value}")
        return False

def log_location():
    frame = inspect.currentframe().f_back
    file = os.path.basename(frame.f_code.co_filename)
    method = frame.f_code.co_name
    return f"📄 File: {file} | 🔧 Method: {method}"

def select_dropdown_option(element, option: str, by: str = "text") -> None:

    if by == "text":
        element.select_option(label=option)
    elif by == "value":
        element.select_option(value=option)
    elif by == "index":
        element.select_option(index=int(option))
    else:
        raise ValueError(f"Unsupported selection method: {by}")

