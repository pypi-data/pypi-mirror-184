from setuptools import setup

setup(
    name='sinaToolsPyPip',
    version='0.4',
    description='A simple Python package',
    url='https://github.com/TymaaHammouda/sina-portal-code/blob/main/parser.py',
    author='Tymaa Hammouda',
    author_email='tymaahasanain@gmail.com',
    license='MIT',
    packages=['sinaToolsPyPip'],
    install_requires=[
        'regex==2021.4.4',
        'numpy>=1.15',
        'pandas>=0.23'
    ],
    zip_safe=False
)
