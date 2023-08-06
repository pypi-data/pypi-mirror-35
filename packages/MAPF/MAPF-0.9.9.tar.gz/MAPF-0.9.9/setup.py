from setuptools import setup, find_packages

setup(
    name='MAPF',
    version='0.9.9',
    description='An experimental image format written in Python.',
    url='https://github.com/olokelo/MAPF',
    author='olokelo',
    author_email='olokelo@gmail.com',
    license='MIT',
    classifiers=[
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: System :: Archiving :: Compression',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='MAPF',
    packages=['MAPF',],
    install_requires=['numpy', 'Pillow', 'bitstruct'],
)
