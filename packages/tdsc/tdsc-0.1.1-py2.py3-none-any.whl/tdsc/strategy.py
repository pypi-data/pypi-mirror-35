from __future__ import unicode_literals, absolute_import, print_function

from .context import Context


class Strategy:
    def __init__(self, strategies=None, states=None):
        self.strategies = strategies or []
        self.states = states or []

    def run(self, context=None):
        context = context or Context()

        for state in self.states:
            state.run(context)

        for strategy in self.strategies:
            strategy.run(context)
