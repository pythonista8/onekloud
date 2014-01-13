import hashlib


def hmac_sha256(string):
    try:
        string.decode('utf8')
    except UnicodeDecodeError:
        string = string.encode('utf8')
    hash_ = hashlib.sha256(string).hexdigest()
    return hash_
