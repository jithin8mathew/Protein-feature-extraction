import subprocess

def fasta_process():
	print("Processing fasta files....")
	subprocess.run(['python.exe','process_fasta.py'])

def feat_ext():
	print("Extracting features....")
	subprocess.run(['python.exe','feature_extraction.py'])

if __name__ == '__main__':
	fasta_process()
	feat_ext()
	print("Feature extraction complete...")
	print("Extracted features are saved in data/output directory in .txt, .arff and .csv formats")
	import os
	print("Have a great day ",os.getlogin(), "!")
	

