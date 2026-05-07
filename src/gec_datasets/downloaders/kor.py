from .base import DownloaderBase, Metadata
import subprocess
import shutil
import itertools

class DownloaderKor(DownloaderBase):
    name: str = 'kor'
    available = [f'kor-{t}-{split}' for t, split in itertools.product(['learner', 'native'], ['train', 'dev', 'test'])]

    def download(self):
        if not (self.base_path / "korean_learner/").exists():
            zip_path = self.base_path / 'Preprocessed.zip'
            if not zip_path.exists():
                raise FileNotFoundError(f'{zip_path} is not found. Please request the data from https://docs.google.com/forms/d/e/1FAIpQLSfewjAmqcrKF5GDYuIWOfyMVBI3FN6tCwI8jalzQNhGoVAlRg/viewform in advance.')
            subprocess.run(f'unzip {zip_path} -d {self.base_path}'.split(' '))

        for t, split in itertools.product(['learner', 'native'], ['train', 'dev', 'test']):
            data_path = self.base_path.parent / f'kor-{t}-{split}'
            data_path.mkdir(parents=True, exist_ok=True)
            prefix = 'korean_learner' if t == 'learner' else 'native'
            if (t, split) == ('native', 'train'):
                # this combination provides only M2 format, so we extract srcs and refs.
                self.m2_to_src(self.base_path / f'Preprocessed/{prefix}/{prefix}_{split}.m2', data_path / "src.txt")
                self.m2_to_raw(self.base_path / f'Preprocessed/{prefix}/{prefix}_{split}.m2', 0, data_path / "ref0.txt")
                shutil.copy(
                    self.base_path / f'Preprocessed/{prefix}/{prefix}_{split}.m2',
                    data_path / f"m2.txt"
                )
            else:
                shutil.copy(
                    self.base_path / f"Preprocessed/{prefix}/{prefix}_{'val' if split == 'dev' else split}_original.txt",
                    data_path / f"src.txt"
                )
                shutil.copy(
                    self.base_path / f"Preprocessed/{prefix}/{prefix}_{'val' if split == 'dev' else split}_corrected.txt",
                    data_path / f"ref0.txt"
                )
                shutil.copy(
                    self.base_path / f"Preprocessed/{prefix}/{prefix}_{'val' if split == 'dev' else split}.m2",
                    data_path / f"m2.txt"
                )
            self.save_metadata(
                Metadata(
                    name=f'kor-{t}-{split}',
                    lang='ko',
                    split=split,
                    paper_url='https://aclanthology.org/2023.acl-long.371',
                    data_url="https://docs.google.com/forms/d/e/1FAIpQLSfewjAmqcrKF5GDYuIWOfyMVBI3FN6tCwI8jalzQNhGoVAlRg/viewform",
                ),
                save_dir=data_path
            )