import matplotlib.pyplot as plt

def DDALine(x1, y1, x2, y2, color):
    fig = plt.figure()

    dx = x2 - x1
    dy = y2 - y1

    x, y = x1, y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xinc = float(dx / steps)
    yinc = float(dy / steps)

    for i in range (0, steps + 1):
        plt.plot(round(x1), round(y1), color, marker='s', markersize=5) # marker='s', markersize=5
        # if(i == round(steps+1)):
        #     plt.plot(round(x1), round(y1), color, marker='o', markersize=25) # marker='0', markersize=25
        x1 += xinc
        y1 += yinc
    # plt.xlim(0, 100)
    # plt.ylim(0, 100)
    plt.plot(round((x1 + x)/2), round((y1 + y)/2), 'bo', markersize=5)
    
    return fig

def Bres(x1,y1,x2,y2, color):
    fig = plt.figure()

    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    # print(f"x = {x}, y = {y}")
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        # print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates, color, marker='s', markersize=5)
    plt.plot(round(dx/2 + x1), round(dy/2 + y1), 'bo', markersize=5)

    return fig

def midpoint(x1, y1, x2, y2, color):
    fig = plt.figure()

    dx = x2 - x1
    dy = y2 - y1

    # Initialize the decision parameter
    d  = dy - (dx/2)
    x = x1
    y = y1

    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    while (x<x2):
        x = x + 1
        # East is Chosen
        if (d<0):
            d = d + dy

        # North East is Chosen
        else:
            d = d + (dy - dx)
            y = y + 1

        xcoordinates.append(x)
        ycoordinates.append(y)
        # print(f"x = {x}, y = {y}")
    plt.plot(xcoordinates, ycoordinates, color, marker='s', markersize=5)

    return fig

def main():
    x = int(input("Enter x1: "))
    y = int(input("Enter y1: "))
    x_end = int(input("Enter x2: "))
    y_end = int(input("Enter y2: "))
    color = "#aa2533"
    fig = DDALine(x, y, x_end, y_end, color)
    plt.show()
    Bres(x, y, x_end, y_end, color)
    midpoint(x, y, x_end, y_end, color)

if __name__ == "__main__":
    main()