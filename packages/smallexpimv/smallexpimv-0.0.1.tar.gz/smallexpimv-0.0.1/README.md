# smallexpimv
This repository provides some Fortran routines and python wrappers to apply the imaginary exponential of a matrix (real tridiagonal or complex) to a vector. More precisely,

$$
\beta\mathrm{e}^{\pm\mathrm{i} t X} u \in\mathbb{C}^n,
$$

for a matrix $X\in\mathbb{C}^{n\times n}$, a time-step $t\in\mathbb{R}$, a scaling factor $\beta\in\mathbb{R}$, a vector $u\in\mathbb{C}^n$ and the imaginary number $\mathrm{i}^2 = -1 $. Our first routine computes this vector by an adaptive and restarted Taylor approximation. We also provide a second routine for a tridiagonal case, namely

$$
\beta\mathrm{e}^{\pm\mathrm{i} t T} e_1 \in\mathbb{C}^n,
$$

where $T\in\mathbb{R}^{n\times n}$ refers to a tridiagonal symmetric matrix and $e_1$ denotes the first unit vector, i.e., $e_1 = (1,0,\ldots,0)^\ast \in\mathbb{R}^{n}$. For the tridiagonal case, the action of the matrix exponential is computed using an eigendecomposition of $T$ via the lapack $\texttt{dstevr}$ routine.

The matrix exponentials above have some relevance for the Lanczos or Arnoldi approximations to the action of large-dimensional matrix exponentials, e.g., for time-dependent Schrödinger-type problems. In this context, $X$ or $T$ correspond to small dimensional Krylov representations of a large problem.

The main code is written in Fortran, and can be used in Python using f2py.

To generate the main python module smallexpimv.so run
> python3 -m numpy.f2py -c src/F_smallexpimv.F90 -m smallexpimv -lblas

optional, generate f2py header files:
> python3 -m numpy.f2py -h smexp.pyf -m smallexpimv src/F_smallexpimv.F90

For more user-friendly Python code which also handles working memory (most relevant when applying the matrix exponential multiple times)
we also provide the module smallexpimv_pyclass.py. Keep in mind that this module requires still the smallexpimv.so module.

makefile: run
> make test

to run the python and fortran tests, and
> make libs

to generate smallexpimv.so and smallexpimv_pyclass.pyc. To use the Makefile, first check that (in the makefile) the compiler commands and the f2py filename extension are defined correctly for your system!


python3.7 -m build --sdist
python3.7 -m twine upload --repository testpypi dist/*
python3.7 -m pip install --index-url https://test.pypi.org/simple/ --no-deps mypackagetjx

python3.7 -m pip install mypackagetjx==0.0.14 --extra-index-url=https://test.pypi.org/simple/

from mypackagetjx import onef
