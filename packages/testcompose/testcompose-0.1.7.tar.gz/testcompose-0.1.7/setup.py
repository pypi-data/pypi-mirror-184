# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testcompose',
 'testcompose.client',
 'testcompose.configs',
 'testcompose.containers',
 'testcompose.models',
 'testcompose.models.bootstrap',
 'testcompose.models.client',
 'testcompose.models.container',
 'testcompose.models.network',
 'testcompose.waiters']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'docker==6.0.1',
 'pydantic==1.10.2',
 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'testcompose',
    'version': '0.1.7',
    'description': 'Provide an easy way to perform integration testing with docker and python',
    'long_description': '<h1 align="center" style="font-size: 3rem; margin: -15px 0">\nTestcompose\n</h1>\n\n\n\n<p align="center" style="margin: 30px 0 10px">\n  <img width="350" height="208" src="docs/images/testcompose.png" alt=\'Testcompose\'>\n</p>\n\n<p align="center"><strong>Testcompose</strong> <em>- A clean and better way to test your Python containerized applications.</em></p>\n\n\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/testcompose)\n![PyPI - Implementation](https://img.shields.io/pypi/implementation/testcompose)\n![PyPI](https://img.shields.io/pypi/v/testcompose)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/testcompose)\n[![Tests](https://github.com/rugging24/python-testcompose/workflows/RunningTests/badge.svg)](https://github.com/rugging24/python-testcompose/blob/main/.github/workflows/tests.yaml)\n\n\n---\n**Testcompose** provides an easy way of using docker containers for functional and integration testing. It allows for combination of more than one containers and allows for interactions with these containers from your test code without having to write extra scripts for such interactions. I.e providing a docker compose kind of functionality with the extra benefit of being able to fully control the containers from test codes.\n\nThis is inspired by the [testcontainers-python](https://testcontainers-python.readthedocs.io/en/latest/index.html#) project and goes further to add a few additional functionalities to improve software integration testing while allowing the engineer to control every aspect of the test.\n\n---\n\nInstall testcompose using pip:\n\n```shell\n$ pip install testcompose\n```\n\ntestcompose requires Python 3.7+.\n\nUsing a config file. See the [Quickstart](https://github.com/rugging24/python-testcompose/blob/main/docs/quickstart.md) for other options\n\n```yaml\nservices:\n  - name: database\n    image: "postgres:13"\n    command: ""\n    environment:\n      POSTGRES_USER: postgres\n      POSTGRES_DB: postgres\n      POSTGRES_PASSWORD: password\n    exposed_ports:\n      - 5432\n    log_wait_parameters:\n      log_line_regex: "database system is ready to accept connections"\n      wait_timeout_ms: 30000\n      poll_interval_ms: 2000\n  - name: application\n    image: "python:3.9"\n    command: "/bin/bash -x /run_app.sh"\n    environment:\n      DB_URL: "${database.postgres_user}:${database.postgres_password}@${database.container_hostname}:5432/${database.postgres_db}"\n    volumes:\n      - host: "docker-test-files/run_app.sh"\n        container: "/run_app.sh"\n        mode: "ro"\n        source: "filesystem"\n      - host: "docker-test-files/app.py"\n        container: "/app.py"\n        mode: "ro"\n        source: "filesystem"\n    exposed_ports:\n      - "8000"\n    log_wait_parameters:\n      log_line_regex: ".*Application startup complete.*"\n      wait_timeout_ms: 45000\n      poll_interval_ms: 2000\n    http_wait_parameters:\n      http_port: 8000\n      response_status_code: 200\n      end_point: "/ping"\n      startup_delay_time_ms: 30000\n      use_https": false\n    depends_on:\n      - database\n```\n\nVerify it as follows:\n\n```python\nimport json\nfrom typing import Any, Dict\nfrom requests import Response, get\nfrom testcompose.configs.service_config import Config\nfrom testcompose.models.bootstrap.container_service import ContainerServices\nfrom testcompose.models.container.running_container import RunningContainer\nfrom testcompose.run_containers import RunContainers\n\nconfig_services: ContainerServices = TestConfigParser.parse_config(file_name=\'some-config.yaml\')\nrunning_config: Config = Config(test_services=config_services)\n\nwith RunContainers(\n        config_services=config_services,\n        ranked_services=running_config.ranked_config_services,\n) as runner:\n    assert runner\n    app_container_srv_name = "application"\n    app_service: RunningContainer = runner.running_containers[app_container_srv_name]\n    app_env_vars: Dict[str, Any] = app_service.config_environment_variables\n    mapped_port = app_service.generic_container.get_exposed_port("8000")\n    print(app_env_vars)\n    app_host = app_service.generic_container.get_container_host_ip()\n    assert app_env_vars\n    assert mapped_port\n    assert app_host\n    response: Response = get(url=f"http://{app_host}:{int(mapped_port)}/version")\n    assert response\n    assert response.status_code == 200\n    assert response.text\n    assert isinstance(json.loads(response.text), dict)\n```\n\n\n## Documentation\n\n[Quickstart](https://github.com/rugging24/python-testcompose/blob/main/docs/quickstart.md)\n\n[Special-Variables](https://github.com/rugging24/python-testcompose/blob/main/docs/environment_variables.md)\n\n[Full-Doc](https://rugging24.github.io/python-testcompose/)\n',
    'author': 'Olakunle Olaniyi',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
