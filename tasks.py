from invoke import task

@task
def update_toolchain(c):
    c.run("pip install --upgrade --user pip hatch build twine")

@task
def setup(c):
    c.run("cd .. && ln -s pkgtasks/tasks.py")
    
@task    
def create(c, pkg):
    c.run("hatch new {0}".format(pkg))

@task
def doc(c, pkg):
    c.run("cd {pkg}/doc &&")

@task
def build(c, pkg):
    c.run("python3 -m build {0}".format(pkg))

# @task
# def upload(c, pkg):
#     c.run("
