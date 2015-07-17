from distutils.core import setup
import py2exe

pythonMainProgram = "my main program to package.py"


DATA=[
    'C:\\Windows\system32\\USER32.dll',
    'C:\\Windows\system32\\SHELL32.dll',
    'C:\\Windows\system32\\ADVAPI32.dll',
    'C:\\Windows\system32\\WS2_32.dll',
    'C:\\Windows\system32\\GDI32.dll',
    'C:\\Windows\system32\\KERNEL32.dll'
    ]


py2exe_options = dict(ascii=True,  # Exclude encodings
                      excludes=['_ssl',  # Exclude _ssl
                                 'pyreadline',
                                 'difflib',
                                 'doctest',
                                 'locale',
                                 'optparse',
                                 'pickle',
                                 'calendar'],  # Exclude some of the larger
                      dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
                      compressed=True,  # Compress library.zip
                         )

setup(
	options={"py2exe":{'bundle_files': 1, 'compressed': True}},
	windows = [{'script': pythonMainProgram}],
	zipfile = None,
        excludes=['_ssl',  # Exclude _ssl
            'pyreadline', 'difflib', 'doctest',
            'optparse', 'pickle', 'calendar', 'pbd', 'unittest', 'inspect'],  # Exclude standard library
        dll_excludes=['msvcr71.dll', 'w9xpopen.exe',
                                 'API-MS-Win-Core-LocalRegistry-L1-1-0.dll',
                                 'API-MS-Win-Core-ProcessThreads-L1-1-0.dll',
                                 'API-MS-Win-Security-Base-L1-1-0.dll',
                                 'KERNELBASE.dll',
                                 'POWRPROF.dll',
                                 ],
	data_files = DATA,
        optimize =2,
)
