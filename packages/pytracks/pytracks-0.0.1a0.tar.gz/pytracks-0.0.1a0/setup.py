import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'pytracks',
    version = '0.0.1a',
    author='Alexandre Fioravante de Siqueira',
    author_email = 'afdesiqueira@gmail.com',
    description = 'pytracks: Acquiring fission-tracks using image processing',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    url = 'http://github.com/alexandrejaguar/software/pytracks',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
)
