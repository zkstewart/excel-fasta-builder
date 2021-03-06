# excel-fasta-builder

# Introduction
This script was designed to assist anyone attempting to parse the information in the Excel document associated with the study "Transcriptomic investigation of wound healing and regeneration in the cnidarian *Calliactis polypus*" that lacks coding experience. If you wish to obtain a fasta file of the differentially expressed genes from this study, this file may be of help.

# Description
This script works by reading in two text files with corresponding transcript IDs and nucleotide/protein sequences. For example, that means **text_file_1.txt** may look like this after you copy-paste a column into a text file:
```
TR84742|c4_g1_i2
TR85979|c5_g1_i1
TR87067|c2_g2_i2
TR87067|c2_g5_i3
TR87487|c1_g3_i4
```
And **text_file_2.txt** may look like this:

```
FPVIPGSCPTLPTAAECPPEEDIDHKCQKDADCPGNVKCCLDGCERRCFNPATPAPTTKFPVSSGSCPIFPIAEECPPEEE
MSPEAIYDQVFTTESDIWSYGVVLWEISTLGGAPYPSMFTRDLVREIRKGYRMEKPEMCSDEVYKIMRTCWEANPSDRPSFHDIVKQFEELLLEDNPYLDFSNFDNNKDYYLVPSFNSAQDENSASNLPEV*
DGLKGNYGMLDQVHALKWVQNNIKSFGGDPEDVTIFGESAGGASVGFLVLSPLAKGLFHKAILQSGDPDAVWAYRNYEEALYLAKDPNRPDPIPLAWPKYDVNQQKFMALKPMYAVQEKPRSSHV
MSLLFIQCFNMLPSMFLTLILLLNFALREAKVVKYAPEVTLKSGKIRGLLSDLSTGGTVRKYLGVPFAKAERFQVPTDPDSWTGVKDMFTIGKICPQQPHN
YAEVPLKRSENKPFQVVFEYAAGDNSEGWAHIGNIQMFNCSFETRPFKAKPNLDDVKVRLRGGKSNMEGRAEVFADGSWGTFQGRWQWYPRSATVICRQLKFGGAVRVHHGSYFGKSTVNGPVWGTRTHIYPTCKSNETNIGRCLHKSSMRMVDSNHVDVGVECFDARLVGGNSPNEGRVEINYKGKWG
```
Because each entry is placed on a new line, this script can simply join each line together in a fasta format. Make sure this script file is in the same directory as the two text files.

# Usage
Download and install Python versions 3.4 or 3.5 from https://www.python.org/. Following the prompts of the script, supply the names of two text files with contents formatted as exampled above and specify the name for the output file that will be generated.
