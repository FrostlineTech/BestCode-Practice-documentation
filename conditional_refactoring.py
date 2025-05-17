"""
Conditional Logic Refactoring Example

Demonstrates:
1. Dictionary-based dispatch pattern
2. Polymorphic approach
3. Guard clause validation
"""
from typing import Callable

# Anti-pattern example
class BadPriceCalculator:
    def get_discount(self, customer_type: str) -> float:
        if customer_type == "VIP":
            return 0.30
        elif customer_type == "LOYALTY":
            return 0.25
        elif customer_type == "FIRST_TIME":
            return 0.15
        elif customer_type == "BULK":
            return 0.40
        elif customer_type == "STAFF":
            return 0.50
        else:
            return 0.10

# Preferred approach 1: Dictionary dispatch
class GoodPriceCalculator:
    DISCOUNT_MAP = {
        "VIP": 0.30,
        "LOYALTY": 0.25,
        "FIRST_TIME": 0.15,
        "BULK": 0.40,
        "STAFF": 0.50
    }

    def get_discount(self, customer_type: str) -> float:
        return self.DISCOUNT_MAP.get(customer_type, 0.10)

# Preferred approach 2: Polymorphic handlers
class DiscountStrategy:
    def calculate(self) -> float:
        raise NotImplementedError

class VIPDiscount(DiscountStrategy):
    def calculate(self) -> float:
        return 0.30

class DiscountFactory:
    STRATEGIES = {
        "VIP": VIPDiscount(),
        # Other strategies...
    }

    def get_strategy(self, customer_type: str) -> DiscountStrategy:
        return self.STRATEGIES.get(customer_type, DefaultDiscount())

"""
Key Benefits Shown:
- Eliminates elif chains
- Centralized decision logic
- Easier maintenance
- Better testability
"""
