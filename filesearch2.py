import os
import re

user_input = input('What is the name of your directory?: ')
directory = os.listdir(user_input)

pattern = re.compile(".*50870.*SIGP.*")

for fname in directory:
    if os.path.isfile(user_input + os.sep + fname):
        f = open(user_input + os.sep + fname, 'r')
        if re.search(pattern, f.read()):
            print('found string in file %s' % fname)
        f.close()