# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['demisto_sdk',
 'demisto_sdk.commands',
 'demisto_sdk.commands.common',
 'demisto_sdk.commands.common.content',
 'demisto_sdk.commands.common.content.objects.abstract_objects',
 'demisto_sdk.commands.common.content.objects.pack_objects',
 'demisto_sdk.commands.common.content.objects.pack_objects.abstract_pack_objects',
 'demisto_sdk.commands.common.content.objects.pack_objects.author_image',
 'demisto_sdk.commands.common.content.objects.pack_objects.change_log',
 'demisto_sdk.commands.common.content.objects.pack_objects.classifier',
 'demisto_sdk.commands.common.content.objects.pack_objects.connection',
 'demisto_sdk.commands.common.content.objects.pack_objects.contributors',
 'demisto_sdk.commands.common.content.objects.pack_objects.corrlation_rule',
 'demisto_sdk.commands.common.content.objects.pack_objects.dashboard',
 'demisto_sdk.commands.common.content.objects.pack_objects.doc_file',
 'demisto_sdk.commands.common.content.objects.pack_objects.generic_definition',
 'demisto_sdk.commands.common.content.objects.pack_objects.generic_field',
 'demisto_sdk.commands.common.content.objects.pack_objects.generic_module',
 'demisto_sdk.commands.common.content.objects.pack_objects.generic_type',
 'demisto_sdk.commands.common.content.objects.pack_objects.incident_field',
 'demisto_sdk.commands.common.content.objects.pack_objects.incident_type',
 'demisto_sdk.commands.common.content.objects.pack_objects.indicator_field',
 'demisto_sdk.commands.common.content.objects.pack_objects.indicator_type',
 'demisto_sdk.commands.common.content.objects.pack_objects.integration',
 'demisto_sdk.commands.common.content.objects.pack_objects.job',
 'demisto_sdk.commands.common.content.objects.pack_objects.layout',
 'demisto_sdk.commands.common.content.objects.pack_objects.lists',
 'demisto_sdk.commands.common.content.objects.pack_objects.modeling_rule',
 'demisto_sdk.commands.common.content.objects.pack_objects.pack_ignore',
 'demisto_sdk.commands.common.content.objects.pack_objects.pack_metadata',
 'demisto_sdk.commands.common.content.objects.pack_objects.parsing_rule',
 'demisto_sdk.commands.common.content.objects.pack_objects.playbook',
 'demisto_sdk.commands.common.content.objects.pack_objects.pre_process_rule',
 'demisto_sdk.commands.common.content.objects.pack_objects.readme',
 'demisto_sdk.commands.common.content.objects.pack_objects.release_note',
 'demisto_sdk.commands.common.content.objects.pack_objects.release_note_config',
 'demisto_sdk.commands.common.content.objects.pack_objects.report',
 'demisto_sdk.commands.common.content.objects.pack_objects.script',
 'demisto_sdk.commands.common.content.objects.pack_objects.secret_ignore',
 'demisto_sdk.commands.common.content.objects.pack_objects.tool',
 'demisto_sdk.commands.common.content.objects.pack_objects.trigger',
 'demisto_sdk.commands.common.content.objects.pack_objects.widget',
 'demisto_sdk.commands.common.content.objects.pack_objects.wizard',
 'demisto_sdk.commands.common.content.objects.pack_objects.xdrc_template',
 'demisto_sdk.commands.common.content.objects.pack_objects.xsiam_dashboard',
 'demisto_sdk.commands.common.content.objects.pack_objects.xsiam_dashboard_image',
 'demisto_sdk.commands.common.content.objects.pack_objects.xsiam_report',
 'demisto_sdk.commands.common.content.objects.pack_objects.xsiam_report_image',
 'demisto_sdk.commands.common.content.objects.root_objects',
 'demisto_sdk.commands.common.content.objects.root_objects.content_descriptor',
 'demisto_sdk.commands.common.content.objects.root_objects.documentation',
 'demisto_sdk.commands.common.content.tests',
 'demisto_sdk.commands.common.content.tests.objects.abstract_objects',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.abstract_pack_objects',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.author_image',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.change_log',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.classifier',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.connection',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.correlation_rule',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.dashboard',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.doc_file',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.incident_field',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.incident_type',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.indicator_field',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.indicator_type',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.integration',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.integration.integration_test.TestNotUnifiedIntegration',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.job',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.layout',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.lists',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.modeling_rule',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.pack_ignore',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.pack_metadata',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.parsing_rule',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.playbook',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.pre_process_rule',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.readme',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.release_note',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.release_note_config',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.report',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.script',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.script.script_test.TestNotUnifiedScript',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.secret_ignore',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.trigger',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.widget',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.wizard',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.xdrctemplate',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.xsiam_dashboard',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.xsiam_dashboard_image',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.xsiam_report',
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.xsiam_report_image',
 'demisto_sdk.commands.common.content.tests.objects.root_objects.content_descriptor',
 'demisto_sdk.commands.common.content.tests.objects.root_objects.documentation',
 'demisto_sdk.commands.common.handlers',
 'demisto_sdk.commands.common.handlers.json',
 'demisto_sdk.commands.common.handlers.tests',
 'demisto_sdk.commands.common.handlers.yaml',
 'demisto_sdk.commands.common.hook_validations',
 'demisto_sdk.commands.common.tests',
 'demisto_sdk.commands.content_graph',
 'demisto_sdk.commands.content_graph.interface',
 'demisto_sdk.commands.content_graph.interface.neo4j',
 'demisto_sdk.commands.content_graph.interface.neo4j.queries',
 'demisto_sdk.commands.content_graph.objects',
 'demisto_sdk.commands.content_graph.parsers',
 'demisto_sdk.commands.content_graph.tests',
 'demisto_sdk.commands.convert',
 'demisto_sdk.commands.convert.converters',
 'demisto_sdk.commands.convert.converters.classifier',
 'demisto_sdk.commands.convert.converters.classifier.tests',
 'demisto_sdk.commands.convert.converters.layout',
 'demisto_sdk.commands.convert.converters.layout.tests',
 'demisto_sdk.commands.convert.converters.layout.tests.test_data',
 'demisto_sdk.commands.convert.converters.tests',
 'demisto_sdk.commands.convert.tests',
 'demisto_sdk.commands.coverage_analyze',
 'demisto_sdk.commands.coverage_analyze.tests',
 'demisto_sdk.commands.create_artifacts',
 'demisto_sdk.commands.create_artifacts.tests',
 'demisto_sdk.commands.create_artifacts.tests.data.common_server',
 'demisto_sdk.commands.create_id_set',
 'demisto_sdk.commands.create_id_set.tests',
 'demisto_sdk.commands.create_id_set.tests.test_data',
 'demisto_sdk.commands.doc_reviewer',
 'demisto_sdk.commands.doc_reviewer.tests',
 'demisto_sdk.commands.download',
 'demisto_sdk.commands.download.tests',
 'demisto_sdk.commands.download.tests.tests_env.content.Packs.TestPack.Integrations.TestIntegration',
 'demisto_sdk.commands.download.tests.tests_env.content.Packs.TestPack.Scripts.TestScript',
 'demisto_sdk.commands.download.tests_backup.tests_env.content.Packs.TestPack.Integrations.TestIntegration',
 'demisto_sdk.commands.download.tests_backup.tests_env.content.Packs.TestPack.Scripts.TestScript',
 'demisto_sdk.commands.error_code_info',
 'demisto_sdk.commands.error_code_info.tests',
 'demisto_sdk.commands.find_dependencies',
 'demisto_sdk.commands.find_dependencies.tests',
 'demisto_sdk.commands.format',
 'demisto_sdk.commands.format.tests',
 'demisto_sdk.commands.generate_docs',
 'demisto_sdk.commands.generate_docs.tests',
 'demisto_sdk.commands.generate_integration',
 'demisto_sdk.commands.generate_integration.tests',
 'demisto_sdk.commands.generate_integration.tests.test_files.VirusTotalTest',
 'demisto_sdk.commands.generate_outputs',
 'demisto_sdk.commands.generate_outputs.generate_context',
 'demisto_sdk.commands.generate_outputs.generate_context.tests',
 'demisto_sdk.commands.generate_outputs.generate_descriptions',
 'demisto_sdk.commands.generate_outputs.generate_descriptions.tests',
 'demisto_sdk.commands.generate_outputs.json_to_outputs',
 'demisto_sdk.commands.generate_outputs.json_to_outputs.tests',
 'demisto_sdk.commands.generate_test_playbook',
 'demisto_sdk.commands.generate_test_playbook.tests',
 'demisto_sdk.commands.generate_unit_tests',
 'demisto_sdk.commands.generate_unit_tests.tests',
 'demisto_sdk.commands.generate_unit_tests.tests.test_files',
 'demisto_sdk.commands.generate_unit_tests.tests.test_files.inputs',
 'demisto_sdk.commands.generate_unit_tests.tests.test_files.outputs',
 'demisto_sdk.commands.generate_yml_from_python',
 'demisto_sdk.commands.generate_yml_from_python.tests',
 'demisto_sdk.commands.init',
 'demisto_sdk.commands.init.templates.BaseIntegration',
 'demisto_sdk.commands.init.templates.BaseScript',
 'demisto_sdk.commands.init.templates.FeedHelloWorld',
 'demisto_sdk.commands.init.templates.HelloIAMWorld',
 'demisto_sdk.commands.init.templates.HelloWorld',
 'demisto_sdk.commands.init.templates.HelloWorldScript',
 'demisto_sdk.commands.init.templates.HelloWorldSlim',
 'demisto_sdk.commands.init.tests',
 'demisto_sdk.commands.integration_diff',
 'demisto_sdk.commands.integration_diff.tests',
 'demisto_sdk.commands.lint',
 'demisto_sdk.commands.lint.resources.pylint_plugins',
 'demisto_sdk.commands.lint.tests',
 'demisto_sdk.commands.lint.tests.test_linter',
 'demisto_sdk.commands.lint.tests.test_pylint_plugin',
 'demisto_sdk.commands.openapi_codegen',
 'demisto_sdk.commands.openapi_codegen.tests',
 'demisto_sdk.commands.postman_codegen',
 'demisto_sdk.commands.postman_codegen.tests',
 'demisto_sdk.commands.prepare_content',
 'demisto_sdk.commands.prepare_content.preparers',
 'demisto_sdk.commands.prepare_content.tests',
 'demisto_sdk.commands.run_cmd',
 'demisto_sdk.commands.run_cmd.tests',
 'demisto_sdk.commands.run_playbook',
 'demisto_sdk.commands.run_test_playbook',
 'demisto_sdk.commands.run_test_playbook.tests',
 'demisto_sdk.commands.secrets',
 'demisto_sdk.commands.secrets.tests',
 'demisto_sdk.commands.split',
 'demisto_sdk.commands.split.tests',
 'demisto_sdk.commands.test_content',
 'demisto_sdk.commands.test_content.test_modeling_rule',
 'demisto_sdk.commands.test_content.test_modeling_rule.tests',
 'demisto_sdk.commands.test_content.tests',
 'demisto_sdk.commands.test_content.xsiam_tools',
 'demisto_sdk.commands.update_release_notes',
 'demisto_sdk.commands.update_release_notes.tests',
 'demisto_sdk.commands.update_xsoar_config_file',
 'demisto_sdk.commands.update_xsoar_config_file.tests',
 'demisto_sdk.commands.upload',
 'demisto_sdk.commands.upload.tests',
 'demisto_sdk.commands.validate',
 'demisto_sdk.commands.validate.tests',
 'demisto_sdk.commands.zip_packs',
 'demisto_sdk.commands.zip_packs.tests',
 'demisto_sdk.utils',
 'demisto_sdk.utils.circle-ci']

package_data = \
{'': ['*'],
 'demisto_sdk.commands.common': ['schemas/*'],
 'demisto_sdk.commands.common.content': ['docs/*'],
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.classifier': ['classifier_test/*'],
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.indicator_type': ['indicator_type_test/*'],
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.integration': ['integration_test/TestUnifiedIntegration/*'],
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.job': ['job_test/Jobs/*'],
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.layout': ['layout_test/*'],
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.script': ['script_test/TestUnifiedScript/*'],
 'demisto_sdk.commands.common.content.tests.objects.pack_objects.wizard': ['wizard_test/Wizards/*'],
 'demisto_sdk.commands.common.tests': ['test_files/*'],
 'demisto_sdk.commands.content_graph': ['images/*'],
 'demisto_sdk.commands.content_graph.tests': ['test_data/*',
                                              'test_data/mock_import_files_multiple_repos__valid/*'],
 'demisto_sdk.commands.convert.converters.classifier.tests': ['test_data/*'],
 'demisto_sdk.commands.coverage_analyze.tests': ['data/*',
                                                 'data/coverage_data_files/*'],
 'demisto_sdk.commands.create_artifacts.tests': ['data/*'],
 'demisto_sdk.commands.download': ['tests_backup/tests_data/custom_content/*',
                                   'tests_backup/tests_env/content/Packs/TestPack/Layouts/*',
                                   'tests_backup/tests_env/content/Packs/TestPack/Playbooks/*'],
 'demisto_sdk.commands.download.tests': ['tests_data/custom_content/*',
                                         'tests_env/content/Packs/TestPack/Layouts/*',
                                         'tests_env/content/Packs/TestPack/Playbooks/*'],
 'demisto_sdk.commands.generate_docs.tests': ['test_files/*'],
 'demisto_sdk.commands.generate_integration.tests': ['test_files/*'],
 'demisto_sdk.commands.generate_outputs.generate_context.tests': ['test_data/*'],
 'demisto_sdk.commands.generate_outputs.generate_descriptions.tests': ['test_data/*'],
 'demisto_sdk.commands.init.templates.BaseScript': ['test_data/*'],
 'demisto_sdk.commands.init.templates.FeedHelloWorld': ['test_data/*'],
 'demisto_sdk.commands.init.templates.HelloWorld': ['test_data/*'],
 'demisto_sdk.commands.init.templates.HelloWorldSlim': ['test_data/*'],
 'demisto_sdk.commands.init.tests': ['RN/*', 'RN_ENTITY/*', 'test_files/*'],
 'demisto_sdk.commands.lint': ['resources/installation_scripts/*',
                               'resources/pipfile_python2/*',
                               'resources/pipfile_python3/*'],
 'demisto_sdk.commands.openapi_codegen': ['resources/*'],
 'demisto_sdk.commands.postman_codegen': ['resources/*'],
 'demisto_sdk.commands.postman_codegen.tests': ['test_files/*'],
 'demisto_sdk.commands.run_cmd.tests': ['test_data/*'],
 'demisto_sdk.commands.test_content.test_modeling_rule.tests': ['test_data/*'],
 'demisto_sdk.commands.update_release_notes': ['tests_data/*',
                                               'tests_data/Packs/Test/*',
                                               'tests_data/Packs/release_notes/*'],
 'demisto_sdk.commands.upload.tests': ['data/*']}

install_requires = \
['GitPython>=3.1.27,<4.0.0',
 'Jinja2>=3.1.1,<4.0.0',
 'MarkupSafe>=2.1.1,<3.0.0',
 'Pebble>=4.6.3,<6.0.0',
 'PyPDF2>=1.28.6,<2.0.0',
 'autopep8>=1.6.0,<2.0.0',
 'bandit>=1.7.4,<2.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'chardet>=4,<6',
 'click>=8.0.0,<9.0.0',
 'colorama>=0.4.4,<0.5.0',
 'coloredlogs>=15.0.1,<16.0.0',
 'configparser>=5.2.0,<6.0.0',
 'coverage==6.3.2',
 'cryptography>=36.0.2,<37.0.0',
 'dateparser>=1.1.1,<2.0.0',
 'decorator>=5.1.1,<6.0.0',
 'demisto-py>=3.2.5,<4.0.0',
 'dictdiffer>=0.9.0,<0.10.0',
 'dictor>=0.1.9,<0.2.0',
 'docker>=5.0.3,<6.0.0',
 'flake8>=4.0.1,<5.0.0',
 'flatten-dict>=0.4.2,<0.5.0',
 'gitdb>=4.0.9,<5.0.0',
 'giturlparse>=0.10.0,<0.11.0',
 'google-cloud-storage>=2.2.1,<3.0.0',
 'imagesize>=1.3.0,<2.0.0',
 'importlib-resources>=5.6.0,<6.0.0',
 'inflection>=0.5.1,<0.6.0',
 'isort>=5.10.1,<6.0.0',
 'jsonschema>=4.4.0,<5.0.0',
 'klara>=0.6.3,<0.7.0',
 'mergedeep>=1.3.4,<2.0.0',
 'mypy>=0.982,<0.983',
 'neo4j>=4.4.8,<5.0.0',
 'networkx>=2.7.1,<3.0.0',
 'nltk>=3.7,<4.0',
 'ordered-set>=4.1.0,<5.0.0',
 'orjson>=3.8.3,<4.0.0',
 'packaging<22',
 'paramiko>=2.11.0,<3.0.0',
 'pipenv>=2022.3.28,<2023.0.0',
 'prettytable>=3.2.0,<4.0.0',
 'pydantic>=1.9.2,<2.0.0',
 'pykwalify>=1.8.0,<2.0.0',
 'pylint==2.12.2',
 'pyspellchecker>=0.6.3,<0.7.0',
 'pytest-freezegun>=0.4.2,<0.5.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'requests>=2.27.1,<3.0.0',
 'ruamel.yaml>=0.17.21,<0.18.0',
 'slackclient>=2.9.3,<3.0.0',
 'tabulate>=0.8.9,<0.10.0',
 'typed-ast>=1.5.2,<2.0.0',
 'typer[all]>=0.6.1,<0.7.0',
 'types-Markdown>=3.3.21,<4.0.0',
 'types-PyMySQL>=1.0.15,<2.0.0',
 'types-PyYAML>=6.0.5,<7.0.0',
 'types-chardet>=4.0.3,<6.0.0',
 'types-dateparser>=1.1.0,<2.0.0',
 'types-decorator>=5.1.8,<6.0.0',
 'types-emoji>=1.2.7,<3.0.0',
 'types-filelock>=3.2.5,<4.0.0',
 'types-futures>=3.3.8,<4.0.0',
 'types-ipaddress>=1.0.8,<2.0.0',
 'types-mock>=4.0.15,<5.0.0',
 'types-paramiko>=2.8.17,<3.0.0',
 'types-pkg-resources>=0.1.3,<0.2.0',
 'types-protobuf>=3.19.15,<4.0.0',
 'types-python-dateutil>=2.8.10,<3.0.0',
 'types-pytz>=2021.3.6,<2023.0.0',
 'types-pyvmomi>=7.0.6,<9.0.0',
 'types-requests==2.28.11',
 'types-setuptools>=65.6.0.1,<66.0.0.0',
 'types-six>=1.16.12,<2.0.0',
 'types-tabulate>=0.8.6,<0.10.0',
 'types-ujson>=5.6.0.0,<6.0.0.0',
 'typing-extensions>=4.1.1,<5.0.0',
 'ujson>=5.1.0,<6.0.0',
 'urllib3>=1.26.9,<2.0.0',
 'vulture>=2.3,<3.0',
 'wcmatch>=8.3,<9.0',
 'yamlordereddictloader>=0.4.0,<0.5.0']

extras_require = \
{'build': ['gsutil==5.17']}

entry_points = \
{'console_scripts': ['demisto-sdk = demisto_sdk.__main__:main']}

setup_kwargs = {
    'name': 'demisto-sdk',
    'version': '1.8.2',
    'description': '"A Python library for the Demisto SDK"',
    'long_description': '# Demisto SDK\n\n[![PyPI version](https://badge.fury.io/py/demisto-sdk.svg)](https://badge.fury.io/py/demisto-sdk)\n[![CircleCI](https://circleci.com/gh/demisto/demisto-sdk/tree/master.svg?style=svg)](https://circleci.com/gh/demisto/demisto-sdk/tree/master)\n[![Coverage Status](https://coveralls.io/repos/github/demisto/demisto-sdk/badge.svg?branch=master)](https://coveralls.io/github/demisto/demisto-sdk?branch=master)\n\nThe Demisto SDK library can be used to manage your Cortex XSOAR content with ease and efficiency.\nThe library uses python 3.8+.\n\n## Usage\n\n### Installation\n\n1. **Install** - `pip3 install demisto-sdk`\n2. **Upgrade** - `pip3 install --upgrade demisto-sdk`\n3. **Connect demisto-sdk with Cortex XSOAR server** - In order that demisto-sdk and Cortex XSOAR server communicate, perfrom the following steps:\n\n   1. Get an API key for Cortex XSOAR/XSIAM-server - `Settings` -> `Integrations` -> `API keys` -> `Get your Key` (copy it)\n   2. Add the following parameters to your environment. You can also use a [.env file](https://pypi.org/project/python-dotenv/), the demisto-sdk will automatically load that file.:\n\n      ```bash\n      export DEMISTO_BASE_URL=<http or https>://<demisto-server url or ip>:<port>\n      export DEMISTO_API_KEY=<API key>\n      ```\n      To use on Cortex XSIAM the `XSIAM_AUTH_ID` environment variable should also be set.\n      ```bash\n      export XSIAM_AUTH_ID=<auth id>\n      ```\n\n      for example:\n      ```bash\n      export DEMISTO_BASE_URL=http://127.0.0.1:8080\n      export DEMISTO_API_KEY=XXXXXXXXXXXXXXXXXXXXXX\n      ```\n      As long as `XSIAM_AUTH_ID` environment variable is set, SDK commands will be configured to work with an XSIAM instance.\n      In order to set Demisto SDK to work with Cortex XSOAR instance, you need to delete the XSIAM_AUTH_ID parameter from your environment.\n      ```bash\n      unset XSIAM_AUTH_ID\n      ```\n\n      >For more configurations, check the [demisto-py](https://github.com/demisto/demisto-py) repo (the SDK uses demisto-py to communicate with Cortex XSOAR).\n\n   3. For the **Validate** and **Format** commands to work properly:\n     - Install node.js, and make sure `@mdx-js/mdx`, `fs-extra` and `commander` are installed in node-modules folder (`npm install ...`).\n     - Set the `DEMISTO_README_VALIDATION` environment variable to True.\n\n       MDX is used to validate markdown files, and make sure they render properly on XSOAR and [xsoar.pan.dev](https://xsoar.pan.dev).\n\n   4. Reload your terminal.\n\n---\n\n### Content path\n\nThe **demisto-sdk** is made to work with Cortex content, structured similar to the [official Cortex content repo](https://github.com/demisto/content).\n\nDemisto-SDK commands work best when called from the content directory or any of its subfolders.\nTo run Demisto-SDK commands from other folders, you may set the `DEMISTO_SDK_CONTENT_PATH` environment variable.\n\nWe recommend running all demisto-SDK commands from a folder with a git repo, or any of its subfolders. To suppress warnings about running commands outside of a content repo folder, set the `DEMISTO_SDK_IGNORE_CONTENT_WARNING` environment variable.\n\n### CLI usage\n\nYou can use the SDK in the CLI as follows:\n\n```bash\ndemisto-sdk <command> <args>\n```\n\nFor more information, run `demisto-sdk -h`.\nFor more information on a specific command execute `demisto-sdk <command> -h`.\n\n### Version Check\n\n`demisto-sdk` will check against the GitHub repository releases for a new version every time it runs and will issue a warning if you are not using the latest and greatest. If you wish to skip this check you can set the environment variable: `DEMISTO_SDK_SKIP_VERSION_CHECK`. For example:\n\n```bash\nexport DEMISTO_SDK_SKIP_VERSION_CHECK=yes\n```\n\n---\n\n## Commands\n\nSupported commands:\n\n1. [init](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md)\n1. [Validate](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md)\n1. [Lint](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/lint/README.md)\n1. [Secrets](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/secrets/README.md)\n2. [Unify](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/prepare_content/README.md#Unify)\n3. [Prepare-Content](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/prepare_content/README.md#prepare-content)\n4. [Split](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/split/README.md)\n5. [Format](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/format/README.md)\n6. [Run](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/run_cmd/README.md)\n7. [Run-playbook](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/run_playbook/README.md)\n8. [Upload](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/upload/README.md)\n9. [Download](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/download/README.md)\n10. [Generate-docs](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/generate_docs/README.md)\n11. [Generate-test-playbook](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/generate_test_playbook/README.md)\n12. [Generate-outputs](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/generate_outputs/README.md)\n13. [Update-release-notes](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/update_release_notes/README.md)\n14. [Zip-packs](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/zip_packs/README.md)\n15. [openapi-codegen](https://xsoar.pan.dev/docs/integrations/openapi-codegen)\n16. [postman-codegen](https://xsoar.pan.dev/docs/integrations/postman-codegen)\n17. [generate-integration](https://xsoar.pan.dev/docs/integrations/code-generator)\n18. [generate-yml-from-python](https://xsoar.pan.dev/docs/integrations/yml-from-python-code-gen)\n---\n\n### Customizable command configuration\n\nYou can create your own configuration for the `demisto-sdk` commands by creating a file named `.demisto-sdk-conf` within the directory from which you run the commands.\nThis file will enable you to set a default value to the existing command flags that will take effect whenever the command is run.\nThis can be done by entering the following structure into the file:\n\n```INI\n[command_name]\nflag_name=flag_default_value\n```\n\nNote: Make sure to use the flag\'s full name and input `_` instead of a `-` if it exists in the flag name (e.g. instead of `no-docker-checks` use `no_docker_checks`).\n\nHere are a few examples:\n\n- As a user, I would like to not use the `mypy` linter in my environment when using the `lint` command. In the `.demisto-sdk-conf` file I\'ll enter:\n\n ```INI\n[lint]\nno_mypy=true\n```\n\n- As a user, I would like to include untracked git files in my validation when running the `validate` command. In the `.demisto-sdk-conf` file I\'ll enter:\n\n```INI\n[validate]\ninclude_untracked=true\n```\n\n- As a user, I would like to automatically use minor version changes when running the `update-release-notes` command. In the `.demisto-sdk-conf` file I\'ll enter:\n\n```INI\n[update-release-notes]\nupdate_type=minor\n```\n\n---\n\n### Autocomplete\n\nOur CLI supports autocomplete for Linux/MacOS machines, you can turn this feature on by running one of the following:\nfor zsh users run in the terminal\n\n```bash\neval "$(_DEMISTO_SDK_COMPLETE=source_zsh demisto-sdk)"\n```\n\nfor regular bashrc users run in the terminal\n\n```bash\neval "$(_DEMISTO_SDK_COMPLETE=source demisto-sdk)"\n```\n\n---\n\n## License\n\nMIT - See [LICENSE](LICENSE) for more information.\n\n---\n\n## How to setup development environment?\n\nFollow the guide found [here](CONTRIBUTION.md#2-install-demisto-sdk-dev-environment) to setup your `demisto-sdk` dev environment.\nThe development environment is connected to the branch you are currently using in the SDK repository.\n\n---\n\n## Contributions\n\nContributions are welcome and appreciated.\nFor information regarding contributing, press [here](CONTRIBUTION.md).\nFor release guide, press [here](docs/release_guide.md)\n',
    'author': 'Demisto',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
