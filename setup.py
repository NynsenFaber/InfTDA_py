from setuptools import setup, find_packages

setup(
    name='inf_tda',
    version='0.1',
    description='Differentially private hierarchical queries with a Top-Down Approach, It uses the InfTDA mechanism '
                'developed by Boninsegna, Fabrizio, and Francesco Silvestri. '
                '"Differential Privacy Releasing of Hierarchical Origin/Destination Data with a TopDown Approach." '
                'arXiv preprint arXiv:2412.09256 (2024).',
    author='Fabrizio Boninsegna',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)