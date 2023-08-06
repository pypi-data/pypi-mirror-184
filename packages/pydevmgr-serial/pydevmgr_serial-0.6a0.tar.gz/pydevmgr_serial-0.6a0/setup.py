# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydevmgr_serial']

package_data = \
{'': ['*']}

install_requires = \
['pydevmgr-core==0.6.a0', 'pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'pydevmgr-serial',
    'version': '0.6a0',
    'description': 'based pydevmgr object for serial communication',
    'long_description': 'An pydevmgr_core extension for serial communication \n\n\n\nSources are [here](https://github.com/efisoft-elt/pydevmgr_serial) \n\nDoc to comme\n\n\n# Install\n\n```bash\n> pip install pydevmgr_serial \n```\n\n# Basic Usage\n\nBellow is an exemple of implementation of a node that check a value from a Tesla Sensor. \nAn extra configuration argument is added and the fget method is implemented. \n\n```python \nfrom pydevmgr_serial import BaseSerialNode\nimport time\n\n    \nclass TesaNode(BaseSerialNode):\n    class Config:\n        delay: float = 0.1\n        \n    def fget(self):\n        self.serial.write(b\'?\\r\')\n        time.sleep(self.config.delay)\n        sval = self.serial.read(20)\n        val = float(sval)\n        return val\n```\n\nyou can simply use the node with a Serial object :\n\n```python \nfrom serial import Serial \n\n# build a standalone node \ncom = Serial(port=\'COM1\', baudrate=9600)\ntesa = TesaNode(com=com)\n\nprint( "Position is ", tesa.get() )\ncom.close()\n\n```\n\nOne can include the node in a serial device which will hold the communcation\n\nNote: One creating a SerialDevice the port is not directly opened one needs to use\nthe ``connect`` method or within a with statement. \n\n\n```python \nfrom pydevmgr_serial import SerialDevice\nfrom pydevmgr_core import nodealias\n\n\n\nclass Tesa(SerialDevice):    \n    raw_pos = TesaNode.Config()\n    \n    @nodealias(\'raw_pos\')\n    def position(self, raw_pos):\n        return 10 + 1.3 * raw_pos    \n```\n\n```python \ntesa = Tesa(\'tesa\',  port =\'COM1\', baudrate=9600)\n\nwith tesa:\n    tesa.position.get()\n```\n\n\n\n',
    'author': 'Sylvain Guieu',
    'author_email': 'sylvain.guieu@univ-grenoble-alpes.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
