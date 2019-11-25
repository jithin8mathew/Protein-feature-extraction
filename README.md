[![Build Status](https://travis-ci.org/jithin8mathew/Protein-feature-extraction.svg?branch=master)](https://travis-ci.org/jithin8mathew/Protein-feature-extraction)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/jithin8mathew/Protein-feature-extraction/branch/master/graph/badge.svg)](https://codecov.io/gh/jithin8mathew/Protein-feature-extraction)
[![GitHub version](https://badge.fury.io/gh/jithin8mathew%2FProtein-feature-extraction.svg)](https://badge.fury.io/gh/jithin8mathew%2FProtein-feature-extraction)
[![GitHub issues](https://img.shields.io/github/issues/jithin8mathew/Protein-feature-extraction)](https://github.com/jithin8mathew/Protein-feature-extraction/issues)

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
import discere

discere.extract_feature('positive_training.fasta', 'negative_training.fasta')

```
## output
