from .base import DownloaderBase, Metadata
import subprocess
import shutil

class DownloaderHiGEC(DownloaderBase):
    name: str = 'hi-gec'
    available = [f'hi-gec-{split}' for split in ['train', 'dev', 'test']]

    def download(self):
        url = "https://github.com/ujjwalsharmaIITB/Hi-GEC.git"
        if not (self.base_path / "Hi-GEC").exists():
            subprocess.run(
                f"git clone {url} {str(self.base_path)}/Hi-GEC".split(' '),
                check=True,
            )
        for split in ['train', 'dev', 'test']:
            data_path = self.base_path.parent / f'hi-gec-{split}'
            data_path.mkdir(parents=True, exist_ok=True)
            directories = [d for d in (self.base_path / f'Hi-GEC/data/{"valid" if split == "dev" else split}/m2').glob('R_*')]
            srcs = []
            trgs = []
            m2 = []
            # Merge error type wise data
            for d in directories:
                name = d.name  # e.g., R_ADJ
                srcs += (d / f'{name}.src').read_text().strip().split('\n')
                trgs += (d / f'{name}.tgt').read_text().strip().split('\n')
                m2 += (d / f'{name}.m2').read_text().strip().split('\n\n')
            (data_path / 'src.txt').write_text('\n'.join(srcs))
            (data_path / 'ref0.txt').write_text('\n'.join(trgs))
            (data_path / 'm2.txt').write_text('\n\n'.join(m2))
            self.save_metadata(
                Metadata(
                    name=f'hi-gec-{split}',
                    lang='hi',
                    split=split,
                    paper_url='https://aclanthology.org/2025.coling-main.406/',
                    data_url="https://github.com/ujjwalsharmaIITB/Hi-GEC",
                ),
                save_dir=data_path
            )