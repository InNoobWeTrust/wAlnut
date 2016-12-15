class Network(object):
    """A set of layers arranged in a hierarchy from largest layer at the
    bottom and the smallest layer at the top.

    Example network is walnut/model/images/explanatory/network_structure.png.

    :param layers: 2d array of nodes
    """
    def __init__(self, layers, retina):
        self.layers = layers
        self.retina = retina
