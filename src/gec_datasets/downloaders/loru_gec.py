from .base import DownloaderBase, Metadata
import subprocess
import shutil

class DownloaderLORuGEC(DownloaderBase):
    name: str = 'loru-gec'
    available = [f'loru-gec-{split}' for split in ['dev', 'test']]

    def download(self):
        url = "https://github.com/ReginaNasyrova/LORuGEC.git"
        if not (self.base_path / "LORuGEC").exists():
            subprocess.run(
                f"git clone {url} {str(self.base_path)}/LORuGEC".split(' '),
                check=True,
            )
        for split in ['dev', 'test']:
            data_path = self.base_path.parent / f"loru-gec-{split}"
            data_path.mkdir(parents=True, exist_ok=True)
            m2_file = self.base_path / f"LORuGEC/LORuGEC.{split if split =='test' else 'val'}.m2"
            shutil.copy(m2_file, data_path / f"m2.txt")
            self.m2_to_src(m2_file, data_path / "src.txt")
            self.m2_to_raw(m2_file, 0, data_path / "ref0.txt")
            self.save_metadata(
                Metadata(
                    name=f'loru-gec-{split}',
                    lang='ru',
                    split=split,
                    paper_url='https://aclanthology.org/2025.bea-1.38/',
                    data_url="https://github.com/ReginaNasyrova/LORuGEC",
                ),
                save_dir=data_path
            )