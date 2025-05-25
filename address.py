
class Address:
    def __init__(self, logradouro: str, bairro: str, city: str, state: str, cep: str):
        self.logradouro = logradouro or "Não informado"
        self.bairro = bairro or "Não informado"
        self.city = city or "Não informado"
        self.state = state or "Não informado"
        self.cep = cep

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            logradouro=data.get("logradouro"),
            bairro=data.get("bairro"),
            city=data.get("localidade"),
            state=data.get("uf"),
            cep=data.get("cep")
        )

    def __str__(self):
        return (
            f"📍 {self.logradouro}\n"
            f"🏘️  {self.bairro}\n"
            f"🌆 {self.city} - {self.state}\n"
            f"📫 CEP: {self.cep}"
        )
