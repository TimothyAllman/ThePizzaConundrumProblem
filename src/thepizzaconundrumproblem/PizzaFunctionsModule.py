from multimethod import multimethod

from ploomberpipelinetemplate.PizzaDataModule import PizzaDto
from ploomberpipelinetemplate.PizzaFromRomansDataModule import PizzaFromRomansDto
from thepizzaconundrumproblem.ConstantsDataModule import _PI


@multimethod
def WorkOutArea(
    pizza: PizzaDto,
):
    r = pizza.DiameterInCm / 2
    pi = _PI

    area = pi * r * r

    return area
