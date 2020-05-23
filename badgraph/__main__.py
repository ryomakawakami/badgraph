import matplotlib.pyplot as plt

import badgraph.badart.line as line

if __name__ == '__main__':
    xAxis = line.getHorizontal(0, 100, 0)
    yAxis = line.getVertical(0, 100, 0)

    plt.plot(xAxis[0], xAxis[1], 'b')
    plt.plot(yAxis[0], yAxis[1], 'b')
    plt.axis('off')
    plt.savefig('test.png', bbox_inches='tight', pad_inches=0)
