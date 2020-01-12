def DIM_LIGHT_ENTER(button):
    button.mutate_color(button.color * 0.9)


def ORIGINAL_COLOR_EXIT(button):
    button.mutate_color(button.original_color)


def DIM_TRANSPARENCY_ENTER(button):
    button._mutable_color *= 0.9
