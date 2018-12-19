from setuptools import setup
import cir_ave

setup(
    name='cir_ave',
    description="""python package for 1D data reduction of  x-ray scattering""",
    #version=cir_ave.__version__,
    author='Jiliang Liu',
    author_email='ligerliu@gmail.com',
    license="MIT",
    url="",
    packages=['cir_ave'],
    install_requires=['numpy',
                      'scipy',
                      'matplotlib'],
    python_requires='>=3',
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='x-ray scattering',
)
