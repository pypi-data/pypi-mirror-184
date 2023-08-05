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
    'version': '0.1.1',
    'description': '',
    'long_description': '# emedit\n\n`emedit` is a command line tool for performing semantic searches on a set of text files. It allows you to specify a search query and a list of text files to search, and returns a list of results ranked by their similarity to the query.\n\n## Installation\n\nInstall `emedit` using `pip`:\n\n```bash\npip install emedit\n```\n\n## Usage\n\nTo use `emedit`, run the following command and specify your search query and the list of text files you want to search:\n\n```bash\nemedit search "search query" file1.txt file2.txt ...\n```\nYou can also specify the following optional arguments:\n\n\n`--order`: the order in which the results should be displayed (ascending or descending by similarity score). Default: `ascending`.\n`--top-n`: the number of top results to display. Default: `3`.\n`--threshold`: a similarity threshold below which results should be filtered out. Default: `0.0`.\n`--frament_lines`: the target fragment length in number of lines. Default: `10`.\n`--min_fragment_lines`: the minimum fragment length in number of lines. Default: `0`.\n\n## Examples\n\nHere is an example of a search for the query "machine learning" in a set of text files:\n\n```bash\nemedit search "machine learning" file1.txt file2.txt file3.txt\nThis will display the top 3 results for the search, ranked in descending order by similarity score.\n```\n\nYou can also specify a different number of top results to display using the `--top-n` argument:\n\n```bash\nemedit search "machine learning" file1.txt file2.txt file3.txt --top-n 5\n```\n\nThis will display the top 5 results for the search.\n\nYou can also specify a different order for the results using the `--order` argument:\n\n```bash\nemedit search "machine learning" file1.txt file2.txt file3.txt --order ascending\n```\n\nThis will display the results in ascending order by similarity score.\n\nFinally, you can specify a similarity threshold to filter out results below a certain similarity score using the `--threshold` argument:\n\n```bash\nemedit search "machine learning" file1.txt file2.txt file3.txt --threshold 0.5\n```\n\nThis will only display results with a similarity score greater than or equal to 0.5.\n\n### Wildcards\n \n\nYou can lso use wildcards to specify a pattern of files to search in. Here\'s an example of how you can use the `**` wildcard to search for Python files in all directories in the current directory and its subdirectories:\n\n```bash\nemedit search "query" **/*.py\n```\n\nBear in mind that the behavior of the `*` and `**` wildcards may vary depending on your operating system and the terminal shell you\'re using.\n\n## Contributing\n\nIf you find a bug or want to contribute to the development of `emedit`, you can create a new issue or submit a pull request.\n\n## License\n\n`emedit` is released under the MIT license. Do whatever you want with it.',
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
