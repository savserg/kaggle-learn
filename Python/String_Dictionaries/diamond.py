def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    outStr = ""
    for i in range(1, height//2+1,1):
        tmpStr = "/"*i + "\\"*i
        outStr += tmpStr.center(height) + "\n"
    for i in range(height//2, 0, -1):
        tmpStr = "\\"*i + "/"*i
        outStr += tmpStr.center(height) + "\n"
    return outStr[:-1]
   
