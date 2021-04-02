import arcade
from game import constants
from game.gameover import GameOver

class Director(arcade.View):
    def __init__(self,cast,script,input_service):
        """Class constructor. Intializes the game."""
        # super().__init__(constants.MAX_X, constants.MAX_Y, "TRON")
        super().__init__()
        self.window.set_mouse_visible(False)
        self._cast = cast
        self._script = script
        self._input = input_service

    def setup(self):
        """Sets up the background for the game."""
        arcade.set_background_color(arcade.color.BLACK)

    def _cue_action(self,tag):
        """Execute the actions of the given tag.
        Args:
            tag(string) The tag within the script."""
        for action in self._script[tag]:
            action.execute(self._cast)

    def on_key_press(self,symbol,modifier):
        self._input.set_key(symbol)
        self._cue_action("input")

    def on_key_release(self,symbol,modifier):
        self._input.remove_key(symbol)
        self._cue_action("input")

    def on_update(self, delta_time):
        if constants.GAMEOVER == False:
            self._cue_action("update")
        else:
            # window = arcade.Window(constants.MAX_X, constants.MAX_Y, "TRON")
            end_view = GameOver(self._cast,self._script,self._input, constants.WINNER)
            self.window.show_view(end_view)

    def on_draw(self):
        self._cue_action("output")