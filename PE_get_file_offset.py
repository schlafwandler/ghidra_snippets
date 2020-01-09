# Example code for working with PE structures in python

# Converts an offset in the memory mapped executable to an offset in the file on disk using PE structures.

#@author schlafwandler
#@category Examples.Python
#@keybinding 
#@menupath 
#@toolbar 

import ghidra.app.util.bin.MemoryByteProvider as MemoryByteProvider
import generic.continues.RethrowContinuesFactory as RethrowContinuesFactory

def imagebase_offset_to_file_offset_PE(imagebase_offset):
    """Convert an offset in the memory mapped executable to an offset in the PE file on disk."""
    import ghidra.app.util.bin.format.pe as pe
    mem_provider = MemoryByteProvider(currentProgram.getMemory(), currentProgram.getImageBase())
    pefile = pe.PortableExecutable.createPortableExecutable(
                            RethrowContinuesFactory.INSTANCE,
                            mem_provider,
                            pe.PortableExecutable.SectionLayout.MEMORY)
    
    section = pefile.getNTHeader().getFileHeader().getSectionHeaderContaining(imagebase_offset)
    section_offset = section.getPointerToRawData()
    section_RVA = section.getVirtualAddress()
    file_offset = section_offset + imagebase_offset - section_RVA
    return file_offset

imagebase_offset = currentAddress.getOffset() - currentProgram.getImageBase().getOffset()
file_offset = imagebase_offset_to_file_offset_PE(imagebase_offset)
print("%08x"%(file_offset))
