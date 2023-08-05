import setuptools

requirements = ['boto3',
 'botocore',
 'certifi',
 'chardet',
 'decorator',
 'docutils',
 'idna',
 'ipython-genutils',
 'jmespath',
 'jsonschema',
 'jupyter-core',
 'nbformat',
 'numpy',
 'pandas',
 'plotly',
 'pyarrow',
 'python-dateutil',
 'pytz',
 'requests',
 's3fs',
 's3transfer',
 'scipy',
 'six',
 'scikit-learn',
 'traitlets',
 'urllib3']

setuptools.setup(
    name="stats_comp",
    version="0.1.0",
    author="Shrey",
    author_email="shrey.anand@ymail.com",
    description="A package to explore and visualize huge data sets",
    url='https://github.com/Shreyanand/stats_comp',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    )
