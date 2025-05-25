from thepizzaconundrumproblem.PizzaDataModule import PizzaDto

def CreatePizzaFromNySliceRegularDto():
        return PizzaDto(
            diameterInCm=30,
            thicknessInCm=1,
            priceInRands=94,
            restaurantName="NY Slice",
        )


class PizzaFromNySliceLargeBaseDto(PizzaDto):
    def __init__(
        self,
    ):
        """
        a
        """
        return PizzaDto(
            diameterInCm=50,
            thicknessInCm=1,
            priceInRands=94,
            restaurantName="NY Slice",
        )


_NY_REGULAR_BASE_PIZZA = CreatePizzaFromNySliceRegularDto()

_NY_VERY_LARGE_BASE_PIZZA = PizzaFromNySliceLargeBaseDto()
