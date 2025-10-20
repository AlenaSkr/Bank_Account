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
    
    def withdraw(self, amount): #Снятие денежных средств с комиссией
        if amount <= 0 or amount > self.withdraw_limit: #снятие вместе с комиссией банка
            print("Недопустимая сумма снятия!")
        elif amount + (amount * self.commission_rate) > self.balance: #Проверка достаточно ли средств на балансе
            print("Недостаточно средств на счете для операции.")
        else:
            commission = amount * self.commission_rate #Выполняется операция, если все условия успешной пройдены
            total_withdrawal = amount + commission
            self.balance -= total_withdrawal
            print(f"Снято {amount}, комиссия составила {commission:.2f}. Остаток на счету: {self.balance:.2f}")
