class Color:
    foreground = 'white'
    background = '#1B374C'
    lightForeground = '#67c1f5'
    darkBackground = '#171A21'
    darkForeground = '#C5C3C0'
    buttonForeground = '#68a6c9'
    buttonBackground = '#1d5676'
    primaryButtonForeground = '#bdd46c'
    primaryButtonBackground = '#7C9D05'
    boxBackground = '#38434F'
    boxForeground = 'white'

    @staticmethod
    def paint(widget):
        widget.config(fg=Color.foreground, bg=Color.background)
        widget.config(activebackground=Color.background)

    @staticmethod
    def paintLight(widget):
        widget.config(fg=Color.lightForeground, bg=Color.darkBackground)
        widget.config(activebackground=Color.darkBackground, activeforeground=Color.lightForeground)

    @staticmethod
    def paintButton(widget):
        widget.config(fg=Color.buttonForeground, bg=Color.buttonBackground)
        widget.config(activebackground=Color.buttonBackground)
        widget.config(activeforeground=Color.buttonForeground)

    @staticmethod
    def paintPrimaryButton(widget):
        widget.config(fg=Color.primaryButtonForeground, bg=Color.primaryButtonBackground)
        widget.config(activebackground=Color.primaryButtonBackground)
        widget.config(activeforeground=Color.primaryButtonForeground)

    @staticmethod
    def paintDark(widget):
        widget.config(fg=Color.darkForeground, bg=Color.darkBackground)
        widget.config(activebackground=Color.darkBackground)
        widget.config(activeforeground=Color.darkForeground)

    @staticmethod
    def paintBox(widget):
        widget.config(fg=Color.boxForeground, bg=Color.boxBackground)
        widget.config(activebackground=Color.boxBackground)
        widget.config(activeforeground=Color.boxForeground)
