import hashlib

def get_image_hash(file):
    """Generate MD5 hash of uploaded image file."""
    md5 = hashlib.md5()
    for chunk in file.chunks():
        md5.update(chunk)
    file.seek(0)  # Reset file pointer after reading
    return md5.hexdigest()
