# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'vendor'}

packages = \
['fb303',
 'hive_metastore',
 'pyiceberg',
 'pyiceberg.avro',
 'pyiceberg.avro.codecs',
 'pyiceberg.catalog',
 'pyiceberg.cli',
 'pyiceberg.expressions',
 'pyiceberg.io',
 'pyiceberg.table',
 'pyiceberg.utils',
 'tests',
 'tests.avro',
 'tests.catalog',
 'tests.cli',
 'tests.expressions',
 'tests.io',
 'tests.table',
 'tests.utils']

package_data = \
{'': ['*']}

modules = \
['check-license', 'Makefile', 'NOTICE']
install_requires = \
['click==8.1.3',
 'fsspec==2022.10.0',
 'mmhash3==3.0.1',
 'pydantic==1.10.2',
 'pyyaml==6.0.0',
 'requests==2.28.1',
 'rich==12.6.0',
 'zstandard==0.19.0']

extras_require = \
{'duckdb': ['pyarrow==10.0.1', 'duckdb==0.6.0'],
 'glue': ['boto3==1.24.59'],
 'hive': ['thrift==0.16.0'],
 'pyarrow': ['pyarrow==10.0.1'],
 's3fs': ['s3fs==2022.10.0'],
 'snappy': ['python-snappy==0.6.1']}

entry_points = \
{'console_scripts': ['pyiceberg = pyiceberg.cli.console:run']}

setup_kwargs = {
    'name': 'pyiceberg',
    'version': '0.2.1',
    'description': 'Apache Iceberg is an open table format for huge analytic datasets',
    'long_description': '<!--\n - Licensed to the Apache Software Foundation (ASF) under one or more\n - contributor license agreements.  See the NOTICE file distributed with\n - this work for additional information regarding copyright ownership.\n - The ASF licenses this file to You under the Apache License, Version 2.0\n - (the "License"); you may not use this file except in compliance with\n - the License.  You may obtain a copy of the License at\n -\n -   http://www.apache.org/licenses/LICENSE-2.0\n -\n - Unless required by applicable law or agreed to in writing, software\n - distributed under the License is distributed on an "AS IS" BASIS,\n - WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n - See the License for the specific language governing permissions and\n - limitations under the License.\n -->\n\n# Iceberg Python\n\npyiceberg is a python library for programmatic access to iceberg table metadata as well as to table data in iceberg format. It is a Python implementation of [iceberg table spec](https://iceberg.apache.org/spec/). Documentation is available at [https://py.iceberg.apache.org/](https://py.iceberg.apache.org/).\n\n## Getting Started\n\npyiceberg is currently in development, for development and testing purposes the best way to install the library is to perform the following steps:\n\n```\ngit clone https://github.com/apache/iceberg.git\ncd iceberg/python\npip install -e .\n```\n\n## Development\n\nDevelopment is made easy using [Poetry](https://python-poetry.org/docs/#installation). Poetry provides virtual environments for development:\n\n```bash\npoetry shell\nmake install\nmake test\n```\n\nFor more information, please refer to the [Manage environments](https://python-poetry.org/docs/managing-environments/) section of Poetry.\n\n## Testing\n\nTesting is done using Poetry:\n\n```\npoetry install -E pyarrow\npoetry run pytest\n```\n\n## Get in Touch\n\n- [Iceberg community](https://iceberg.apache.org/community/)\n',
    'author': 'Apache Software Foundation',
    'author_email': 'dev@iceberg.apache.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://iceberg.apache.org/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
