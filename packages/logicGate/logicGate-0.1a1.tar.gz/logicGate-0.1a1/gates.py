class Gates:
    def nand(one, two):
        return (not (one & two))

    def nor(one, two):
        return (not (one / two))

    def xor(one, two):
        return ((one & (not two)) / (two & (not one)))

    def xnor(one, two):
        return (not ((one & (not two)) / (two & (not one))))