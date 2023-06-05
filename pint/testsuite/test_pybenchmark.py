import pytest
import pint

unit_registry = pint.get_application_registry()


@pytest.mark.parametrize(
    "input",
    [
        "42.123 m",
        "42.123 m^2",
        "42.123 m/s^2",
        [42.123, "m"],
        [42.123, "m^2"],
        [42.123, "m/s^2"],
    ],
)
def test_quantity_create(benchmark, input):
    """
    Benchmark how long quantity creation takes with a range of Quantity unit strings
    """
    benchmark(unit_registry.Quantity, input)
