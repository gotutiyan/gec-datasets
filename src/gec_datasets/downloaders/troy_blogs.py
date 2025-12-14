from dataclasses import dataclass
from .base import DownloaderBase, Metadata
import shutil
import subprocess

class DownloaderTroyBlogs(DownloaderBase):
    name: str = 'troy-blogs'
    available: list[str] = ['troy-blogs-train', 'troy-blogs-dev']

    def download(self):
        url = "https://drive.google.com/file/d/1sKCxtx2k41WIdshyjQjo_gIAAbB1LWNs/view?usp=drive_link"
        download_path = self.base_path / 'Troy-Blogs.zip'
        if not download_path.exists():
            subprocess.run(
                f"gdown --fuzzy {url} -O {download_path}".split(' '),
                check=True,
            )
            subprocess.run(f"unzip {download_path} -d {self.base_path}".split(' '))
        for split in ['train', 'dev']:
            data_path = self.base_path.parent / f'troy-blogs-{split}'
            data_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(
                self.base_path / f"blogs/{split}_src", data_path / "src.txt"
            )
            shutil.copy(
                self.base_path / f"blogs/{split}_tgt", data_path / "ref0.txt"
            )
            self.save_metadata(
                Metadata(
                    name=f'troy-blogs-{split}',
                    lang='en',
                    split=split,
                    paper_url='https://aclanthology.org/2022.acl-long.266/',
                    data_url=url,
                ),
                save_dir=data_path
            )
        return