# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ispcr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ispcr',
    'version': '0.9.1',
    'description': 'Simple in silico PCR',
    'long_description': "# ispcr\n\n[![PyPI](https://img.shields.io/pypi/v/ispcr?style=flat-square)](https://pypi.python.org/pypi/ispcr/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ispcr?style=flat-square)](https://pypi.python.org/pypi/ispcr/)\n[![PyPI - License](https://img.shields.io/pypi/l/ispcr?style=flat-square)](https://pypi.python.org/pypi/ispcr/)\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\n\n---\n\n**Documentation**: [https://pommevilla.github.io/ispcr](https://pommevilla.github.io/ispcr)\n\n**Source Code**: [https://github.com/pommevilla/ispcr](https://github.com/pommevilla/ispcr)\n\n**PyPI**: [https://pypi.org/project/ispcr/](https://pypi.org/project/ispcr/)\n\n---\n\nA simple, light-weight package written in base Python to perform *in silico* PCR to determine primer performance.\n\n**Currently in development**\n\n## Installation\n\n```sh\npip install ispcr\n```\n## Demonstration\n\n### File-based *in silico* PCR\n\nThe main function to use in this package is `get_pcr_products`, which performs *in silico* PCR using two files:\n  * `primer_file` - the path to fasta file containing your primers\n    * This is currently limited to a fasta file containing two sequences, with the forward primer coming first and the reverse primer coming second\n  * `sequence_file` the path to the fasta file containing the sequences to test your primers against\n\n`get_pcr_products` will then iterate through the sequences in `sequence_file` and find all products amplified by the forward and reverse primer.\n\n![](imgs/get_pcr_products_1.png)\n\n### Refining results\n\nYou can also refine your results by using the `min_product_length` and `max_product_length` arguments, and only print out the columns you are interested in by using the `cols` argument. For example, if we're only interested in products between 100 and 250 bp and we only want the name of the sequence the product was amplified from, the length of the product, and the start and end position of the product in the sequence:\n\n![](imgs/get_pcr_products_2.png)\n\n### Writing out isPCR results to a file\n\n`get_pcr_products` also takes an `output_file` argument. If provided, the results of the *in silico* PCR (including any product length restrictions or column selections) to that file. This will overwrite the file.\n\n![](imgs/get_pcr_products_3.png)\n\n### Sequence-based *in silico* PCR\n\nThe `get_pcr_products` function is a wrapper around `calculate_pcr_product`. The following arguments are required to run `calculate_pcr_product`:\n  * `sequence`: the target sequence to test the primers against\n  * `forward_primer`: the forward primer used to amplify the sequence\n  * `reverse_primer`: the reverse primer (5'-3') used to amplify the sequence\n\n`sequence`, `forward_primer`, and `reverse_primer` should be entered as `FastaSequence` objects. A `FastaSequence` is just a small convenience class to package a sequence with its header. An example run of `calculate_pcr_products` might look like:\n\n![](imgs/calculate_pcr_product_1.png)\n\n`calculate_pcr_product` uses all of the same arguments as `get_pcr_products`, so you can filter results and select columns just as before:\n\n![](imgs/calculate_pcr_product_2.png)\n\nThis will also work with the `output_file` argument.\n",
    'author': 'Paul Villanueva',
    'author_email': 'pvillanueva13@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pommevilla.github.io/ispcr',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
