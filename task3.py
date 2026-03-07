import re


def normalize_phone(phone_number: str) -> str:
    normalized = re.sub(r"\D", "", phone_number.strip())

    if normalized.startswith("380"):
        return "+" + normalized
    if normalized.startswith("0"):
        return "+38" + normalized
    return "+38" + normalized
