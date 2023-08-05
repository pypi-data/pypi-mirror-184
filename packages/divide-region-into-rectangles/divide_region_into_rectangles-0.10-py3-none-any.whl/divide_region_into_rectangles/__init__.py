def divide_number_to_generator_with_rest(number, divider):
    splittedx = divmod(number, divider)
    rangex = (
        divider if ini != splittedx[0] - 1 else divider + splittedx[-1]
        for ini, _ in enumerate(range(splittedx[0]))
    )
    return rangex


def cropimage(img, coords):
    return img[coords[1] : coords[3], coords[0] : coords[2]]


def divide_region_into_rect(startx, starty, w, h, square_w=10, square_h=10):
    imgheight = h
    imgwidth = w
    pixel_width = square_w
    pixel_height = square_h
    listx = list(divide_number_to_generator_with_rest(imgwidth, pixel_width))
    listy = list(divide_number_to_generator_with_rest(imgheight, pixel_height))
    listx.insert(0, startx)
    listy.insert(0, starty)
    width = 0
    allc = []
    for x, addx in zip(listx, listx[1:]):
        width = width + x
        height = 0
        for y, addy in zip(listy, listy[1:]):
            height = height + y
            coords = (width, height, width + addx, height + addy)
            allc.append(coords)
    return allc


