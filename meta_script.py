import math
import sys
import argparse
import os
import subprocess
from Bio import SeqIO
parser=argparse.ArgumentParser(description="find 16s genes")
parser.add_argument('-f','--folder',metavar="",help='input genome folder ',required =True )
parser.add_argument('-i','--inputmodel',metavar="",help="bac or arc",required =True )
parser.add_argument('-l','--length',metavar="",help="minimum gene length",type=int)
parser.add_argument('-e','--evalue',metavar="",help="e value threeshold,must be float",type=float)
args=parser.parse_args()

#args no 1
if args.evalue is None:
    E_value = str(0.0001)
    print ("default E value  0.0001 is set")
elif args.evalue is float:
    E_value= str(args.evalue)
else:
    print("E value must float number")

#arg 2
if args.length is None :
    len_mini= 0
    print ("default minimum  hit length  0 is set")
elif args.length is int :
    len_mini= args.length
else:
    print(" minimum hit length required must be int")

#arg4  # add \n in case
if args.inputmodel.lower()  in ["bac","bacteria"]:
    model="bac.ssu.rnammer.hmm"
    print (" Hidden markov bacterial model is set")
elif args.inputmodel.lower()  in ["arc","archea"]:
    model= "arc.ssu.rnammer.hmm"
    print (" Hidden markov archeal model is set")
else:
    print ("please choose a correct model (arc-bac)")

#args5
if os.path.exists(args.folder) :
     print("folder exist in this directory")
else:
    print("folder dont exist in the script working directory")

# after checking if folder exist 
#  now i want to group all the input files fo nhmeer

files=[f for f in os.listdir(args.folder) if f.endswith(".fna")]
#print(files)
files_fasta=[g for g in os.listdir(args.folder) if g.endswith(".fasta")]
files.extend(files_fasta)

if files :

    print("list of  sequence files found %s"%files)
else:
    print(" no  supported seq.files  is found  (fasta,fna)")
    
    
###### now will input  and run nhmmer 
dfam_output=[]
seq_output=[]


for file in files:
    print("Analysing seq of  %s\n"% file)
    records = SeqIO.parse(args.folder+"/"+file, 'fasta')
    record_dict = SeqIO.to_dict(records)    
    list_coo=[] 
    subprocess.run(["nhmmer", "-E", E_value, "-o", "output.txt", "--dfamtblout" ,"outputfam.txt", model, args.folder +"/%s" % file])
    #out_read=open("output.txt",r).read()
    outfam_read=open("outputfam.txt","r").readlines()
    #seq_output.append(f"@   bacterial hmm  for {file} \n {out_read} \n")
    dfam_output.append(f"@   bacterial hmm hits summary  for {file} \n {outfam_read} \n")
    for line in outfam_read:
        if not line.startswith("#"):
            lst=line.split(" ")
            res = list(filter(None, lst))
            final_res=[]
            final_res.append(res[0])
            final_res.append(int(res[9]))
            final_res.append(int(res[10]))
            final_res.append(res[8])
            list_coo.append(final_res)

    if list_coo :

        with open("%s_16s.fasta"%file[0:5],"w+") as curr:
            print(f"\nFasta file generated for {file}") 
            for i in list_coo:
                if i :

                    if i[3] =="-":

                        end=i[1]  
                        start=i[2]  
                        x=record_dict[i[0]]   
                        subseq=x.seq[start:end]
                        str_seq=str(subseq)
                        str_seq=str_seq.strip()
                        if len(str_seq)>len_mini:
                            curr.write(f"> {i[0]}\n{str_seq}\n")


                    else:
                        end=i[2]
                        start=i[1]
                        x=record_dict[i[0]]
                        subseq=x.seq[start:end]
                        str_seq=str(subseq)
                        str_seq=str_seq.strip()
                        if len(str_seq)>len_mini:
                            curr.write(f"> {i[0]}\n{str_seq}\n")
    else:
        print(f"\nThere is no hits for {file} \n")

os.remove("output.txt")
os.remove("outputfam.txt")
