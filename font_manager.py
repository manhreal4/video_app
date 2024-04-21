# configure the font for the user interface in the application using the tkinter library
import tkinter.font as tkfont

# used to configure fonts for different parts of the user interface

def configure():
    family = "Helvetica"
    
    # Returns the default font used for elements such as labels, buttons, etc
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=15, family=family)
    
    # Returns the font used for the text area (Text)
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=12, family=family)
    
    # Returns the font used for the fixed text area (Text has a fixed font style)
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=12, family=family)
