from setuptools import find_packages, setup

setup(
    name='pavlova',
    version='0.1.0',
    description='Simplified deserialization using dataclasses',
    long_description=open('README.rst').read(),
    author='Freelancer.com',
    author_email='chris@freelancer.com',
    url='https://github.com/freelancer/pavlova',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    install_requires=[
        'dateparser',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Lesser '
        'General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.7',
    ]
)
