import os
from pathlib import Path
from dataclasses import dataclass
import json
from .downloaders import (
    Metadata,
    get_downloader_list
)

class GECDatasets:
    def __init__(self, base_path="gec_datasets_base/", custom_downloaders=[]):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
        self.custom_downloaders = custom_downloaders
        # Validation for custom downloaders
        for custom_cls in custom_downloaders:
            assert hasattr(custom_cls, 'available')

    @dataclass
    class GECData:
        srcs: list[str] = None
        refs: list[list[str]] = None
        m2_path: str = None  # will be used v.0.2.1?
        metadata: Metadata = None

    def available(self):
        ids = []
        for _cls in get_downloader_list() + self.custom_downloaders:
            ids += _cls.available
        return ids

    def download(self, data_id):
        for download_cls in get_downloader_list() + self.custom_downloaders:
            if data_id in download_cls.available:
                downloader = download_cls(base_path=self.base_path)
                downloader.download()
                return
        raise ValueError(
            f"The data_id={data_id} is invalid. It should be in: {self.available()})."
        )

    def load(self, data_id: str) -> GECData:
        data_path = self.base_path / data_id
        src_file = data_path / "src.txt"
        if not src_file.exists():
            self.download(data_id)

        with open(src_file, "r", encoding="utf-8") as f:
            srcs = [line.strip() for line in f]

        refs = []
        ref_index = 0
        while True:
            ref_file = data_path / f"ref{ref_index}.txt"
            if not ref_file.exists():
                break
            with open(ref_file, "r", encoding="utf-8") as f:
                refs.append([line.strip() for line in f])
            ref_index += 1

        if len(refs) > 0 and not all(len(ref) == len(srcs) for ref in refs):
            raise ValueError(
                "Mismatch in number of sentences between src.txt and ref*.txt files."
            )

        metadata = None
        if (data_path / 'metadata.json').exists():
            metadata_dict = json.load(open(data_path / 'metadata.json'))
            metadata = Metadata(**metadata_dict)
        return self.GECData(srcs=srcs, refs=refs, metadata=metadata)
