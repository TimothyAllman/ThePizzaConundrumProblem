from abc import ABC, abstractmethod


class PizzaDto(ABC):
    def __init__(
        self,
        diameterInCm: float,
        thicknessInCm: float,
        priceInRands: float,
        restaurantName: str,
    ):
        self.RestaurantName = restaurantName
        self.DiameterInCm = diameterInCm
        self.ThicknessInCm = thicknessInCm
        self.PriceInRands = priceInRands
