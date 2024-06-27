import click
import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Unix101.settings")
django.setup()

from commands.models import Command

@click.group()
def cli():
    """Personal Unix Command Management System CLI"""
    pass

@cli.command()
@click.option('--name', prompt='Command name', help='The name of the command.')
@click.option('--description', prompt='Command description', help='The description of the command.')
@click.option('--category', prompt='Command category', help='The category of the command.')
def add(name, description, category):
    """Add a new command"""
    command = Command(name=name, description=description, category=category)
    command.save()
    click.echo(f'Command "{name}" added successfully.')

@cli.command()
def list():
    """List all commands"""
    commands = Command.objects.all()
    for command in commands:
        click.echo(f"Name: {command.name}, Description: {command.description}, Category: {command.category}")

@cli.command()
@click.argument('name')
@click.argument('description')
@click.argument('category')
def update(name, description,category):
    """Update a command's description or category"""
    try:
        command = Command.objects.get(name=name)
        command.description = description
        command.category=category
        command.save()
        click.echo(f'Command "{name}" updated successfully.')
    except Command.DoesNotExist:
        click.echo(f'Command "{name}" not found.')

@cli.command()
@click.argument('name')
def delete(name):
    """Delete a command by name"""
    try:
        command = Command.objects.get(name=name)
        command.delete()
        click.echo(f'Command "{name}" deleted successfully.')
    except Command.DoesNotExist:
        click.echo(f'Command "{name}" not found.')

@cli.command()
@click.argument('name')
def favourite(name):
    """Mark a command as favorite"""
    try:
        command = Command.objects.get(name=name)
        command.favourite = True
        command.save()
        click.echo(f'Command "{name}" marked as favorite.')
    except Command.DoesNotExist:
        click.echo(f'Command "{name}" not found.')

@cli.command()
@click.option('--keyword', prompt='Search keyword', help='The keyword to search for commands.')
def search_command(keyword):
    """Search for commands by keyword."""
    commands = Command.objects.filter(name__icontains=keyword) | Command.objects.filter(description__icontains=keyword)
    for command in commands:
        click.echo(f"Name: {command.name}, Description: {command.description}, Category: {command.category}")

if __name__ == '__main__':
    cli()
