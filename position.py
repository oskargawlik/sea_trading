import inspect


class Position:
    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= 90):
            raise ValueError(f'Latitude{latitude} out of range')

        if not (-180 <= longitude <= 180):
            raise ValueError(f'Latitude{longitude} out of range')

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return 'N' if self.latitude >= 0 else 'S'

    @property
    def longitude_hemisphere(self):
        return 'E' if self.longitude >= 0 else 'W'

    def __repr__(self):
        return f'{type(self).__name__}(latitude={self.latitude}, longitude = {self.longitude})'

    def __str__(self):
        return f'{abs(self.latitude)}° {self.latitude_hemisphere}, {abs(self.longitude)}° {self.longitude_hemisphere} '

    def __format__(self, format_spec):
        print(format_spec)
        component_format_spec = '.2f'

        prefix, dot, suffix = format_spec.partition('.')
        if dot:
            component_format_spec = f'.{suffix}f'

        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return f'{latitude}° {self.latitude_hemisphere}, {longitude}° {self.longitude_hemisphere} '


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


def auto_repr(cls):
    members = vars(cls)

    if '__repr__' in members:
        raise TypeError(f'{cls.__name__} already defines __repr__')

    if '__init__' not in members:
        raise TypeError(f'{cls.__name__} does not override __init__')

    signature = inspect.signature(cls.__init__)
    parameter_names = list(signature.parameters)[1:]

    if not all(
        isinstance(members.get(name, None), property)
        for name in parameter_names
     ):
        raise TypeError(
            f'Cannot apply auto_repr to {cls.__name__} '
            f'because not all __init__ parameters have matching properties')

    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=cls.__name__,
            args=', '.join(
                "{name}={value}".format(
                    name=name,
                    value=getattr(self, name)
                ) for name in parameter_names
            )
        )

    setattr(cls, "__repr__", synthesized_repr)
    return cls


@auto_repr
class Location:
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __str__(self):
        return self.name


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

print(repr(maracaibo))
