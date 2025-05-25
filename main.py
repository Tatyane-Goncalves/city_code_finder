from cep import CEP
from validator import ValidatorCEP
from api_client import APIClient
from address import Address

def main():
  raw_cep = input("Digite o CEP: ")
  cep_obj = CEP(raw_cep)

  if not ValidatorCEP.is_valid(cep_obj.number):
    print("❌ CEP inválido. Deve conter 8 dígitos numéricos.")
    return
  
  print(f"✅ CEP válido: {cep_obj}")
  print("🔍 Buscando dados...")

  dados = APIClient.find_address(cep_obj.number)

  if dados:
    show_address = Address.from_dict(dados)
    print("📦 Endereço encontrado:")
    print(show_address)
  else:
    print("❌ Não foi possível obter o endereço.")

if __name__ == "__main__":
  main()