try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import versioneer

README_MD = ''
with open('README.md') as f:
    README_RST = f.read()

INSTALL_REQUIRES = [
    'pandas', 'biopython'
]
# TEST_REQUIRES = [
#     # testing and coverage
#     'pytest', 'coverage', 'pytest-cov',
#     # non-testing packagesrequired by tests, not by the package
#     'scikit-learn', 'pdutil',
#     # to be able to run `python setup.py checkdocs`
#     'collective.checkdocs', 'pygments',
# ]

setup(
    name='#############################',
    description="Protein Feature Extraction package for Machine Learning",
    long_description=README_MD,
    author="Jithin Mathew",
    author_email="jithinjm1995@gmail.com",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/jithin8mathew/Protein-feature-extraction',
    license="MIT",
    packages=['#############################'],
    install_requires=INSTALL_REQUIRES,
    # extras_require={
    #     'sklearn': ['scikit-learn', 'skutil'],
    #     'nltk': ['nltk'],
    #     'test': TEST_REQUIRES
    # },
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
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
