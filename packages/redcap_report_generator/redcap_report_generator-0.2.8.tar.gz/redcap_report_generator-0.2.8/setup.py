from setuptools import setup

setup(
    name='redcap_report_generator',
    version='0.2.8',
    scripts=['redcap_report_generate'],
    install_requires=['PyCap','python-docx','argparse']
)
