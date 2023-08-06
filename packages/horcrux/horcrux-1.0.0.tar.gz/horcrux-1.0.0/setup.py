# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shamir', 'shamir.math', 'shamir.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'horcrux',
    'version': '1.0.0',
    'description': "Horcrux - A Python implementation of Shamir's Secret Sharing.",
    'long_description': '# Horcrux\nA Python implemntation of Shamir\'s Secret Sharing, based of Hashicorp\'s implementation for Vault.\n\n## Shamir\'s Secret Sharing\nShamir\'s Secret Sharing in an efficient algorithm for distributing private information. A secret is transformed into _shares_ from which the secret can be reassembled once a _threshold_ number are combined.\n\n## Example\n```python\nfrom shamir import combine, split\n\n\ndef hello() -> None:\n    """Split a byte-string and recombine its parts."""\n    secret: bytes = b"Hello, World!"\n    shares: int = 5\n    threshold: int = 3\n\n    parts: list[bytearray] = split(secret, shares, threshold)\n    combined: bytearray = combine(parts[:3])\n    print(combined.decode("utf-8"))\n\n\nif __name__ == "__main__":\n    hello()\n```\n',
    'author': 'Reid Hochstedler',
    'author_email': 'reidhoch@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/reidhoch/horcrux',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
