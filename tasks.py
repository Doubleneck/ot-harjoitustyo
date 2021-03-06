from invoke import task

@task
def foo(ctx):
    print("toimii!")

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty = True)

@task
def test(ctx):
    ctx.run("pytest src")

@task
def build(ctx):
    ctx.run("python3 src/initialize_database.py")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task(coverage)
def lint(ctx):
    ctx.run("pylint src")    
