from setuptools import setup, find_packages


setup(
    name='moremodels',
    version='1.0.0',
    license='',
    author="AbdelRahman Yaghi",
    author_email='abd20200355@std.psut.edu.jo',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/AbdelRahmanYaghi/WeightedModels/edit/main/README.md',
    keywords='More models',
    install_requires=[
          'scikit-learn',
      ],

)