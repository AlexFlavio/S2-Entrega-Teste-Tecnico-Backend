class ModelingTransicao:
    types_to_string = {
        "1": "Débito",
        "2": "Boleto",
        "3": "Financiamento",
        "4": "Crédito",
        "5": "Recebimento Empréstimo",
        "6": "Vendas",
        "7": "Recebimento TED",
        "8": "Recebimento DOC",
        "9": "Aluguel",
    }

    types_pos_neg = {
        "1": "pos",
        "2": "neg",
        "3": "neg",
        "4": "pos",
        "5": "pos",
        "6": "pos",
        "7": "pos",
        "8": "pos",
        "9": "neg",
    }

    def __init__(self, string_base):
        self.string_base = string_base
        self.formatar()
        ...

    def formatar(self):
        self.tipo = self.types_to_string[self.string_base[0]]
        self.data = (
            f"{self.string_base[1:5]}-{self.string_base[5:7]}-{self.string_base[7:9]}"
        )
        self.valor = (
            ((int(self.string_base[9:19])) / 100.00)
            if self.types_pos_neg[self.string_base[0]] == "pos"
            else (((int(self.string_base[9:19])) * -1) / 100.00)
        )
        self.cpf = self.string_base[19:30]
        self.cartao = self.string_base[30:42]
        self.hora = self.string_base[42:48]
        self.hora = f"{self.string_base[42:44]}:{self.string_base[44:46]}:{self.string_base[46:48]}"
        self.dono = self.string_base[48:62]
        self.loja = self.string_base[62:]
        self.formatado = {
            "tipo": self.tipo,
            "data": self.data,
            "valor": self.valor,
            "cpf": self.cpf,
            "cartao": self.cartao,
            "hora": self.hora,
            "dono": self.dono,
            "loja": self.loja,
        }

        ...

    ...
