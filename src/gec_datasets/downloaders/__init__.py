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
from .unlp2023 import DownloaderUNLP2023
from .akces_gec import DownloaderAKCESGEC
from .geccc import DownloaderGECCC
from .falko_merlin import DownloaderFalkoMerlin
from .loru_gec import DownloaderLORuGEC
from .ronacc import DownloaderRONACC
from .k_nct import DownloaderKNCT
from .kor import DownloaderKor
from .hi_gec import DownloaderHiGEC

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
        DownloaderPIESynthetic,
        DownloaderUNLP2023,
        DownloaderAKCESGEC,
        DownloaderGECCC,
        DownloaderFalkoMerlin,
        DownloaderLORuGEC,
        DownloaderRONACC,
        DownloaderKNCT,
        DownloaderKor,
        DownloaderHiGEC
    ]