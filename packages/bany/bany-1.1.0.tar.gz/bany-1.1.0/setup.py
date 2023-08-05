# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bany',
 'bany.cmd',
 'bany.cmd.extract',
 'bany.cmd.extract.extractors',
 'bany.cmd.solve',
 'bany.cmd.solve.network',
 'bany.cmd.solve.solvers',
 'bany.core',
 'bany.ynab']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'diskcache>=5.4.0,<6.0.0',
 'networkx>=2.8.8,<3.0.0',
 'oauthlib>=3.2.2,<4.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pdfplumber>=0.7.6,<0.8.0',
 'py-moneyed>=3.0,<4.0',
 'pydantic>=1.10.4,<2.0.0',
 'pytest>=7.2.0,<8.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0',
 'responses>=0.22.0,<0.23.0',
 'rich>=13.0.0,<14.0.0',
 'scipy>=1.10.0,<2.0.0']

entry_points = \
{'console_scripts': ['bany = bany.__main__:main']}

setup_kwargs = {
    'name': 'bany',
    'version': '1.1.0',
    'description': '',
    'long_description': "# BANY\n\nA collection of scripts I've created to aid with budgeting using YNAB\n\n# Setup\n\n```bash\npyenv local 3.11.1\npipx install bany --python $(which python)\nbany --help\n```\n\n# Commands\n\n## `bany extract`\n\nCreate YNAB transactions from a PDF\n\n### Examples\n\n- Run the extact command to parse a PDF and upload transactions to YNAB\n\n```bash\nbany extract pdf --inp /path/to/pdf --config config.yaml\nbany extract pdf --inp /path/to/pdf --config config.yaml --upload\n```\n\n### `config.yaml`\n\n- Define rules to match patterns in the text of a PDF\n- Define the transactions to create from these matches\n\n```yaml\n# Regular Expressions defined for date like values\ndates:\n  Force Date:\n    value: |-\n      2023-01-01\n\n  Check Date:\n    regex: |-\n      Check\\s+Date\\s+(?P<DATE>{MONTHS}\\s+\\d+,?\\s+\\d\\d\\d\\d)\n\n# Regular Expressions defined for money like values\namounts:\n  401K:\n    group: EARNINGS\n    inflow: true\n    regex: |-\n      401K\\s+\n      (?P<HOURS>{NUMBER})\\s+\n      (?P<MONEY>{AMOUNT})\\s+\n      (?P<TOTAL>{AMOUNT})\n\n  Salary:\n    group: EARNINGS\n    inflow: true\n    regex: |-\n      REGULAR\\s+\n      (?P<RATES>{NUMBER})\\s+\n      (?P<HOURS>{NUMBER})\\s+\n      (?P<MONEY>{AMOUNT})\\s+\n      (?P<TOTAL>{AMOUNT})\n\n  TOTAL-EARNINGS:\n    group: EARNINGS\n    inflow: true\n    total: true\n    regex: |-\n      Gross\\s+Earnings\\s+\n      (?P<HOURS>{NUMBER})\\s+\n      (?P<MONEY>{AMOUNT})\\s+\n      (?P<TOTAL>{AMOUNT})\n\n# Transactions to push to a YNAB budget (these may reference the matches defined above)\ntransactions:\n- budget: 2023\n  account: 'Checking'\n  category: 'Internal Master Category: Inflow: Ready to Assign'\n  payee: Company\n  color: red\n  amount: Salary\n  date: Check Date\n\n- budget: 2023\n  account: 'Company'\n  category: 'Investment: Fidelity'\n  payee: 'Transfer : Fidelity : Syapse'\n  memo: 2023\n  color: yellow\n  amount: 401K\n  date: Check Date\n\n```\n\n## `bany solve`\n\nThis is a script to solve a math problem.\n\n- I have a few investment funds and want them each to have a certain percent of my savings.\n- I need to know which funds to put the money in to reach my desired allocation.\n\n> We have a histogram and want to morph it into a new shape\n\n  1)  Given a set of labeled buckets with known item counts...\n  2)  Given a new amount of items to place into the buckets...\n  3)  Given a desired distribution of items for the buckets...\n\nHow should we place the new items into the buckets?\n\n### Examples\n\n```bash\n# The problem will be solved in an unconstrained way by default\n# Values can be added or removed from existing bins\nbany solve unconstrained --config allocate.yaml\n\n# The problem can be solved in a constrained way as well\n# Values can only be added to bins\nbany solve constrained --config allocate.yaml\n\n# A Monte Carlo based solver also exists, which is non-deterministic\n# Values can be added in fixed sizes\nbany solve montecarlo --config allocate.yaml --stepsize 25\n```\n\n#### Input Distribution\n\n```bash\nTOTAL     level=[0] current_value=[ 6,000.00] optimal_ratio=[1.000] amount_to_add=[ 8,000.00]\n ├─VIGAX  level=[1] current_value=[ 1,000.00] optimal_ratio=[0.220] amount_to_add=[     0.00]\n ├─VVIAX  level=[1] current_value=[ 1,000.00] optimal_ratio=[0.280] amount_to_add=[     0.00]\n ├─VMGMX  level=[1] current_value=[ 1,000.00] optimal_ratio=[0.100] amount_to_add=[     0.00]\n ├─VMVAX  level=[1] current_value=[ 1,000.00] optimal_ratio=[0.150] amount_to_add=[     0.00]\n ├─VSGAX  level=[1] current_value=[ 1,000.00] optimal_ratio=[0.100] amount_to_add=[     0.00]\n └─VSIAX  level=[1] current_value=[ 1,000.00] optimal_ratio=[0.150] amount_to_add=[     0.00]\n```\n\n#### Output Distribution\n\n```bash\nTOTAL     level=[0] results_value=[14,000.00] results_ratio=[1.000] amount_to_add=[     0.00]\n ├─VIGAX  level=[1] results_value=[ 3,080.00] results_ratio=[0.220] amount_to_add=[ 2,080.00]\n ├─VVIAX  level=[1] results_value=[ 3,920.00] results_ratio=[0.280] amount_to_add=[ 2,920.00]\n ├─VMGMX  level=[1] results_value=[ 1,400.00] results_ratio=[0.100] amount_to_add=[   400.00]\n ├─VMVAX  level=[1] results_value=[ 2,100.00] results_ratio=[0.150] amount_to_add=[ 1,100.00]\n ├─VSGAX  level=[1] results_value=[ 1,400.00] results_ratio=[0.100] amount_to_add=[   400.00]\n └─VSIAX  level=[1] results_value=[ 2,100.00] results_ratio=[0.150] amount_to_add=[ 1,100.00]\n```\n\n### `config.yaml`\n\nThe input is a hierarchy of bins with current values and desired ratios.\n\n##### yaml\n\nThe input can be given as a YAML file.\n\n```yaml\n- { label: 'TOTAL', optimal_ratio: 100, current_value: 6000, amount_to_add: 8000, children: [\n    'VIGAX', 'VVIAX', 'VMGMX', 'VMVAX', 'VSGAX', 'VSIAX'] }\n- { label: 'VIGAX', optimal_ratio:  22, current_value: 1000, amount_to_add:    0, children: [] }\n- { label: 'VVIAX', optimal_ratio:  28, current_value: 1000, amount_to_add:    0, children: [] }\n- { label: 'VMGMX', optimal_ratio:  10, current_value: 1000, amount_to_add:    0, children: [] }\n- { label: 'VMVAX', optimal_ratio:  15, current_value: 1000, amount_to_add:    0, children: [] }\n- { label: 'VSGAX', optimal_ratio:  10, current_value: 1000, amount_to_add:    0, children: [] }\n- { label: 'VSIAX', optimal_ratio:  15, current_value: 1000, amount_to_add:    0, children: [] }\n```\n\nYou can use regular expressions when specifying the children of a category.\n\n```yaml\n- { label: 'TOTAL', optimal_ratio: 100, current_value: 6000, amount_to_add: 8000, children: ['regex::.*'] }\n...\n```\n\n##### csv\n\nThe input can be given as a CSV file.\n\n```csv\n   label  optimal_ratio  current_value  amount_to_add                             children\n0  TOTAL          100.0         6000.0         8000.0  VIGAX;VVIAX;VMGMX;VMVAX;VSGAX;VSIAX\n1  VIGAX           22.0         1000.0            0.0\n2  VVIAX           28.0         1000.0            0.0\n3  VMGMX           10.0         1000.0            0.0\n4  VMVAX           15.0         1000.0            0.0\n5  VSGAX           10.0         1000.0            0.0\n6  VSIAX           15.0         1000.0            0.0\n```\n",
    'author': 'Adam Gagorik',
    'author_email': 'adam.gagorik@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<3.12',
}


setup(**setup_kwargs)
