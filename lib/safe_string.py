"""
Safe string
"""
import re
from datetime import date
from unidecode import unidecode

CURP_REGEXP = r"^[A-Z]{4}\d{6}[A-Z]{6}[A-Z0-9]{2}$"
EMAIL_REGEXP = r"^[\w.-]+@[\w.-]+\.\w+$"
PASSWORD_REGEXP = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,24}$"
TELEFONO_REGEXP = r"^[1-9]\d{9}$"

PASSWORD_REGEXP_MESSAGE = "La contrasena debe tener de 8 a 24 caracteres, comenzando con una letra y contener por lo menos una mayuscula y un numero"


def safe_clave(input_str):
    """Safe clave"""
    if not isinstance(input_str, str):
        raise ValueError("La clave esta vacia")
    new_string = input_str.strip().upper()
    regexp = re.compile("^[A-Z0-9-]{2,16}$")
    if regexp.match(new_string) is None:
        raise ValueError("La clave es incorrecta")
    return new_string


def safe_curp(input_str):
    """Safe CURP"""
    if not isinstance(input_str, str):
        raise ValueError("CURP no es texto")
    removed_spaces = re.sub(r"\s", "", input_str)
    removed_simbols = re.sub(r"[()\[\]:/.-]+", "", removed_spaces)
    final = unidecode(removed_simbols.upper())
    if re.fullmatch(CURP_REGEXP, final) is None:
        raise ValueError("CURP es incorrecto")
    return final


def safe_email(input_str):
    """Safe email"""
    if not isinstance(input_str, str) or input_str.strip() == "":
        raise ValueError("Email es incorrecto")
    new_string = input_str.strip().lower()
    regexp = re.compile(EMAIL_REGEXP)
    if regexp.match(new_string) is None:
        raise ValueError("Email es incorrecto")
    return new_string


def safe_expediente(input_str):
    """Safe expediente"""
    if not isinstance(input_str, str) or input_str.strip() == "":
        return ""
    elementos = re.sub(r"[^0-9]+", "-", input_str).split("-")
    try:
        numero = int(elementos[0])
        ano = int(elementos[1])
    except (IndexError, ValueError) as error:
        raise error
    if numero < 0:
        raise ValueError
    if ano < 1950 or ano > date.today().year:
        raise ValueError
    return f"{str(numero)}/{str(ano)}"


def safe_integer(input_str, default=1):
    """Safe integer"""
    if not isinstance(input_str, str):
        return default
    final = input_str.strip()
    if re.match(r"^\d+$", final) is None:
        return default
    return int(final)


def safe_string(input_str, max_len=250):
    """Safe string"""
    if not isinstance(input_str, str):
        return ""
    new_string = re.sub(r"[^a-zA-Z0-9,/-]+", " ", unidecode(input_str))
    removed_multiple_spaces = re.sub(r"\s+", " ", new_string)
    final = removed_multiple_spaces.strip().upper()
    return (final[:max_len] + "...") if len(final) > max_len else final


def safe_telefono(input_str):
    """Safe telefono"""
    if not isinstance(input_str, str):
        raise ValueError("Telefono no es texto")
    solo_numeros = re.sub(r"[^0-9]+", "", unidecode(input_str))
    if re.match(TELEFONO_REGEXP, solo_numeros) is None:
        raise ValueError("Telefono está incompleto")
    return solo_numeros
