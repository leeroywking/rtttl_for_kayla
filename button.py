from digitalio import DigitalInOut, Direction, Pull


def make_button(pin):
    btn = DigitalInOut(pin)
    btn.direction = Direction.INPUT
    btn.pull = Pull.UP
    return btn
