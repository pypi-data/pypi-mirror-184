from django.utils.translation import gettext as _
from rest_framework import serializers
from validate_docbr import CNPJ, CPF


def validate_cpf(num_cpf):
    cpf = CPF()

    if not cpf.validate(num_cpf):
        raise serializers.ValidationError(_("Invalid CPF"), "invalid_cpf")


def validate_cnpj(num_cnpj):
    cnpj = CNPJ()

    if not cnpj.validate(num_cnpj):
        raise serializers.ValidationError(_("Invalid CNPJ"), "invalid_cnpj")
