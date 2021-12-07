#! /usr/bin/env sh

# don't abort cookiecutter if git is not installed or not configured properly (i.e. no email address configured)
git init || true
git add . || true
git commit -m "initial commit: cookiecutter template" || true
