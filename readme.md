## Various Ghidra script fragments

* [PE_get_file_offset.py](https://github.com/schlafwandler/ghidra_snippets/blob/master/PE_get_file_offset.py)
Example code on how to to access PE structures from Ghidra python.
Converts an offset in the memory mapped executable to an offset in the file on disk using PE structures.
* [ELF_get_file_offset.py](https://github.com/schlafwandler/ghidra_snippets/blob/master/ELF_get_file_offset.py) 
Example code on how to to access ELF structures from Ghidra python.
Converts an offset in the memory mapped executable to an offset in the file on disk using ELF structures.
* [MassLabeler.py](https://github.com/schlafwandler/ghidra_snippets/blob/master/MassLabeler.py)
Small piece of code to quickly add labels to many locations.
Originally written to transfer function names of a custom import table from x64dbg to ghidra.
