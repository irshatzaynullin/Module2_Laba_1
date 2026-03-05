from __future__ import annotations
class BankCard:
    """
    Базовый класс банковской карты.

    Описывает общие свойства и поведение для любых карт:
    пополнение, снятие, блокировка/разблокировка, проверка PIN.
    """

    def __init__(
        self,
        card_number: str,
        holder_name: str,
        balance: float,
        currency: str,
        pin_code: int,
    ) -> None:
        """
        Инициализация банковской карты.

        Args:
            card_number: Номер карты.
            holder_name: Владелец карты.
            balance: Текущий баланс.
            currency: Валюта счета (например, RUB, USD).
            pin_code: PIN-код карты.

        Notes:
            PIN-код инкапсулирован (__pin_code), так как это чувствительные данные,
            и к ним не должно быть прямого доступа извне.
        """
        self.card_number: str = card_number
        self.holder_name: str = holder_name
        self.balance: float = balance
        self.currency: str = currency
        self._is_active: bool = True  # protected: доступно в наследниках
        self.__pin_code: int = pin_code  # private: безопасное хранение PIN

    def __str__(self) -> str:
        """
        Удобное представление карты для пользователя.
        """
        masked_number: str = f"**** **** **** {self.card_number[-4:]}"
        status: str = "активна" if self._is_active else "заблокирована"
        return (
            f"Карта {masked_number} ({self.currency}), "
            f"владелец: {self.holder_name}, статус: {status}"
        )

    def __repr__(self) -> str:
        """
        Техническое представление объекта для разработчика.
        """
        return (
            f"BankCard(card_number={self.card_number!r}, holder_name={self.holder_name!r}, "
            f"balance={self.balance!r}, currency={self.currency!r}, is_active={self._is_active!r})"
        )

    def check_pin(self, pin: int) -> bool:
        """
        Проверяет корректность PIN-кода.

        Args:
            pin: PIN-код для проверки.

        Returns:
            True, если PIN корректный, иначе False.
        """
        return pin == self.__pin_code

    def deposit(self, amount: float) -> float:
        """
        Пополняет баланс карты.

        Args:
            amount: Сумма пополнения.

        Returns:
            Новый баланс после пополнения.

        Raises:
            ValueError: Если сумма пополнения некорректна или карта заблокирована.
        """
        if not self._is_active:
            raise ValueError("Операция невозможна: карта заблокирована.")
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля.")
        self.balance = round(self.balance + amount, 2)
        return self.balance

    def withdraw(self, amount: float) -> bool:
        """
        Снимает деньги с карты (базовая логика: только в пределах баланса).

        Args:
            amount: Сумма снятия.

        Returns:
            True, если операция выполнена; False, если недостаточно средств.
        """
        if not self._is_active or amount <= 0:
            return False
        if amount > self.balance:
            return False
        self.balance = round(self.balance - amount, 2)
        return True

    def block_card(self) -> None:
        """
        Блокирует карту.
        """
        self._is_active = False

    def unblock_card(self, pin: int) -> bool:
        """
        Разблокирует карту после успешной проверки PIN.

        Args:
            pin: PIN-код пользователя.

        Returns:
            True, если карта разблокирована; иначе False.
        """
        if self.check_pin(pin):
            self._is_active = True
            return True
        return False

    def get_balance(self) -> float:
        """
        Возвращает текущий баланс карты.

        Returns:
            Текущий баланс.
        """
        return self.balance


class CreditCard(BankCard):
    """
    Дочерний класс кредитной карты.

    Дополняет базовую карту кредитным лимитом, долгом и процентной ставкой.
    """

    def __init__(
        self,
        card_number: str,
        holder_name: str,
        balance: float,
        currency: str,
        pin_code: int,
        credit_limit: float,
        annual_rate: float,
    ) -> None:
        """
        Инициализация кредитной карты.

        Args:
            card_number: Номер карты.
            holder_name: Владелец карты.
            balance: Собственные средства на карте.
            currency: Валюта счета.
            pin_code: PIN-код карты.
            credit_limit: Доступный кредитный лимит.
            annual_rate: Годовая процентная ставка (в процентах).
        """
        super().__init__(card_number, holder_name, balance, currency, pin_code)
        self.credit_limit: float = credit_limit
        self.annual_rate: float = annual_rate
        self.debt: float = 0.0

    def __str__(self) -> str:
        """
        Удобное представление кредитной карты.
        """
        masked_number: str = f"**** **** **** {self.card_number[-4:]}"
        status: str = "активна" if self._is_active else "заблокирована"
        return (
            f"Кредитная карта {masked_number} ({self.currency}), владелец: {self.holder_name}, "
            f"долг: {self.debt:.2f}, лимит: {self.credit_limit:.2f}, статус: {status}"
        )

    def __repr__(self) -> str:
        """
        Техническое представление кредитной карты.
        """
        return (
            f"CreditCard(card_number={self.card_number!r}, holder_name={self.holder_name!r}, "
            f"balance={self.balance!r}, currency={self.currency!r}, credit_limit={self.credit_limit!r}, "
            f"annual_rate={self.annual_rate!r}, debt={self.debt!r}, is_active={self._is_active!r})"
        )

    def withdraw(self, amount: float) -> bool:
        """
        Снимает деньги с кредитной карты.

        Причина перегрузки:
            В базовом классе снятие возможно только в пределах собственного баланса.
            Для кредитной карты это неверно, потому что она может использовать
            кредитный лимит. Поэтому метод переопределён с учетом:
            1) списания сначала собственных средств,
            2) затем использования кредитного лимита с ростом долга.

        Args:
            amount: Сумма снятия.

        Returns:
            True, если операция выполнена; False, если недостаточно доступных средств.
        """
        if not self._is_active or amount <= 0:
            return False

        available_total: float = self.balance + (self.credit_limit - self.debt)
        if amount > available_total:
            return False

        if amount <= self.balance:
            self.balance = round(self.balance - amount, 2)
            return True

        # Сначала списываем весь баланс, остаток идёт в долг
        credit_part: float = amount - self.balance
        self.balance = 0.0
        self.debt = round(self.debt + credit_part, 2)
        return True

    def accrue_interest(self, months: int) -> float:
        """
        Начисляет проценты на текущий долг (простая модель).

        Args:
            months: Количество месяцев начисления.

        Returns:
            Новый размер долга после начисления процентов.
        """
        if months <= 0 or self.debt <= 0:
            return self.debt
        monthly_rate: float = self.annual_rate / 12 / 100
        self.debt = round(self.debt * (1 + monthly_rate * months), 2)
        return self.debt

    def pay_debt(self, amount: float) -> float:
        """
        Погашает задолженность по кредитной карте.

        Args:
            amount: Сумма погашения.

        Returns:
            Остаток долга после оплаты.

        Raises:
            ValueError: Если сумма некорректна или карта заблокирована.
        """
        if not self._is_active:
            raise ValueError("Операция невозможна: карта заблокирована.")
        if amount <= 0:
            raise ValueError("Сумма погашения должна быть больше нуля.")

        self.debt = round(max(0.0, self.debt - amount), 2)
        return self.debt


if __name__ == "__main__":
    card: CreditCard = CreditCard(
        card_number="1234567812345678",
        holder_name="Иван Иванов",
        balance=5000.0,
        currency="RUB",
        pin_code=1234,
        credit_limit=20000.0,
        annual_rate=24.0,
    )

    print(card)
    print(repr(card))

    print(card.withdraw(7000.0))
    print("Баланс:", card.get_balance())
    print("Долг:", card.debt)

    print(card.accrue_interest(2))
    print(card.pay_debt(1500.0))

    card.block_card()
    print(card.withdraw(100.0))
    print(card.unblock_card(1234))
    print(card.withdraw(100.0))