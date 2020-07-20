class SpaceAge:

    def __init__(self, seconds):
        self.seconds =  seconds
        self.seconds_in_year_on_earth = 365.25 * 24 * 60 * 60

    def __seconds_in_year_on_planet(self, proportion):
        return self.seconds_in_year_on_earth * proportion

    def __format_response(self, value):
        return round(value,2)

    def on_earth(self):
        years = self.seconds / self.seconds_in_year_on_earth
        return self.__format_response(years)

    def on_mercury(self):
        proportion = 0.2408467
        years = self.seconds / self.__seconds_in_year_on_planet(proportion)
        return self.__format_response(years)

    def on_venus(self):
        proportion = 0.61519726
        years = self.seconds / self.__seconds_in_year_on_planet(proportion)
        return self.__format_response(years)

    def on_mars(self):
        proportion = 1.8808158
        years = self.seconds / self.__seconds_in_year_on_planet(proportion)
        return self.__format_response(years)

    def on_jupiter(self):
        proportion = 11.862615
        years = self.seconds / self.__seconds_in_year_on_planet(proportion)
        return self.__format_response(years)

    def on_saturn(self):
        proportion = 29.447498
        years = self.seconds / self.__seconds_in_year_on_planet(proportion)
        return self.__format_response(years)

    def on_uranus(self):
        proportion = 84.016846
        years = self.seconds / self.__seconds_in_year_on_planet(proportion)
        return self.__format_response(years)

    def on_neptune(self):
        proportion = 164.79132
        years = self.seconds / self.__seconds_in_year_on_planet(proportion)
        return self.__format_response(years)

