import setuptools

setuptools.setup(
    name='gerrymetrics',
    version='0.1',
    packages=setuptools.find_packages(),
    description='Lots of metrics for quantifying gerrymandering',
    author='Princeton Gerrymandering Project',
    author_email='wtadler@princeton.edu',
    license='GNU General Public License v3.0',
    long_description='''
Code for running 16 different metrics for measuring partisan gerrymandering, including:
- Mean-median difference
- Equal vote weight
- Lopsided margins (two-sample t-test on win margins)
- Bootstrap (Monte Carlo) simulation1
- Declination variants
- Declination
- Declination (buffered)
- Declination variant
- Declination variant (buffered)
- Efficiency gap variants
- Efficiency gap
- Difference gap
- Loss gap
- Surplus gap
- Vote-centric gap
- Vote-centric gap 2
- Tau gap
- Partisan bias
''',
    install_requires=['pandas', 'numpy', 'scipy', 'matplotlib', 'tqdm']
)