import allure


def pytest_configure(config):
    config.addinivalue_line("markers", "mark_epic(name): set Allure epic label")
    config.addinivalue_line("markers", "mark_feature(name): set Allure feature label")
    config.addinivalue_line("markers", "mark_story(name): set Allure story label")


def pytest_runtest_setup(item):
    for marker in item.iter_markers(name="mark_epic"):
        if marker.args:
            allure.dynamic.epic(marker.args[0])
    for marker in item.iter_markers(name="mark_feature"):
        if marker.args:
            allure.dynamic.feature(marker.args[0])
    for marker in item.iter_markers(name="mark_story"):
        if marker.args:
            allure.dynamic.story(marker.args[0])
