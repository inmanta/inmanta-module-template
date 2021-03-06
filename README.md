# Inmanta module template

A cookiecutter template to create a new Inmanta module.

# Install dependencies

```bash
pip install cookiecutter
```

# Usage

```bash
cookiecutter https://github.com/inmanta/inmanta-module-template.git
```

This command will prompt for the template parameters.

### Parameters

| Template parameters        | Default value               | Description                                                        |
|----------------------------|-----------------------------|--------------------------------------------------------------------|
| module_name                | test_module                 | The name of the new inmanta module.                                |
| module_description         |                             | A description of the new Inmanta module.                           |
| author                     | Inmanta                     | The author to be mentioned in the project.yml file                 |
| author_email               | code@inmanta.com            | The e-mail address of the author.                                  |
| license                    | ASL 2.0                     | The License of this new Inmanta module.                            |
| copyright                  | ${year} Inmanta             | The owner of the copyright of the project.                         |
| minimal_compiler_version   | 2019.3                      | The minimal supported compiler version.                            |
