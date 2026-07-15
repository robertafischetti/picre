#**********************************************************
# Module: compress_ifs_styled
#
# Author = Roberta Fischetti
#
# Date = 2026-07-15
#
# Description = Styling the module compress_ifs.py
#**********************************************************



from maya import mel as mc


# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrlList=None, color=None):

    for ctrlName in ctrlList:
        try:
            mc.setAttr(ctrlName + 'Shape.overrideEnabled', 1)
        except:
            pass
        
        try:
            if color == 1:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 4)
            elif color == 2:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 13)
            elif color == 3:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 25)
            elif color == 4:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 17)
            elif color == 5:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 17)
            elif color == 6:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 15)
            elif color == 7:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 6)
            elif color == 8:
                mc.setAttr(ctrlName + 'Shape.overrideColor', 16)
        except:
            pass


# Writing a better version of the code

# Making the arguments required to avoid any errors
# Adding function annotations
# Replacing camelCase with snake_case
# Renaming parameters' names 
def set_color_styled(ctrl_list: list[str], color_index: int) -> None:

    # Substituting the if/elif list with a dictionary
    color_map = {
        1: 4,
        2: 13,
        3: 25,
        4: 17,
        5: 17,
        6: 15,
        7: 6,
        8: 16,
    }

    # Making sure that only available color indexes are passed
    override_color = color_map.get(color_index)

    if override_color is None:
        print(f"Invalid color index: {color_index}")

    for ctrl_name in ctrl_list:
        # Replacing try/except with if/else, avoiding silent errors
        if mc.objExists(f"{ctrl_name}Shape.overrideEnabled"): # Replacing the string concat with format
            mc.setAttr(f"{ctrl_name}Shape.overrideEnabled", 1)
            mc.setAttr(f"{ctrl_name}Shape.overrideColor", override_color)
        else:
            print(f"Missing shape attribute for {ctrl_name}.")

        

# EXAMPLE
# set_color(['circle','circle1'], 8)
