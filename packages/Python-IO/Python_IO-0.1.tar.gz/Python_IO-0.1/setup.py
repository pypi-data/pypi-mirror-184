from setuptools import setup, find_packages


setup(
    name='Python_IO',
    version='0.1',
    license='GNU General Public License v3.0',
    author="Ben G",
    author_email='formal.software@outlook.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/BenjaminTGa/Python_IO',
    keywords=['python', 'GUI', 'I/O', 'Input', 'Output'],
    install_requires=[
          'customtkinter', 'tkinter', 'os', 'time', 'sys', 'PIL', 'requests', 'io'
      ],
    python_requires='>=3.6',
)