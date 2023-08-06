

class Client:

    keys = [
        "cpfCnpj",
        "name",
        "sex",
        "dateOfBirth",
        "phone",
        "cellphone",
        "email",
        "typePerson",
        "zipCode",
        "address",
        "number",
        "complement",
        "neighborhood",
        "city",
        "uf",
        "note",
        "paymentMethod"

    ]

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in self.keys:
                raise Exception(f"{key} not found on Client")

        self.data = kwargs

    def get(self):
        return self.data
