# Author: Jithin Mathew # 14_11_2018
import itertools as it
import os,pickle
import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def feature_extraction(outdir):
	path_=os.getcwd()		# get the current working directory
	_=(os.path.join(path_,"data/data.txt"))		# path to input data (sequence) folder

	print('Reading data...')
	if os.path.exists(_):data=pd.read_table(_)		#read the file as Pandas DataFrame
	print('Clearing existing files...')
	try:[os.remove(filenames[0]+x) for filenames in os.walk(path_+'/data/') for x in (filenames[2])]		# remove the file if already exist
	except Exception:pass

	seq_list, cls_list=data['sequence'].tolist(), data['class'].tolist() # get the sequence and class to lists

	pth=outdir+'/'
	if not os.path.exists(pth):os.makedirs(pth)

	try:[os.remove(filenames[0]+x) for filenames in os.walk(pth) for x in (filenames[2])]		# remove the file if already exist
	except Exception:pass

	attr=open(path_+"/config/attrib","rb")
	attr=pickle.load(attr)		# load the pickle file with attribue names (for weka)
	with open(pth+"/weka_output.arff","a+") as wk: wk.write("".join('{}\n'.format(x) for x in attr))

	def format_output(aa_count,cnt):				 # write the extracted feature values to arff (weka), txt(svm) and csv file
		a=(dict(zip(it.count(), list(aa_count.values()))))
		if cnt==1:
			with open(pth+"svm_out.txt","a+")as s: s.write("+1 "+' '.join("{}:{}".format(k, v) for k, v in a.items())+"\n")
			with open(pth+"weka_output.arff","a+") as w: w.write(' '.join("{},".format(x) for x in list(aa_count.values()))+" serk\n")
			with open(pth+"tain_DL.csv","a+") as DPL: DPL.write(''.join("{},".format(x) for x in list(aa_count.values()))+str(round(aromat,3))+","+str(round(fraction[0],3))+","+str(round(fraction[1],3))+","+str(round(fraction[2],3))+","+str(round(iso,3))+","+str(mol_w)+","+str(ins)+","+str(cnt)+"\n")
		else:
			with open(path_+"svm_out.txt","a+")as s:s.write("-1 "+' '.join("{}:{}".format(k, v) for k, v in a.items())+"\n")
			with open(pth+"weka_output.arff","a+") as w: w.write(' '.join("{},".format(x) for x in list(aa_count.values()))+" loc\n")
			with open(pth+"tain_DL.csv","a+") as DPL: DPL.write(''.join("{},".format(x) for x in list(aa_count.values()))+str(round(aromat,3))+","+str(round(fraction[0],3))+","+str(round(fraction[1],3))+","+str(round(fraction[2],3))+","+str(round(iso,3))+","+str(mol_w)+","+str(ins)+","+"0"+"\n")

	for seq,cl in zip(seq_list,cls_list):		# main loop to extract the features
		_= ProteinAnalysis(seq)					# Biopython protein analysis package
		aa_count=(_.count_amino_acids())		# amino acid count
		aromat, fraction, iso=_.aromaticity(), _.secondary_structure_fraction(), _.isoelectric_point()
		try:mol_w, ins=("%0.2f" % _.molecular_weight()),("%0.2f" %_.instability_index())
		except Exception:mol_w,ins= mol_w,ins	# aromaticity, sec_strucure_fraction, iso_electric point , molecular weight, instability index
		format_output(aa_count,cl)
	print("Feature extraction complete...")
	print("Extracted features are saved in" +outdir + "/ directory in .txt, .arff and .csv formats")
