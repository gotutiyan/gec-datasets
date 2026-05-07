from .base import DownloaderBase, Metadata
import subprocess
import shutil

class DownloaderRONACC(DownloaderBase):
    name: str = f"ronacc"
    available: list[str] = [f"ronacc-{split}" for split in ['train', 'dev', 'test']]

    def download(self):
        url = "https://drive.google.com/file/d/1un7Gy2EbBuroMyyrn3lOq7N76ODMxYfR/view"
        download_path = self.base_path / 'RONACC_corpus.zip'
        if not download_path.exists():
            subprocess.run(
                f"gdown --fuzzy {url} -O {download_path}".split(' '),
                check=True,
            )
            subprocess.run(f"unzip {download_path} -d {self.base_path}".split(' '))

        for split in ['dev', 'test']:
            data_path = self.base_path.parent / f"ronacc-{split}"
            data_path.mkdir(parents=True, exist_ok=True)
            shutil.copy(
                self.base_path / f"cna/{split}/{split}_added_wronged.txt",
                data_path / "src.txt"
            )
            shutil.copy(
                self.base_path / f"cna/{split}/{split}_added_gold.txt",
                data_path / "ref0.txt"
            )
            self.save_metadata(
                Metadata(
                    name=f"ronacc-{split}",
                    lang='ro',
                    split=split,
                    paper_url='https://ieeexplore.ieee.org/abstract/document/9288338',
                    data_url=url,
                ),
                save_dir=data_path
            )
        # For training data
        data_path = self.base_path.parent / f"ronacc-train"
        data_path.mkdir(parents=True, exist_ok=True)
        content = (self.base_path / f"cna/train/train_combined.txt").read_text().split('\n')
        srcs = content[::2]
        trgs = content[1::2]
        (data_path / 'src.txt').write_text('\n'.join(srcs))
        (data_path / 'ref0.txt').write_text('\n'.join(trgs))
        self.save_metadata(
            Metadata(
                name=f"ronacc-train",
                lang='ro',
                split='train',
                paper_url='https://ieeexplore.ieee.org/abstract/document/9288338',
                data_url=url,
            ),
            save_dir=data_path
        )