"""
    This script has as purpose to create the 'Inmanta module name' using 
    the module name input (or the default module name).
    The 'Inmanta module name' (which is also the name of the Python module name) uses "_" to separate
    words and can have uppercase letters except for the first letter which is always lowercase.
"""
{{ cookiecutter.update({"inmanta_module_name": (cookiecutter.module_name[0].lower() + cookiecutter.module_name[1:]).replace("-","_") }) }}
