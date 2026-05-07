from .base import DownloaderBase, Metadata
import subprocess
import shutil
import json

class DownloaderKNCT(DownloaderBase):
    name: str = 'k-nct'
    available = ['k-nct-test']

    def remove_error_tags(self, sent):
        idx = 1
        while f'<e{idx}>' in sent:  # check for <e1>, <e2> ...
            sent = sent.replace(f'<e{idx}>', '').replace(f'</e{idx}>', '')
            idx += 1

        # For Line 21 in the dataset because it contains only <e2>.
        sent = sent.replace(f'<e2>', '').replace(f'</e2>', '')

        return sent
            

    def download(self):
        url = "https://github.com/seonminkoo/K-NCT.git"
        if not (self.base_path / "K-NCT").exists():
            subprocess.run(
                f"git clone {url} {str(self.base_path)}/K-NCT".split(' '),
                check=True,
            )
        data_path = self.base_path.parent / f"k-nct-test"
        data_path.mkdir(parents=True, exist_ok=True)
        json_file = self.base_path / f"K-NCT/K-NCT_v1.4.json"
        content = json.load(open(json_file))
        srcs = [self.remove_error_tags(c["error_sentence"]) for c in content['data']]
        refs = [c["correct_sentence"] for c in content['data']]
        assert len(srcs) == len(refs)
        with open(data_path / 'src.txt', 'w') as f:
            f.write('\n'.join(srcs))
        with open(data_path / 'ref0.txt', 'w') as f:
            f.write('\n'.join(refs))
        self.save_metadata(
            Metadata(
                name=f'k-nct-test',
                lang='ko',
                split='test',
                paper_url='https://ieeexplore.ieee.org/abstract/document/9938990',
                data_url="https://github.com/seonminkoo/K-NCT",
            ),
            save_dir=data_path
        )