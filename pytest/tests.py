import pytest, requests, json

class TestRequests:

    @pytest.fixture(scope="function")
    def by_imo(self):
        pass

    def test_connection(self):
        response = requests.get("http://localhost:8000/")
        assert response.status_code == 200

    def test_ships(self):
        response = requests.get("http://localhost:8000/api/ships/")
        assert response.status_code == 200

    def test_ships_json_format(self):
        response = requests.get("http://localhost:8000/api/ships.json")
        get_json = json.loads(response.text)
        assert get_json['count'] > 1

    def test_positions(self):
        response = requests.get("http://localhost:8000/api/positions/")
        assert response.status_code == 200

    def test_positions_json_format(self):
        response = requests.get("http://127.0.0.1:8000/api/positions"
                                "/")
        get_json = json.loads(response.text)
        assert get_json['count'] > 1

    @pytest.mark.parametrize('imo', [])
    def test_positions_by_imo_json_format(self, by_imo, imo):
        response = requests.get("http://127.0.0.1:8000/api/positions.json?imo=" + imo)
        get_json = json.loads(response.text)
        assert get_json['count'] > 1

    @pytest.mark.parametrize('imo', [])
    def test_pagination(self, by_imo, imo):
        response = requests.get('http://127.0.0.1:8000/api/positions.json?imo='+imo+'&page=2')
        assert json.loads(response.text)['count'] > 1