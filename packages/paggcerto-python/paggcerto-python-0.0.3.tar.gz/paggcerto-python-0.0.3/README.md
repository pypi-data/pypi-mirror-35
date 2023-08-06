# Paggcerto Python API
The Paggcerto Python API provides convenient access to the Paggcerto API from applications written in the Python language. 

## Quick Install
This lib can be found on pip. To install it, use:


```
$ pip install paggcerto-python
```

## Usage

### Export environment variables

```
export PAGGCERTO_API_USER=...
export PAGGCERTO_API_PASSWORD=...
export PAGGCERTO_API_USE_SANDBOX=True
```

### Creating a Client

```
import python_http_client
from paggcerto import PaggcertoAPIClient, Client, PersonType, SexType, PaymentMethodType

api = PaggcertoAPIClient()

client = Client(
    cpfCnpj="31618850075",
    name="Maria Joao dos Santos",
    sex=SexType.F,
    dateOfBirth="01/25/1978",
    phone="7927667035",
    cellphone="79993764596",
    email="saragabriellyribeiro_@zf.com",
    typePerson=PersonType.F,
    zipCode="49030-720",
    address="Avenida Tancredo Neves",
    number="10",
    complement="Próximo ao conjunto inácio barbosa",
    neighborhood="Inacio Barbosa",
    city="Aracaju",
    uf="SE",
    note="O cliente possui apenas um dependente.",
    paymentMethod=PaymentMethodType.C
)
try:
    response = api.client.core.client.register.post(request_body=client.get())
    print(response.to_dict['client']['publicId'])
except python_http_client.HTTPError as e:
    print(e.to_dict)
```

### Adding a credit card

```
import python_http_client
from paggcerto import PaggcertoAPIClient, CreditCard, Expiration

api = PaggcertoAPIClient()

credit_card = CreditCard(
    numberCard="4329626344167265",
    name="Maria Joao dos Santos",
    cvv="345",
    publicIdClient="MAY0uoO7mTpO4tBnY"
    expiration=Expiration(month="11", year="21")
)
try:
    response = api.client.core.card.register.post(request_body=credit_card.get())
    print(response.to_dict['card']['publicId'])
except python_http_client.HTTPError as e:
    print(e.to_dict)
```


## Documentation
- <a href="https://desenvolvedor.paggcerto.com.br/v1">Paggcerto API Docs</a>

