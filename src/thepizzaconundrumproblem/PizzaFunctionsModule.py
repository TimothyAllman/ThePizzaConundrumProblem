from ploomberpipelinetemplate.PizzaDataModule import PizzaDto
from ploomberpipelinetemplate.PizzaFromRomansDataModule import PizzaFromRomansDto
from thepizzaconundrumproblem.ConstantsDataModule import _PI


def WorkOutArea(
    pizza: PizzaDto,
):
    r = pizza.DiameterInCm / 2
    pi = _PI

    area = pi * r * r

    return area
