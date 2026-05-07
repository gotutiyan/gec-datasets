from .base import DownloaderBase, Metadata
import subprocess
import shutil

class DownloaderFalkoMerlin(DownloaderBase):
    name: str = 'falko-merlin'
    available = [f'falko-merlin-{split}' for split in ['train', 'dev', 'test']]

    def download(self):
        url = "https://github.com/adrianeboyd/boyd-wnut2018/releases/download/wnut2018/data.tar.gz"
        if not (self.base_path / "data").exists():
            self.download_and_extract(url, self.base_path)
        for split in ['train', 'dev', 'test']:
            data_path = self.base_path.parent / f'falko-merlin-{split}'
            data_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(self.base_path / f"data/fm-{split}.m2", data_path / f"m2.txt")
            shutil.copy(self.base_path / f"data/fm-{split}.src", data_path / f"src.txt")
            shutil.copy(self.base_path / f"data/fm-{split}.trg", data_path / f"ref0.txt")
            self.save_metadata(
                Metadata(
                    name=f'falko-merlin-{split}',
                    lang='de',
                    split=split,
                    paper_url='https://aclanthology.org/W18-6111/',
                    data_url=url,
                ),
                save_dir=data_path
            )
