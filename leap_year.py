# Akseptansekriterier:

# Et år er et skuddår
# Når det er delelig med 4, men ikke 100
# Når det er delelig med 400
# (For eksempel var år 2000 et skuddår)

# Et år er ikke et skuddår
# Når det ikke er delelig med 4
# Når det er delelig med 100, men ikke 400.
# (For eksempel var ikke 1700, 1800 og 1900 skuddår, ei heller blir 2100 et)

# pytest test_leap_year.py

def is_a_leap_year(year):
    """
        Sjekk om et år er et skuddår.

        Args:
            year(int): Året som skal sjekkes.

        Returns:
            bool: True hvis året er et skuddår, False ellers.
        """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    elif (year % 4 != 0 or year % 400 != 0) and year % 100 == 0:
        return False


year = 2000
is_leap = is_a_leap_year(year)
if is_leap:
    print(f"året {year} er et skuddår")
else:
    print(f"året {year} er ikke et skuddår")
