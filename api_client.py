import requests

class APIClient:
  BASE_URL = "https://viacep.com.br/ws"

  @staticmethod
  def find_address(cep: str) -> dict:
    url = f"{APIClient.BASE_URL}/{cep}/json/"

    try:
      response = requests.get(url, timeout=5)
      response.raise_for_status() # dispara erro se a resposta for 4xx ou 5xx

      data = response.json()

      if "erro" in data:
        print("⚠️ CEP não encontrado na base do ViaCEP.")
        return None
      
      return data
    
    except requests.RequestException as e:
      print(f"❌ Erro ao conectar com o ViaCEP: {e}")
      return None