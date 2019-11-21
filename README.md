[![Build Status](https://travis-ci.org/jithin8mathew/Protein-feature-extraction.svg?branch=master)](https://travis-ci.org/jithin8mathew/Protein-feature-extraction)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/jithin8mathew/Protein-feature-extraction/branch/master/graph/badge.svg)](https://codecov.io/gh/jithin8mathew/Protein-feature-extraction)
[![GitHub version](https://badge.fury.io/gh/jithin8mathew%2FProtein-feature-extraction.svg)](https://badge.fury.io/gh/jithin8mathew%2FProtein-feature-extraction)

<br>

# Protein Feature Extraction for Machine Learning
<br>

Python code to extract features from Protein sequences for Machine Learning/Deep Learning

Protein feature extraction is carried out using Biopython package

**Features inculde:
1. AA-count
2. aromaticity
3. secondary_structure_fraction
4. isoelectric_point
5. molecular_weight
6. instability_index

Packages required (other than built-in) for the execution of code...
-Pandas
-pickle
-Biopython
-subprocess

## Installation
For windows
```
pip install discere
```
For linux
```
pip3 install discere
```

## Usage

```
from discere import discere
```

Steps to run the code..
1. Add fasta file containing positive sequences with the file name "positive_training.fasta" to the "data" folder
2. Add fasta file containing negative sequences with the file name "negative_training.fasta" to the "data" folder
3. Run ML.py script*
4. The output will be saved in /data/output/ folder in three different file formats upon the successful execution of the code

*Although you could also run process_fasta.py and feature_extraction.py individually in the respective order
