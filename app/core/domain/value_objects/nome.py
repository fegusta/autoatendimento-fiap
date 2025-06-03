class Nome:
    def __init__(self, valor: str):
        if not valor or not valor.strip():
            raise ValueError("Nome não pode ser vazio.")
        self.valor = valor.strip()

    def __str__(self):
        return self.valor