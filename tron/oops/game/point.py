class Point:
    """Represents the distance from an origin(0,0).

    Stereotype:
        Information Holder

    Attributes:
        _x (integer): The horizontal distance.
        _y (integer): The vertical distance."""
    def __init__(self, x, y):
        """The class constructor. Passes in x and y values."""
        self._x = x
        self._y = y

    def get_x(self):
        """returns x value"""
        return self._x

    def get_y(self):
        """returns y value"""
        return self._y

    def set_x(self, x):
        """sets new x value"""
        self._x = x

    def set_y(self, y):
        """sets new y value"""
        self._y = y
    
    def add(self, other):
        """Get a new point that is the sum of self point
        and passed-in point.

        Args:
            other (Point): the Point to add.

        Returns:
            Point: a new Point."""
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x,y)

    def reverse(self):
        """Gets a new point that is the reverse of self point.

        Returns:
            reverse: reverse of current point."""
        x = self._x * -1
        y = self._y * -1
        return Point(x,y)

    def equals(self,other):
        """Returns a boolean value to verify if two points
        are equal."""
        return self._x == other.get_x() and self._y == other.get_y()

    def scale(self,scale_by):
        """returns a point scaled by specified amount."""
        x = self._x * scale_by
        y = self._y * scale_by
        return Point(x,y)

    def is_zero(self):
        """Determines whether or not the point is zero. Useful for 
        determining zero-velocity objects.

        Returns:
            boolean: True if x and y are both zero. Else false."""
        return self._x == 0 and self._y == 0