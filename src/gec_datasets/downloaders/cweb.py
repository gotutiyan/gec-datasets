from dataclasses import dataclass
from .base import DownloaderBase, Metadata
import shutil
import subprocess

class DownloaderCWEB(DownloaderBase):
    name: str = 'cweb'
    available: list[str] = ['cweb-g-dev', 'cweb-g-test', 'cweb-s-dev', 'cweb-s-test']

    def download(self):
        url = "https://github.com/SimonHFL/CWEB.git"
        if not (self.base_path / 'CWEB').exists():
            subprocess.run(
                f"git clone {url} {str(self.base_path)}/CWEB".split(' '),
                check=True
            )
        for split in ['dev', 'test']:
            for sg in 'SG':
                data_path = self.base_path.parent / f'cweb-{sg.lower()}-{split}'
                data_path.mkdir(parents=True, exist_ok=True)
                shutil.copy(
                    self.base_path / f"CWEB/data/tokenized/CWEB-{sg}.{split}.tok.source", data_path / "src.txt"
                )
                norm = '.norm' if f'cweb-{sg.lower()}-{split}' == 'cweb-g-test' else ''
                shutil.copy(
                    self.base_path / f"CWEB/data/tokenized/CWEB-{sg}.{split}{norm}.tok.ann1", data_path / "ref0.txt"
                )
                shutil.copy(
                   self.base_path / f"CWEB/data/tokenized/CWEB-{sg}.{split}.tok.ann2", data_path / "ref1.txt"
                )
                self.save_metadata(
                    Metadata(
                        name=f'cweb-{sg.lower()}-{split}',
                        lang='en',
                        split=split,
                        paper_url='https://www.aclweb.org/anthology/2020.emnlp-main.680',
                        data_url=url,
                    ),
                    save_dir=data_path
                )       
        return