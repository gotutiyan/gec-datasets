from dataclasses import dataclass
from .base import DownloaderBase, Metadata
import shutil
import subprocess

class DownloaderTroy1BW(DownloaderBase):
    name: str = 'troy-1bw'
    available: list[str] = ['troy-1bw-train', 'troy-1bw-dev']

    def download(self):
        url = "https://drive.google.com/file/d/1aaUGLGyV3lxIbX2CIt0qw0_UM7nQUrhx/view?usp=drive_link"
        download_path = self.base_path / 'Troy-1BW.zip'
        if not download_path.exists():
            subprocess.run(
                f"gdown --fuzzy {url} -O {download_path}".split(' '),
                check=True,
            )
            subprocess.run(f"unzip {download_path} -d {self.base_path}".split(' '))
        for split in ['train', 'test']:
            data_path = self.base_path.parent / f"troy-1bw-{split if split == 'train' else 'dev'}"
            data_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(
                self.base_path / f"new_1bw/{split}_source", data_path / "src.txt"
            )
            shutil.copy(
                self.base_path / f"new_1bw/{split}_target", data_path / "ref0.txt"
            )
            self.save_metadata(
                Metadata(
                    name=f'troy-1bw-{split}',
                    lang='en',
                    split=split,
                    paper_url='https://aclanthology.org/2022.acl-long.266/',
                    data_url=url,
                ),
                save_dir=data_path
            )
        return