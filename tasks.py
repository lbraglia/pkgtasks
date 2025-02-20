from invoke import task
import os

@task
def updatetools(c):
    """
    update toolchain for package management
    """
    c.run("pip install --upgrade --user pip hatch uv ruff pandas-stubs mypy pytest")


@task
def create(c, pkg):
    """
    create a new library/package
    """
    c.run(f"uv init --lib {pkg}")


@task
def test(c, pkg):
    """
    pytest
    """
    c.run(f"cd {pkg} && pytest")


@task
def check(c, pkg):
    """
    mypy
    """
    os.system(f"cd {pkg} && mypy . | less")


@task
def lint(c, pkg):
    """
    ruff
    """
    os.system(f"cd {pkg} && ruff check | less")


@task
def install(c, pkg):
    """
    install package from local source in editable mode
    """
    c.run(f"cd {pkg} && pip install -e .")


@task
def upload(c, pkg):
    """
    build and upload to PyPI
    """
    c.run(f"cd {pkg} && rm -rf dist/*")
    c.run(f"cd {pkg} && uv build .")
    c.run(f"cd {pkg} && uv publish dist/* --verbose")


@task
def streamlitrun(c, pkg):
    """
    run streamlit app locally
    """
    c.run(f"cd {pkg} && streamlit run streamlit_app.py")

    
@task
def list(c):
    """
    invoke tasks
    """
    c.run("invoke -l")


@task
def help(c):
    """
    invoke's help
    """
    c.run("invoke -h") 


# @task
# def build(c, pkg):
#     """
#     build sdist and wheel files
#     """
#     c.run(f"uv build {pkg}")


# @task
# def installpypi(c, pkg):
#     """
#     Install package from pypi.
#     """
#     c.run(f"python3 -m pip install -U --upgrade {pkg}")    


@task
def doc(c, pkg):
    """
    Refresh package doc using sphinx.
    """
    c.run(f"cd {pkg} && sphinx-apidoc -f src/{pkg}/ -o docs")


# @task
# def securitycheck(c, pkg):
#     """
#     Run bandit.
#     """
#     os.system(f"cd {pkg} && bandit -r . | less")
    

# @task
# def lint(c, pkg):
#     """
#     Run black.
#     """
#     c.run(f"cd {pkg} && black --line-length 79 .")
