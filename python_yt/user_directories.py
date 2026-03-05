import os

try:
    with open('users.txt', 'r') as usersfile:
        for line in usersfile:
            os.makedirs("users/"+line.rstrip('\r\n'))
except FileExistsError as err:
    print("Directory already exists:",line)

import sys
try:
    with open(sys.argv[1], 'r') as usersfile:
        for line in usersfile:
            os.makedirs(sys.argv[2]+'/'+line.rstrip('\r\n'))
except FileExistsError as err:
     print("Directory already exists:", line)