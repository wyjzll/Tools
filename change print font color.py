
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'警告的字体
    UNDERLINE = '\033[4m'
    BBG = '\033[1;33;44m'
    PUR ='\033[1;35m'
    
print(bcolors.PUR + "Font sample" + bcolors.ENDC)
print(bcolors.OKBLUE + "Font sample" + bcolors.ENDC)
