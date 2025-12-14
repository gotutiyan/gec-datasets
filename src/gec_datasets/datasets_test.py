import pytest
from gec_datasets import GECDatasets
import itertools

cases = [
    # ("conll14", 1312, 2),
    # ("conll13", 1381, 1),
    # ("jfleg-dev", 754, 4),
    # ("jfleg-test", 747, 4),
    # ("fce-train", 28350, 1),
    # ("fce-dev", 2191, 1),
    # ("fce-test", 2695, 1),
    # ("cweb-g-test", 3981, 2),
    # ("cweb-g-dev", 3867, 2),
    # ("cweb-s-test", 2864, 2),
    # ("cweb-s-dev", 2862, 2),
    ("bea19-test", 4477, 0),
    ("bea19-dev", 4384, 1),
    ("wi-locness-train", 34308, 1),
    # ("troy-1bw-train", 1172689, 1),
    # ("troy-1bw-dev", 23933, 1),
    # ("troy-blogs-train", 1244011, 1),
    # ("troy-blogs-dev", 25388, 1),
    # ("pie-synthetic-a1", 8865347, 1),
    # ("pie-synthetic-a2", 8865347, 1),
    # ("pie-synthetic-a3", 8865347, 1),
    # ("pie-synthetic-a4", 8865347, 1),
    # ("pie-synthetic-a5", 8865347, 1),
    # ("lang8-train", 1037561, 1),
    # ("nucle-train", 57151, 1),
]


class TestGECDatasets:
    @pytest.fixture(scope="class")
    def gec(self):
        return GECDatasets()

    @pytest.mark.parametrize("data_id,num_sents,num_refs", cases)
    def test_loading(self, gec, data_id, num_sents, num_refs):
        data = gec.load(data_id)
        assert len(data.srcs) == num_sents
        assert len(data.refs) == num_refs
        assert data.metadata is not None
        if data_id != 'bea19-test':
            sent_lists = [data.srcs] + data.refs
            for s1, s2 in itertools.combinations(sent_lists, 2):
                # source and references have the same number of sentences.
                assert len(s1) == len(s2)
                # Check that src and refs are being read from diffent files.
                assert any([ss1 != ss2 for ss1, ss2 in zip(s1, s2)])
