from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def hash_pass(password: str):
    return pwd_context.hash(password)


def verify_pass(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)
