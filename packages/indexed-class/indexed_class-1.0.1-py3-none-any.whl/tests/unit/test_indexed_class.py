from abc import ABC

from pytest import raises

from indexed_class import (AbstractIndexedClass, AbstractIndexedClassMeta,
                           IndexedClass, IndexedClassMeta,
                           NoMatchingSubclassError, NoRootClassError,
                           SubclassValidationError)


class TestMeta:
    def test_prepare_simple(self):
        data = IndexedClassMeta.__prepare__("TestMeta", (object,))
        assert isinstance(data, dict), f"failed to initialize class dict, got {data}"
        assert (
            data["root"] is False
        ), f"root initialized incorrectly, got {data['root']}"
        assert data["key"] is None, f"key initialized incorrectly, got {data['key']}"

    def test_prepare_inheritance(self):
        class ParentMeta(type):
            @classmethod
            def __prepare__(meta, *args, kwarg1, kwarg2):
                return {**super().__prepare__(*args), "kwargs": [kwarg1, kwarg2]}

            def __new__(meta, *args, kwarg1, kwarg2):
                return super().__new__(meta, *args)

            def __init__(cls, *args, kwarg1, kwarg2):
                pass

        class ChildMeta(IndexedClassMeta, ParentMeta):
            pass

        with raises(TypeError):
            data = ChildMeta.__prepare__("TestMeta", (object,))

        data = ChildMeta.__prepare__("TestMeta", (object,), kwarg1=1, kwarg2=2)
        assert isinstance(data, dict), f"failed to initialize class dict, got {data}"
        assert (
            data["root"] is False
        ), f"root initialized incorrectly, got {data['root']}"
        assert data["key"] is None, f"key initialized incorrectly, got {data['key']}"
        assert data["kwargs"] == [
            1,
            2,
        ], f"kwargs initialized incorrectly, got {data['kwargs']}"

    def test_new(self):
        def factory(
            name="TestMeta", bases=(object,), root=False, key=None, registry_class=dict
        ):
            return IndexedClassMeta(
                name,
                bases,
                IndexedClassMeta.__prepare__(name, bases, key=key, root=root),
                key=key,
                root=root,
                registry_class=registry_class,
            )

        cls = factory()
        assert cls.root is False, f"root initialized incorrectly, got {cls.root}"
        assert cls.key is None, f"key initialized incorrectly, got {cls.key}"
        assert not hasattr(cls, "__registry__"), "registry initialized, should be UNDEF"
        with raises(NoRootClassError):
            cls.keys

        with raises(NoRootClassError):
            cls = factory(key="k1")

        cls = factory(root=True, registry_class=int)
        assert cls.root is True, f"root initialized incorrectly, got {cls.root}"
        assert cls.key is None, f"key initialized incorrectly, got {cls.key}"
        assert isinstance(
            cls.__registry__, int
        ), f"registry class initialized incorrectly, got {cls.__registry__.__class__.__name__}"

        parent = factory(name="Parent", root=True)
        assert (
            parent.root is True
        ), f"parent root initialized incorrectly, got {parent.root}"
        assert (
            parent.key is None
        ), f"parent key initialized incorrectly, got {parent.key}"
        assert hasattr(parent, "__registry__"), "registry not initialized, should be {}"
        assert (
            parent.__registry__ == {}
        ), f"parent registry initialized incorrectly, got {parent.__registry__}"
        child = factory(name="Child", bases=(parent,), key="k1")
        assert (
            child.root is False
        ), f"child root initialized incorrectly, got {child.root}"
        assert child.key == "k1", f"child key initialized incorrectly, got {child.key}"
        assert (
            parent.keys == {"k1": None}.keys()
        ), f"parent keys value incorrect, got {parent.keys}"
        assert (
            parent.keys == child.keys
        ), f"child keys value incorrect, got {child.keys}"
        assert (
            parent.__registry__ is child.__registry__
        ), f"parent-child registry mismatch"
        assert (
            parent.__registry__.get(child.key) is child
        ), "child not assigned to own index"

    def test_getitem(self):
        def factory(
            name="TestMeta", bases=(object,), root=False, key=None, registry_class=dict
        ):
            return IndexedClassMeta(
                name,
                bases,
                IndexedClassMeta.__prepare__(name, bases, key=key, root=root),
                key=key,
                root=root,
                registry_class=registry_class,
            )

        cls = factory()
        with raises(NoRootClassError):
            cls[1] = 1

        parent = factory(name="Parent", root=True)
        with raises(SubclassValidationError):
            parent[1] = 1
        child = factory(name="Child", bases=(parent,), key="k1")
        parent[1] = child
        assert 1 in parent.__registry__, "key add failed"
        assert (
            parent.keys == {1: None, "k1": None}.keys()
        ), f"keys value incorrect, got {parent.keys}"
        assert (
            parent[1] is child
        ), f"invalid __getitem__ value for key '1', got {parent[1]}"
        del parent[1]
        assert 1 not in parent.__registry__, "key removal failed"
        assert parent.keys == {"k1": None}.keys(), "key removal failed"
        with raises(NoMatchingSubclassError):
            parent[1]
