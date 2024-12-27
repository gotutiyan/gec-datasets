import pytest
from gec_datasets import GECDatasets

cases = [
    ("conll14", 1312, 2),
    ("conll13", 1381, 1),
    ("jfleg-dev", 754, 4),
    ("jfleg-test", 747, 4),
    ("fce-train", 28350, 1),
    ("fce-dev", 2191, 1),
    ("fce-test", 2695, 1),
    ("cweb-g-test", 3981, 2),
    ("cweb-g-dev", 3867, 2),
    ("cweb-s-test", 2864, 2),
    ("cweb-s-dev", 2862, 2),
    ("bea19-test", 4477, 0),
    ("bea19-dev", 4384, 1),
    ("wi_locness-train", 34308, 1),
]


class TestGECDatasets:
    @pytest.fixture(scope="class")
    def gec(self):
        return GECDatasets("test-dir")

    @pytest.mark.parametrize("data_id,num_sents,num_refs", cases)
    def test_loading(self, gec, data_id, num_sents, num_refs):
        data = gec.load(data_id)
        assert len(data.srcs) == num_sents
        assert len(data.refs) == num_refs
        for ref in data.refs:
            assert len(ref) == num_sents
