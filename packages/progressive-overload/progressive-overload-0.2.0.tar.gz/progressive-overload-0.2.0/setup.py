from setuptools import find_packages, setup


with open('README.md') as file:
    long_description = file.read()

setup(
    name='progressive-overload',
    version='0.2.0',
    description='Calculates the next workout sets for progressive overload given previous ones.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thomasleese/progressive-overload',
    author='Thomas Leese',
    author_email='thomas@leese.io',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['progressive-overload = progressive_overload.cli:main']
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=['PyYaml'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
