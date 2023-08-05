from ._database import geezDB
from ._misc import _Misc
from .converter import Convert
from .func import Funci
from .funcb import FuncBot
from .helpers import Helpers
from .hosting import where_hosted
from .Inlinebot import InlineBot
from .queue import Queue


class Methods(
    _Misc,
    Changers,
    Convert,
    Funci,
    FuncBot,
    InlineBot,
    Helpers,
    Queues,
    Thumbnail,
):
    pass
