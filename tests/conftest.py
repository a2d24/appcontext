import os
import pytest



@pytest.fixture(scope="function")
def dev():
    TEMP_ENV_VARS = {
        'APPCONTEXT_MODULE': 'dev_context'
    }
    ENV_VARS_TO_SUSPEND = []

    # Will be executed before the first test
    old_environ = dict(os.environ)
    os.environ.update(TEMP_ENV_VARS)
    for env_var in ENV_VARS_TO_SUSPEND:
        os.environ.pop(env_var, default=None)

    yield

    os.environ.clear()
    os.environ.update(old_environ)

@pytest.fixture(scope="function")
def prod():
    TEMP_ENV_VARS = {
        'APPCONTEXT_MODULE': 'context'
    }
    ENV_VARS_TO_SUSPEND = []

    # Will be executed before the first test
    old_environ = dict(os.environ)
    os.environ.update(TEMP_ENV_VARS)
    for env_var in ENV_VARS_TO_SUSPEND:
        os.environ.pop(env_var, default=None)

    yield

    os.environ.clear()
    os.environ.update(old_environ)


@pytest.fixture(scope="function")
def settings():
    from appcontext import LazySettings
    settings = LazySettings()

    return settings