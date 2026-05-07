import pytest
from gec_datasets import GECDatasets
import itertools

cases = [
    # (ID, number of sentences, number of references)
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
    ("wi-locness-train", 34308, 1),
    ("troy-1bw-train", 1172689, 1),
    ("troy-1bw-dev", 23933, 1),
    ("troy-blogs-train", 1244011, 1),
    ("troy-blogs-dev", 25388, 1),
    ("pie-synthetic-a1", 8865347, 1),
    ("pie-synthetic-a2", 8865347, 1),
    ("pie-synthetic-a3", 8865347, 1),
    ("pie-synthetic-a4", 8865347, 1),
    ("pie-synthetic-a5", 8865347, 1),
    ("lang8-train", 1037561, 1),
    ("nucle-train", 57151, 1),
    ("unlp2023-gec-only-train", 32743, 1),
    ("unlp2023-gec-only-dev", 1509, 1),
    ("unlp2023-gec-fluency-train", 32734, 1),
    ("unlp2023-gec-fluency-dev", 1506, 1),
    ("akces-gec-train", 42210, 1),
    ("akces-gec-dev", 2485, 2),
    ("akces-gec-test", 2676, 2),
    ('geccc-sentence-train', 66673, 1),
    ('geccc-sentence-dev', 8478, 1),
    ('geccc-sentence-test', 7907, 1),
    ('geccc-paragraph-train', 23744, 1),
    ('geccc-paragraph-dev', 3592, 1),
    ('geccc-paragraph-test', 3242, 1),
    ('falko-merlin-train', 19237, 1),
    ('falko-merlin-dev', 2503, 1),
    ('falko-merlin-test', 2337, 1),
    ('loru-gec-dev', 348, 1),
    ('loru-gec-test', 612, 1),
    ('k-nct-test', 3000, 1),
    ('kor-learner-train', 19898, 1),
    ('kor-learner-dev', 4264, 1),
    ('kor-learner-test', 4265, 1),
    ('kor-native-train', 12292, 1),
    ('kor-native-dev', 2634, 1),
    ('kor-native-test', 2634, 1),
    ('hi-gec-train', 5696, 1),
    ('hi-gec-dev', 976, 1),
    ('hi-gec-test', 1465, 1)
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
