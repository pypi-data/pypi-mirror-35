import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='nochi',
    version='0.0.3',
    author='Nochi Zajac',
    author_email='nochizajac@gmail.com',
    description='Programmes created by me',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NochiZajac/programmes',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
