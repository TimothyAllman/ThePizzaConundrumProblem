from multimethod import multimethod


from thepizzaconundrumproblem.ConstantsDataModule import _PI
from thepizzaconundrumproblem.PizzaDataModule import PizzaDto


@multimethod
def WorkOutArea(
    pizza: PizzaDto,
):
    r = pizza.DiameterInCm / 2
    pi = _PI

    area = pi * r * r

    return area
