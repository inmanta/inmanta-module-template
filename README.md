# Inmanta module template

A cookiecutter template to create a new V2 Inmanta module.

# Install dependencies

```bash
pip install cookiecutter
```

# Usage
Currently Modules v1 and v2 can be created using the inmanta-module-template.

 - To create a v1 module run:
```bash
cookiecutter --checkout v1 https://github.com/inmanta/inmanta-module-template.git
```

 - To create a v2 module run:
```bash
cookiecutter --checkout v2 https://github.com/inmanta/inmanta-module-template.git
```

Both commands will prompt for the template parameters.

### Parameters

| Template parameters        | Default value               | Description                                                        |
|----------------------------|-----------------------------|--------------------------------------------------------------------|
| module_name                | test_module                 | The name of the new inmanta module.                                |
| module_description         |                             | A description of the new Inmanta module.                           |
| author                     | Inmanta                     | The author to be mentioned in the project.yml file                 |
| author_email               | code@inmanta.com            | The e-mail address of the author.                                  |
| license                    | ASL 2.0                     | The License of this new Inmanta module.                            |
| copyright                  | ${year} Inmanta             | The owner of the copyright of the project.                         |
