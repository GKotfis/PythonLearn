import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver_init(request):
    print("initiating chrome web driver")
    web_driver = webdriver.Chrome()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", web_driver)
        
    yield
    web_driver.close()
