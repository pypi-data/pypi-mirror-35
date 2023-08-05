import abc
import typing


class BaseDecorator(object, metaclass=abc.ABCMeta):
    def __init__(self, func: typing.Optional[typing.Callable] = ...) -> None: ...

    @property
    def _func(self) -> typing.Optional[typing.Callable]: ...

    @abc.abstractmethod
    def _get_function_wrapper(self, func: typing.Callable) -> typing.Callable: ...

    def __call__(self, *args: typing.Tuple, **kwargs: typing.Dict) -> typing.Any: ...
