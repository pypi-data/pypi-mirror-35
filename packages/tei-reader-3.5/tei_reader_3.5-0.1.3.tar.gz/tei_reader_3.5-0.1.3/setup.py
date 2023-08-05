from setuptools import setup, find_packages

setup(
    name='tei_reader_3.5',
    python_requires='>=3.5, <3.6',
    version='0.1.3',
    description='TEI Reader',
    author='Nejc Mlakar (Department Intelligent Systems, Jozef Stefan Institute), based from Sheean Spoel (Digital Humanities Lab, Utrecht University)',
    author_email='',
    url='https://github.com/UUDigitalHumanitieslab/tei_reader',
    license='MIT',
    packages=['tei_reader', 'tei_reader.models', 'tei_reader.transform'],
    package_data={'tei_reader.transform':['*']},
    zip_safe=False,
    install_requires=['beautifulsoup4', 'lxml', 'bs4', 'six', 'astroid']
)
