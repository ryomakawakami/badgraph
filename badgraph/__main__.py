import matplotlib.pyplot as plt

from badgraph.drawer import Drawer

if __name__ == '__main__':
    drawer = Drawer(100, 100)
    drawer.visualize(width = 0.7, data = [
        ['a', 30],
        ['b', 80],
        ['c', 60],
        ['d', 50]
    ])

    plt.axis('off')
    plt.savefig('test.png', bbox_inches='tight')
