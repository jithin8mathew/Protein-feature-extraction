from setuptools import setup

README_MD = ''
with open('README.md') as f:
    README_RST = f.read()

INSTALL_REQUIRES = [
    'pandas', 'biopython'
]

setup(
    name='discere',
    description="Protein Feature Extraction package for Machine Learning",
    long_description=README_MD,
    author="Jithin Mathew",
    author_email="jithinjm1995@gmail.com",
    version='0.0.1',
    url='https://github.com/jithin8mathew/Protein-feature-extraction',
    license="MIT",
    packages=['discere'],
    install_requires=INSTALL_REQUIRES,
    setup_requires=INSTALL_REQUIRES,
    platforms=['any'],
    keywords='feature extraction protein sequence bioinformatics machine learning deep learning',
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
