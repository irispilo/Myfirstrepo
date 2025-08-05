ZODIAC_SIGNS = [
    ("Capricornio",  (12, 22), (1, 19)),
    ("Acuario",      (1, 20),  (2, 18)),
    ("Piscis",       (2, 19),  (3, 20)),
    ("Aries",        (3, 21),  (4, 19)),
    ("Tauro",        (4, 20),  (5, 20)),
    ("Géminis",      (5, 21),  (6, 20)),
    ("Cáncer",       (6, 21),  (7, 22)),
    ("Leo",          (7, 23),  (8, 22)),
    ("Virgo",        (8, 23),  (9, 22)),
    ("Libra",        (9, 23),  (10, 22)),
    ("Escorpio",     (10, 23), (11, 21)),
    ("Sagitario",    (11, 22), (12, 21)),
]

def list_signs():
    print("Signos del Zodiaco y sus fechas:")
    for sign, (start_month, start_day), (end_month, end_day) in ZODIAC_SIGNS:
        print(f"{sign}: {start_month}/{start_day} - {end_month}/{end_day}")

def get_zodiac_sign(month, day):
    for sign, (start_month, start_day), (end_month, end_day) in ZODIAC_SIGNS:
        # Caso cuando el rango cruza de diciembre a enero (Capricornio)
        if start_month == 12 and end_month == 1:
            if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
                return sign
        else:
            # Caso normal
            if (month == start_month and day >= start_day) or (month == end_month and day <= end_day) or (start_month < month < end_month):
                return sign
    return None  # Si no encuentra un signo (debería cubrir todas fechas válidas)
