from invoke import task

@task
def update_toolchain(c):
    '''
    update software for package management
    '''
    c.run("pip install --upgrade --user pip hatch build twine")

@task
def setup(c):
    '''
    setup these tasks in the parent directory
    '''
    c.run("cd .. && ln -s pkgtasks/tasks.py")
    
@task    
def create(c, pkg):
    '''
    create a new project using hatch
    '''
    c.run("hatch new {0}".format(pkg))
    c.run("cd {0} && mkdir docs && cd docs && sphinx-quickstart".format(pkg))

@task
def doc(c, pkg):
    '''
    refresh package doc using sphinx
    '''
    c.run("cd {0} && sphinx-apidoc -f src/{1}/ -o docs".format(pkg, pkg))

@task
def test(c, pkg):
    '''
    run package tests using hatch and pytest
    '''
    c.run("cd {0} && hatch run test".format(pkg))
    
@task
def build(c, pkg):
    '''
    build package sdist and wheel
    '''
    c.run("python3 -m build {0}".format(pkg))

@task
def upload(c, pkg):
    '''
    upload pkg to pypi
    '''
    pass
