from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from Utilities import ButtonBox, GridBox, DconfEditBox, DconfEditRow, DconfCheckBox, CommandButton, aur_helper


class GnomeWin(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create Wayland section
        self.gbxWayland = \
            ButtonBox("Wayland Settings", "GUI/Assets/Tweaks/wayland.png",
                      "<p>Wayland is a new technology to replace Xorg display server. Its may be lighter and faster. Waydroid only works on Wayland but because of it is a new technology, some features are not compatible yet. I.e. global keyboard shourtcuts does not supported right now. Discord cannot share screen on.</p>\
                       <p>Wayland has its own <font color='green'>advantages</font> and <font color='red'>disadvantages</font>. So you may want to change this setting in the future depending on your needs. But for now using Xorg and ditching Wayland is more compatible.</p>", (
                          CommandButton(QIcon("GUI/Assets/configure.png"), "Use Wayland",
                                        "sudo sed -i \"s/^WaylandEnable=false/#WaylandEnable=false/\" /etc/gdm/custom.conf",
                                        self),
                          CommandButton(QIcon("GUI/Assets/configure.png"), "Use XOrg",
                                        "sudo sed -i \"s/^#WaylandEnable=false/WaylandEnable=false/\" /etc/gdm/custom.conf",
                                        self))
                      )

        # Create context menu section
        self.gbxContext = \
            ButtonBox("Context Menu", "GUI/Assets/Tweaks/contextmenu.png",
                      "Enable context (right click) menu icons.", (
                          CommandButton(QIcon("GUI/Assets/enabled.png"), "Enable Icons",
                                        "gsettings set org.gnome.settings-daemon.plugins.xsettings overrides \"{\\\"Gtk/ButtonImages\\\": <1>, \\\"Gtk/MenuImages\\\": <1>}\"",
                                        self),
                          CommandButton(QIcon("GUI/Assets/disabled.png"), "Disable Icons",
                                        "gsettings set org.gnome.settings-daemon.plugins.xsettings overrides \"{}\"", self))
                      )

        # Create Gnome Terminal/Console section
        self.gbxTerm = GridBox("Gnome Terminal / Console")
        # Chose Gnome Terminal over Console
        self.appTerminal = \
            ButtonBox("Gnome Terminal", "GUI/Assets/Tweaks/gnometerminal.png",
                      "Gnome terminal is more compatible than console with Gnome desktop environment (open with terminal etc.). But may not be able to adapt dark/light theme.", (
                          CommandButton(QIcon("GUI/Assets/configure.png"), "Use Gnome Terminal",
                                        f"""if [ ! "$(pacman -Qqs gnome-terminal-transparency | grep ^gnome-terminal-transparency$)" = "gnome-terminal-transparency" ]
                                            then
                                            if [ "$(command -v {aur_helper()})" ]
                                                then {aur_helper()} -S gnome-terminal-transparency
                                            else
                                                read
                                                exit 1
                                            fi
                                        fi &&
                                        if [ -f /usr/bin/kgx ]
                                            then sudo pacman -R gnome-console
                                        fi""", self),)
                      )
        # Chose Gnome Console over Terminal
        self.appConsole = \
            ButtonBox("Gnome Console", "GUI/Assets/Tweaks/gnomeconsole.png",
                      "Gnome Console is more compatible with dark/light theme but is not compatible with default terminal application configuration.", (
                          CommandButton(QIcon("GUI/Assets/configure.png"), "Use Gnome Console",
                                        """if [ ! -f /usr/bin/kgx ]
                                            then sudo pacman -S gnome-console
                                        fi &&
                                        if [ "$(pacman -Qqs gnome-terminal)" = "gnome-terminal-transparency" ]
                                            then sudo pacman -R gnome-terminal-transparency
                                        elif [ "$(pacman -Qqs gnome-terminal)" = "gnome-terminal" ]
                                            then sudo pacman -R gnome-terminal
                                        fi""", self),)
                      )
        # Create keybinds section
        self.gbxKeyBinds = DconfEditBox("Keybindings", (
            DconfEditRow(
                "Show Desktop", "org.gnome.desktop.wm.keybindings show-desktop", (
                    DconfCheckBox("Super+D", "'<Super>d'"),
                    DconfCheckBox("Control+Alt+D", "'<Control><Alt>d'"),
                )
            ),
            DconfEditRow(
                "Open Home Folder", "org.gnome.settings-daemon.plugins.media-keys home", (
                    DconfCheckBox("Super+E", "'<Super>e'"),
                    DconfCheckBox("Super+F", "'<Super>f'"),
                )
            ),
            DconfEditRow(
                "Open Run Dialog", "org.gnome.desktop.wm.keybindings panel-run-dialog", (
                    DconfCheckBox("Super+R", "'<Super>r'"),
                    DconfCheckBox("Alt+F2", "'<Alt>F2'")
                )
            ),
            DconfEditRow(
                "Switch Applications (Not Windows!)", "org.gnome.desktop.wm.keybindings switch-applications", (
                    DconfCheckBox("Super+Tab", "'<Super>Tab'"),
                    DconfCheckBox("Alt+Tab", "'<Alt>Tab'")
                )
            ),
            DconfEditRow(
                "Switch Applications (Backward)", "org.gnome.desktop.wm.keybindings switch-applications-backward", (
                    DconfCheckBox("Shift+Super+Tab", "'<Shift><Super>Tab'"),
                    DconfCheckBox("Shift+Alt+Tab", "'<Shift><Alt>Tab'"),
                )
            ),
            DconfEditRow(
                "Switch Windows", "org.gnome.desktop.wm.keybindings switch-windows", (
                    DconfCheckBox("Alt+Tab", "'<Alt>Tab'"),
                    DconfCheckBox("Super+Tab", "'<Super>Tab'"),
                )
            ),
            DconfEditRow(
                "Switch Windows (Backward)", "org.gnome.desktop.wm.keybindings switch-windows-backward", (
                    DconfCheckBox("Shift+Alt+Tab", "'<Shift><Alt>Tab'"),
                    DconfCheckBox("Shift+Super+Tab", "'<Shift><Super>Tab'"),
                )
            ),
            DconfEditRow(
                "Close Active Window", "org.gnome.desktop.wm.keybindings close", (
                    DconfCheckBox("Super+Shift+Q", "'<Super><Shift>q'"),
                    DconfCheckBox("Super+Q", "'<Super>q'"),
                    DconfCheckBox("Alt+F4", "'<Alt>F4'"),
                )
            ),
            DconfEditRow(
                "Toggle Fullscreen (F11 may conflict with some apps)", "org.gnome.desktop.wm.keybindings toggle-fullscreen", (
                    DconfCheckBox("Alt+F12", "'<Alt>F12'"),
                    DconfCheckBox("Super+F12", "'<Super>F12'"),
                    DconfCheckBox("Alt+F11", "'<Alt>F11'"),
                    DconfCheckBox("Super+F11", "'<Super>F11'"),
                )
            ),
            DconfEditRow(
                "Toggle Windows Always On Current Workspace", "org.gnome.desktop.wm.keybindings toggle-on-all-workspaces", (
                    DconfCheckBox("Alt+F9", "'<Alt>F9'"),
                    DconfCheckBox("Super+F9", "'<Super>F9'"),
                )
            ),
            DconfEditRow(
                "Focus Active Notification", "org.gnome.shell.keybindings focus-active-notification", (
                    DconfCheckBox("Super+Shift+N", "'<Super><Shift>n'"),
                    DconfCheckBox("Super+N", "'<Super>n'"),
                )
            ),
            DconfEditRow(
                "Show Notification List", "org.gnome.shell.keybindings toggle-message-tray", (
                    DconfCheckBox("Super+N", "'<Super>n'"),
                    DconfCheckBox("Super+Shift+N", "'<Super><Shift>n'"),
                )
            ),
            DconfEditRow(
                "Toggle Touchpad", "org.gnome.settings-daemon.plugins.media-keys touchpad-toggle", (
                    DconfCheckBox("Super+Shift+P", "'<Super><Shift>p'"),
                    DconfCheckBox("Super+F3", "'<Super>F3'"),
                )
            )
        ))

        self.gbxTerm.addWidget(self.appTerminal)
        self.gbxTerm.addWidget(self.appConsole, 0, 1)

        # Insert groupboxes into layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.gbxWayland)
        self.layout.addWidget(self.gbxContext)
        self.layout.addWidget(self.gbxTerm)
        self.layout.addWidget(self.gbxKeyBinds)
