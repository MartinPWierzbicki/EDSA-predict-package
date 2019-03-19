#analysepredmpw
This library was created as an example of how to publish your own package.
The package contains four recursive functions: sum_array, fibonacci, factorial and reverse
as well as three sorting functions: bubble_sort, merge_sort and quick_sort

##building this package locally
`python setup.py sdist`

##installing this package from GitHub
`pip install git+https://github.com/MartinPWierzbicki/EDSA-predict-package`


##updating this package from GitHub
`pip install --upgrade git+https://github.com/MartinPWierzbicki/EDSA-predict-package`



______________________________
usage
______________________________

After the installation, import the package into python:

import analysepredmpw as mw

To perform recursive any of the recursive functions:

sum_array:

mw.recursion.sum_array(array)

fibonacci:

mw.recursion.fibonacci(n)

factorial:

mw.recursion.factorial(n)

reverse:

mw.recursion.reverse(string)






To perform recursive any of the recursive functions:

bubble_sort:

mw.sorting.bubble_sort(list)

merge_sort:

mw.sorting.merge_sort(list)

quick_sort:

mw.sorting.quick_sort(list)
