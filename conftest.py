import pytest

from api.api import BuilderGet, BuilderPost


@pytest.fixture(scope="session")
def builder_get():
    builder_get = BuilderGet()
    return builder_get


@pytest.fixture(scope="session")
def builder_post():
    builder_post = BuilderPost()
    return builder_post

