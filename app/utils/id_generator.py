import secrets
import string


def generate_user_id() -> str:
    letters = string.ascii_uppercase
    digits = string.digits
    part1 = "".join(secrets.choice(letters) for _ in range(2))
    part2 = secrets.choice(digits) + secrets.choice(letters)
    part3 = "".join(secrets.choice(digits) for _ in range(4))
    return f"{part1}-{part2}-{part3}"
