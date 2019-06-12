__all__ = ["OptimizationHints", "resolver_hints"]


class OptimizationHints(object):
    def __init__(self, model_field=None, select_related=None, prefetch_related=None, only=None):
        self.model_field = model_field
        self.prefetch_related = prefetch_related if prefetch_related else []
        self.select_related = select_related if select_related else []
        self.only = only if only else []


def resolver_hints(*args, **kwargs):
    optimization_hints = OptimizationHints(*args, **kwargs)

    def apply_resolver_hints(resolver):
        resolver.optimization_hints = optimization_hints
        return resolver

    return apply_resolver_hints
