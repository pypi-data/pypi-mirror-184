import inspect
import logging

import flet
from flet import (
    AlertDialog,
    Column,
    Dropdown,
    FilledButton,
    Row,
    Text,
    TextButton,
    TextField,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HackerMode:
    def __init__(self, *args, **kwargs):
        # Set up the UI layout of your Hacker Mode feature
        self.sidebar_items = Column()
        self.canvas_items = Column()
        self.toolbar_items = Row()
        self.settings_form = Column()
        self.selected_element = None
        self.settings_dialog = None
        self.canvas = Column()
        self.toolbar = Row()
        self.sidebar = Column()

        # Populate the sidebar with all the available controls, widgets, and components
        self.populate_sidebar()

    def build(self):
        # Create the sidebar
        self.sidebar = Column(
            controls=[
                Text("Sidebar"),
                self.sidebar_items,
            ]
        )

        # Create the toolbar
        self.toolbar = Row(
            controls=[
                Text("Toolbar"),
                self.toolbar_items,
            ]
        )

        # Create the canvas
        self.canvas = Column(
            controls=[
                Text("Canvas"),
                self.canvas_items,
            ]
        )

        # Create the main layout
        self.main_layout = Row(
            controls=[
                self.sidebar,
                self.canvas,
                self.toolbar,
            ]
        )

        # Return the main layout
        return self.main_layout

    def populate_sidebar(self):
        # Iterate through all the classes in the flet module and create a Text widget for each one
        for name, obj in inspect.getmembers(flet):
            if inspect.isclass(obj):
                # self.sidebar_items.append(Text(name, on_click=self.select_element))
                pass

    def select_element(self, e):
        # Set the selected element
        self.selected_element = e.text

        # Get the list of input arguments for the selected element's class
        element_class = getattr(flet, self.selected_element)
        arg_spec = inspect.getargspec(element_class)

        # Create the input fields in a Form widget
        self.settings_form = Form()
        for arg in arg_spec.args:
            self.settings_form.add(TextField(label=arg))

        # Show the Dialog widget with the Form widget
        self.settings_dialog = AlertDialog(content=self.settings_form, open=True)

    def add_element(self, e):
        # Create a new instance of the selected element with the user-specified settings
        element_class = getattr(flet, self.selected_element)
        element_args = {}
        for field in self.settings_form.fields:
            element_args[field.label] = field.value
        element = element_class(**element_args)

        # Determine the position of the element in the canvas based on the user-specified value
        position = int(self.settings_form.fields[-1].value)

        # Insert the element at the specified position in the canvas_items column
        self.canvas_items.insert(position, element)

    def update_element(self, e):
        # Update the selected element's properties based on the user-specified settings
        for field in self.settings_form.fields:
            setattr(self.selected_element, field.label, field.value)

        # Determine the new position of the element in the canvas based on the user-specified value
        position = int(self.settings_form.fields[-1].value)

        # Remove the element from the canvas_items column and reinsert it at the specified position
        self.canvas_items.remove(self.selected_element)
        self.canvas_items.insert(position, self.selected_element)

    def element_options(self, e):
        # Returns a list of option value for Dropdown widgets
        return [str(i) for i in range(len(self.canvas_items))]

    def save_composition(self, e):
        # Generate the Python code for the elements in the canvas
        code = ""
        for element in self.canvas_items:
            element_code = f"{element.__class__.__name__}("
            for arg in inspect.getargspec(element.__class__).args:
                element_code += f"{arg}={getattr(element, arg)}, "
            element_code += ")"
            code += element_code + "\n"

        # Save the code to a file
        with open(self.save_path, "w") as f:
            f.write(code)

    def clear_canvas(self, e):
        # Clear the canvas
        self.canvas_items.clear()

    def delete_element(self, e):
        # Delete the selected element
        self.canvas_items.remove(self.selected_element)

    def move_element_up(self, e):
        # Move the selected element up
        index = self.canvas_items.index(self.selected_element)
        if index > 0:
            self.canvas_items.remove(self.selected_element)
            self.canvas_items.insert(index - 1, self.selected_element)

    def move_element_down(self, e):
        # Move the selected element down
        index = self.canvas_items.index(self.selected_element)
        if index < len(self.canvas_items) - 1:
            self.canvas_items.remove(self.selected_element)
            self.canvas_items.insert(index + 1, self.selected_element)

    def load_composition(self, e):
        # Load the code from a file and execute it to render the page
        with open(self.load_path, "r") as f:
            code = f.read()
        try:
            exec(code)
        except Exception as e:
            self.code_view.text = "Fix syntax"
        else:
            self.page.open()

    def switch_view(self, e):
        if e.text == "Canvas":
            self.page.open()
        else:
            self.code_view.open()

    def update_code_view(self, e):
        # Generate the Python code for the elements in the canvas
        code = ""
        for element in self.canvas_items:
            element_code = f"{element.__class__.__name__}("
            for arg in inspect.getargspec(element.__class__).args:
                element_code += f"{arg}={getattr(element, arg)}, "
            element_code += ")"
            code += element_code + "\n"
        # Update the code view with the generated code
        self.code_view.text = code

    def code_view(self):
        # Create the code view
        self.code_view = TextField(
            text="",
            width="100%",
            height="100%",
            on_change=self.update_code_view,
        )
        return self.code_view


if __name__ == "__main__":

    def main(page: flet.Page):
        page.title = "Flet Trello clone"
        page.padding = 0
        page.bgcolor = "#0079bf"
        app = HackerMode(page)
        page.add(
            [
                Column(
                    [
                        Row(
                            [
                                TextButton("Canvas", on_click=app.switch_view),
                                TextButton("Code", on_click=app.switch_view),
                            ],
                        ),
                        Row(
                            [
                                Column(
                                    [
                                        TextButton("Add element"),
                                        TextButton("Update element"),
                                        TextButton("Save composition"),
                                        TextButton("Clear canvas"),
                                        TextButton("Delete element"),
                                        TextButton("Move element up"),
                                        TextButton("Move element down"),
                                        TextButton("Load composition"),
                                    ],
                                ),
                                Column(),
                            ],
                        ),
                    ]
                )
                # Row(
                #     [
                #         Column(
                #             [
                #                 TextButton("Add element"),
                #                 TextButton("Update element"),
                #                 TextButton("Save composition"),
                #                 TextButton("Clear canvas"),
                #                 TextButton("Delete element"),
                #                 TextButton("Move element up"),
                #                 TextButton("Move element down"),
                #                 TextButton("Load composition"),
                #             ],
                #         ),
                #         Column(
                #             [
                #                 Text("Select element"),
                #                 Dropdown(
                #                     options=app.element_options,
                #                     on_change=app.select_element,
                #                 ),
                #                 Text("Settings"),
                #                 app.settings_dialog,
                #                 FilledButton("Add element", on_click=app.add_element),
                #                 FilledButton(
                #                     "Update element", on_click=app.update_element
                #                 ),
                #                 FilledButton(
                #                     "Save composition", on_click=app.save_composition
                #                 ),
                #                 FilledButton("Clear canvas", on_click=app.clear_canvas),
                #                 FilledButton(
                #                     "Delete element", on_click=app.delete_element
                #                 ),
                #                 FilledButton(
                #                     "Move element up", on_click=app.move_element_up
                #                 ),
                #                 FilledButton(
                #                     "Move element down", on_click=app.move_element_down
                #                 ),
                #                 FilledButton(
                #                     "Load composition", on_click=app.load_composition
                #                 ),
                #             ],
                #         ),
                #         Column(
                #             [
                #                 Text("Canvas"),
                #                 app.canvas,
                #             ],
                #         ),
                #     ],
                # ),
                # Row(
                #     [
                #         Text("Code view"),
                #     ],
                # ),
                # Row(
                #     [
                #         Column(
                #             [
                #                 Text("Code view"),
                #                 app.code_view,
                #             ],
                #         ),
                #     ],
                # ),
            ]
        )
        app.populate_sidebar()
        page.update()

    flet.app(
        assets_dir="../assets",
        target=main,
        view=flet.WEB_BROWSER,
        route_url_strategy="path",
    )
