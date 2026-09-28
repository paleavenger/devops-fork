def validate_phone(phone: str) -> bool:
    """Валидация ffроссийского номера телефона."""
    import re
    pattern = r'^\+?7\d{10}$'
    return bool(re.match(pattern, phone.replace('-', '').replace(' ', '')))


def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС (Страховой номер индивидуального лицевого счёта).
    
    СНИЛС состоит из 11 цифр: 9 цифр номера + 2 цифры контрольного числа.
    """
    import re
    
    cleaned = snils.replace('-', '').replace(' ', '')
    
    if not re.match(r'^\d{11}$', cleaned):
        return False
    
    numbers = [int(digit) for digit in cleaned[:9]]
    check_sum = int(cleaned[9:11])
    
    calculated = sum((9 - i) * numbers[i] for i in range(9))
    
    if calculated < 100:
        expected = calculated
    elif calculated % 101 == 100:
        expected = 0
    else:
        expected = calculated % 101
    
    return expected == check_sum