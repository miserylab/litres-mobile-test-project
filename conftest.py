import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import litres_mobile_tests.utils.selene.patch_selector_strategy  # noqa
    import litres_mobile_tests.utils.selene.patch_element_mobile_commands  # noqa
