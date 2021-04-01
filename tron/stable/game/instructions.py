import arcade
from game import constants
from game.director import Director
class Instructions(arcade.View):
    """A view to hold the instructions. This will appear
    before the game begins."""
    def __init__(self,cast,script,input_service):
        """Class constructor. Variables should be passed to Director."""
        # super().__init__(constants.MAX_X, constants.MAX_Y, "TRON")
        super().__init__()
        self._cast = cast
        self._script = script
        self._input = input_service

    def on_show(self):
        """This will run when we switch to this view."""
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
    
    def on_draw(self):
        """This draws the view"""
        arcade.start_render()
        arcade.draw_text("Welcome to TRON", constants.MAX_X / 2,
                         constants.MAX_Y * 0.66, arcade.color.WHITE,
                         font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", constants.MAX_X / 2,
                         constants.MAX_Y / 3, arcade.color.WHITE,
                         font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """If mouse is pressed, start the game."""
        director = Director(self._cast, self._script, self._input)
        director.setup()
        self.window.show_view(director)