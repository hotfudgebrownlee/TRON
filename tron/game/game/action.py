class Action:
    """Code template for a thing done in the game. Takes objects
    as arguments and manipulates them. This is the superclass for all
    other objects in the game.

    Stereotype:
        Controller

    Attributes:
        _tag(string): The action tag from the script."""
    def execute(self,cast):
        """Execute the selected action with given actors.

        Args:
            cast(dict): an object passed in full of actors.
                {key:tag, value:list}"""
        raise NotImplementedError("execution not implemented in superclass")