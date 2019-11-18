import pytest

def test_basics(project):
    project.compile("""
    import {{cookiecutter.module_name}}
    """)

    assert project.get_stdout() == "hello world\n"
