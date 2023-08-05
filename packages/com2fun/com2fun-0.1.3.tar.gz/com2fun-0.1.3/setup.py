# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['com2fun', 'com2fun.simulated_function']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.25.0,<0.26.0']

setup_kwargs = {
    'name': 'com2fun',
    'version': '0.1.3',
    'description': 'Transform document into function',
    'long_description': '# com2fun - Transform document into function.\n\nThis liabrary leverages [OpenAI API](https://github.com/openai/openai-python) to predict the output of a function based on its documentation.\n\n## Install\n\n```\npip install --upgrade com2fun\n```\n\n## Usage\n\n```\n@com2fun.com2fun\ndef top(category: str, n) -> list[str]:\n    """Return a list of top-n items in a category."""\n\nIn  [1]: top("fish", 5)\nOut [1]: [\'salmon\', \'tuna\', \'cod\', \'halibut\', \'mackerel\']\nIn  [2]: top("Pen Brand", 3)\nOut [2]: [\'Pilot\', \'Uni-ball\', \'Zebra\']\n```\n\n## Add Example\n\n```\nIn [3]: top.add_example(\'continents\', 3)([\'Asia\', \'Africa\', \'North America\'])\n```\n\n## Different Prompt Format\n\n### Python Interpreter\n\n```\nIn  [3]: pirnt(top.invoke_prompt("Pen Brand", 3))\n>>> 1\n1\n>>> def top(category: str, n) -> list[str]:\n>>>     """Return a list of top-n items in a category."""\n>>>     _top(*locals())\n>>>\n>>> top(\'continents\', 3)\n[\'Asia\', \'Africa\', \'North America\']\n>>> top(\'Pen Brand\', 3)\n\n```\n\n### Flat\n\n```\n@functools.partial(com2fun.com2fun, SF=com2fun.FlatSF)\ndef text2tex(text: str) -> str:\n    pass\n\nIn  [1]: text2tex.add_example("x divided by y")(r"\\frac{x}{y}")\nIn  [2]: print(text2tex.invoke_prompt("integrate f(x) from negative infinity to infinity"))\ndef text2tex(text: str) -> str:\n    pass\n###\n\'x divided by y\'\n---\n\\frac{x}{y}\n###\n\'integrate f(x) from negative infinity to infinity\'\n---\n\n```\n\n### Template\nThis format is inspired by [lambdaprompt](https://github.com/approximatelabs/lambdaprompt).\n\n```\nIn  [1]: text2tex = com2fun.prompt("{} into latex: ")\nIn  [2]: text2tex.add_example("x divided by y")(r"\\frac{x}{y}")\nIn  [3]: print(text2tex.invoke_prompt("integrate f(x) from negative infinity to infinity"))\nx divided by y into latex: \\frac{x}{y}\nintegrate f(x) from negative infinity to infinity into latex: \n```\n',
    'author': 'xiaoniu',
    'author_email': 'hzmxn@mail.ustc.edu.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
