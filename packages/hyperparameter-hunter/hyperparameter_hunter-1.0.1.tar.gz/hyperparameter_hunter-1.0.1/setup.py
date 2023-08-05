from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='hyperparameter_hunter',
    version='1.0.1',
    description='Easy hyperparameter optimization and automatic result saving across machine learning algorithms and libraries',
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords='hyperparameter tuning optimization machine learning artificial intelligence neural network keras scikit-learn xgboost catboost lightgbm rgf',
    url='https://github.com/HunterMcGushion/hyperparameter_hunter',
    author='Hunter McGushion',
    author_email='hunter@mcgushion.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        # 'h5py',  # ?
        # 'keras',  # TODO: Move to extras_require, with 'tensorflow'?
        'numpy',
        'pandas',
        'scikit-learn',
        'scikit-optimize',
        'scipy',
        'simplejson',
        'dill',  # New
        'tensorflow==1.5.0',  # TODO: Might want to include in extras_require with 'keras'?
    ],
    extras_require={
        'docs': [
            'hyperparameter-hunter',
            'keras',
            'nbconvert',
            'nbformat'
        ],
        'ipynb': [
            'nbconvert',
            'nbformat'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Topic :: Desktop Environment :: File Managers',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
