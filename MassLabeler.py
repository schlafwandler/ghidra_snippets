#
#@author schlafwanlder
#@category 
#@keybinding 
#@menupath 
#@toolbar 

infile = "/media/tmp/Lab_06-1-ImportTable"
name_prefix = "p_"

# assuming format as copied from x86dbg dump window in address mode (no blank lines!)
#
# 00406010  76821856  kernel32.VirtualAlloc
# 00406014  7683D9B0  kernel32.VirtualAllocEx
# 00406018  768214B1  kernel32.GetModuleFileNameA
# [...]

import ghidra.program.model.symbol.SourceType as SourceType

def main():
	symtab = currentProgram.getSymbolTable()
	
	with open(infile,"r") as f:
		for l in f.readlines():
			addr,value,name = l.split()
			
			address = currentAddress.getAddress(addr)
			name = name_prefix+name
			
			symtab.createSymbol(address,name,SourceType.IMPORTED)
			
main()
