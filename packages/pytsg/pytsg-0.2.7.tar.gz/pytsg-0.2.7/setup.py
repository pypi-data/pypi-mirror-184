# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pytsg']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23,<2.0', 'pandas>=1.4.3,<2.0.0', 'simplejpeg>=1.6.5,<2.0.0']

setup_kwargs = {
    'name': 'pytsg',
    'version': '0.2.7',
    'description': 'Library to read .tsg file package',
    'long_description': "# pytsg\n## Rationale\nThe spectral geologist (TSG) is an industry standard software for hyperspectral data analysis\nhttps://research.csiro.au/thespectralgeologist/\n\npytsg is an open source one function utility that imports the spectral geologist file package into a simple object.\n\n## Installation\nInstallation is simple\n```pip install pytsg```\n\n## Usage\n\nIf using the top level importer the data is assumed to follow this structure\n```\n\\HOLENAME\n         \\HOLEMAME_tsg.bip\n         \\HOLENAME_tsg.tsg\n         \\HOLENAME_tsg_tir.bip\n         \\HOLENAME_tsg_tir.tsg\n         \\HOLENAME_tsg_hires.dat\n         \\HOLENAME_tsg_cras.bip\n\n```\n\n```python\nfrom matplotlib import pyplot as plt\nfrom pytsg import parse_tsg\n\ndata = parse_tsg.read_package('example_data/ETG0187')\n\nplt.plot(data.nir.wavelength, data.nir.spectra[0, 0:10, :].T)\nplt.plot(data.tir.wavelength, data.tir.spectra[0, 0:10, :].T)\nplt.xlabel('Wavelength nm')\nplt.ylabel('Reflectance')\nplt.title('pytsg reads tsg files')\nplt.show()\n\n```\n\nIf you would prefer to have full control over importing individual files the following syntax is what you need\n\n```python\n\n# bip files\nnir = parse_tsg.read_tsg_bip_pair('ETG0187_tsg.tsg','ETG0187_tsg.bip','nir')\ntir = parse_tsg.read_tsg_bip_pair('ETG0187_tsg_tir.tsg','ETG0187_tsg_tir.bip','tir')\n\n# cras file\ncras = parse_tsg.read_cras('ETG0187_tsg_cras.bip')\n\n# hires dat file\nlidar = parse_tsg.read_lidar('ETG0187_tsg_hires.dat')\n\n\n```\n\n## Thanks\nThanks to CSIRO and in particular Andrew Rodger for their assistance in decoding the file structures.",
    'author': 'Ben',
    'author_email': 'ben@fractalgeoanalytics.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
