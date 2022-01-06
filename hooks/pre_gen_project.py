{{ cookiecutter.update({"package_name": "inmanta-module-"+cookiecutter.module_name.lower().replace("_","-") }) }}
{{ cookiecutter.update({"inmanta_module_name": (cookiecutter.module_name[0].lower()+cookiecutter.module_name[1:]).replace("-","_") }) }}

print("===========================")
print("module name: {{ cookiecutter.inmanta_module_name }}")
print("Python package name: {{ cookiecutter.package_name }}")