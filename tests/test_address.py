import unittest
from address import Address

class TestAddress(unittest.TestCase):
  def test_from_dict_completed(self):
    data = {
      "logradouro": "Rua Teste",
      "bairro": "Bairro xxx",
      "localidade": "localidade xxx",
      "uf": "MG",
      "cep": "30140071"
    }

    address = Address.from_dict(data)
    self.assertEqual(address.logradouro, "Rua Teste")
    self.assertEqual(address.bairro, "Bairro xxx")
    self.assertEqual(address.city, "localidade xxx")
    self.assertEqual(address.state, "MG")
    self.assertEqual(address.cep, "30140071")

  def test_from_dict_incompleted(self):
    data = {
      "logradouro": None,
      "bairro": "",
      "localidade": None,
      "state": "",
      "cep": "000000000"
    }

    address = Address.from_dict(data)
    self.assertEqual(address.logradouro, "Não informado")
    self.assertEqual(address.bairro, "Não informado")
    self.assertEqual(address.city, "Não informado")
    self.assertEqual(address.state, "Não informado")


if __name__ == "__main__":
  unittest.main()