class ElecFence(object):
    def __init__(self):
        self.__fence = []

    def create(self, geojson: object):
        """

        :type geojson: object
        :param geojson:
        :return:
        """
        pass

    def inside(self, point: object):
        """

        :type point: object
        :param point:
        :return:
        """
        pass

    def outside(self, point: list):
        """

        :type point: object
        :param point:
        :return:
        """
        pass

    pass


class Point(object):
    def __init__(self, point=None, swap=None, **kwargs):
        """

        :param point:
        :param swap:
        :param kwargs:
        """
        self.__long = None
        self.__lat = None
        """
        Get point from point.
        """
        if point:
            if isinstance(point, str):
                self.__long, self.__lat = point.split(',')
            if isinstance(point, list):
                self.__long, self.__lat = point
            if swap:
                self.__long, self.__lat = self.__lat, self.__long
        """
        Get point from kwargs.
        """
        if not (self.__long or self.__lat):
            self.__long = kwargs.get('long')
            self.__lat = kwargs.get('lat')
        """
        Convert str to float.
        """
        if isinstance(self.__long, str):
            self.__long = float(self.__long)
        if isinstance(self.__lat, str):
            self.__lat = float(self.__lat)

    def array(self, swap=None):
        return [self.__lat, self.__long] if swap else [self.__long, self.__lat]

    def __repr__(self):
        return '{},{}'.format(self.__long, self.__lat)

    def __add__(self, other):
        return Point(long=self.__long + other.__long, lat=self.__lat + other.__lat)
