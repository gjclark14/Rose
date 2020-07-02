
class Nucleotides:
    def __init__(self):
        self.__a = 0
        self.__c = 0
        self.__g = 0
        self.__t = 0

    def get_a(self):
        return self.__a
    def get_c(self):
        return self.__c
    def get_g(self):
        return self.__g
    def get_t(self):
        return self.__t

    def set_a(self, a):
        self.__a = a
    def set_c(self, c):
        self.__c = c
    def set_g(self, g):
        self.__g = g
    def set_t(self, t):
        self.__t = t

    def __repr__(self):
        return "A: {0}, C: {1}, G: {2}, T: {3}".format(self.__a, self.__c,
                                                  self.__g, self.__t)

    def get_counts(self):
        return "{0} {1} {2} {3}".format(self.__a, self.__c, self.__g, self.__t)
