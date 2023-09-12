#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Resources
import pickle
import base64

# Self-modification: Open pickle file and update main source code
with open(__file__, "r+") as this, open(".script", "rb") as pkl:
	this.write(
		base64.b64decode(
			pickle.load(pkl).strip()
		).decode()
	)

# Note: User should run the code again
print("Run again!")