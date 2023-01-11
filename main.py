# Missing module docstring
import datetime as dt


class Record:
    # Missing class docstring
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            # If-else clause could be clearer to read
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    # Missing class docstring
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        # Missing function or method docstring
        self.records.append(record)

    def get_today_stats(self):
        # Missing function or method docstring
        today_stats = 0
        # Redefining name 'Record' from outer scope. You should use another name.
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        # Missing function or method docstring
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Missing class docstring
    def get_calories_remained(self):  # Gets the remaining calories for today
        # Comment about function description used incorrectly, doesn't follow docstring style
        ###
        # One letter variable makes the code harder to understand
        x = self.limit - self.get_today_stats()
        if x > 0:
            # Backslash should not be used and line with more than 79 characters should be avoided
            # The text is not exactly the same as described in the instructions
            return f'You can eat something else today,' \
                   f' but with a total calorie content of no more than {x} kcal'
        # Unnecesary else, you can delete it and de-ident the code inside it
        else:
            # Unnecessary parens after 'return' keyword
            return('Stop eating!')


class CashCalculator(Calculator):
    # Missing class docstring
    USD_RATE = float(60)  # US dollar exchange rate.
    EURO_RATE = float(70)  # Euro exchange rate.
    
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # Missing function or method docstring
        # You can use a dictionary to map the currency with its name, so you can avoid
        # assigning it every if-else clause 
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # Is there a mistake here? Did you wanted to use /= or two (==) equal signs?
            cash_remained == 1.00
            # Should say 'Rubles' according to the requirements
            currency_type = 'rub'
        if cash_remained > 0:
            return (
                f'Left for today {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        # Unnecesary elif after return. if should be used
        elif cash_remained == 0:
            return 'No money, keep it up!'
        # Unnecesary elif after return. 'if' should be used or none at all if it's the case
        elif cash_remained < 0:
            # You should use a f-string for formatting here and backslash should not be used
            return 'No money, keep it up:' \
                   ' your debt is - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)
    # Useless parent method override
    def get_week_stats(self):
        super().get_week_stats()

