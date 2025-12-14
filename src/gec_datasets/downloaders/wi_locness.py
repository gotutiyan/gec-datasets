from dataclasses import dataclass
from .base import DownloaderBase, Metadata
import shutil

class DownloaderWiLocness(DownloaderBase):
    name: str = 'wi-locness'
    available: list[str] = ['bea19-dev', 'bea19-test', 'wi-locness-train']

    def download(self):
        data_path = self.base_path.parent / 'bea19-dev'
        url = "https://www.cl.cam.ac.uk/research/nl/bea2019st/data/wi+locness_v2.1.bea19.tar.gz"
        self.download_and_extract(url, self.base_path)

        m2_file = self.base_path / "wi+locness/m2/ABCN.dev.gold.bea19.m2"
        self.m2_to_src(m2_file, data_path / "src.txt")
        self.m2_to_raw(m2_file, 0, data_path / "ref0.txt")
        self.save_metadata(
            Metadata(
                name='bea19-dev',
                lang='en',
                split='dev',
                paper_url='https://aclanthology.org/W19-4406/',
                data_url=url,
            ),
            save_dir=data_path
        )

        data_path = self.base_path.parent / 'bea19-test'
        data_path.mkdir(parents=True, exist_ok=True)
        src_file = self.base_path / "wi+locness/test/ABCN.test.bea19.orig"
        shutil.copy(src_file, data_path / "src.txt")
        self.save_metadata(
            Metadata(
                name='bea19-test',
                lang='en',
                split='test',
                paper_url='https://aclanthology.org/W19-4406/',
                data_url=url,
            ),
            save_dir=data_path
        )

        data_path = self.base_path.parent / 'wi-locness-train'
        m2_file = self.base_path / "wi+locness/m2/ABC.train.gold.bea19.m2"
        self.m2_to_src(m2_file, data_path / "src.txt")
        self.m2_to_raw(m2_file, 0, data_path / "ref0.txt")
        self.save_metadata(
            Metadata(
                name='wi-locness-train',
                lang='en',
                split='train',
                paper_url='https://aclanthology.org/W19-4406/',
                data_url=url,
            ),
            save_dir=data_path
        )
        return