import os
import sys

filename = sys.argv[1]
filename += ".py"
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("#!/usr/bin/env python3\nimport os\nimport re")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(2)
