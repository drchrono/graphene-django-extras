__all__ = ["OptimizationHints", "resolver_hints"]


class OptimizationHints(object):
    def __init__(self, model_field=None, select_related=None, prefetch_related=None, only=None):
        self.model_field = model_field
        self.prefetch_related = set(prefetch_related) if prefetch_related else set()
        self.select_related = set(select_related) if select_related else set()
        self.only = set(only) if only else set()


def resolver_hints(*args, **kwargs):
    optimization_hints = OptimizationHints(*args, **kwargs)

    def apply_resolver_hints(resolver):
        resolver.optimization_hints = optimization_hints
        return resolver

    return apply_resolver_hints
