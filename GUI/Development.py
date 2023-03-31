from PyQt5.QtWidgets import QWidget, QGroupBox, QLabel, QVBoxLayout
from Utilities import AppBox, GridBox
from json import load


class DevelopmentTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create Devs section
        self.gbxDev = QGroupBox("Development packages", self)
        self.glyDev = QVBoxLayout(self.gbxDev)
        self.lblDev = QLabel(
            "Here are collections of development packages separated by languages for developers.")
        self.lblDev.setWordWrap(True)
        self.glyDev.addWidget(self.lblDev)

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxDev)
        self.load_programs_lists()

    def load_programs_lists(self):
        with open("GUI/Data/Applications.json", "r") as programs_json:
            program_lists = load(programs_json)
        for language_name, program_list in program_lists.items():
            grid_box = GridBox(language_name)
            for number, program in enumerate(program_list):
                match number:
                    case 1:
                        grid_box.addWidget(AppBox(*program), 0, 1)
                    case 2:
                        grid_box.addWidget(AppBox(*program), 0, 2)
                    case _:
                        grid_box.glyField.addWidget(AppBox(*program))
            self.layout.addWidget(grid_box)
