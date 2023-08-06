class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, scope):
        async def asgi(receive, send):
            await self.handler(scope, receive, send)

        return asgi

    async def handler(self, scope, receive, send):
        raise NotImplemented()  # pragma: nocover
