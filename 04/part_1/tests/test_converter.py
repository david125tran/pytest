import pytest

from uc.converter import ConversionGraph, Quantity

@pytest.fixture(
        scope="session",
        params=["bfs", "dfs"],

        )
def unit_registry(request):
    unit_registry = ConversionGraph(search_algo=request.param)
    unit_registry.add_unit("m", "length")
    unit_registry.add_unit("cm", "length")
    unit_registry.add_unit("mm", "length")
    unit_registry.add_unit("mi", "length")
    unit_registry.add_unit("km", "length")
    unit_registry.add_linear("m", "cm", scale=100.0)
    unit_registry.add_linear("cm", "mm", scale=10.0)
    unit_registry.add_linear("mi", "km", scale=1.60934)

    return unit_registry

def test_example1(unit_registry):
    from_unit = "m"
    from_value = 1
    to_unit = "mm"
    expected_value = 1000

    from_quantity = Quantity(value=from_value, unit=from_unit)

    to_quantity = unit_registry.convert(from_quantity, to_unit)

    assert to_quantity.value == pytest.approx(expected_value)

def test_example2(unit_registry):
    from_unit = "m"
    from_value = 0.5
    to_unit = "mm"
    expected_value = 500

    from_quantity = Quantity(value=from_value, unit=from_unit)

    to_quantity = unit_registry.convert(from_quantity, to_unit)

    assert to_quantity.value == pytest.approx(expected_value)


# ------------------------------ Manual Parameterization w/For Loop ------------------------------
def test_conversions_calculation_combined(unit_registry):
    for from_unit, from_value, to_unit, expected_value in [
        ("m", 1, "mm", 1000),
        ("m", 0.5, "mm", 500),
    ]:
        from_quantity = Quantity(value=from_value, unit=from_unit)
        to_quantity = unit_registry.convert(from_quantity, to_unit)

        assert to_quantity.value == pytest.approx(expected_value)


# ------------------------------ Pytest Parameterization (@pytest.mark.parametrize) ------------------------------
@pytest.mark.parametrize(
    "from_unit, from_value, to_unit, expected_value",
    [
        ("m", 1, "mm", 1000),
        ("m", 0.5, "mm", 500),
        ("m", 5000, "mm", 5000000),
    ]
)
def test_conversions_calculation_combined(unit_registry, from_unit, from_value, to_unit, expected_value):
    from_quantity = Quantity(value=from_value, unit=from_unit)
    to_quantity = unit_registry.convert(from_quantity, to_unit)

    assert to_quantity.value == pytest.approx(expected_value)


# ------------------------------ Fixture Parameterization (params=) ------------------------------
@pytest.fixture(
    params = [
        ("m", 1, "mm", 1000),
        ("m", 0.5, "mm", 500),
        ("m", 5000, "mm", 5000000),
    ],
    ids=lambda p: f"{p[0]}_{p[1]}_{p[2]}_{p[3]}"
)

def convertion_case(request):
    return request.param

def test_conversions_calculation_combined(unit_registry, convertion_case):
    from_unit, from_value, to_unit, expected_value = convertion_case
    from_quantity = Quantity(value=from_value, unit=from_unit)
    to_quantity = unit_registry.convert(from_quantity, to_unit)

    assert to_quantity.value == pytest.approx(expected_value)


# ------------------------------ Dynamic Test Generation (pytest_generate_tests) ------------------------------

def pytest_generate_tests(metafunc):
    # if "test_conversions_calculation" == metafunc.function.__name__:
    expected_fixtures = [
        "from_unit",
        "from_value",
        "to_unit",
        "expected_value",
    ]

    is_relevant_test = all(fixture in metafunc.fixturenames for fixture in expected_fixtures)
    if is_relevant_test: 
        metafunc.parametrize(
            "from_unit, from_value, to_unit, expected_value",
            [
                ("m", 1, "mm", 1000),
                ("m", 0.5, "mm", 500),
                ("m", 5000, "mm", 5000000),
            ]
        )

def test_conversions_calculation(unit_registry, from_unit, from_value, to_unit, expected_value):
    from_quantity = Quantity(value=from_value, unit=from_unit)
    to_quantity = unit_registry.convert(from_quantity, to_unit)

    assert to_quantity.value == pytest.approx(expected_value)


# ------------------------------ Factory Fixture ------------------------------
# def test_conversion_unknown_units_fails(unit_registry):
#     from_value = 1
#     from_unit = "unknown_unit"
#     to_unit = "mm"
    
#     with pytest.raises(KeyError):
#         from_quantity = Quantity(value=from_value, unit=from_unit)
#         to_quantity = unit_registry.convert(from_quantity, to_unit)

# def test_conversion_no_conv_path_fails(unit_registry):
#     from_value = 1
#     from_unit = "miles"
#     to_unit = "mm"

#     expected_value = 1.60934

#     with pytest.raises(ValueError):
#         from_quantity = Quantity(value=from_value, unit=from_unit)
#         to_quantity = unit_registry.convert(from_quantity, to_unit)







# ------------------------------ Factory Fixture ------------------------------
@pytest.fixture
def convert_value(unit_registry):
    def _convert(value, source_unit, target_unit) -> float:
        from_quantity = Quantity(value=value, unit=source_unit)
        to_quantity = unit_registry.convert(from_quantity, target_unit)
        return to_quantity.value

    return _convert


@pytest.mark.parametrize(
    "source_unit, input_value, target_unit, expected_result",
    [
        ("m", 1, "mm", 1000),
        ("m", 0.5, "mm", 500),
        ("m", 5000, "mm", 5_000_000),
    ],
)
def test_conversion_with_factory_fixture(
    convert_value,
    source_unit,
    input_value,
    target_unit,
    expected_result,
):
    actual_result = convert_value(
        input_value,
        source_unit,
        target_unit,
    )

    assert actual_result == pytest.approx(expected_result)