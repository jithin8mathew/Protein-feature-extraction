[![Build Status](https://travis-ci.org/jithin8mathew/Protein-feature-extraction.svg?branch=master)](https://travis-ci.org/jithin8mathew/Protein-feature-extraction)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/jithin8mathew/Protein-feature-extraction/branch/master/graph/badge.svg)](https://codecov.io/gh/jithin8mathew/Protein-feature-extraction)
[![GitHub version](https://badge.fury.io/gh/jithin8mathew%2FProtein-feature-extraction.svg)](https://badge.fury.io/gh/jithin8mathew%2FProtein-feature-extraction)
[![GitHub issues](https://img.shields.io/github/issues/jithin8mathew/Protein-feature-extraction)](https://github.com/jithin8mathew/Protein-feature-extraction/issues)
<!--[PyPI - Downloads](https://img.shields.io/pypi/dm/discere) -->
[![Downloads](https://pepy.tech/badge/discere/week)](https://pepy.tech/project/discere)
[![Downloads](https://pepy.tech/badge/discere/month)](https://pepy.tech/project/discere)
[![Downloads](https://pepy.tech/badge/discere)](https://pepy.tech/project/discere)

<br>

# Protein Feature Extraction for Machine Learning
<br>

Python code to extract features from Protein sequences for Machine Learning/Deep Learning

Protein feature extraction is carried out using Biopython package

## Features (27 features):
1. AA-count (20x features)
2. aromaticity (1x)
3. secondary_structure_fraction (3x)
4. isoelectric_point (1x)
5. molecular_weight (1x)
6. instability_index (1x)

Packages required (other than built-in) for the execution of code...
-Pandas
-pickle
-Biopython
-subprocess

### Top N features for identifying Insuliin protein sequence


![insulin best N features](https://github.com/jithin8mathew/Protein-feature-extraction/blob/master/images/insulin_bestNfeatures.jpg)
Format: ![](url)

## Installation
For windows
Windows users have to specify the path to fasta files and output folder in linux style of referencing directory using ```/``` slash rather than ```\```
eg ```C:/folder_name/file_name.fasta```
This issue will be fixed in future updates

```python 
pip install discere
```
For linux
```python
pip3 install discere
```

## Usage

```python
  import discere.discere as di
  
  di.extract_feature('./Documents/positive_training.fasta', 
                     './Documents/negative_training.fasta', 
                     './Documents')
```
di.extract_feature(input_file1, input_file2, output_directory)

## output

Outputs are stored in user_specified_path/output in .txt, .arff and .csv formats 


