import unittest
from cep import CEP

class TestCEP(unittest.TestCase):
  def test_clean_format(self):
    cep = CEP("30.140-071")
    self.assertEqual(cep.number, "30140071")

  def test_str_format(self):
    cep = CEP("30140071")
    self.assertEqual(str(cep), "30140-071")
  
  def test_str_not_formated(self):
    cep = CEP("123")
    self.assertEqual(str(cep), "123")


if __name__ == "__main__":
  unittest.main()