#
#@author schlafwandler
#@category 
#@keybinding 
#@menupath 
#@toolbar 

name_prefix = "p_"

# assuming format as copied from x86dbg dump in address mode (no blank lines!)
#
# 00406010  76821856  kernel32.VirtualAlloc
# 00406014  7683D9B0  kernel32.VirtualAllocEx
# 00406018  768214B1  kernel32.GetModuleFileNameA
# [...]

import ghidra.program.model.symbol.SourceType as SourceType

def main():
    symtab = currentProgram.getSymbolTable()
    infile = str(askFile("Select input file","Input file"))
	
    with open(infile,"r") as f:
        for l in f.readlines():
            elements = l.split()
            if len(elements) == 3:
                addr,value,name = elements
            elif len(elements) == 2:
                addr,value = elements
            else:
                print("Malformed line '%s'"%(l))
                continue
			
            address = currentAddress.getAddress(addr)
            name = name_prefix+name

            symtab.createSymbol(address,name,SourceType.IMPORTED)
			
main()
