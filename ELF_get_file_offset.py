# Example code for working with ELF structures in python

# Converts an offset in the memory mapped executable to an offset in the file on disk using ELF structures.

#@author schlafwandler
#@category Examples.Python
#@keybinding 
#@menupath 
#@toolbar 

import ghidra.app.util.bin.MemoryByteProvider as MemoryByteProvider
import generic.continues.RethrowContinuesFactory as RethrowContinuesFactory
import ghidra.app.util.bin.format.elf as elf

def imagebase_offset_to_file_offset_ELF(imagebase_offset):
    """Convert an offset in the memory mapped executable to an offset in the ELF file on disk."""

    mem_provider = MemoryByteProvider(currentProgram.getMemory(), currentProgram.getImageBase())
    elffile = elf.ElfHeader.createElfHeader(RethrowContinuesFactory.INSTANCE,mem_provider)

    try:
        elffile.parse()
    except:
        pass

    segment = elffile.getProgramLoadHeaderContaining(imagebase_offset)
    segment_offset = segment.getOffset()
    segment_RVA = segment.getVirtualAddress()
    file_offset = segment_offset + imagebase_offset - segment_RVA
    return file_offset

imagebase_offset = currentAddress.getOffset() - currentProgram.getImageBase().getOffset()
file_offset = imagebase_offset_to_file_offset_ELF(imagebase_offset)
print("%08x"%(file_offset))
