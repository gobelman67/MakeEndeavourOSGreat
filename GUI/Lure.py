from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from Utilities import AppBox, GridBox, color, CommandLine


class LureWin(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.gbxLure = AppBox("Linux User Repository", "linux-user-repository-bin", "GUI/Assets/Apps/lure.png",
                              "LURE allows users to install software that may not be widely distributed through official repositories, while still maintaining the convenience of installation through repository sources. This includes features such as updates and simple uninstallation. Additionally, LURE provides developers with a central location for all their users to use to install their software.")

        self.gbxUsage = GridBox("Usage of LURE")
        self.lblUsage = QLabel(
            "You can use LURE by following commands:", self.gbxUsage)
        self.cmdUsage = CommandLine(
            "<div>" +
            color("green", "lure ") +
            color("yellow", "install ") +
            color("orange", "package_name ") +
            color("gray", "# Installs specified package.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "remove ") +
            color("orange", "package_name ") +
            color("gray", "# Uninstalls specified package.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "refresh ") +
            color("gray", "# Refresh database.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "upgrade ") +
            color("gray", "# Upgrades all available packages.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "list ") +
            color("gray", "# Lists all packages in repository.") + "</div><div>" +
            color("green", "lure ") +
            color("yellow", "help ") +
            color("gray", "# Prints detailed help page.") +
            "</div>",
            150
        )
        self.gbxUsage.addWidgets(self.lblUsage, self.cmdUsage)

        # Insert groupboxes to layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxLure)
        self.layout.addWidget(self.gbxUsage)
