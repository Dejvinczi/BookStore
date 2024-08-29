import uuid


def generate_order_number():
    """Generate order number."""
    unique_sequence = uuid.uuid4().hex.upper()

    return unique_sequence
