#
# Alice J Black
# 2024SEP24
# Budget Analysis Programming Project
# COSC 1010
#
# This program calculates budget for a month
#
# Format
from decimal import Decimal, DecimalException
from locale import currency, setlocale, LC_ALL
from typing import Iterator, Optional
def try_get_decimal(as_string: str) -> Optional[Decimal]:
    try:
        value = Decimal(as_string)
        if value <= 0:
            print('Number must be positive')
        else:
            return value
    except DecimalException:
        print('Invalid decimal number')
# Define budget for the month
def get_budget() -> Decimal:
    while True:
        value = try_get_decimal(input('Enter the budget of the month: '))
        if value is not None:
            return value
# Define expenses
def get_expenses() -> Iterator[Decimal]:
    while True:
        as_string = input('Enter an expense, or press enter ')
        if as_string == '':
            break
        value = try_get_decimal(as_string)
        if value is not None:
            yield value
# Calculate budget
def main() -> None:
    setlocale(LC_ALL, '')

    budget = get_budget()
    total = sum(get_expenses())

    surplus = budget - total
    if surplus > 0:
        print(f'You are {currency(surplus)} under the budget')
    elif surplus == 0:
        print('Your budget is enough for expenses')
    else:
        print(f'You are {currency(-surplus)} over the budget')

    print(f'Total: {currency(total)}')
#
if __name__ == '__main__':
    main()