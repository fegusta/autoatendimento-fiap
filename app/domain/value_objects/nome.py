class Nome:
    def __init__(self, valor: str):
        valor = valor.strip()
        if not valor:
            raise ValueError("Nome não pode ser vazio.")
        if len(valor) < 2:
            raise ValueError("Nome deve conter ao menos 2 caracteres.")
        self.valor = valor

    def __str__(self) -> str:
        return self.valor

    def __eq__(self, other) -> bool:
        return str(self) == str(other)

    def __repr__(self) -> str:
        return f"Nome('{self.valor}')"
