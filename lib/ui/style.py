from ui.color import Color

class Style:
    @staticmethod
    def styleButton(widget):
        Color.paintButton(widget)
        Style._defaultButtonHighlight(widget)
        widget.config(font=("Impact", 15))

    def stylePrimaryButton(widget):
        Color.paintPrimaryButton(widget)
        Style._defaultButtonHighlight(widget)
        widget.config(font=("Impact", 30))

    def styleBox(widget):
        Color.paintBox(widget)
        Style._defaultButtonHighlight(widget)
        widget.config(font=("Impact", 20))

    def styleDarkBox(widget):
        Color.paintButton(widget)
        Style._defaultButtonHighlight(widget)
        widget.config(font=("Impact", 15))

    def _defaultButtonHighlight(widget):
        widget.config(highlightbackground='black', highlightthickness='2')
