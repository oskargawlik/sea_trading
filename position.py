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

