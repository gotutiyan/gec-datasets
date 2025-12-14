from dataclasses import dataclass
from .base import DownloaderBase, Metadata

class DownloaderCoNLL2014(DownloaderBase):
    name: str = 'conll14'
    available: list[str] = ['conll14']

    def download(self):
        url = "https://www.comp.nus.edu.sg/~nlp/conll14st/conll14st-test-data.tar.gz"
        self.download_and_extract(url, self.base_path)

        m2_file = self.base_path / "conll14st-test-data/noalt/official-2014.combined.m2"
        self.m2_to_src(m2_file, self.base_path / "src.txt")
        self.m2_to_raw(m2_file, 0, self.base_path / "ref0.txt")
        self.m2_to_raw(m2_file, 1, self.base_path / "ref1.txt")
        self.save_metadata(
            Metadata(
                name='conll14',
                lang='en',
                split='test',
                paper_url='https://aclanthology.org/W14-1701/',
                data_url=url,
            )
        )
        return