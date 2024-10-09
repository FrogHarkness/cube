
def fun (hsv_values):

    h = hsv_values[0]
    s = hsv_values[1]
    v = hsv_values[2]
    
    if(s > 30):

        if(h < 8):
            return "red"

        elif(h < 20):
            return "orange"

        elif(h < 40):
            return "yellow"

        elif(h < 75):
            return "green"

        elif(h < 132):
            return "blue"
    
    else:
        return "white"

def hsv_distance(hsv1, hsv2):
    """
    Calculate the Euclidean distance between two HSV colors.
    
    :param hsv1: tuple or list of (h, s, v) values for the first color (normalized).
    :param hsv2: tuple or list of (h, s, v) values for the second color (normalized).
    :returns: float - Euclidean distance between the two colors in HSV space.
    """
    h_diff = min(abs(hsv1[0] - hsv2[0]), 1 - abs(hsv1[0] - hsv2[0]))  # Wrap around hue (circular)
    s_diff = hsv1[1] - hsv2[1]
    v_diff = hsv1[2] - hsv2[2]
    return np.sqrt(h_diff**2 + s_diff**2 + v_diff**2)

def fun1(hsv_values):
    """
    Determines the closest color name based on HSV values using Euclidean distance.
    
    :param hsv_values: tuple or list of (h, s, v) values from the HSV color space (scaled to 0-255).
    :returns: string - The name of the closest color.
    """
    # Normalize the HSV values to a range of 0-1 for comparison
    h = hsv_values[0] / 180.0  # Hue is in range [0, 180] in OpenCV
    s = hsv_values[1] / 255.0  # Saturation is in range [0, 255]
    v = hsv_values[2] / 255.0  # Value is in range [0, 255]
    hsv_normalized = (h, s, v)
    
    # Calculate the distance to each color in the palette
    distances = {
        color_name: hsv_distance(hsv_normalized, hsv_ref)
        for color_name, hsv_ref in color_palette_hsv.items()
    }
    
    # Find the color with the smallest distance
    closest_color = min(distances, key=distances.get)
    return closest_color



def fun2(color):

    if(color == 'red'):
        return (0, 0, 255)
    
    elif(color == 'orange'):
        return (0, 165, 255)
    
    elif(color == 'yellow'):
        return (0, 255, 255)
    
    elif(color == 'green'):
        return (0, 255, 0)
    
    elif(color == 'blue'):
        return (255, 0, 0)
    
    else:
        return (255, 255, 255) #white 


