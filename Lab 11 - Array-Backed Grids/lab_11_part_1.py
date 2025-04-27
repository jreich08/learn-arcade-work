import arcade

WIDTH = 20
HEIGHT = 20
MARGIN = 5
ROW_COUNT = 10
COLUMN_COUNT = 10
SCREEN_WIDTH = ROW_COUNT * WIDTH + MARGIN * (ROW_COUNT +1)
SCREEN_HEIGHT = COLUMN_COUNT  * HEIGHT + MARGIN * (COLUMN_COUNT + 1)

class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        # --- Create grid of numbers
        # Create an empty list
        self.grid = []
        # Loop for each row
        for row in range(ROW_COUNT):
            # For each row, create a list that will
            # represent an entire row
            self.grid.append([])
            # Loop for each column
            for column in range(COLUMN_COUNT):
                # Add a the number zero to the current row
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()
        for column in range(COLUMN_COUNT):
            x = column * WIDTH + WIDTH / 2 + ( column +1 ) * MARGIN
            for row in range (ROW_COUNT):
                y = row * HEIGHT + HEIGHT / 2 + (row + 1) * MARGIN

                color = arcade.color.WHITE
                if self.grid[row][column] == 1:
                    color = arcade.color.CANDY_APPLE_RED


                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_RIGHT:
            column = x // (WIDTH + MARGIN)
            row = y // (HEIGHT + MARGIN)
            print(f"Click coordinates: ({x}, {y}). Grid Coordinates: ({row}, {column})")

            if row >= 0 and row < ROW_COUNT and column >= 0 and column < COLUMN_COUNT:
                # Toggle clicked cell
                self.grid[row][column] = 1 if self.grid[row][column] == 0 else 0

                # Toggle adjacent cells
                adjacent = [
                    (row - 1, column),  # Up
                    (row + 1, column),  # Down
                    (row, column - 1),  # Left
                    (row, column + 1)  # Right
                ]

                for r, c in adjacent:
                    if 0 <= r < ROW_COUNT and 0 <= c < COLUMN_COUNT:
                        self.grid[r][c] = 1 if self.grid[r][c] == 0 else 0





def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()

#finished