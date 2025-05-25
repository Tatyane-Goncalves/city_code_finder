from cep import CEP
from validator import ValidatorCEP

def main():
  raw_cep = input("Digite o CEP: ")
  cep_obj = CEP(raw_cep)

  if not ValidatorCEP.is_valid(cep_obj.number):
    print("❌ CEP inválido. Deve conter 8 dígitos numéricos.")
    return
  
  print(f"✅ CEP válido: {cep_obj}")

if __name__ == "__main__":
  main()