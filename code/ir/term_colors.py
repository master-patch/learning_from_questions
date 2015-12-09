HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKPURPLE = '\033[35m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def ir(string):
    return BOLD + OKBLUE + string + ENDC


def q(string):
    return OKPURPLE + string + ENDC


def c(integer):
    return OKBLUE + "(" + str(integer) + " questions)" + ENDC
