from dataclasses import dataclass
from .base import DownloaderBase, Metadata
import shutil
import subprocess
import tarfile

class DownloaderLang8BEA19(DownloaderBase):
    name: str = 'lang8'
    available: list[str] = ['lang8-train']

    def download(self):
        tar_file = self.base_path / "lang8.bea19.tar.gz"
        if not tar_file.exists():
            raise FileNotFoundError(f'{tar_file} is not found. Please download lang8.bea19.tar.gz from https://docs.google.com/forms/d/e/1FAIpQLSflRX3h5QYxegivjHN7SJ194OxZ4XN_7Rt0cNpR2YbmNV-7Ag/viewform , and put it on {tar_file} in advance.')

        with tarfile.open(tar_file, "r:gz") as tar:
            tar.extractall(path=self.base_path)
        tar_file.unlink()

        data_path = self.base_path.parent / 'lang8-train'
        m2_file = self.base_path / "lang8.train.auto.bea19.m2"
        self.m2_to_src(m2_file, data_path / "src.txt")
        self.m2_to_raw(m2_file, 0, data_path / "ref0.txt")
        self.save_metadata(
            Metadata(
                name=f'lang8-train',
                lang='en',
                split='train',
                paper_url='https://aclanthology.org/I11-1017',
                data_url='https://docs.google.com/forms/d/e/1FAIpQLSflRX3h5QYxegivjHN7SJ194OxZ4XN_7Rt0cNpR2YbmNV-7Ag/viewform',
            ),
            save_dir=data_path
        )       
        return