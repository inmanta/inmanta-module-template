"""
    This script has as purpose to create the Python package name and the 
    'Inmanta module name' using the module name inputed by the user (or the default module name).
    The Python package name uses the same naming convention as standard Python packages: 
    all lowercase and words separated by "-".
    The 'Inmanta module name' (which is also the name of the Python module name) uses "_" to separate
    words and can have uppercase letters except for the first letter which is always lowercase.

"""

{{ cookiecutter.update({"package_name": "inmanta-module-" + cookiecutter.module_name.lower().replace("_","-") }) }}
{{ cookiecutter.update({"inmanta_module_name": (cookiecutter.module_name[0].lower() + cookiecutter.module_name[1:]).replace("-","_") }) }}