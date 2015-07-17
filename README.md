# Python-EXE-Packaging

This Git describes how to package python code as an excutable (EXE) for dristubution to Windows platforms.



## Dependencies
### py2exe
[Home](http://www.py2exe.org/)

[Download](http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/)

#### Installation

Nothing special, just run the exe and click "next" a few times

### UPX (optional)
[Home](http://upx.sourceforge.net/)

[Download](http://upx.sourceforge.net/download/)

This utility compresses the final exe to about 60% the original size.

#### Installation

This is a standalone excutable and is run with the command: `upx.exe yourProgram.exe`


## Files

### setup.py
Configuration for py2exe. It includes the name of the main program that is entered at the top. All other files will be caught by scraping all imports recursivly. This file need to be placed in the same directory as the main program file.

### setup.bat
For quicker compiling it is best to make this file to chain all the commands so an exe can be created with just a click.

1. Create the exe with py2exe (by running setup.py)
2. Compress the exe with UPX

## Running Everything Together
Once py2exe is installed and UPX is downloaded, all that is left is to place the setup.exe and setup.py in your python programs folder that you want to package and edit them with paths.

### setup.py
1. Enter the naim of your main program (full path is not needed)
2. Read list of excluded packages and make sure you dont need any of them
3. Settings are stored in a dictionary structure, for their meaning and more options see [py2exe settings](http://www.py2exe.org/index.cgi/ListOfOptions)

### setup.bat
1. Enter full path of setup.py (C:\\...programFolder\\setup.py)
2. Enter full path of EXE outputted by py2exe (C:\\...programFolder\dist\programName.exe)
3. Enter full path of UPX.exe
