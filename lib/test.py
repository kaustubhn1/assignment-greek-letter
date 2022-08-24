import pytest


class ViewTestMixin(object):
    """
    Automatically load in a  client, this is common for a lot of
    tests that work with views.
    """

    @pytest.fixture(autouse=True)
    def set_common_fixtures(self, client):
        self.client = client
