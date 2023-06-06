import pytest
import pint

unit_registry = pint.get_application_registry()


@pytest.mark.parametrize(
    "input_string",
    [
        "42.123 m",
        "42.123 m^2",
        "42.123 m/s^2",
    ],
)
def test_quantity_create_single_input(func_registry, benchmark, input_string):
    """
    Benchmark how long quantity creation takes with a range of Quantity unit strings
    """
    benchmark(func_registry.Quantity, input_string)


@pytest.mark.parametrize(
    "value, unit_string",
    [
        [42.123, "m"],
        [42.123, "m^2"],
        [42.123, "m/s^2"],
    ],
)
def test_quantity_create_split_input(func_registry, benchmark, value, unit_string):
    """
    Benchmark how long quantity creation takes with a range of Quantity unit strings
    """
    benchmark(func_registry.Quantity, value, unit_string)
