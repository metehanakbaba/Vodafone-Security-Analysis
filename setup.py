from setuptools import setup, find_packages

setup(
    name='vodafone_app',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyfiglet',
        'loguru'
    ],
    entry_points={
        'console_scripts': [
            'vodafone_app = vodafone_app.vodafone_app:VodafoneApp().start',
        ],
    },
    author='Your Name',
    description='A Python package for Vodafone automation.',
    keywords='vodafone automation python',
)
