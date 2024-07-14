import os
import sys
import django
import typer
import subprocess
from rich.console import Console
from rich.table import Table
import platform
from typing import List

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Unix101.settings')
django.setup()
from commands.models import Command

console = Console()
app = typer.Typer()

def validate_command(command: str, alias: str = None) -> bool:
    if Command.objects.filter(name__iexact=command).exists():
        return False
    if alias and Command.objects.filter(alias__iexact=alias).exists():
        return False
    return True

@app.command(short_help="Adds a command")
def add(command: str, category: str, description: str, alias: str = None):
    if not validate_command(command, alias):
        typer.echo("Command or alias already exists.")
        raise typer.Exit(code=1)

    Command.objects.create(name=command, category=category, description=description, alias=alias)
    typer.echo(f"Added Command: {command}, Category: {category}, Description: {description}")

@app.command(short_help="Deletes a command by position")
def delete(position: int):
    commands = Command.objects.all()
    if 0 < position <= commands.count():
        cmd = commands[position - 1]
        cmd.delete()
        typer.echo(f"Deleted Command: {cmd.name}")
    else:
        typer.echo("Invalid position")

@app.command(short_help="Updates a command by position")
def update(position: int, command: str = None, category: str = None, description: str = None, alias: str = None):
    commands = Command.objects.all()
    if 0 < position <= commands.count():
        cmd = commands[position - 1]
        if command and validate_command(command, alias):
            cmd.name = command
        if category:
            cmd.category = category
        if description:
            cmd.description = description
        if alias:
            cmd.alias = alias
        cmd.save()
        typer.echo(f"Updated Command at position {position}")
    else:
        typer.echo("Invalid position")

@app.command(short_help="Shows all commands")
def show():
    console.print("[bold magenta]Commands[/bold magenta]!")
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Command", width=20)
    table.add_column("Alias", width=20)
    table.add_column("Description", min_width=12)
    table.add_column("Category", min_width=12)
    table.add_column("Favourite", min_width=8)

    commands = Command.objects.all()
    for i, cmd in enumerate(commands, 1):
        favourite = "★" if cmd.favourite else " "
        table.add_row(str(i), cmd.name, cmd.alias or "", cmd.description, cmd.category, favourite)

    console.print(table)

@app.command(short_help="Searches commands")
def search(term: str):
    results = Command.objects.filter(name__icontains=term) | Command.objects.filter(description__icontains=term) | Command.objects.filter(alias__icontains=term)
    if results:
        console.print(f"[bold magenta]Search Results for '{term}'[/bold magenta]!")
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("#", style="dim", width=6)
        table.add_column("Command", width=20)
        table.add_column("Alias", width=20)
        table.add_column("Description", min_width=12)
        table.add_column("Category", min_width=12)
        table.add_column("Favourite", min_width=8)

        commands = Command.objects.all()
        for cmd in results:
            favourite = "★" if cmd.favourite else " "
            position = list(commands).index(cmd) + 1
            table.add_row(str(position), cmd.name, cmd.alias or "", cmd.description, cmd.category, favourite)

        console.print(table)
    else:
        typer.echo(f"No commands found for search term '{term}'")

@app.command(short_help="Filters commands by category")
def filter(category: str):
    results = Command.objects.filter(category__iexact=category)
    if results:
        console.print(f"[bold magenta]Commands in Category '{category}'[/bold magenta]!")
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("#", style="dim", width=6)
        table.add_column("Command", width=20)
        table.add_column("Alias", width=20)
        table.add_column("Description", min_width=12)
        table.add_column("Category", min_width=12)
        table.add_column("Favourite", min_width=8)

        commands = Command.objects.all()
        for cmd in results:
            favourite = "★" if cmd.favourite else " "
            position = list(commands).index(cmd) + 1
            table.add_row(str(position), cmd.name, cmd.alias or "", cmd.description, cmd.category, favourite)

        console.print(table)
    else:
        typer.echo(f"No commands found in category '{category}'")

@app.command(short_help="Marks a command as favourite")
def favourite(position: int):
    commands = Command.objects.all()
    if 0 < position <= commands.count():
        cmd = commands[position - 1]
        cmd.favourite = not cmd.favourite
        cmd.save()
        state = "favourited" if cmd.favourite else "unfavourited"
        typer.echo(f"Command {cmd.name} has been {state}")
    else:
        typer.echo("Invalid position")

@app.command(short_help="Runs a command by position with arguments")
def run(position: int, args: List[str] = typer.Argument(None)):
    commands = Command.objects.all()
    if 0 < position <= commands.count():
        cmd = commands[position - 1]
        typer.echo(f"Running Command: {cmd.name}")
        full_command = f"{cmd.name} {' '.join(args)}" if args else cmd.name
        
        if platform.system() == "Windows":
            result = subprocess.run(f"powershell.exe {full_command}", shell=True, capture_output=True, text=True)
        else:
            result = subprocess.run(full_command, shell=True, capture_output=True, text=True)

        typer.echo(result.stdout)
        if result.stderr:
            typer.echo(result.stderr)
    else:
        typer.echo("Invalid position")

  

if __name__ == "__main__":
    app()
