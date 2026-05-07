from .base import DownloaderBase, Metadata
import subprocess
import shutil
import itertools

class DownloaderGECCC(DownloaderBase):
    name: str = 'geccc'
    available = [f'geccc-{unit}-{split}' for unit, split in itertools.product(['sentence', 'paragraph'], ['train', 'dev', 'test'])]

    def download(self):
        path = self.base_path / 'geccc.zip'
        if not (self.base_path / 'README.md').exists():
            if not path.exists():
                subprocess.run(f'curl -o {path} https://lindat.mff.cuni.cz/repository/server/api/core/bitstreams/handle/11234/1-4639/geccc.zip'.split(' '))
                # raise FileNotFoundError(f'{path} is not found. Please download it from https://lindat.mff.cuni.cz/repository/items/6bb20485-b97d-461b-a5cb-14df813cb5c7 in advance.')
                subprocess.run(f"unzip {path} -d {self.base_path}".split(' '))
        for unit, split in itertools.product(['sentence', 'paragraph'], ['train', 'dev', 'test']):
            data_path = self.base_path.parent / f'geccc-{unit}-{split}'
            data_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(self.base_path / f'data/{split}/{unit}.m2', data_path / 'm2.txt')
            shutil.copy(self.base_path / f'data/{split}/{unit}.input', data_path / 'src.txt')
            shutil.copy(self.base_path / f'data/{split}/{unit}.gold', data_path / 'ref0.txt')
            self.save_metadata(
                Metadata(
                    name=f'geccc-{unit}-{split}',
                    lang='cs',
                    split=split,
                    paper_url="https://aclanthology.org/2022.tacl-1.26/",
                    data_url="https://lindat.mff.cuni.cz/repository/items/6bb20485-b97d-461b-a5cb-14df813cb5c7",
                ),
                save_dir=data_path
            )