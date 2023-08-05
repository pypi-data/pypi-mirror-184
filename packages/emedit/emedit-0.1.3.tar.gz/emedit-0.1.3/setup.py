# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emedit',
 'emedit.behaviour',
 'emedit.behaviour.pipeline_components',
 'emedit.behaviour.pipeline_components.a01_gather',
 'emedit.behaviour.pipeline_components.a02_split',
 'emedit.behaviour.pipeline_components.a03_process',
 'emedit.behaviour.pipeline_components.a03_process.edit',
 'emedit.behaviour.pipeline_components.a03_process.search',
 'emedit.behaviour.pipeline_components.a04_combine',
 'emedit.behaviour.pipeline_components.a05_save',
 'emedit.behaviour.pipelines',
 'emedit.cli',
 'emedit.structures']

package_data = \
{'': ['*']}

install_requires = \
['delegatefn>=0.3.4,<0.4.0', 'openai>=0.25.0,<0.26.0', 'rich>=13.0.0,<14.0.0']

entry_points = \
{'console_scripts': ['emedit = emedit.cli:main']}

setup_kwargs = {
    'name': 'emedit',
    'version': '0.1.3',
    'description': '',
    'long_description': '# emedit\n\n`emedit` is a command line tool for performing semantic searches on text files. You specify a search query and a list of text files to search, and `emedit` returns a list of text segments ranked by their similarity to the query.\n\n## Installation\n\nInstall `emedit` using `pip`:\n\n```bash\npip install emedit\n```\n\nThis will install `emedit` and its dependencies, including `openai`. You will also need to set the `OPENAI_API_KEY` environment variable to your OpenAI API key if you haven\'t already done so.\n\n## Usage\n\nTo use `emedit`, run the following command:\n\n```bash\nemedit search "search query" file1.txt file2.txt ...\n```\nYou can also specify the following optional arguments:\n\n\n- `--order`: the order in which the results should be displayed (ascending or descending by similarity score). Default: `ascending`.\n\n- `--top-n`: the number of top results to display. Default: `3`.\n\n- `--threshold`: a similarity threshold below which results should be filtered out. Default: `0.0`.\n\n- `--frament_lines`: the target fragment length in number of lines. Default: `10`.\n\n- `--min_fragment_lines`: the minimum fragment length in number of lines. Default: `0`.\n\nYou can also use wildcards to specify a pattern of files to search in. Here\'s an example of how you can use the `**` wildcard to search for Python files in all directories in the current directory and its subdirectories:\n\n```bash\nemedit search "query" **/*.py\n```\n\nBear in mind that the behavior of the `*` and `**` wildcards may vary depending on your operating system and the terminal shell you\'re using.\n\n## Contributing\n\nIf you find a bug or want to contribute to the development of `emedit`, you can create a new issue or submit a pull request.\n\n## License\n\n`emedit` is released under the MIT license. Do whatever you want with it.',
    'author': 'IsaacBreen',
    'author_email': 'mail@isaacbreen.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
