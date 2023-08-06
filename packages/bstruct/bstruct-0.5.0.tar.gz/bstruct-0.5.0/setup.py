# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bstruct']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'bstruct',
    'version': '0.5.0',
    'description': 'Simple and efficient binary (de)serialization using type annotations.',
    'long_description': "# bstruct\n\n[![ci](https://github.com/flxbe/bstruct/actions/workflows/ci.yml/badge.svg)](https://github.com/flxbe/bstruct/actions/workflows/ci.yml)\n[![pypi](https://img.shields.io/pypi/v/bstruct)](https://pypi.org/project/bstruct/)\n[![python](https://img.shields.io/pypi/pyversions/bstruct)](https://img.shields.io/pypi/pyversions/bstruct)\n\n<!-- start elevator-pitch -->\n\nSimple and efficient binary parsing using type annotations.\nSupports easy fallback to Python's built-in `struct` library for maximum performance.\n\n<!-- end elevator-pitch -->\n\n## Getting Started\n\n<!-- start quickstart -->\n\n```bash\npip install bstruct\n```\n\n```python\nfrom typing import Annotated\nfrom dataclasses import dataclass\n\nimport bstruct\n\n\n@dataclass\nclass Measurement:\n    timestamp: bstruct.u32  # shorthand for: Annotated[int, bstruct.Encodings.u32]\n    values: Annotated[list[bstruct.u8], bstruct.Array(3)]\n\n\nMeasurementEncoding = bstruct.derive(Measurement)\n\n\nmeasurement = Measurement(\n    timestamp=1672764049,\n    values=[1, 2, 3],\n)\n\nencoded = MeasurementEncoding.encode(measurement)\ndecoded = MeasurementEncoding.decode(encoded)\n\nassert decoded == measurement\n```\n\n<!-- end quickstart -->\n\nSee the [documentation](https://bstruct.readthedocs.io/) for more information.\n\n## Benchmarks\n\nPlease see the source of the benchmarks in the `benchmarks` directory.\nFeel free to create an issue or PR should there be a problem with the methodology.\nThe benchmarks where executed with\n[pyperf](https://github.com/psf/pyperf)\nusing Python 3.11.1 and\n[construct](https://pypi.org/project/construct/) 2.10.68\non a MacBook Pro 2018 with a 2.3GHz i5 processor.\n\n### `benchmarks/builtins.py`\n\n| Name                 | decode  | encode   |\n| -------------------- | ------- | -------- |\n| struct               | 0.54 us | 0.23 us  |\n| bstruct              | 2.51 us | 1.64 us  |\n| construct (compiled) | 9.49 us | 10.00 us |\n\n### `benchmarks/native_list.py`\n\n| Name                 | decode  | encode  |\n| -------------------- | ------- | ------- |\n| struct               | 0.17 us | 0.33 us |\n| bstruct              | 1.70 us | 0.59 us |\n| construct (compiled) | 4.04 us | 6.61 us |\n\n### `benchmarks/class_list.py`\n\n| Name                 | decode  | encode  |\n| -------------------- | ------- | ------- |\n| bstruct              | 7.37 us | 4.81 us |\n| construct (compiled) | 34.5 us | 36.6 us |\n\n### `benchmarks/nested.py`\n\n| Name                 | decode  | encode  |\n| -------------------- | ------- | ------- |\n| bstruct              | 6.05 us | 4.42 us |\n| construct (compiled) | 27.6 us | 29.5 us |\n\n## Issues and Contributing\n\nI am very happy to receive any kind of feedback or contribution.\nJust open an issue and let me know.\n",
    'author': 'flxbe',
    'author_email': 'flxbe@mailbox.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/flxbe/bstruct',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
