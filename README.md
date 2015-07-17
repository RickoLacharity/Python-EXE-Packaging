# Python-EXE-Packaging

This Git describes how to package python code as an excutable (EXE) for dristubution to Windows platforms.



## Dependencies
### py2exe
[Home](http://www.py2exe.org/)

[Download](http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/)



### UPX (optional)
[Home](http://upx.sourceforge.net/)

[Download](http://upx.sourceforge.net/download/)

This utility compresses the final exe to about 60% the original size.

This is a standalone excutable and is run with the command: "upx.exe yourProgram.exe"


## Files

### setup.py
Configuration for py2exe. It includes the name of the main program that is entered at the top. All other files will be caught by scraping all imports recursivly.

### setup.bat
For quicker compiling it is best to make this file to chain all the commands so an exe can be created with just a click.

1. Create the exe with py2exe (by running setup.py)
2. Compress the exe with UPX