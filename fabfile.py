from fabric.api import local, task


@task
def db():
    local('heroku pg:reset DATABASE_URL --confirm sleepy-wave-2913')
    local('heroku run python manage.py syncdb --noinput')
    local('heroku run python manage.py migrate')
    local('heroku run python manage.py filldb')


@task
def update():
    local('git push heroku master')
