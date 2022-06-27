import os

for (dirpath, dirnames, filenames) in os.walk('.'):
    for fname in filenames:
        path = os.path.join(dirpath, fname)
        if open(path).read().strip() == "":
            os.remove(path)
            print('removed: %s' % path)
