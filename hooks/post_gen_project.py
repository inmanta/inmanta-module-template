"""
This script will make sure that:
1. We don't leak any internal configuration files (non-sensitive but potentially confusing)
    to external users.
2. The repo is initialized with git
"""
import os
import subprocess


# if the module is not generated for inmanta internal users, remove some unnecessary files
REMOVE_PATHS = [
    '{% if cookiecutter.author_email != "code@inmanta.com" %}.ci-integration-tests.yml{% endif %}',
    '{% if cookiecutter.author_email != "code@inmanta.com" %}.github/pull_request_template.md{% endif %}',
    '{% if cookiecutter.author_email != "code@inmanta.com" %}.gitlab/merge_request_templates{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)

# don't abort cookiecutter if git is not installed or not configured properly (i.e. no email address configured)
subprocess.check_call("git init || true", shell=True)
subprocess.check_call("git add . || true", shell=True)
subprocess.check_call("git commit -m 'initial commit: cookiecutter template' || true", shell=True)
