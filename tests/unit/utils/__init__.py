from unittest.mock import Mock

_RESOLVER_EXCUTOR = Mock()
MOCKED_GET_RESOLVER_EXECUTOR = Mock(return_value=_RESOLVER_EXCUTOR)


def call_with_mocked_resolver_factory(acallable, *args, **kargs):
    from tartiflette.resolver.factory import ResolverExecutorFactory

    old_methd = ResolverExecutorFactory.get_resolver_executor
    ResolverExecutorFactory.get_resolver_executor = (
        MOCKED_GET_RESOLVER_EXECUTOR
    )

    ret = acallable(*args, **kargs)

    ResolverExecutorFactory.get_resolver_executor = old_methd

    return ret


from unittest.mock import MagicMock


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        #  super(AsyncMock, self).__call__(*args, **kwargs)
        pass


__all__ = [
    "MOCKED_GET_RESOLVER_EXECUTOR",
    "call_with_mocked_resolver_factory",
    "AsyncMock",
]
