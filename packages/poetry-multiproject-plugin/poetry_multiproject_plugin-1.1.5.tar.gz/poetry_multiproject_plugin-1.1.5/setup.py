# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_multiproject_plugin',
 'poetry_multiproject_plugin.commands',
 'poetry_multiproject_plugin.commands.buildproject',
 'poetry_multiproject_plugin.commands.checkproject',
 'poetry_multiproject_plugin.components',
 'poetry_multiproject_plugin.components.check',
 'poetry_multiproject_plugin.components.deps',
 'poetry_multiproject_plugin.components.project',
 'poetry_multiproject_plugin.components.toml']

package_data = \
{'': ['*']}

install_requires = \
['mypy>=0.991,<0.992', 'poetry>=1.2,<2.0', 'tomlkit>=0.11.5,<0.12.0']

entry_points = \
{'poetry.application.plugin': ['poetry-multiproject-plugin = '
                               'poetry_multiproject_plugin:MultiProjectPlugin']}

setup_kwargs = {
    'name': 'poetry-multiproject-plugin',
    'version': '1.1.5',
    'description': 'A Poetry plugin that makes it possible to use relative package includes.',
    'long_description': '# Poetry Multiproject Plugin\n\nThis is a Python `Poetry` plugin, adding the `build-project` and `check-project` commands.\n\n[![CircleCI](https://dl.circleci.com/status-badge/img/gh/DavidVujic/poetry-multiproject-plugin/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/DavidVujic/poetry-multiproject-plugin/tree/main)\n\nThe `build-project` command will make it possible to use relative package includes.\nThis feature is very useful for monorepos and when sharing code between projects.\n\n\nThe `check-project` command is useful to check that dependencies are added properly in a project.\nIt uses the `MyPy` tool under the hood, and will output any errors from the static type checker.\n\n\n## Usage\nNavigate to the project folder (where the `pyproject.toml` file is).\n\nBuild a project:\n``` shell\npoetry build-project\n```\n\nCheck the code used in a project:\n\n``` shell\npoetry check-project\n```\n\nCheck the code, with a custom `MyPy` configuration to override the defaults:\n\n``` shell\npoetry check-project --config-file <PATH-TO-MYPY.INI-CONFIG-FILE>\n```\n\n## Installation\nThis plugin can be installed according to the official [Poetry docs](https://python-poetry.org/docs/plugins/#using-plugins).\n\n``` shell\npoetry self add poetry-multiproject-plugin\n```\n\n## What does it do?\n\nthe `poetry build-project` command will:\n\n1. copy the actual project into a temporary folder.\n2. collect relative includes - such as `include = "foo/bar", from = "../../shared"` -  and copy them into the temprary folder.\n3. generate a new pyproject.toml.\n4. run the `poetry build` command in the temporary folder.\n5. copy the built `dist` folder (containing the wheel and sdist) into the actual project folder.\n6. remove the temporary folder.\n\n\nthe `poetry check-project` command will:\n\n1. copy the actual project into a temporary folder.\n2. collect relative includes - such as `include = "foo/bar", from = "../../shared"` -  and copy them into the temprary folder.\n3. generate a new pyproject.toml.\n4. run `poetry install` in the temporary folder.\n5. run `poetry run mypy` in the temporary folder.\n6. remove the temporary folder.\n\n\nThe default setting for the underlying `MyPy` configuration is:\n\n``` shell\n--explicit-package-bases --namespace-packages --no-error-summary --no-color-output\n```\n\n\n## How is it different from the "poetry build" command?\nPoetry does not allow package includes outside of the __project__ root.\n\n``` shell\n# Note the structure of the shared folder: namespace/package\n\npackages = [\n    { include = "my_namespace/my_package", from = "../../shared" }\n    { include = "my_namespace/my_other_package", from = "../../shared" }\n]\n```\n\nThis plugin will allow relative package includes. You will now be able to share code between projects.\n\nAn suggested Monorepo structure, with the shared code extracted into a separate folder structure:\n\n``` shell\nprojects/\n  my_app/\n    pyproject.toml (including a shared package)\n\n  my_service/\n    pyproject.toml (including other shared packages)\n\nshared/\n  my_namespace/\n    my_package/\n      __init__.py\n      code.py\n\n    my_other_package/\n      __init__.py\n      code.py\n```\n',
    'author': 'David Vujic',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/davidvujic/poetry-multiproject-plugin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
