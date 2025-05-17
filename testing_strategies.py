"""
Testing Best Practices

Demonstrates:
1. Unit test structure
2. Mocking external services
3. Parametrized tests
4. Fixture usage
5. Coverage analysis
"""
import pytest
from unittest.mock import Mock
from conditional_refactoring import GoodPriceCalculator

# Test fixture
@pytest.fixture
def price_calc():
    return GoodPriceCalculator()

# Parametrized test cases
test_data = [
    ("VIP", 0.3),
    ("NEW_USER", 0.1),
    ("STAFF", 0.5)
]

@pytest.mark.parametrize("customer_type,expected", test_data)
def test_discount_calculation(price_calc, customer_type, expected):
    assert price_calc.get_discount(customer_type) == expected

# Mocking example
def test_external_service():
    mock_service = Mock()
    mock_service.get_data.return_value = {"status": "ok"}
    
    result = mock_service.get_data()
    mock_service.get_data.assert_called_once()
    assert result["status"] == "ok"

"""
Testing Features Shown:
- Fixture dependency management
- Data-driven testing
- Mock object verification
- Clear test isolation
- Meaningful assertions
"""
