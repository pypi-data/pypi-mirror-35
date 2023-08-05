import click
import shutil
import os
from os import environ
import subprocess
import urllib2
import re
import git
import inspect


@click.group()
def cli():
    pass


@cli.command()
@click.pass_context
def init(ctx):
    """ Initalise a new subscribie project """
    click.echo("Initalising a new subscribie project")
    # Get example .env file, rename & place it in current working directory
    click.echo("... getting example config.py file")
    response = urllib2.urlopen('https://raw.githubusercontent.com/Subscribie/subscribie/master/subscribie/config.py.example')  # noqa
    configfile = response.read()
    print "#"*80
    fullpath = os.path.join('./instance/config.py')
    with open(fullpath, 'wb') as fh:
        fh.write(configfile)

    # Create instance folder for prod
        click.echo("... creating instance folder for production use")
        try:
            shutil.rmtree('./venv/var/', ignore_errors=True)
        except Exception:
            pass
        try:
            os.makedirs('./venv/var/subscribie-instance/')
            click.echo("... creating symlink to .env file")
            os.symlink(os.getcwd() + '/.env', os.getcwd() + '/venv/var/subscribie-instance/.env')
        except Exception:
            click.echo("Warning: failed to create symlink to .env file for production use")
            pass

    # Get example jamla.yaml file, rename & place it in current working directory
    click.echo("... getting example jamla.yaml file")
    response = urllib2.urlopen('https://raw.githubusercontent.com/Subscribie/subscribie/master/subscribie/jamla.yaml.example')
    jamlafile = response.read()
    with open('jamla.yaml', 'wb') as fh:
        fh.write(jamlafile)
    # Replace static assets path
    with open('jamla.yaml', 'r+') as fh:
        jamla = fh.read()
        static_folder = ''.join([os.getcwd(), '/themes/theme-jesmond/static/'])
        jamla = re.sub(r'static_folder:.*', 'static_folder: ' + static_folder, jamla)
    os.unlink('jamla.yaml')
    # Write jamla file
    with open('jamla.yaml', 'w') as fh:
        fh.write(jamla)
    try:
        os.mkdir('themes')
    except OSError:
        click.echo("Warning: Failed to create themes directory", err=True)
    # Git clone default template
    try:
        click.echo("... cloning default template")
        git.Git('themes/').clone('https://github.com/Subscribie/theme-jesmond.git')
    except Exception as inst:
        click.echo("Warning: Failed to clone default theme. Perhaps it's already cloned?", err=True)

    # Edit .env file with correct paths
    fp = open('.env', 'a+')
    fp.write(''.join(['JAMLA_PATH="', os.getcwd(), '/', 'jamla.yaml"', "\n"]))
    fp.write(''.join(['TEMPLATE_FOLDER="', os.getcwd(), '/themes/"', "\n"]))
    fp.close()
    ctx.invoke(initdb)
    click.echo("Done")


@cli.command()
def initdb():
    """ Initalise the database """
    if os.path.isfile('data.db'):
        click.echo('Error: data.db already exists.', err=True)
        return -1

    with open('data.db', 'w'):
        click.echo('... creating data.db')
        pass
    click.echo('... running initial database creation script')
    response = urllib2.urlopen('https://raw.githubusercontent.com/Subscribie/subscribie/master/subscribie/createdb.py')
    createdb = response.read()
    exec(createdb) #TODO change all these to migrations


@cli.command()
@click.option('--DB_FULL_PATH', default='./data.db', help="Full path to data.db")
def migrate(db_full_path):
    """ Run latest migrations """
    click.echo("... running migrations")
    migrationsDir = os.path.join(os.getcwd(), 'subscribie', 'migrations')
    for root, dirs, files in os.walk(migrationsDir):
        files.sort()
        for name in files:
            migration = os.path.join(root, name)
            click.echo("... running migration: " + name)
            subprocess.call("python " + migration + ' -up -db ' + db_full_path, shell=True)


@cli.command()
@click.option('--JAMLA_PATH', default=None, help='full path to \
               jamla.yaml')
@click.option('--SECRET_KEY', default=None, help='Random key for flask \
               sessions')
@click.option('--TEMPLATE_FOLDER', default=None, help='Path to theme \
               folder')
@click.option('--STATIC_FOLDER', default=None, help='Path to static assets \
               folder')
@click.option('--UPLOADED_IMAGES_DEST', default=None, help='Path to image\
               upload folder')
@click.option('--DB_FULL_PATH', default=None, help='Path to database')
@click.option('--SUCCESS_REDIRECT_URL', \
                default=None, \
                help='Mandate complete redirect url')
@click.option('--THANKYOU_URL', default=None, \
              help='Thank you url (journey complete url)')
@click.option('--EMAIL_HOST', default=None, help='IP or hostname of email \
              server')
@click.option('--GOCARDLESS_CLIENT_ID', default=None, help='GoCardless client id \
              (not needed by default, unless doing a partner integration)')
@click.option('--GOCARDLESS_CLIENT_SECRET', default=None, help='GoCardless client \
               secret (not needed by default, unless doing partner integration')
def setconfig(jamla_path, secret_key, template_folder, static_folder, \
              uploaded_images_dest, db_full_path, success_redirect_url, \
              thankyou_url, email_host, gocardless_client_id, \
              gocardless_client_secret):
    """Updates the config.py which is stored in instance/config.py
    :param config: a dictionary 
    """
    newConfig = ''
    with open('./instance/config.py', 'r') as fh:
        for line in fh:
            frame = inspect.currentframe()
            options = inspect.getargvalues(frame).args
            for option in options:
                if option.swapcase() in line and frame.f_locals[option] is not None :
                    newValue = ''.join([option.swapcase(), '="', str(frame.f_locals[option]), '"'])
                    expr = r"^" + option.swapcase() + ".*"
                    line = re.sub(expr, newValue, line)
            newConfig = ''.join([newConfig, line])
    # Writeout new config file
    with open('./instance/config.py', 'wb') as fh:
        fh.write(newConfig)


@cli.command()
def run():
    """Run subscribie"""
    environ['FLASK_APP'] = 'subscribie'
    click.echo('Running subscribie...')
    subprocess.call("flask run", shell=True)


if __name__ == '__main__':
    cli()
