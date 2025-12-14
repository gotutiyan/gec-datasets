from dataclasses import dataclass
from .base import DownloaderBase, Metadata

class DownloaderCoNLL2013(DownloaderBase):
    name: str = 'conll13'
    available: list[str] = ['conll13']

    def download(self):
        url = "https://www.comp.nus.edu.sg/~nlp/conll13st/release2.3.1.tar.gz"
        self.download_and_extract(url, self.base_path)

        m2_file = self.base_path / "release2.3.1/original/data/official-preprocessed.m2"
        self.m2_to_src(m2_file, self.base_path / "src.txt")
        self.m2_to_raw(m2_file, 0, self.base_path / "ref0.txt")
        self.save_metadata(
            Metadata(
                name='conll13',
                lang='en',
                split='test',
                paper_url='https://aclanthology.org/W13-3601/',
                data_url='https://www.comp.nus.edu.sg/~nlp/conll13st/release2.3.1.tar.gz',
            )
        )
        return