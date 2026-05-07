from .base import DownloaderBase, Metadata
import subprocess
import shutil
import itertools

class DownloaderUNLP2023(DownloaderBase):
    name: str = 'unlp2023'
    available: list[str] = [f'unlp2023-{mode}-{split}' for mode, split in itertools.product(['gec-only', 'gec-fluency'], ['train', 'dev'])]

    def download(self):
        url = "https://github.com/unlp-workshop/unlp-2023-shared-task.git"
        if not (self.base_path / 'unlp-2023-shared-task').exists():
            subprocess.run(
                f"git clone {url} {str(self.base_path)}/unlp-2023-shared-task".split(' '),
                check=True,
            )
        for mode in ['gec-only', 'gec-fluency']:
            for split in ['valid', 'train']:
                data_path = self.base_path.parent / f"unlp2023-{mode}-{'train' if split == 'train' else 'dev'}"
                data_path.mkdir(parents=True, exist_ok=True)
                shutil.copy(
                    self.base_path / f'unlp-2023-shared-task/data/{mode}/{split}.src.tok',
                    data_path / "src.txt"
                )
                shutil.copy(
                    self.base_path / f'unlp-2023-shared-task/data/{mode}/{split}.tgt.tok',
                    data_path / "ref0.txt"
                )
                m2_file = self.base_path / f'unlp-2023-shared-task/data/{mode}/{split}.m2'
                shutil.copy(m2_file, data_path / "m2.txt")
                self.save_metadata(
                    Metadata(
                        name=f'unlp2023-{mode}-{split}',
                        lang='uk',
                        split=split,
                        paper_url='https://aclanthology.org/2023.unlp-1.16/',
                        data_url='https://github.com/unlp-workshop/unlp-2023-shared-task',
                    ),
                    save_dir=data_path
                )