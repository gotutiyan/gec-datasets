from dataclasses import dataclass
from .base import DownloaderBase, Metadata
import shutil
import subprocess

class DownloaderJFLEG(DownloaderBase):
    name: str = 'jfleg'
    available: list[str] = ['jfleg-dev', 'jfleg-test']

    def download(self):
        url = "https://github.com/keisks/jfleg.git"
        if not (self.base_path / 'jfleg').exists():
            subprocess.run(
                f"git clone {url} {str(self.base_path)}/jfleg".split(' '),
                check=True,
            )

        for split in ['dev', 'test']:
            data_path = self.base_path.parent / f'jfleg-{split}'
            data_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(self.base_path / f"jfleg/{split}/{split}.src", data_path / "src.txt")
            shutil.copy(self.base_path / f"jfleg/{split}/{split}.ref0", data_path / "ref0.txt")
            shutil.copy(self.base_path / f"jfleg/{split}/{split}.ref1", data_path / "ref1.txt")
            shutil.copy(self.base_path / f"jfleg/{split}/{split}.ref2", data_path / "ref2.txt")
            shutil.copy(self.base_path / f"jfleg/{split}/{split}.ref3", data_path / "ref3.txt")
            self.save_metadata(
                Metadata(
                    name=f'jfleg-{split}',
                    lang='en',
                    split=split,
                    paper_url='https://aclanthology.org/E17-2037/',
                    data_url=url,
                ),
                save_dir=data_path
            )
        return