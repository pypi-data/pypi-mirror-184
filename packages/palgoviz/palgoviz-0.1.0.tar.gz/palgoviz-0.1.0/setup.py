# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['palgoviz']

package_data = \
{'': ['*']}

install_requires = \
['graphviz>=0.20.1,<0.21.0',
 'more-itertools>=9.0.0,<10.0.0',
 'sympy>=1.11.1,<2.0.0']

setup_kwargs = {
    'name': 'palgoviz',
    'version': '0.1.0',
    'description': 'Materials for Python and algorithms, with visualization',
    'long_description': '<!-- SPDX-License-Identifier: 0BSD -->\n\n<a href="https://github.com/EliahKagan/palgoviz">\n  <img src="https://raw.githubusercontent.com/EliahKagan/palgoviz/main/doc/example.svg"\n       alt="Drawing of a nested tuple structure, made using palgoviz.object_graph"\n       title="Drawing of a nested tuple structure, made using palgoviz.object_graph"\n       width="350px">\n</a>\n\n# palgoviz - Materials for Python and algorithms, with visualization\n\n*palgoviz* is a project to develop approaches and materials for teaching and\nlearning Python together with algorithms and data structures, with a\nsubstantial component of visualization.\n\n**This package is not most of palgoviz.** Most users of palgoviz should clone\n[**the palgoviz GitHub repository**](https://github.com/EliahKagan/palgoviz)\ninstead. That page includes instructions. You most likely will *not* want to\ninstall palgoviz with `pip` or have it as a dependency of another project, but\nit is for those rather special situations that this PyPI package exists.\n\nBecause of palgoviz’s educational nature, its unit tests and Jupyter notebooks\nare important in most uses. This package omits them, as well as most\ndocumentation. Furthermore, the main use for palgoviz, as detailed further in\nthe repository readme, is as a source of exercises (which may require\nmodification for your needs) or of ideas for them. In that use, installing this\nvery limited palgoviz package does not help at all.\n\nDepending on the direction of the project, it is possible that, in the future,\nmore reasons to install palgoviz as a library will arise. For now, that is a\nniche use, and [the palgoviz GitHub\nrepository](https://github.com/EliahKagan/palgoviz) is the recommended way to\nread about, and obtain, palgoviz.\n\n*[palgoviz is licensed under\n**0BSD**](https://github.com/EliahKagan/palgoviz/blob/main/LICENSE), a\n“public-domain equivalent” license.*\n',
    'author': 'David Vassallo',
    'author_email': 'vassallo.davidm@gmail.com',
    'maintainer': 'Eliah Kagan',
    'maintainer_email': 'degeneracypressure@gmail.com',
    'url': 'https://github.com/EliahKagan/palgoviz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<3.12',
}


setup(**setup_kwargs)
