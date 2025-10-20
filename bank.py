class Account:
    def __init__(self, number, initial_balance=0):
        self.number = number
        self.balance = initial_balance
        self.withdraw_limit = 20.000 # Ограничение на максимальное снятие
        self.commission_rate = 0.1  # Процент комиссии за каждую операцию снятия

    def add_account(self, amount):  #Пополнение счета
        if amount > 0:
            self.balance += amount
            print(f"Счет {self.number}: Пополнен на {amount}. Текущий баланс: {self.balance:.2f}")
        else:
            print("Ошибка.Сумма должна быть положительной.")
    
  