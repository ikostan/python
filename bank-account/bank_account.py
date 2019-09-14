import threading


class BankAccount(object):
    """
    Simulate a bank account supporting opening/closing,
    withdrawals, and deposits of money.
    """

    def __init__(self):
        self._balance = 0.0
        self._is_opened = False
        self._lock = threading.Lock()

    def get_balance(self):
        """
        Returns current balance
        :return:
        """

        self._check_is_account_opened()
        return self._balance

    def open(self):
        """
        Simulate a bank account supporting opening
        :return:
        """

        if not self._is_opened:
            self._is_opened = True
        else:
            raise ValueError("ERROR: account already opened")
        return None

    def deposit(self, amount):
        """
        Clients can make deposits
        :param amount:
        :return:
        """

        self._check_is_account_opened()
        BankAccount._check_is_negative_amount(amount)

        with self._lock:
            self._balance += amount
        return None

    def withdraw(self, amount):
        """
        Clients can make withdrawals
        :param amount:
        :return:
        """

        self._check_is_account_opened()
        BankAccount._check_is_negative_amount(amount)

        with self._lock:
            if amount <= self.get_balance():
                self._balance = self._balance - amount
            else:
                raise ValueError("ERROR: insufficient balance")
        return None

    def close(self):
        """
        It should be possible to close an account
        :return:
        """

        self._check_is_account_opened()
        self._is_opened = False
        self._balance = 0.0
        return None

    def _check_is_account_opened(self):
        """
        Operations against a closed account must fail
        :return:
        """

        if not self._is_opened:
            raise ValueError('ERROR: account is closed.')
        return None

    @staticmethod
    def _check_is_negative_amount(amount):
        """
        Cannot withdraw or deposit negative amount
        :param amount:
        :return:
        """

        if amount < 0:
            raise ValueError("ERROR: Cannot withdraw/deposit negative amount")
        return None
