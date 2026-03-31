import logging

import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup browser instance")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup browser instance")
    yield
    print("I teardown browser instance")

def test_initialCheck(preWork, secondWork):
    print("This is the first test")
    assert preWork == "pass"

@pytest.mark.smoke
def test_secondCheck(preSetupWork, secondWork):
    print("This is the Second test")