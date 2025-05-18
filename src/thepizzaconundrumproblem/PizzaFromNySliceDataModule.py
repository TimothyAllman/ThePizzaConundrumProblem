from thepizzaconundrumproblem.PizzaDataModule import PizzaDto


class PizzaFromNySliceDto(PizzaDto):
    def __init__(
        self,
        diameterInCm: float,
        thicknessInCm: float,
        priceInRands: float,
        restaurantName: str = "NY Slice",
    ):
        self.RestaurantName = restaurantName
        self.DiameterInCm = diameterInCm
        self.ThicknessInCm = thicknessInCm
        self.PriceInRands = priceInRands


_NY_REGULAR_BASE_PIZZA = PizzaFromNySliceDto(
    diameterInCm=30,
    thicknessInCm=1,
    priceInRands=94,
)

_NY_VERY_LARGE_BASE_PIZZA = PizzaFromNySliceDto(
    diameterInCm=50,
    thicknessInCm=1,
    priceInRands=255,
)

_NY_ONE_SLICE_BASE_PIZZA = PizzaFromNySliceDto(
    diameterInCm=50,
    thicknessInCm=1,
    priceInRands=34,
)
