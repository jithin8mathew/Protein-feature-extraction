import subprocess
import sys

system = sys.platform

def fasta_process():
	print("Processing fasta files....")
	if system == 'linux':
		subprocess.run(['python3','process_fasta.py'])
	else:
		subprocess.run(['python.exe','process_fasta.py'])

def feat_ext():
	print("Extracting features....")
	if system == 'linux':
		subprocess.run(['python3','feature_extraction.py'])
	else:
		subprocess.run(['python.exe','process_fasta.py'])

if __name__ == '__main__':
	fasta_process()
	feat_ext()
	print("Feature extraction complete...")
	print("Extracted features are saved in data/output directory in .txt, .arff and .csv formats")
	import os
	print("Have a great day ",os.getlogin(), "!")
