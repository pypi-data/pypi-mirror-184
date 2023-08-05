from importlib import import_module
from pkgutil import iter_modules
from types import ModuleType

from .. import PROJECT_NAME


class PackageTreeNode:
    registry = {}
    sentinel = object()

    def __new__(cls, node_value):
        value_id = id(node_value)
        output = cls.registry.get(value_id, cls.sentinel)
        if output is cls.sentinel:
            if isinstance(node_value, ModuleType):
                output = cls.registry[value_id] = {}
                for fieldname in dir(node_value):
                    field = getattr(node_value, fieldname)
                    if isinstance(field, ModuleType) or fieldname.startswith("__"):
                        continue
                    output[fieldname] = PackageTreeNode(field)
                if hasattr(node_value, "__path__"):
                    for _, child, __ in iter_modules(node_value.__path__):
                        if child == "__main__":
                            continue
                        try:
                            output[child] = PackageTreeNode(
                                import_module(f"{node_value.__name__}.{child}")
                            )
                        except:
                            continue
                return output
            else:
                output = cls.registry[value_id] = node_value
        return output


def test_import_tree():
    root = import_module(PROJECT_NAME)
    assert PackageTreeNode(root)
