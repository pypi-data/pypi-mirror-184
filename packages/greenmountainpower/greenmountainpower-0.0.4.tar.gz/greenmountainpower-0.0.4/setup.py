# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['greenmountainpower']

package_data = \
{'': ['*']}

install_requires = \
['oauthlib>=3,<4', 'requests-oauthlib>=1,<2', 'requests>=2,<3']

setup_kwargs = {
    'name': 'greenmountainpower',
    'version': '0.0.4',
    'description': 'This is an unofficial Python client that uses the undocumented API for Green Mountain Power accounts.',
    'long_description': '# Green Mountain Power\n\nThis is an unofficial Python client that uses the undocumented API for Green Mountain Power accounts.\n\n## Quickstart\n\nTo start using this client, install it using pip.\n\n```sh\npip3 install greenmountainpower\n```\n\nAnd then import the client and use it to fetch usage data.\n\n```python\nimport datetime\nimport greenmountainpower\n\nprint("Collecting usage...")\n\ngmp = greenmountainpower.api.GreenMountainPowerApi(\n    account_number=58504395849, username="jsmith", password="mypassword"\n)\n\nnow = datetime.datetime.now()\none_day_ago = now - datetime.timedelta(days=1)\nusages = gmp.get_usage(\n    precision=greenmountainpower.api.UsagePrecision.HOURLY,\n    start_time=one_day_ago,\n    end_time=now,\n)\n\nfor usage in usages:\n    print(f" - Time: {usage.start_time.isoformat()}, Usage: {usage.consumed_kwh} KWH")\n\n```\n\nOutput:\n\n```\nCollecting usage...\n - Time: 2021-11-14T01:00:00, Usage: 0.27 KWH\n - Time: 2021-11-14T02:00:00, Usage: 0.22 KWH\n - Time: 2021-11-14T03:00:00, Usage: 0.24 KWH\n - Time: 2021-11-14T04:00:00, Usage: 0.25 KWH\n - Time: 2021-11-14T05:00:00, Usage: 0.26 KWH\n - Time: 2021-11-14T06:00:00, Usage: 0.26 KWH\n ...\n```\n\n## Publishing\n\nTo publish a new version, follow these steps.\n\n```sh\ngit tag <version> # ensure all changes are committed\npython3 -m build # build the package\ntwine upload --repository pypi dist/*\n```\n',
    'author': 'Kodey Converse',
    'author_email': 'kodey@conve.rs',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sbrinkerhoff/greenmountainpower/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
