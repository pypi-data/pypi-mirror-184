from model_bakery import baker
from validate_docbr import CNPJ, CPF

from b2_utils.models import Address, City, Phone

__all__ = [
    "sample_city",
    "sample_address",
    "sample_phone",
    "sample_cpf",
    "sample_cnpj",
]


def sample_city(**kwargs):
    return baker.make(City, **kwargs)


def sample_address(**kwargs):
    kwargs["city"] = kwargs.get("city", sample_city)
    return baker.make(Address, **kwargs)


def sample_phone(**kwargs):
    return baker.make(Phone, **kwargs)


def sample_cpf():
    return CPF().generate()


def sample_cnpj():
    return CNPJ().generate()
