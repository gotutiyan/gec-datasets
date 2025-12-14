from dataclasses import dataclass
from .base import DownloaderBase, Metadata
import shutil
import subprocess
import tarfile

class DownloaderNUCLE(DownloaderBase):
    name: str = 'nucle'
    available: list[str] = ['nucle-train']

    def download(self):
        tar_file = self.base_path / "release3.3.tar.bz2"
        if not tar_file.exists():
            raise FileNotFoundError(f'{tar_file} is not found. Please download release3.3.tar.bz2 from https://sterling8.d2.comp.nus.edu.sg/nucle_download/nucle.php , and put it on {tar_file} in advance.')

        with tarfile.open(tar_file, "r:bz2") as tar:
            tar.extractall(path=self.base_path)
        tar_file.unlink()

        data_path = self.base_path.parent / 'nucle-train'
        m2_file = self.base_path / "release3.3/bea2019/nucle.train.gold.bea19.m2"
        self.m2_to_src(m2_file, data_path / "src.txt")
        self.m2_to_raw(m2_file, 0, data_path / "ref0.txt")
        self.save_metadata(
            Metadata(
                name=f'nucle-train',
                lang='en',
                split='train',
                paper_url='https://www.aclweb.org/anthology/W13-1703',
                data_url='https://sterling8.d2.comp.nus.edu.sg/nucle_download/nucle.php',
            ),
            save_dir=data_path
        )       
        return