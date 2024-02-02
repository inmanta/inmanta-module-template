{%- if cookiecutter.license == "ASL 2.0" -%}
"""
    Copyright {{ cookiecutter.copyright }}

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Contact: {{ cookiecutter.author_email }}
"""
{%- else -%}
"""
    :copyright: {{ cookiecutter.copyright }}
    :contact: {{ cookiecutter.author_email }}
    :license: {{ cookiecutter.license }}
"""
{%- endif %}

from pytest_inmanta.plugin import Project


def test_basics(project: Project) -> None:
    project.compile(
        """
            import {{cookiecutter.inmanta_module_name}}
        """
    )

    assert project.get_stdout() == "hello world\n"
