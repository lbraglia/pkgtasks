from invoke import task


@task
def updatetools(c):
    """
    Update software for package management.
    """
    c.run("pip install --upgrade --user pip hatch build twine flake8 mypy sphinx bandit")


@task
def create(c, pkg):
    """
    Create a new project using hatch.
    """
    c.run(f"hatch new {pkg}")
    c.run(f"cd {pkg} && mkdir docs && cd docs && sphinx-quickstart")


@task
def doc(c, pkg):
    """
    Refresh package doc using sphinx.
    """
    c.run(f"cd {pkg} && sphinx-apidoc -f src/{pkg}/ -o docs")


@task
def test(c, pkg):
    """
    Run package tests using hatch and pytest.
    """
    c.run(f"cd {pkg} && hatch test")


@task
def flake8(c, pkg):
    """
    Run flake8.
    """
    c.run(f"cd {pkg} && flake8 .")


@task
def bandit(c, pkg):
    """
    Run bandit.
    """
    c.run(f"cd {pkg} && bandit -r .")
    

@task
def mypy(c, pkg):
    """
    Run mypy.
    """
    c.run(f"cd {pkg} && mypy .")


@task
def black(c, pkg):
    """
    Run black.
    """
    c.run(f"cd {pkg} && black --line-length 79 .")


@task
def ruff(c, pkg):
    """
    Run ruff.
    """
    c.run(f"cd {pkg} && ruff check")
    

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
    c.run(f"python3 -m pip install --upgrade {pkg}")    


@task
def build(c, pkg):
    """
    Build package sdist and wheel.
    """
    c.run(f"python3 -m build {pkg}")


@task
def upload(c, pkg):
    """
    Upload pkg to pypi.
    """
    c.run(f"cd {pkg} && rm -rf dist/*")
    c.run(f"cd {pkg} && python3 -m build")
    c.run(f"cd {pkg} && python3 -m twine upload dist/* --verbose")


@task
def streamlitrun(c, pkg):
    """
    Run streamlit app locally.
    """
    c.run(f"cd {pkg} && streamlit run streamlit_app.py")

    
@task
def completion(c):
    """
    Refresh ~/.invoke-completion.sh.
    """
    c.run("invoke --print-completion-script bash > ~/.invoke-completion.sh")


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
   
