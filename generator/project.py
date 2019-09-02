from model.project import Project
import random
import string
import os.path
import jsonpickle
import getopt
import sys


n = 5
f = "data/groups.json"


def random_number(maxlen):
    symbols = string.digits
    return "-".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Project(name=random_string("name", 5), description=random_string("description", 5))
             for i in range(n)
             ]

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)



for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
