def decimal_to_RGB(color_number):
    color_hex = hex(color_number)
    if len(color_hex)<8:
        lenght = len(color_hex)
        color_hex = color_hex[:2]+'0'*(8-lenght)+color_hex[2:]

    blue = int(color_hex[2:4],16)
    green = int(color_hex[4:6],16)
    red = int(color_hex[6:8],16)

    return[red,green,blue]
