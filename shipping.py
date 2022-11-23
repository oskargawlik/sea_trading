import iso6346


class ShippingContainer:
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.bic = type(self)._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    @property
    def volume_ft3(self):
        return self._calc_volume()


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, temperature):
        self._set_celsius(temperature)

    def _set_celsius(self, temperature):
        if temperature > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError('Temperature too hot!')
        self._celsius = temperature

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20

    def _set_celsius(self, value):
        if HeatedRefrigeratedShippingContainer.MIN_CELSIUS > value:
            raise ValueError(f'Temperature too cold!')
        super()._set_celsius(value)


sc = ShippingContainer('elo', 200, ['drugs'])
rsc = RefrigeratedShippingContainer('ELO', 200, ['drugs'], celsius=3)
hrsc = HeatedRefrigeratedShippingContainer('ELO', 200, ['drugs'], celsius=3)

print(sc.volume_ft3)
print(rsc.volume_ft3)
hrsc.celsius = 2
print(hrsc.celsius)