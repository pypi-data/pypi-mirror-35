class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, scope):
        async def asgi(receive, send):
            await self.handler(scope, receive, send)

        return asgi

    async def handler(self, scope, receive, send):
        raise NotImplemented()  # pragma: nocover


class ExceptionMiddleware:
    def __init__(self, app, handled_exceptions=None):
        self.app = app
        self.handled_exceptions = handled_exceptions or {}

    def __call__(self, scope):
        async def app(receive, send):
            try:
                instance = self.app(scope)
                await instance(receive, send)
            except Exception as exc:
                scope["exc"] = exc
                for cls, handler in self.handled_exceptions.items():
                    if isinstance(exc, cls):
                        instance = handler(scope)
                        await instance(receive, send)
                        return
                raise exc from None

        return app

    async def handler(self, scope, receive, send):
        raise NotImplemented()  # pragma: nocover
