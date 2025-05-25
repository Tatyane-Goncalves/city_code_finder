class CEP:
  def __init__(self, number: str):
    self.number = self._clean(number)

  def _clean(self, value: str) -> str:
    # Remove qualquer caractere que não seja número
    return "".join(filter(str.isdigit, value))

  def __str__(self):
    return f"{self.number[:5]}-{self.number[5:]}" if len(self.number) == 8 else self.number