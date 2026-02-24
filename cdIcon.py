newPage(1024, 1024)
colorSpace("sRGB")

grey = .17
white = .90

def roundedRect(x, y, w, h, radius):
    path = BezierPath()
    # Move to the starting point (bottom left, after the corner curve)
    path.moveTo((x + radius, y))
    # Bottom edge and bottom-right corner
    path.lineTo((x + w - radius, y))
    path.arcTo((x + w, y), (x + w, y + radius), radius)
    # Right edge and top-right corner
    path.lineTo((x + w, y + h - radius))
    path.arcTo((x + w, y + h), (x + w - radius, y + h), radius)
    # Top edge and top-left corner
    path.lineTo((x + radius, y + h))
    path.arcTo((x, y + h), (x, y + h - radius), radius)
    # Left edge and bottom-left corner
    path.lineTo((x, y + radius))
    path.arcTo((x, y), (x + radius, y), radius)
    path.closePath()
    drawPath(path)

fill(grey, grey, grey)
roundedRect(101, 201, 822, 592, 176)

fill(white, white, white)
fontSize(400)
font("Aviette Regular")
textBox("cd ..", (101, 141, 822, 540), align="center")

saveImage("~/Desktop/cdto.png", imageResolution=300)