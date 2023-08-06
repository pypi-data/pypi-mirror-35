

import enum
import collections
from datetime import date
from dataclasses import asdict, dataclass

from .utils import make_enum_json_serializable


class SexType(enum.Enum):
    M = 'masculino'
    F = 'feminino'


class PaymentMethodType(enum.Enum):
    C = 'Cartão de crédito'
    B = 'Boleto bancário'
    CB = 'Ambas as opções'


class PersonType(enum.Enum):
    F = 'Pessoa Física'
    J = 'Pessoa Jurídica'


@dataclass
class Client:

    name: str
    cellphone: str
    email: str
    cpfCnpj: str = None
    sex: SexType = None
    dateOfBirth: date = None
    phone: str = None
    typePerson: PersonType = None
    zipCode: str = None
    address: str = None
    number: str = None
    complement: str = None
    neighborhood: str = None
    city: str = None
    uf: str = None
    note: str = None
    paymentMethod: PaymentMethodType = None

    def get(self):
        obj = asdict(self)
        return {key: value for key, value in obj.items() if value is not None}


@dataclass
class Expiration:
    month: str
    year: str


@dataclass
class CreditCard:

    numberCard: str
    name: str
    cvv: str
    publicIdClient: str
    expiration: Expiration

    def get(self):
        obj = asdict(self)
        return {key: value for key, value in obj.items() if value is not None}
