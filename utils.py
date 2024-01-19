def add_years_to_date(original_date, years_to_add: int):
    return original_date.replace(year=original_date.year + years_to_add)
