from setuptools import setup, find_packages


setup(
    name='weightedmodels',
    version='1.0.7',
    license='',
    author="AbdelRahman Yaghi",
    author_email='abd20200355@std.psut.edu.jo',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/AbdelRahmanYaghi/WeightedModels/edit/main/README.md',
    keywords='Weighted models',
    install_requires=[
          'scikit-learn',
      ],

)