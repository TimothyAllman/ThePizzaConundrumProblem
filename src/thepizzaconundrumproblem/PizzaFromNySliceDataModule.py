from thepizzaconundrumproblem.PizzaDataModule import PizzaDto


class PizzaFromNySliceRegularDto(PizzaDto):
    def __init__(
        self,
    ):
        self.DiameterInCm = 30
        self.ThicknessInCm = 1
        self.PriceInRands = 94
        self.RestaurantName = "NY Slice"


class PizzaFromNySliceLargeBaseDto(PizzaDto):
    def __init__(
        self,
    ):
        self.DiameterInCm = 50
        self.ThicknessInCm = 1
        self.PriceInRands = 94
        self.RestaurantName = "NY Slice"
