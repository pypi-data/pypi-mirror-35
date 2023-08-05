from setuptools import setup, find_packages

setup(
    name='tei_reader_3.5_test33553355',
    python_requires='>=3.4, <4',
    version='0.1.1',
    description='TEI Reader',
    author='Sheean Spoel (Digital Humanities Lab, Utrecht University) modified by Nejc Mlakar (Intelligent Systems Lab, Jozef Stefan Institute)',
    author_email='s.j.j.spoel@uu.nl',
    url='https://github.com/UUDigitalHumanitieslab/tei_reader',
    license='MIT',
    packages=['tei_reader', 'tei_reader.models', 'tei_reader.transform'],
    package_data={'tei_reader.transform':['*']},
    zip_safe=False,
    install_requires=['beautifulsoup4', 'lxml']
)
