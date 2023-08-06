# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['confect']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'confect',
    'version': '0.1.2',
    'description': 'Python configuration library that provides pleasant configuration definition and access interface, and it reads unrestricted python configuration file.',
    'long_description': "Confect\n=======\n\n``confect`` is a Python configuration library.\n\nIt provides a pleasant configuration definition and access interface, and it reads unrestricted python configuration file.\n\nBasic Usage\n-----------\n\nCalling ``confect.Conf()`` creates a new configuration manager object. All\nconfiguration properties resides in it. It is possible to create multiple\n``Conf`` object, but normally, one ``Conf`` object per application. Initialize\nit in some module, then import and use it anywhere in your application.\n\nPut following lines in your application package. For example, in ``your_package.__init__.py``.\n\n>>> from confect import Conf\n>>> conf = Conf()\n\nConfiguration properties should be declared with a default value and group name\nbefore using it. Default value can be any type as long as it can be deepcopy.\nGroup name shuold be a valid attribute name.\n\nPut your configuration group declaration code in the module which you need those\nproperties. And make sure that the declaration is before all lines that access\nthese properties. Normally, the group name is your class name, module name or\nsubpackage name.\n\n>>> from your_package import conf\n>>> with conf.add_group('yummy') as yummy:\n...     yummy.kind = 'seafood'\n...     yummy.name = 'fish'\n...     yummy.weight = 10\n>>> conf.yummy.name\n'fish'\n>>> conf.yummy.weight\n10\n\nConfiguration properties and groups are immutable. You can only globally change\nit by loading configuration files. Otherwise, they are always default values.\n\n>>> conf.yummy.name = 'octopus'\nTraceback (most recent call last):\n   ...\nconfect.error.FrozenConfPropError: Configuration properties are frozen.\n\nConfiguration File\n------------------\n\nUse ``Conf.load_conf_file(path)`` or ``Conf.load_conf_module(module_name)`` to\nload configuration files. No matter it is loaded before or after\ngroups/properties declaration, property values in configuration file always\noverride default values. Loading multiple files is possible, the latter one\nwould replace old values.\n\nBe aware, you should access your configuration property values after load\nconfiguration file. If not, you might get wrong/old/default value.\n\n>>> conf.load_conf_file('path/to/conf.py')\n\nThe default configuration file is in Python. That makes your configuration file\nprogrammable and unrestricted. Here's an example of configuration file.\n\n.. code-block:: python\n\n   from confect import c\n\n   c.yummy.kind = 'poultry'\n   c.yummy.name = 'chicken'\n   c.yummy.weight = 25\n\n   import os\n   c.cache.expire = 60 * 60 # one hour\n   c.cache.key = os.environ['CACHE_KEY']\n\n   DEBUG = True\n   if DEBUG:\n       c.cache.disable = True\n\nIf it's hard for you to specify the path of configuration file. You can load it\nthrough the import system of Python. Put your configuration file somewhere under\nyour package or make ``PYTHONPATH`` pointing to the directory it resides. Then\nload it with ``Conf.load_conf_module(module_name)``.\n\n.. code-block:: bash\n\n   $ edit my_conf.py\n   $ export PYTHONPATH=.\n   $ python your_application.py\n\n>>> from confect import Conf\n>>> conf = Conf()\n>>> conf.load_conf_module('my_conf')\n\nLocal Environment\n-----------------\n\n``Conf.local_env()`` context manager creates an environment that makes ``Conf``\nobject temporarily mutable. All changes would be restored when it leaves the\nblock.\n\n>>> conf = Conf()\n>>> conf.add_group('dummy', prop1=3, prop2='some string') # add group through keyword arguments\n>>> with conf.local_env():\n...     conf.dummy.prop1 = 5\n...     print(conf.dummy.prop1)\n5\n...     call_some_function_use_this_property()\n>>> print(conf.dummy.prop1)  # all configuration restored\n3\n",
    'author': '顏孜羲',
    'author_email': 'joseph.yen@gmail.com',
    'url': 'https://github.com/d2207197/confect',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
