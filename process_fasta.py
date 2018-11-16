from Bio import SeqIO
import os

path_=os.getcwd()  			# get the location of Current working directory
_=(os.path.join(path_,"data\\data.txt"))

if os.path.isfile(_):
	try:os.remove("data\\data.txt")		# Remove the data.txt file from previous run
	except Exception:pass

o_put=open("data\\data.txt","a+")		# create and open a new data.txt file
o_put.write("sequence"+"\t"+"class"+"\n")
for record in SeqIO.parse("data\\positive_training.fasta", "fasta"):		# Code to parse multiple sequences using Bio Python
	o_put.write(str(record.seq)+"\t"+"1"+"\n")								# Positive sequence output
	
for record in SeqIO.parse("data\\negative_training.fasta", "fasta"):		# Code to parse multiple sequences using Bio Python
	o_put.write(str(record.seq)+"\t"+"0"+"\n")								# Negative sequence output

o_put.close()