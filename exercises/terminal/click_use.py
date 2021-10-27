#click_use.py 12Sep2021  crs,
# https://click.palletsprojects.com
# exercise click,terminal package
# Can't be run from IDLE - Use python directly
import click

click.echo('Continue? [yn] ', nl=False)
c = click.getchar()
print(c)
click.echo()
if c == 'y':
    click.echo('We will go on')
elif c == 'n':
    click.echo('Abort!')
else:
    click.echo('Invalid input :(')
