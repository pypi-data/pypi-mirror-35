import pytest

from star_builder import Service, inject
from star_builder.bases.exceptions import Readonly


class A:
    pass


class MyService(Service):

    aaa = inject << A


def test_inject_prop_annotation():
    my_service = MyService()
    assert my_service.resolve.__annotations__["aaa"] == A


def test_inject_return_annotation():
    my_service = MyService()
    assert my_service.resolve.__annotations__["return"] == MyService


def test_assign_value():
    my_service = MyService()
    a = A()
    my_service = my_service.resolve(a)
    assert a is my_service.aaa


def test_readonly():
    my_service = MyService()
    a = A()
    my_service = my_service.resolve(a)
    with pytest.raises(Readonly):
        my_service.aaa = 1


class B:
    pass


def test_have_resolve():
    class HaveResolveService(Service):
        a = inject << A

        def resolve(self, b: B):
            self.b = b
            return self

    service = HaveResolveService()

    assert "b" in service.resolve.__annotations__
    assert "a" not in service.resolve.__annotations__


def test_empty_inject():
    class EmptyService(Service):
        pass

    service = EmptyService()
    assert service.resolve.__annotations__["return"] == EmptyService


def test_default():
    class DefaultService(Service):
        a = inject(default=3) << A

    service = DefaultService()
    service = service.resolve()
    assert service.a == 3
    service = service.resolve(2)
    assert service.a == 2


def test_inherit1():
    class Father(Service):
        a = inject << A

    class Child(Father):
        b = inject << B

    service = Child()
    assert service.resolve.__annotations__["return"] == Child
    assert service.resolve.__annotations__["a"] == A
    assert service.resolve.__annotations__["b"] == B
    service = service.resolve(3, 6)
    assert service.a == 3
    assert service.b == 6


def test_inherit2():
    class Father(Service):
        a = inject << A

    class Child(Father):
        a = inject << A

    service = Child()
    assert service.resolve.__annotations__["return"] == Child
    assert service.resolve.__annotations__["a"] == A
    service = service.resolve(3)


def test_inherit3():
    class Father(Service):
        a = inject << A

    class Child(Father):
        a = inject << B

    service = Child()
    assert service.resolve.__annotations__["return"] == Child
    assert service.resolve.__annotations__["a"] == B
    assert service.resolve.__annotations__["qwertrewq_a"] == A
    service = service.resolve(3, 5)
    assert service.a == 5


def test_inherit4():
    class Father(Service):
        def resolve(self, a: A):
            print(a)
            return self

    class Child(Father):
        a = inject << B

    service = Child()
    assert service.resolve.__annotations__["return"] == Child
    assert service.resolve.__annotations__["a"] == B
    assert service.resolve.__annotations__["qwertrewq_a"] == A
    service = service.resolve(3, 5)
    assert service.a == 5


def test_inherit5():
    class Father(Service):
        def resolve(self, b: B, a: A):
            print(a)
            return self

    class Child(Father):
        c = inject << B
        a = inject << A

    service = Child()
    assert service.resolve.__annotations__["return"] == Child
    assert service.resolve.__annotations__["a"] == A
    service = service.resolve(4, 3, 3)


def test_inherit6():
    class Father(Service):
        def resolve(self, b: B, a: int=10):
            print(a)
            return self

    class Child(Father):
        c = inject << B
        a = inject << A

    service = Child()
    assert service.resolve.__annotations__["return"] == Child
    assert service.resolve.__annotations__["a"] == A
    service = service.resolve(4, 3, 7)


def test_inherit7():
    """
    a: A=10不会生效，在子类中的定义会无视父类的参数列表
    :return:
    """
    class Father(Service):
        def resolve(self, b: B, a: A=10):
            print(a)
            return self

    class Child(Father):
        c = inject << B
        a = inject << A

    service = Child()
    assert service.resolve.__annotations__["return"] == Child
    assert service.resolve.__annotations__["a"] == A
    service = service.resolve(4, 3, 12)
    assert service.a == 3


