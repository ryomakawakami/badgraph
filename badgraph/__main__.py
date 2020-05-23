import matplotlib.pyplot as plt

from badgraph.badart.line import Line

if __name__ == '__main__':
    line = Line(100, 100)

    line.drawAxes()
    line.drawBar(25, 0, 15, 30)
    line.drawBar(50, 0, 15, 80)
    line.drawBar(75, 0, 15, 60)

    plt.axis('off')
    plt.savefig('test.png', bbox_inches='tight', pad_inches=0)
