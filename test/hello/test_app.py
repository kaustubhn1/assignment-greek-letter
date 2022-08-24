from lib.test import ViewTestMixin
from flask import url_for


class TestGreek(ViewTestMixin):
    def test_home_page(self):
        """letter Endpoint should respond with a success sent letter"""
        response = self.client.get(url_for("api.letter", letter="test"))
        assert response.status_code == 200
        assert response.json == {"choosen-letter": "test"}
