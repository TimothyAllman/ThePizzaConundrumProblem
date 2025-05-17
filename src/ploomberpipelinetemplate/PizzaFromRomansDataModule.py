from ploomberpipelinetemplate.PizzaDataModule import PizzaDto


class PizzaFromRomansDto(PizzaDto):
    def __init__(
        self,
        diameterInCm: float,
        thicknessInCm: float,
        priceInRands: float,
        restaurantName: str = "Romans",
    ):
        self.RestaurantName = restaurantName
        self.DiameterInCm = diameterInCm
        self.ThicknessInCm = thicknessInCm
        self.PriceInRands = priceInRands


_ROMANS_THICK_BASE_PIZZA = PizzaFromRomansDto(
    diameterInCm=30,
    thicknessInCm=2,
    priceInRands=100,
)

_ROMANS_THIN_BASE_PIZZA = PizzaFromRomansDto(
    diameterInCm=30,
    thicknessInCm=1,
    priceInRands=100,
)
