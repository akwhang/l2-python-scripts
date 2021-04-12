import os
import re

user_input = input('What is the name of your directory')
directory = os.listdir(user_input)

pattern = re.compile(".*50870.*SIGP.*")

for fname in directory:
    if os.path.isfile(user_input + os.sep + fname):
        with open(user_input + os.sep + fname, 'r') as f:
            for line in f:
                if re.search(pattern, line):
                    print('%s' % line)
                    # To print filename with string, use below:
                    # print('found string in file %s' % fname)
        f.close()