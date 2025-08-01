from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)

def verify_password(stored_hash, plain_password):
    return check_password_hash(stored_hash, plain_password)
