import arcade
from game import constants
# import sys
# from game.director import Director
class GameOver(arcade.View):
    """View to show who won"""
    def __init__(self,cast,script,input_service,winner):
        """Class constructor. Variables should be passed to Director
        only if player chooses to play again."""
        # super().__init__(constants.MAX_X, constants.MAX_Y, "TRON")
        super().__init__()
        self.window.set_mouse_visible(True)
        self._cast = cast
        self._script = script
        self._input = input_service
        self._winner = winner

    def on_show(self):
        """This will run when we switch to this view."""
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
    
    def on_draw(self):
        """This draws the view"""
        arcade.start_render()
        arcade.draw_text("GAME OVER", constants.MAX_X / 2,
                         constants.MAX_Y * 0.75, arcade.color.WHITE,
                         font_size=50, anchor_x="center")
        arcade.draw_text(f"{self._winner} won!", constants.MAX_X / 2,
                         constants.MAX_Y / 2, arcade.color.WHITE,
                         font_size=20, anchor_x="center")
        arcade.draw_text(f"Click to exit.",constants.MAX_X / 2,
                         constants.MAX_Y * 0.25,arcade.color.WHITE,
                          font_size=20, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """If mouse is pressed, exit the game."""
        arcade.close_window()