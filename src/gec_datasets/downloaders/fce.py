from dataclasses import dataclass
from .base import DownloaderBase, Metadata
import shutil
import subprocess

class DownloaderFCE(DownloaderBase):
    name: str = 'fce'
    available: list[str] = ['fce-train', 'fce-dev', 'fce-test']

    def download(self):
        url = "https://www.cl.cam.ac.uk/research/nl/bea2019st/data/fce_v2.1.bea19.tar.gz"
        if not (self.base_path / "fce_v2.1.bea19.tar.gz").exists():
            self.download_and_extract(url, self.base_path)
        for split in ['train', 'dev', 'test']:
            data_path = self.base_path.parent / f'fce-{split}'
            data_path.mkdir(parents=True, exist_ok=True)
            dev_m2_file = self.base_path / f"fce/m2/fce.{split}.gold.bea19.m2"
            self.m2_to_src(dev_m2_file, data_path / "src.txt")
            self.m2_to_raw(dev_m2_file, 0, data_path / "ref0.txt")
            self.save_metadata(
                Metadata(
                    name=f'fce-{split}',
                    lang='en',
                    split=split,
                    paper_url='https://aclanthology.org/P11-1019/',
                    data_url=url,
                ),
                save_dir=data_path
            )       
        return