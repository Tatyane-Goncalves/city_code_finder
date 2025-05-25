from cep import CEP
from validator import ValidatorCEP
from api_client import APIClient

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
    print("📍 Endereço encontrado:")
    print(f"Logradouro: {dados.get('logradouro', 'Não informado')}")
    print(f"Bairro: {dados.get('bairro', 'Não informado')}")
    print(f"Cidade: {dados.get('localidade', 'Não informado')}")
    print(f"Estado: {dados.get('uf', 'Não informado')}")
  else:
    print("❌ Não foi possível obter o endereço.")

if __name__ == "__main__":
  main()