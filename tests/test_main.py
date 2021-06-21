import pytest

from appcontext import ImproperlyConfigured


def test_throws_when_accessing_unknown_before_configure(settings):

    with pytest.raises(ImproperlyConfigured):
        assert settings.NAME == "Jane Doe"


def test_throws_can_configure_with_custom_settings(settings):
    from tests import context as default_settings

    settings.configure(default_settings=default_settings)
    assert settings.NAME == "Jane Doe"
    assert settings.STAGE == 'prod'


def test_context_using_dev_env_variable_module(dev, settings):
    assert settings.STAGE == 'dev'

def test_context_using_prod_env_variable_module(prod, settings):
    assert settings.STAGE == 'prod'