import typing
from abc import ABCMeta


class NoRootClassError(TypeError):
    def __init__(self, cls: type):
        super().__init__(f"no registry class defined as root in {cls.__name__}.mro()")


class NoMatchingSubclassError(KeyError):
    def __init__(self, key: str):
        super().__init__(f"no class registered at key '{key}'")


class SubclassValidationError(ValueError):
    def __init__(self, cls: type, value: typing.Any):
        super().__init__(f"'{value}' is not a subclass of {cls.__name__}")


class IndexedClassMeta(type):
    @classmethod
    def __prepare__(
        meta,
        clsname: str,
        bases: typing.Iterable[type],
        key: typing.Optional[str] = None,
        root: bool = False,
        registry_class: typing.Type[dict] = dict,
        **kwargs,
    ):
        output = super().__prepare__(clsname, bases, **kwargs)
        output["root"] = root
        output["key"] = key
        return output

    def __new__(
        meta,
        clsname: str,
        bases: typing.Iterable[type],
        attrs: dict,
        key: typing.Optional[str] = None,
        root: bool = False,
        registry_class: typing.Type[dict] = dict,
        **kwargs,
    ):
        cls = super().__new__(meta, clsname, bases, attrs, **kwargs)
        if root:
            cls.__registry__ = registry_class()
        if key is not None:
            if not hasattr(cls, "__registry__"):
                raise NoRootClassError(cls)
            cls.__registry__[key] = cls
        return cls

    def __init__(
        cls,
        clsname: str,
        bases: typing.Iterable[type],
        attrs: dict,
        key: typing.Optional[str] = None,
        root: bool = False,
        registry_class: typing.Type[dict] = dict,
        **kwargs,
    ):
        super().__init__(clsname, bases, attrs, **kwargs)

    @property
    def keys(cls) -> typing.Iterable[typing.Any]:
        if not hasattr(cls, "__registry__"):
            raise NoRootClassError(cls)
        return cls.__registry__.keys()

    def __getitem__(cls, key: str):
        if not hasattr(cls, "__registry__"):
            raise NoRootClassError(cls)
        try:
            return cls.__registry__[key]
        except KeyError:
            raise NoMatchingSubclassError(key)

    def __setitem__(cls, key: str, target: type):
        if not hasattr(cls, "__registry__"):
            raise NoRootClassError(cls)
        if not isinstance(target, IndexedClassMeta) or cls not in target.mro():
            raise SubclassValidationError(cls, target)
        cls.__registry__[key] = target

    def __delitem__(cls, key: str):
        if not hasattr(cls, "__registry__"):
            raise NoRootClassError(cls)
        try:
            del cls.__registry__[key]
        except KeyError:
            raise NoMatchingSubclassError(key)


class AbstractIndexedClassMeta(IndexedClassMeta, ABCMeta):
    pass


class IndexedClass(metaclass=IndexedClassMeta):
    pass


class AbstractIndexedClass(metaclass=AbstractIndexedClassMeta):
    pass
