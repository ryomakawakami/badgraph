import matplotlib.pyplot as plt

from badgraph.drawer import Drawer

if __name__ == '__main__':
    drawer = Drawer(100, 100)

    drawer.drawAxes()
    drawer.drawBar(25, 0, 15, 30)
    drawer.drawBar(50, 0, 15, 80)
    drawer.drawBar(75, 0, 15, 60)

    plt.axis('off')
    plt.savefig('test.png', bbox_inches='tight', pad_inches=0)
