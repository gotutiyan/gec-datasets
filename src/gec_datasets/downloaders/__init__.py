from .base import DownloaderBase, Metadata
from .conll13 import DownloaderCoNLL2013
from .conll14 import DownloaderCoNLL2014
from .wi_locness import DownloaderWiLocness
from .jfleg import DownloaderJFLEG
from .cweb import DownloaderCWEB
from .fce import DownloaderFCE
from .nucle import DownloaderNUCLE
from .lang8 import DownloaderLang8BEA19
from .troy_1bw import DownloaderTroy1BW
from .troy_blogs import DownloaderTroyBlogs
from .pie_synthetic import DownloaderPIESynthetic

def get_downloader_list():
    return [
        DownloaderCoNLL2013,
        DownloaderCoNLL2014,
        DownloaderWiLocness,
        DownloaderJFLEG,
        DownloaderCWEB,
        DownloaderFCE,
        DownloaderNUCLE,
        DownloaderLang8BEA19,
        DownloaderTroy1BW,
        DownloaderTroyBlogs,
        DownloaderPIESynthetic
    ]