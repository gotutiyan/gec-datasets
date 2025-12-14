from .datasets import GECDatasets
from .downloaders import (
    Metadata,
    DownloaderBase,
    get_downloader_list
)

__all__ = ["GECDatasets", "Metadata", "DownloaderBase"]

def available():
    ids = []
    for c in get_downloader_list():
        ids += c.available
    return ids