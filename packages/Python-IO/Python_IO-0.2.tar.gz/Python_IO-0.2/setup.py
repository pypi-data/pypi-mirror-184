from setuptools import setup, find_packages


setup(
    name='Python_IO',
    description='This is my short discription.',
    long_description='Long description',
    version='0.2',
    license='GNU',
    author="Ben G",
    author_email='formal.software@outlook.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/BenjaminTGa/Python_IO',
    keywords=['python', 'GUI', 'I/O', 'Input', 'Output'],
    install_requires=['customtkinter', 'PIL', 'requests']
)