from .aol import Aol
from .ask import Ask
from .bing import Bing
from .dogpile import Dogpile
from .duckduckgo import Duckduckgo
from .google import Google
from .mojeek import Mojeek
from .startpage import Startpage
from .torch import Torch
from .yahoo import Yahoo
from .daumcafe import Daumcafe
from .naverkin import Naverkin
from .naverblog import Naverblog

search_engines_dict = { 
    'google': Google, 
    'bing': Bing, 
    'yahoo': Yahoo, 
    'aol': Aol, 
    'duckduckgo': Duckduckgo, 
    'startpage': Startpage, 
    'dogpile': Dogpile, 
    'ask': Ask, 
    'mojeek': Mojeek, 
    'torch': Torch,
    'daumcafe': Daumcafe,
    'naverkin': Naverkin,
    'naverblog': Naverblog
}

