import unittest, json
import azure.functions as func
from unittest.mock import MagicMock

from function_app import all_books, getbooksbyyear

class TestFunction(unittest.TestCase):
    def test_all_books(self):

        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/all_books',
            params={}
        )
            # Call the function.
        func_call = all_books.build().get_user_function()
        response = func_call(req)

        assert response.status_code == 200
        assert response.mimetype == "application/json"


    def test_getbooksbyyear(self):

        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/getbooksbyyear/{year}',
            route_params={'year':'2018'},
        )

        func_call = getbooksbyyear.build().get_user_function()
        response = func_call(req)

        assert response.status_code == 200
        assert response.mimetype == "application/json"

        expected_data = [
        {
            "title": "12 Rules of Life",
            "Author": "Jordan Peterson",
            "year": 2018,
            "category": "Self-help",
            "bookcoverUrl": "https://myblob.com/12rulesoflife.jpg"
        },
        {
            "title": "We who Wrestle with god",
            "Author": "Jordan Peterson",
            "year": 2018,
            "category": "Self-help",
            "bookcoverUrl": "https://myblob.com/12rulesoflife.jpg"
        }
        ]
        
        self.assertEqual(
            response.get_body().decode('utf-8'),
            json.dumps(expected_data, indent=True)

        )
