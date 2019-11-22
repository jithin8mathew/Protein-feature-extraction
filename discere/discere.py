import subprocess
import sys
from process_fasta import process_fasta
from feature_extraction import feature_extraction
system = sys.platform

# def feat_ext():
# 	print("Extracting features....")
# 	if system == 'linux':
# 		subprocess.run(['python3','feature_extraction.py'])
# 	else:
# 		subprocess.run(['python.exe','process_fasta.py'])

def extract_feature(positive, negative, outdir):
	code = process_fasta(positive, negative)
	if code is True:
		try:
			feature_extraction(outdir)
		except Exception:
			print('Failed to extract feautres... \n Code exiting with incomplete termination...')
	else:print('Error processing the fasta files !')

if __name__ == '__main__':
	extract_feature(positive, negative)
	import os
	print("Have a great day ",os.getlogin(), "!")
