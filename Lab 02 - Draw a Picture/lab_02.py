import arcade

# import the "arcade" library
arcade.open_window(width=600, height=600, window_title="Drawing Test")
# This defines the size of the drawing window

# Set Background
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0,600,300,0,arcade.csscolor.DARK_GREEN)
# ready to draw starts drawing
# Draw a rectangle
# Left of 0, right of 600
# Top of 300, bottom of 0


# Circle Based Tree
arcade.draw_xywh_rectangle_filled(100,300,20,60,arcade.csscolor.SIENNA)
arcade.draw_circle_filled(110,350,30, arcade.csscolor.LIGHT_GREEN)

# Ellipse Based Trees
arcade.draw_xywh_rectangle_filled(180,300,20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(190, 370,60, 80, arcade.csscolor.LIGHT_GREEN )

# Failed Pine Tree with Arcs
arcade.draw_xywh_rectangle_filled(280,300, 20,75,arcade.csscolor.SIENNA)
arcade.draw_arc_filled(280, 350, 20, 100, start_angle=100,end_angle=180,tilt_angle=450, color=arcade.csscolor.LIGHT_GREEN)
arcade.draw_arc_filled(290, 350, 20, 100, start_angle=100,end_angle=180,tilt_angle=-130, color=arcade.csscolor.LIGHT_GREEN)

# Pine Tree Code
arcade.draw_xywh_rectangle_filled(420, 300, 20, 71, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(390, 320, 470, 320, 430, 340 ,arcade.csscolor.LIGHT_GREEN)
arcade.draw_triangle_filled(395, 330, 465, 330, 430, 355 ,arcade.csscolor.LIGHT_GREEN)
arcade.draw_triangle_filled(400, 340, 460, 340, 430, 370 ,arcade.csscolor.LIGHT_GREEN)
arcade.draw_triangle_filled(405, 340, 455, 340, 430, 385 ,arcade.csscolor.LIGHT_GREEN)
arcade.draw_triangle_filled(410, 340, 450, 340, 430, 400 ,arcade.csscolor.LIGHT_GREEN)

# Pine Tree Code 2
arcade.draw_xywh_rectangle_filled(520, 300, 20, 71, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(490, 320, 570, 320, 530, 340 ,arcade.csscolor.LIGHT_GREEN)
arcade.draw_triangle_filled(495, 330, 565, 330, 530, 355 ,arcade.csscolor.LIGHT_GREEN)
arcade.draw_triangle_filled(500, 340, 560, 340, 530, 370 ,arcade.csscolor.LIGHT_GREEN)
arcade.draw_triangle_filled(505, 340, 555, 340, 530, 385 ,arcade.csscolor.LIGHT_GREEN)
arcade.draw_triangle_filled(510, 340, 550, 340, 530, 400 ,arcade.csscolor.LIGHT_GREEN)

# Sun Drawing
arcade.draw_circle_filled(500,550,40, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# Circle Around the Tree I Drew
arcade.draw_circle_outline(430, 343,60, arcade.color.CADMIUM_RED)

# Circle Around the Tree I Drew #2
arcade.draw_circle_outline(530, 343,60, arcade.color.CADMIUM_RED)

# Text Generation
arcade.draw_text("The Pine Tree Took Forever to Code!", 75, 230, arcade.color.FLORAL_WHITE, 20)

# Cloud Code - Great Name
arcade.draw_circle_filled(100, 550, 20, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(100, 540, 10, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(110, 550, 20, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(120, 550, 10, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(130, 570, 20, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(90, 530, 20, arcade.color.FLORAL_WHITE)

# Cloud Two
arcade.draw_circle_filled(300, 550, 20, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(320, 540, 10, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(310, 539, 20, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(327, 545, 25, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(330, 520, 20, arcade.color.FLORAL_WHITE)
arcade.draw_circle_filled(290, 532, 20, arcade.color.FLORAL_WHITE)

arcade.finish_render()
#Essentially Finishes the Image



arcade.run()
# This code makes the window stay open
