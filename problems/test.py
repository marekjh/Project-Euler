import os
import re

for filename in os.listdir():
    if re.match("problem[0-9][0-9].py", filename):
        n = re.search("[0-9][0-9]", filename).group(0)
        os.rename(filename, f"problem0{n}.py")