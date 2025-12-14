from dataclasses import dataclass
from .base import DownloaderBase, Metadata
import shutil
import subprocess

class DownloaderPIESynthetic(DownloaderBase):
    name: str = f"pie-synthetic"
    available: list[str] = [f"pie-synthetic-a{num}" for num in range(1, 6)]

    def download(self):
        url = "https://drive.google.com/file/d/1bl5reJ-XhPEfEaPjvO45M7w0yN-0XGOA/view"
        download_path = self.base_path / 'synthetic.zip'
        if not download_path.exists():
            subprocess.run(
                f"gdown --fuzzy {url} -O {download_path}".split(' '),
                check=True,
            )
            subprocess.run(f"unzip {download_path} -d {self.base_path}".split(' '))

        for name in ['a1', 'a2', 'a3', 'a4', 'a5']:
            data_path = self.base_path.parent / f"pie-synthetic-{name}"
            data_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(
                self.base_path / f"{name}/{name}_train_incorr_sentences.txt",
                data_path / "src.txt"
            )
            shutil.copy(
                self.base_path / f"{name}/{name}_train_corr_sentences.txt",
                data_path / "ref0.txt"
            )
            self.save_metadata(
                Metadata(
                    name=f"pie-synthetic-{name}",
                    lang='en',
                    split='train',
                    paper_url='https://aclanthology.org/D19-1435/',
                    data_url=url,
                ),
                save_dir=data_path
            )
        return