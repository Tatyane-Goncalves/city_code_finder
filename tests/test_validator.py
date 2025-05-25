import unittest
from validator import ValidatorCEP


class TestValidadorCEP(unittest.TestCase):

    def test_cep_valido(self):
        self.assertTrue(ValidatorCEP.is_valid("30140071"))

    def test_cep_com_letras(self):
        self.assertFalse(ValidatorCEP.is_valid("30A4007B"))

    def test_cep_curto(self):
        self.assertFalse(ValidatorCEP.is_valid("1234567"))

    def test_cep_longo(self):
        self.assertFalse(ValidatorCEP.is_valid("123456789"))


if __name__ == '__main__':
    unittest.main()
