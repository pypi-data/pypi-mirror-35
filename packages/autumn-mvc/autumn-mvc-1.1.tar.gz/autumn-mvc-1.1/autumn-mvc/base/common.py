import threading
import os
import uuid


def guid():
    def get_mac_address():
        node = uuid.getnode()
        return uuid.UUID(int=node).hex[-12:]
    threadId = threading.currentThread().ident
    processId = os.getpid()
    mac = get_mac_address()
    random = list("{threadId}{processId}{mac}".format(**locals()))[0:32] # NOQA
    random.insert(19, "-")
    random.insert(15, "-")
    random.insert(11, "-")
    random.insert(7, '-')
    return "".join(random)


functions = object
for func in [f for f in globals().values() if hasattr(f, "__call__")]:
    name = getattr(func, "__name__")
    setattr(functions, name, func)
