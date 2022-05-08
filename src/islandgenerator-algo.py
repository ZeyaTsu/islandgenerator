from 'islandgenerator-gui' import buttongenerator as btn

class generate:
    noise_scale = 0.07
    def setup():
        size(1000, 750)
        background(143, 171, 204)
        for x in range(1000):
            for y in range(1000):
                n = noise(x * noise_scale, y * noise_scale)
        if (n > 0.5):
            stroke(204, 192, 155)
        if (n > 0.54):
            stroke(96, 117, 94)
        if (n > 0.70):
            stroke(255, 255, 255)
        if (n < 0.5):
            stroke(143, 196, 204)
        if (n > 0.75):
            stroke(150, 150, 150)
        if (n > 0.4):
            point(x, y)