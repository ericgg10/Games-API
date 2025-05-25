from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["md5_crypt"])


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


if __name__ == "__main__":
    contraseña_1 = "2141tt1"
    contraseña_2 = "251651616t"
    hash_1 = get_password_hash(contraseña_1)
    hash_2 = get_password_hash(contraseña_2)

    print("Verificando contraseñas: ")
    print(f"Contraseña_1 vs Hash_1 {verify_password(contraseña_1, hash_1)}")
    print(f"Contraseña_1 vs Hash_2 {verify_password(contraseña_1, hash_2)}")
