class ValidatorCEP:
  @staticmethod
  def is_valid(cep: str) -> bool:
    return cep.isdigit() and len(cep) == 8
  