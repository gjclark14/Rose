
class Fasta:
    def __init__(self, code, dna_string):
        self.__code = code
        self.__dna_string = dna_string

    def __repr__(self):
        return ">Rosalind_{code}\n{dna_string}".format(self.__code,
                                                       self.__dna_string)

    def get_code(self):
        return self.__code

    def set_code(self, code):
        self.__code = code

    def get_dna_string(self):
        return self.__dna_string

    def set_dna_string(self, dna_string):
        self.__dna_string = dna_string



class FastaParser:
    def parse_string(file_name):
        try:
            fin = open(file_name, 'r')
            fin.readlines()
            print(fin)


        except IOError:
            print "Error: {file_name} does not exist.".format(file_name)




