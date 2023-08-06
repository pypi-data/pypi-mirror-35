from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup_args = dict(
    name='dnz',
    version='0.1.0',
    author='Marc Ford',
    url='https://github.com/mfdeux/dnz',
    description='Client for determining domains/subdomains.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'click',
        'tldextract',
        'requests',
        'dnspython'
    ],
    entry_points={
        'console_scripts': ['dnz=dnz.cli:cli'],
    }
)

setup(**setup_args)
