"""
nemosys-setup
"""

import setuptools

with open('README.md', 'r') as fh:
    description = fh.read()

setuptools.setup(
    name='nemosys',
    version='0.0.2',
    author='oakca',
    author_email='okan.akca@congas.net',
    packages=['nemosys'],
    description='',
    long_description=description,
    long_description_content_type='text/markdown',
    url='',
    license='MIT',
    python_requires='>=3.8',
    install_requires=[])
