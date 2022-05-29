# DIGIMON-16S IDentIfication of 16s Genes In MicrObial geNomes
- logo (optional)
- brief introduction about script usage

_This code was developed as part of a project carried out by Erinda Rruci, Giulia Fiorito, Sofia Stocco, Marwan Sharawy during the course of Microbial Metagenomics (Molecular Biology master degree) at the University of Padova. The project was supervised by Prof. Stefano Campanaro, Dr. Maria Silvia Morlino, Dr. Edoardo Bizzotto, and Dr. Gabriele Ghiotto._

## Requirements
This program has been designed to work with a specific folder structure:
- .fasta/.fna/.fa/.faa/.ffn files in a subfolder to the working directory. The user has to provide the name of the folder as an argument when launching the program from the command line;
- .hmm file for nhmmer has to be in the same directory where the software is located;
- the input genome folder need to be in the same directory of the script.


 VOGLIAMO INSERIRE UN'IMMAGINE? o un directory flow?

### Files
The automated nhmmer step makes use of two Hidden Markov Model files, one for Bacteria and one for Archaea. This program comes with two hmm models for the 16S gene, one for Archaeal genomes (arc.ssu.rnammer.hmm) and one for Bacterial genomes (bac.ssu.rnammer.hmm)

### Programs
- [HMMER (v.3.3.3)](http://hmmer.org/)
- [Python 3.8+](https://www.python.org/)

### Packages
- [Bio.SeqIO](https://biopython.org/wiki/Download)
 

## Command line instructions

### Launching the program
The program is provided as a .py file. To permit the executability of the script modify the permissions of the .py file. 
Open a terminal session in the directory where the program is located and enter the following command line: 

```bash
python3 ./meta_script.py [-h] -f  -i  [-l] [-e]
```

### Arguments
The arguments used in the command line define both the program parameters and the ones in the automated nhmmer command.

#### Mandatory arguments
- `-f <folder_name>` or `--folder <folder_name>`
  
  Input genomes folder: indicates the folder where the microbial genomes are located. As a requirement this folder must be a subfolder of the working directory.

- `-i bac` or `--inputmodel bac` or `-i bacteria` or `--inputmodel bacteria` or `-i arc` or `--inputmodel arc` `-i archea` or `--inputmodel archea`
  
  Input hmm: defines which .hmm should be used by nhmmer as query. The software provides two possible .hmm files, one for bacteria and one for archea.

#### Facultative arguments

- `-h` or `--help`
  
  Help: shows a help message with an explanation of the arguments and quit the program

- `-l <number>` or `--lenght <number>`
  
  Minimum 16S sequence lenght: specifies the minimum lenght of alligment to extract the 16S sequences. It is expressed in number of bases. Default value is 0

- `-e` or `--evaue` 
  
  E-value threeshold: allows to run the nhmmer command with a specified e-value. It needs to be  float with “.” as a decimal separator. Default value is 0.0001


### Example


```bash
python3 ./meta_script.py -f BACTERIA -i bac -l 300 -e 0.005
```
The command runs on each fasta files stored in the BACTERIA subfolder searching for alligments between the sequences and the bacterial hmm. Only alligned sequences longer than 300 bases and with a significance more than 0.005 are considered valid and collected into the output.

## Output
The software is designed to give only one output:
- `<first5lettersofgenome>_16s.fasta`
  It's a fasta file obtained for each input genome containing the extracted alligned 16S sequences and the fasta IDs. _ IS IT CORRECT? _
_ MAYBE WE SHOULD PUT s IN CAPITAL LETTER _






