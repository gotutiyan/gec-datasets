from .base import DownloaderBase, Metadata
import subprocess
import shutil
import re

class DownloaderAKCESGEC(DownloaderBase):
    name: str = 'akces-gec'
    available = [f'akces-gec-{split}' for split in ['train', 'dev', 'test']]

    def download(self):
        path = self.base_path / 'AKCES-GEC.zip'
        if not (self.base_path / 'README.md').exists():
            if not path.exists():
                raise FileNotFoundError(f'{path} is not found. Please download it from https://lindat.mff.cuni.cz/repository/items/ba5f9011-0282-4dff-bddd-6d30e518caeb in advance.')
            subprocess.run(f"unzip {path} -d {self.base_path}".split(' '))
        for split in ['train', 'dev', 'test']:
            data_path = self.base_path.parent / f'akces-gec-{split}'
            data_path.mkdir(parents=True, exist_ok=True)
            m2_file = self.base_path / f"{split}/{split}.all.m2"
            m2_content = m2_file.read_text()
            # Adjust the number of break lines among M2 samples
            m2_content = re.sub(r"\n{3,}", "\n\n", m2_content)
            with open(data_path / 'm2.txt', 'w') as f:
                f.write(m2_content)
            m2_file = data_path / 'm2.txt'
            self.m2_to_src(m2_file, data_path / 'src.txt')
            self.m2_to_raw(m2_file, 0, data_path / 'ref0.txt')
            if split != 'train':
                # The train set has a single reference, others have two references.
                self.m2_to_raw(m2_file, 1, data_path / 'ref1.txt')
            self.save_metadata(
                Metadata(
                    name=f'akces-gec-{split}',
                    lang='cs',
                    split=split,
                    paper_url='https://aclanthology.org/D19-5545',
                    data_url="https://lindat.mff.cuni.cz/repository/items/ba5f9011-0282-4dff-bddd-6d30e518caeb",
                ),
                save_dir=data_path
            )