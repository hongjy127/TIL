def get_resolution():
    res = int(input('Reslution(1:320X240, 2:640X480, 3:1024X768)'))

    if res == 3:
        resolution = (1024, 768)
    elif res == 2:
        resolution = (640, 480)
    else:
        resolution = (320, 240)

    return resolution