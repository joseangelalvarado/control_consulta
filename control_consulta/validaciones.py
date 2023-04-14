

# - Validar nombres, y apellidos

def validar_nombre(text3):
    if text3.isdecimal() == True:
        return False
    return True

# - Validar edad


def validar_num(text, num1):
    if len(num1) > 2:
        return False

    return text.isdecimal()

# - Validar semanas


def validar_sdg(text1, num2):
    if len(num2) > 2:
        return False

    return text1.isdecimal()


def cap(ap_paterno):

    ap_paterno.set(ap_paterno.get().capitalize())
