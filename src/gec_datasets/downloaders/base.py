import abc
from dataclasses import dataclass
import json
from pathlib import Path
import requests
import subprocess
import requests
import tarfile
import shutil
from gecommon import Parallel

@dataclass
class Metadata:
    name: str = None
    lang: str = None
    split: str = None
    paper_url: str = None
    data_url: str = None

class DownloaderBase(abc.ABC):
    name: str = 'base'

    def __init__(self, base_path: str = 'gec_datasets_base/'):
        self.base_path = base_path / self.name
        self.base_path.mkdir(parents=True, exist_ok=True)
        
    @classmethod
    def get_ids(self):
        return []

    @abc.abstractmethod
    def download(self):
        raise NotImplementedError

    def download_and_extract(self, url, dest_path, extract=True):
        dest_path = Path(dest_path)
        dest_path.mkdir(parents=True, exist_ok=True)
        tar_file = dest_path / "temp.tar.gz"

        print(f"Downloading from {url} to {tar_file}...")
        response = requests.get(url, stream=True)
        with open(tar_file, "wb") as f:
            shutil.copyfileobj(response.raw, f)

        if extract:
            print(f"Extracting {tar_file}...")
            with tarfile.open(tar_file, "r:gz") as tar:
                tar.extractall(path=dest_path)
            tar_file.unlink()

    def m2_to_raw(self, m2_file, ref_id, output_file):
        print(f"Processing M2 file: {m2_file} with ref_id={ref_id}...")
        gec = Parallel.from_m2(m2_file, ref_id=ref_id)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w") as f:
            f.write("\n".join(gec.trgs) + "\n")

    def m2_to_src(self, m2_file, output_file):
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w") as src_out:
            for line in open(m2_file):
                if line.startswith("S"):
                    src_out.write(" ".join(line.split(" ")[1:]))

    def save_metadata(self, metadata: Metadata, save_dir: str=None):
        if save_dir is None:
            save_dir = self.base_path
        save_dir.mkdir(parents=True, exist_ok=True)
        json.dump(
            metadata.__dict__,
            open(save_dir / 'metadata.json', 'w'),
            indent=2
        )

# === template ====
# from dataclasses import dataclass
# from .base import DownloaderBase, Metadata

# class DownloaderBase(DownloaderBase):
#     name: str = 'base'
        
#     @classmethod
#     def get_ids(self):
#         return []

#     def download(self):
#         pass
