import os
import sys
import django
import npyscreen

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Ensure the settings module is configured
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Unix101.settings')
django.setup()

from commands.models import Command

class CommandApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Command Management Tool")
        self.addForm("SEARCHRESULTS", SearchResultsForm, name="Search Results")

class MainForm(npyscreen.ActionForm):
    def create(self):
        self.search_box = self.add(npyscreen.TitleText, name="Search:")
        self.filter_category = self.add(npyscreen.TitleSelectOne, max_height=4, name="Filter by Category:",
                                        values=self.get_categories(), scroll_exit=True)
        self.search_results = []

    def get_categories(self):
        return list(Command.objects.values_list('category', flat=True).distinct())

    def on_ok(self):
        search_term = self.search_box.value.lower()
        selected_category_index = self.filter_category.value

        print(f"Search term: {search_term}")
        print(f"Selected category index: {selected_category_index}")

        commands = Command.objects.all()

        if search_term:
            commands = commands.filter(name__icontains=search_term) | commands.filter(description__icontains=search_term)

        if selected_category_index is not None and len(selected_category_index) > 0:
            selected_category = self.filter_category.values[selected_category_index[0]]
            print(f"Selected category: {selected_category}")
            commands = commands.filter(category=selected_category)

        self.search_results = [f"{cmd.name} - {cmd.description}" for cmd in commands]
        print(f"Search results: {self.search_results}")

        self.parentApp.getForm("SEARCHRESULTS").result_list.values = self.search_results
        self.parentApp.switchForm("SEARCHRESULTS")

class SearchResultsForm(npyscreen.ActionForm):
    def create(self):
        self.result_list = self.add(npyscreen.MultiLineAction, name="Results", values=[], scroll_exit=True)

    def on_ok(self):
        self.parentApp.switchForm("MAIN")

    def on_cancel(self):
        self.parentApp.switchForm("MAIN")

if __name__ == "__main__":
    app = CommandApp()
    app.run()
