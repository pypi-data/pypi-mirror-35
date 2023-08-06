def get(func):
    def _dec(*args, **kwages):
        func(*args, **kwages)
    return _dec


def post(func):
    def _dec(*args, **kwages):
        func(*args, **kwages)
    return _dec


methods = object()
for method in [m for m in globals().values() if hasattr(m, "__call__")]:
    name = getattr(method, "__name__")
    setattr(methods, name, method)
