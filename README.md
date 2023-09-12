<div align="left">
   <img align="left" src="https://www.clipartmax.com/png/full/240-2404818_lock-clipart-blue-gray-password-icon-png.png" width=100/>
   <h3><b>PicklePasswd</b></h3>
   <p>Simple pickle script to get data from /etc/passwd in Linux machines</p>
</div>
<br><br><br>

# About
This script demonstrates how someone could create a simple script to potentially access your password information without your knowledge.

1. **Initialization**: After running `init.py`, this script will generate a pickle file in the same directory as `init.py`.

2. **Platform Check**: When executed, the script will check the platform. If it's not Linux, the script will delete itself to avoid any unintended consequences on incompatible systems.

3. **Execution**: When you run `run.py`, the script will load the pickle file and modify itself.

4. **Second Execution**: If you execute `run.py` for the second time the main script will attempt to access information stored in `/etc/passwd`. It will then save this information in a file called `.passwd` within the same directory as the script and once the code runs successfully, the script will change its own source code to a simple "Hello, World!" comment, effectively altering its functionality.
<br>
**Note that this script is not harmfull or any other type of viruses. this will just read a file, main porpse is to show how pickle viruses work.**
<br>

# Installation
+ Clone repository
```bash
git clone https://github.com/Kourva/PicklePasswd
```
+ Open source folder
```bash
cd PicklePasswd
```
+ Execute `init.py` to create pickle script
```bash
python3 init.py
```
+ Execute `run.py` to load pickle script
```bash
python3 run.py
```
+ Execute `run.py` again to run script
```bash
python3 run.py
```
