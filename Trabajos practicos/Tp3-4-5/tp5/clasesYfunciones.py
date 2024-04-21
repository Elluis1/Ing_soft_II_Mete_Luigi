# Punto 1

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, number):
        if self.successor:
            self.successor.handle(number)


class PrimeHandler(Handler):
    def handle(self, number):
        if self.is_prime(number):
            print(f"El número {number} es primo y fue consumido por PrimeHandler.")
        else:
            super().handle(number)

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"El número {number} es par y fue consumido por EvenHandler.")
        else:
            super().handle(number)


class DefaultHandler(Handler):
    def handle(self, number):
        print(f"El número {number} no fue consumido.")


class NumberProcessor:
    def __init__(self):
        self.chain = PrimeHandler(EvenHandler(DefaultHandler()))

    def process_numbers(self):
        for number in range(1, 101):
            self.chain.handle(number)
