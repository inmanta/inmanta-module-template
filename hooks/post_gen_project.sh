#! /usr/bin/env sh

# don't abort cookiecutter if git is not installed or not configured properly (i.e. no email address configured)
git init > /dev/null || true
git add . > /dev/null || true
git commit -m "initial commit: cookiecutter template" > /dev/null && echo "Git initialized with initial commit: cookiecutter template" || true
