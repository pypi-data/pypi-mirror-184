import datetime
import functools

from dateutil.parser import parse

from gdshoplib.core.settings import PriceSettins

price_settings = PriceSettins()


class Price:
    def __init__(self, product):
        self.product = product

    @property
    def current_discount(self):
        # Получить текущую скидку
        if self.now == self.profit:
            return 0
        return 100 - round(self.now / self.profit * 100)

    def handle_ratio(*rations):
        def decor(func):
            @functools.wraps(func)
            def wrap(self, *args, **kwargs):
                ration = sum([1, *rations])
                return func(self, *args, **kwargs) * ration

            return wrap

        return decor

    def round(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            return int(round(result, 0))

        return wrap

    @property
    def eur(self):
        return self.product.price_eur

    @property
    @handle_ratio(price_settings.EURO_PRICE)
    def base(self):
        return self.product.price_eur

    @property
    @handle_ratio(price_settings.PRICE_NEITRAL_RATIO, price_settings.PRICE_VAT_RATIO)
    def neitral(self):
        return self.base

    @property
    @round
    def now(self):
        if not self.product.quantity:
            return self.neitral

        created_time = (
            parse(self.product.created_time)
            if isinstance(self.product.created_time, str)
            else self.product.created_time
        )
        created_at = (datetime.date.today() - created_time.date()).days
        if created_at > 60:
            return self.profit * 0.85

        if created_at > 30:
            return self.profit * 0.90

        return self.profit

    @property
    @round
    @handle_ratio(price_settings.PRICE_PROFIT_RATIO)
    def profit(self):
        return self.neitral

    # Коэфиценты
    # 0.16 - Себестоимость
    # 0.40 - Безубыточность
    # 0.60 - Ходовая
    # x.xx - Добавочная стоимость категории
    # x.xx - Добавочная стоимость бренда
    # x.xx - Добавочная стоимость платформы
