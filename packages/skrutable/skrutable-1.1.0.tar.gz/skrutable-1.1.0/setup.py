from setuptools import setup, find_packages


setup(
    name='skrutable',
    version='1.1.0',
    description="skrutable library for working with Sanskrit text",
    license='CC BY-SA 4.0',
    author="Tyler Neill",
    author_email='tyler.g.neill@gmail.com',
    packages=find_packages(),
    url='https://github.com/tylergneill/skrutable',
    keywords='Sanskrit text transliteration scansion meter identification sandhi compound splitting',
    install_requires=[
          'numpy',
      ],

)