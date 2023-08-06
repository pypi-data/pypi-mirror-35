# pyatc
Python tools for working with proprietary Alivecor ATC files in both python 2 and python 3.

Supports reading and writing ATC files, reading from and writing to JSON and exporting to [EDF](http://www.edfplus.info/) (not plus) format.

## Installation
pyatc is available on [pypi](https://pypi.org/project/pyATC/).

Install using pip with `pip install pyatc`

## Usage
This sample requires you to have a file named in.atc in the same folder as the script.
```
from pyatc.pyatc import PyATC

f = PyATC.read_file("in.atc") #Read ATC
f.write_json_to_file("out.json") #Write json
f.write_to_file("out.atc") #Write ATC
f.write_edf_to_file("out.edf") #Write EDF
```
Please refer to [test.py](pyatc/test.py) for more usage.

### File support
Currently only file version 2 & 3 is supported. If you don't know if your file is the right format, try reading the file and the library will throw an `UnsupportedFileVersionException` if it is not.

If you got ATC files of a different version than 2 & 3, and ideally knowledge on how to read them, please let me know so that the library can support them.
