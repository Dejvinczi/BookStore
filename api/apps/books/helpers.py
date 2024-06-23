def book_image_upload_to_path(instance, filename):
    """Get the path for uploading book images."""
    return f"books/{instance.id}/{filename}"
