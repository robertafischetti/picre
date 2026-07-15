#**********************************************************
# Module: pylogger_styled
#
# Author = Roberta Fischetti
#
# Date = 2026-07-15
#
# Description = Styling the module pylogger.py
#**********************************************************



# original: logging.init.py

def findCaller(self):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    f = currentframe()
    #On some versions of IronPython, currentframe() returns None if
    #IronPython isn't run with -X:Frames.
    if f is not None:
        f = f.f_back
    rv = "(unknown file)", 0, "(unknown function)"
    while hasattr(f, "f_code"):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        if filename == _srcfile:
            f = f.f_back
            continue
        rv = (co.co_filename, f.f_lineno, co.co_name)
        break
    return rv

# How can we make this code better?

# Writing a better version of the code

def findCallerStyled(self) -> tuple[str, int, str]: # adding a return annotation

    """
    Find the stack frame of the caller so that we can note 
    the source file name, line number and function name.
    """

    # replacing variable name "f" with "current_frame"
    current_frame = currentframe()  # findCaller_styled()

    # On some versions of IronPython, currentframe() returns None if
    # IronPython isn't run with -X:Frames.

    if current_frame is not None:
        current_frame = current_frame.f_back # go one frame back

    # replacing variable name "rv" with "return_value"
    return_value = "(unknown file)", 0, "(unknown function)" 

    while hasattr(current_frame, "f_code"):
        # replacing variable name "co" with "code_object"
        code_object = current_frame.f_code  
        filename = os.path.normcase(code_object.co_filename)

        if filename == _srcfile:
            current_frame = current_frame.f_back
            continue
        
        # making the return tuple more readable
        return_value = (code_object.co_filename, 
                        current_frame.f_lineno, 
                        code_object.co_name)
        break

    return return_value
