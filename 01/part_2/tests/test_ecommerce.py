from datetime import datetime
import pytest
from src.ecommerce import Product, OrderError, process_order

def test_process_order():
    product = Product(
        name="Banana",
        price = 1,
        stock=100_000
    )
    order_meta = process_order(
        product=product,
        quantity=10_000,
        is_premium_user=False,
        order_time=datetime.now()
    )

    assert order_meta["product"] == "Banana"
    assert order_meta["total"] == 10_000 * 1

def test_premium_user():
    product = Product(
        name="Banana",
        price = 1,
        stock=100_000
    )
    order_meta = process_order(
        product=product,
        quantity=10_000,
        is_premium_user=True,
        order_time=datetime.now()
    )

    assert order_meta["product"] == "Banana"
    assert order_meta["total"] == 9_000

def test_too_large_order():
    product = Product(
        name="Banana",
        price = 1,
        stock=100
    )

    # Test to see if an OrderError exception is raised
    with pytest.raises(OrderError):
        process_order(
            product=product,
            quantity=10_000,
            is_premium_user=False,
            order_time=datetime.now()
        )

    # process_order(
    #     product=product,
    #     quantity=10_000,
    #     is_premium_user=False,
    #     order_time=datetime.now()
    # )