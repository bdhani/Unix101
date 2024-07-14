from django.db import migrations

def load_initial_data(apps, schema_editor):
    Command = apps.get_model('commands', 'Command')
    initial_commands = [
        {"name": "ls", "alias": "list", "description": "List directory contents", "category": "File Management", "favour": True},
        {"name": "cp", "alias": "copy", "description": "Copy files and directories", "category": "File Management", "favour": False},
        {"name": "mv", "alias": "move", "description": "Move or rename files and directories", "category": "File Management", "favour": False},
        {"name": "rm", "alias": "remove", "description": "Remove files or directories", "category": "File Management", "favour": False},
        {"name": "cd", "alias": "chdir", "description": "Change the current directory", "category": "Navigation", "favour": False},
        {"name": "mkdir", "alias": "makedir", "description": "Create new directories", "category": "File Management", "favour": False},
        {"name": "rmdir", "alias": "removedir", "description": "Remove empty directories", "category": "File Management", "favour": False},
        {"name": "grep", "alias": "search", "description": "Search text using patterns", "category": "Text Processing", "favour": False},
        {"name": "find", "alias": "searchfiles", "description": "Search for files in a directory hierarchy", "category": "File Management", "favour": False},
        {"name": "touch", "alias": "create newfile", "description": "Change file timestamps or create empty files", "category": "File Management", "favour": False},
        {"name": "cat", "alias": "concat", "description": "Concatenate and display file content", "category": "Text Processing", "favour": False},
        {"name": "echo", "alias": "print", "description": "Display a line of text", "category": "Text Processing", "favour": False},
        {"name": "head", "alias": "firstpart", "description": "Output the first part of files", "category": "Text Processing", "favour": False},
        {"name": "tail", "alias": "lastpart", "description": "Output the last part of files", "category": "Text Processing", "favour": False},
        {"name": "chmod", "alias": "permissions", "description": "Change file modes or Access Control Lists", "category": "File Management", "favour": False},
        {"name": "chown", "alias": "ownership", "description": "Change file owner and group", "category": "File Management", "favour": False},
        {"name": "ps", "alias": "processes", "description": "Report a snapshot of current processes", "category": "Process Management", "favour": False},
        {"name": "kill", "alias": "terminate", "description": "Send a signal to a process", "category": "Process Management", "favour": False},
        {"name": "ping", "alias": "checknet", "description": "Send ICMP ECHO_REQUEST to network hosts", "category": "Network", "favour": False},
        {"name": "wget", "alias": "download", "description": "Retrieve files from the web", "category": "Network", "favour": False},
        {"name": "pwd", "alias": "", "description": "Print current directory path", "category": "System", "favour": False},
    ]
    for command in initial_commands:
        Command.objects.update_or_create(name=command['name'], defaults=command)

class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0001_initial'),  
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
