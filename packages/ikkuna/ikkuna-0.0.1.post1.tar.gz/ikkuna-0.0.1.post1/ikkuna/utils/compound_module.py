import torch


class CompoundModule(torch.nn.Module):
    '''A module comprised of more submodules which can be treated as a whole.'''

    def __init__(self, module):
        super.__init__()
        self._modules['root'] = module
        leaves = self.leaves()
        self._leaves_w_weight = set()
        self._leaves_w_bias = set()
        for m in leaves:
            if hasattr(m, 'bias') and m.bias is not None:
                self._leaves_w_bias.add(m)
            if hasattr(m, 'weight') and m.weight is not None:
                self._leaves_w_weight.add(m)

    def forward(self, x):
        return self.root(x)

    def add_module(self, *args):
        raise ValueError('Submodules don\'t make sense here.')

    def leaves(self, module=None):
        stack = list(self.children())
        children = set()
        while len(stack) > 0:
            child = stack.pop()
            for grandchild in child.children():
                if len(grandchild.children()) == 0:     # leaf
                    children.add(grandchild)
                else:
                    stack.append(grandchild)
        return children
