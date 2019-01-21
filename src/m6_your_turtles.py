"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Max Jacobs.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg
window = rg.TurtleWindow()
bill = rg.SimpleTurtle()
bill.pen= rg.Pen('purple', 10)
bill.speed = 200
size = 200
for k in range(16):
    bill.draw_circle(size)
    bill.pen_up()
    bill.right(45)
    bill.forward(10)
    bill.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    bill.pen_down()
    size = size - 30

###############################################################################
# Example 2.  It shows how to speed up the animation.
###############################################################################
window.tracer(50)  # Bigger numbers make the animation run faster

ted = rg.SimpleTurtle()
ted.pen = rg.Pen('cyan', 1)
ted.pen_up()
ted.forward(48)
ted.right(90)
ted.forward(44)
ted.pen_down()
# The name k takes on the values 0, 1, 2, ... 499 as the loop runs
for k in range(7000):
    ted.left(12)
    ted.forward(k-0.965*k)

window.close_on_mouse_click()
