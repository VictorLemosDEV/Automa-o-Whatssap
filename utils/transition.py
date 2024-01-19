
# Interpolate between two colors

def interpolate(color_a, color_b, t):
    # 'color_a' and 'color_b' are RGB tuples
    # 't' is a value between 0.0 and 1.0
    # this is a naive interpolation
    return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


