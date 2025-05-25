import requests
import unittest
from unittest.mock import patch
from api_client import APIClient

class TestAPIClient(unittest.TestCase):
  @patch("api_client.requests.get")
  def test_finder_address_with_sucess(self, mock_get):
    mock_response = {
      "cep": "30140071",
      "logradouro": "Avenida Afonso Pena",
      "bairro": "Centro",
      "localidade": "Belo Horizonte",
      "uf": "MG"
    }

    # Config the mock
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    # Run the method
    address = APIClient.find_address("30140071")

    # Check the data
    self.assertEqual(address["logradouro"], "Avenida Afonso Pena")
    self.assertEqual(address["bairro"], "Centro")
    self.assertEqual(address["localidade"], "Belo Horizonte")
    self.assertEqual(address["uf"], "MG")
    self.assertEqual(address["cep"], "30140071")
  
  @patch("api_client.requests.get")
  def test_finder_address_erro_404(self, mock_get):
    mock_get.return_value.status_code = 404
    mock_get.return_value.raise_for_status.side_effect = requests.HTTPError("404 Client Error")

    result = APIClient.find_address("00000000")
    self.assertIsNone(result)


if __name__ == "__main__":
   unittest.main()