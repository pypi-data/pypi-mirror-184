from velait.velait_fastapi.connections.exceptions import RequestError


class NotAuthorizedError(RequestError):
    pass
