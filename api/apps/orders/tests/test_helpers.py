from ..helpers import generate_order_number


def test_generate_order_number():
    """Test that the generate_order_number function generates a valid order number."""
    no = generate_order_number()

    assert len(no) == 32
    assert no.isalnum()
