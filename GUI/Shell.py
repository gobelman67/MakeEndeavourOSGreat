from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtGui import QIcon
from Utilities import ShellBox, ButtonBox, CommandButton, long_bash_script
from os import system


class ShellWin(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        # Create Bash section
        self.appBash = ShellBox("Bash (Default)",
                                "bash",
                                "GUI/Assets/Apps/Shells/bash.png",
                                "Unix shell and command language written for the GNU Project as a replacement for the Bourne shell. <font color='red'>Do not remove this package!</font>",
                                True
                                )

        # Create Shell section
        self.appSh = ShellBox("Sh",
                              "sh",
                              "GUI/Assets/Apps/Shells/sh.png",
                              "Shell command-line interpreter for computer operating systems. <font color='red'>Do not remove this package!</font>",
                              True
                              )

        # Create ZSH section
        self.appZsh = ShellBox("Zsh",
                               "zsh",
                               "GUI/Assets/Apps/Shells/zsh.png",
                               "extended Bourne shell with many improvements, including some features of Bash, ksh, and tcsh."
                               )

        # Create fish section
        self.appFish = ShellBox("Fish",
                                "fish",
                                "GUI/Assets/Apps/Shells/fish.png",
                                "Friendly interactive shell. Smart and user-friendly command line shell"
                                )

        # Create Oh-My-Zsh section
        self.extOhMyZsh = \
            ButtonBox(
                "Oh-My-Zsh",
                "GUI/Assets/Apps/Shells/ohmyzsh.png",
                "<font color=\"orange\">Requires zsh.</font> Delightful, open source, community-driven framework for managing your Zsh configuration. It comes bundled with thousands of helpful functions, helpers, plugins, themes, and a few things that make you shout...", []
            )
        # Add Oh-My-Zsh Theme Buttons
        self.layOhMyZsh = QGridLayout()
        self.layOhMyZsh.addWidget(CommandButton(
            QIcon("GUI/Assets/configure.png"), "Use Elagoht Theme",
            self.zsh_theme_setter("elagoht"), self))
        self.layOhMyZsh.addWidget(CommandButton(
            QIcon("GUI/Assets/configure.png"), "Use Elagoht Iconless Theme",
            self.zsh_theme_setter("elagoht-safe"), self), 0, 1)
        self.layOhMyZsh.addWidget(CommandButton(
            QIcon("GUI/Assets/configure.png"), "Use BashPlus Theme",
            self.zsh_theme_setter("bashplus"), self))
        self.layOhMyZsh.addWidget(CommandButton(
            QIcon("GUI/Assets/configure.png"), "Use Robby Russell Theme",
            self.zsh_theme_setter("robbyrussell"), self))
        self.extOhMyZsh.glyApp.addLayout(self.layOhMyZsh)
        # Create Oh-My-Zsh install/uninstall buttons
        self.btnOhMyZshInstall = CommandButton(
            QIcon("GUI/Assets/install.png"), "Install",
            long_bash_script("GUI/LBSF/OhMyZsh.sh"),
            self.extOhMyZsh, (self.check_oh_my_zsh,), True)
        self.btnOhMyZshUninstall = CommandButton(
            QIcon("GUI/Assets/uninstall.png"), "Uninstall",
            r"""echo Confirm that you really want to uninstall oh-my-zsh; sudo rm -rf /root/.oh-my-zsh/ && rm -rf $HOME/.oh-my-zsh/""",
            self.extOhMyZsh, (self.check_oh_my_zsh,), True)

        # Create SyntShell section
        # ! Looks like it's not working. Will be added when it's ready.

        # Insert groupboxes to layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.appBash)
        self.layout.addWidget(self.appSh, 0, 1)
        self.layout.addWidget(self.appZsh)
        self.layout.addWidget(self.appFish)
        self.layout.addWidget(self.extOhMyZsh, 2, 0, 1, 2)

        # Initialize
        self.check_oh_my_zsh()

    # Shortcut for OhMyZsh theme setter.
    def zsh_theme_setter(self, theme: str) -> str:
        return fr"""[ \"$(grep \"^ZSH_THEME=\" $HOME/.zshrc)\" ] && sudo -i sed -i "s/^ZSH_THEME=.*/ZSH_THEME=\"{theme}\"/" $HOME/.zshrc
                   sudo [ \"$(sudo grep \"^ZSH_THEME=\" /root/.zshrc)\" ] && sudo -i sed -i "s/^ZSH_THEME=.*/ZSH_THEME=\"{theme}\"/" /root/.zshrc"""

    # Show/hide OhMyZsh Install button
    def check_oh_my_zsh(self) -> None:
        installed = system("[ -d ~/.oh-my-zsh ]") == 0
        to_show = self.btnOhMyZshUninstall if installed else self.btnOhMyZshInstall
        to_hide = self.btnOhMyZshInstall if installed else self.btnOhMyZshUninstall
        self.extOhMyZsh.layButtons.addWidget(to_show)
        self.extOhMyZsh.layButtons.removeWidget(to_hide)
        to_show.show()
        to_hide.hide()
