from invoke import task
import os

@task
def updatetools(c):
    """
    Update software for package management.
    """
    c.run("pip install --upgrade --user pip hatch uv ruff pandas-stubs mypy pytest")


@task
def test(c, pkg):
    """
    Run package tests using pytest.
    """
    c.run(f"cd {pkg} && pytest")


@task
def check(c, pkg):
    """
    Run mypy.
    """
    os.system(f"cd {pkg} && mypy . | less")


@task
def lint(c, pkg):
    """
    Run ruff.
    """
    os.system(f"cd {pkg} && ruff check | less")


@task
def install(c, pkg):
    """
    Install package from local source in editable mode.
    """
    c.run(f"cd {pkg} && pip install -e .")


@task
def installpypi(c, pkg):
    """
    Install package from pypi.
    """
    c.run(f"python3 -m pip install -U --upgrade {pkg}")    


@task
def build(c, pkg):
    """
    Build package sdist and wheel.
    """
    c.run(f"uv build {pkg}")


@task
def upload(c, pkg):
    """
    Upload pkg to pypi.
    """
    c.run(f"cd {pkg} && rm -rf dist/*")
    c.run(f"cd {pkg} && uv build .")
    # c.run(f"cd {pkg} && python3 -m twine upload dist/* --verbose")
    c.run(f"cd {pkg} && uv publish dist/* --verbose")


@task
def streamlitrun(c, pkg):
    """
    Run streamlit app locally.
    """
    c.run(f"cd {pkg} && streamlit run streamlit_app.py")

    
@task
def list(c):
    """
    List invoke tasks.
    """
    c.run("invoke -l")


@task
def help(c):
    """
    Invoke's help.
    """
    c.run("invoke -h") 


@task
def create(c, pkg):
    """
    Create a new library/package.
    """
    c.run(f"uv init --lib {pkg}")


# @task
# def doc(c, pkg):
#     """
#     Refresh package doc using sphinx.
#     """
#     c.run(f"cd {pkg} && sphinx-apidoc -f src/{pkg}/ -o docs")


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
