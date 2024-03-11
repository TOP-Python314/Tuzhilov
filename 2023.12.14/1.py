def strong_password(password: str) -> bool:
    if len(password) <= 8:
        return False
    elif password.upper() == password:
        return False
    elif password.lower() == password:
        return False
    elif len(password) < 2:
        return False
    elif len(set(password) and set(' .,:;!@#$%^&*-_+=')) < 1:
        return False
    else:
        return True
        
# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False
# >>> strong_password('Low__!16xxx')
# True
# >>> strong_password('Python')
# False
# >>>