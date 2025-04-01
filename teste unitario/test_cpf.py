import unittest
from app.validacao import validar

class TestValidarCPF(unittest.TestCase):
    def test_cpf_valido(self):
        self.assertTrue(validar("52998224725"))
        self.assertTrue(validar("12345678909"))
    
    def test_cpf_invalido(self):
        self.assertFalse(validar("11111111111"))
        self.assertFalse(validar("52998224724"))
        self.assertFalse(validar("123456"))
        self.assertFalse(validar("abcd.efg.hij-kl"))
    
    def test_cpf_vazio(self):
        self.assertFalse(validar(""))
    
if __name__ == "__main__":
    unittest.main()