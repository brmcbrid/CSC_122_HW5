# Tests for Lab5
# Keno Lottery Game

import os.path
import sys
from HW5 import main
from tud_tests import *

def test_HW5():

    try:
        exists = os.path.exists("HW5.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input(['54','28','18','69','10','11','18','13','33','92','34','$35&*','65'])
    main()
    output = get_display_output()

    assert output == [
        "Keno Lottery Game\n",
        "Enter pick #1: ",
        "Enter pick #2: ",
        "Enter pick #3: ",
        "Enter pick #4: ",
        "Enter pick #5: ",
        "Enter pick #6: ",
        "Enter pick #7: ",
        "18 has already been picked. Try again.",
        "Enter pick #7: ",
        "Enter pick #8: ",
        "Enter pick #9: ",
        "Value out of range. Try again.",
        "Enter pick #9: ",
        "Enter pick #10: ",
        "Invalid data. Try again",
        "Enter pick #10: ",
        "\nYour picks are:[54, 28, 18, 69, 10, 11, 13, 33, 34, 65]",
        "\nThe winning numbers are:[50, 54, 6, 34, 66, 63, 52, 39, 62, 46, 75, 28, 65, 18, 37, 13, 80, 33, 69, 78]",
        "\nYou matched:[54, 28, 18, 69, 13, 33, 34, 65]",
        "\nYou matched 8 of 20 numbers. You have won $250"
        ]
