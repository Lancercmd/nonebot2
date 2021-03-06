from nonebot.typing import Optional
from nonebot.exception import (AdapterException, ActionFailed as
                               BaseActionFailed, NetworkError as
                               BaseNetworkError, ApiNotAvailable as
                               BaseApiNotAvailable)


class CQHTTPAdapterException(AdapterException):

    def __init__(self):
        super().__init__("cqhttp")


class ActionFailed(BaseActionFailed, CQHTTPAdapterException):
    """
    :说明:

      API 请求返回错误信息。

    :参数:

      * ``retcode: Optional[int]``: 错误码
    """

    def __init__(self, retcode: Optional[int] = None):
        super().__init__()
        self.retcode = retcode

    def __repr__(self):
        return f"<ActionFailed retcode={self.retcode}>"

    def __str__(self):
        return self.__repr__()


class NetworkError(BaseNetworkError, CQHTTPAdapterException):
    """
    :说明:

      网络错误。

    :参数:

      * ``retcode: Optional[int]``: 错误码
    """

    def __init__(self, msg: Optional[str] = None):
        super().__init__()
        self.msg = msg

    def __repr__(self):
        return f"<NetWorkError message={self.msg}>"

    def __str__(self):
        return self.__repr__()


class ApiNotAvailable(BaseApiNotAvailable, CQHTTPAdapterException):
    pass
