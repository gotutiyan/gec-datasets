# gec-datasets

This library is to handle datasets of Grammatical Error Correction.


# Usage
```python
from gec_datasets import GECDatasets
gec = GECDatasets(
    base_path='datasets/'
)
conll14 = gec.load('conll14')

assert conll14.srcs is not None
assert conll14.refs is not None
# The number of sentences is 1312.
assert len(conll14.srcs) == 1312
# CoNLL-2014 contains two official references.
assert len(conll14.refs) == 2
# Each reference also contains 1312 sentences.
assert len(conll14.refs[0]) == 1312
assert len(conll14.refs[1]) == 1312
```

The dataset is stored under `base_path=`.  
The first time it is downloaded automatically, and thereafter it is loaded from the saved files.

```
datasets/
├── conll14
│   ├── ref0.txt
│   ├── ref1.txt
│   └── src.txt
├── bea19-dev
│   ├── ref0.txt
│   ├── src.txt
├── bea19-test
│   └── src.txt
...
```

# Supported datasets

### Public datasets

|ID `.load(ID)`|Description|
|:--|:--|
|'conll13'|CoNLL-2013 test set [[Ng+ 2013]](https://aclanthology.org/W13-3601/).|
|'conll14'|CoNLL-2014 test set [[Ng+ 2014]](https://aclanthology.org/W14-1701/).|
|'jfleg-test'|JFLEG test set [[Napoles+ 2017]](https://aclanthology.org/E17-2037/).|
|'jfleg-dev'|JFLEG development set [[Napoles+ 2017]](https://aclanthology.org/E17-2037/).|
|'fce-test'|FCE test set [[Yannakoudakis+ 2011]](https://aclanthology.org/P11-1019/)|
|'fce-dev'|FCE development set [[Yannakoudakis+ 2011]](https://aclanthology.org/P11-1019/).|
|'fce-train'|FCE training set [[Yannakoudakis+ 2011]](https://aclanthology.org/P11-1019/).|
|'cweb-g-test'|CWEB-G test set [[Flachs+ 2020]](https://aclanthology.org/2020.emnlp-main.680/).|
|'cweb-g-dev'|CWEB-G development set [[Flachs+ 2020]](https://aclanthology.org/2020.emnlp-main.680/).|
|'cweb-s-test'|CWEB-S test set [[Flachs+ 2020]](https://aclanthology.org/2020.emnlp-main.680/).|
|'cweb-s-dev'|CWEB-S development set [[Flachs+ 2020]](https://aclanthology.org/2020.emnlp-main.680/).|
|'bea19-test'|BEA-2019 shared task test set [[Bryant+ 2019]](https://aclanthology.org/W19-4406/).|
|'bea19-dev'|BEA-2019 shared task development set [[Bryant+ 2019]](https://aclanthology.org/W19-4406/). It contains only source sentences.|
|'wi-locness-train'|W&I+LOCNESS training set [[Yannakoudakis+ 2018]](https://www.cl.cam.ac.uk/~hy260/WI-cefr.pdf).|

### Non-public datasets

|ID `.load(ID)`|Description|
|:--|:--|
|'nucle-train'|NUCLE training set. [[Dahlmeier+ 2013]](https://aclanthology.org/W13-1703/)|
|'lang8-train'|Lang-8 training set. [[Mizumoto+ 2012]](https://aclanthology.org/C12-2084/) [[Tajiri+ 2012]](https://aclanthology.org/P12-2039/)|

### nucle-train

- Request data from [HERE](https://www.cl.cam.ac.uk/research/nl/bea2019st/).
- You will receive an email with release3.3.tar.bz2 attached.
- `mkdir <base_path>/nucle-train/` and put the data as ` <base_path>/nucle-train/release3.3.tar.bz2`.
- You can now use the data with `.load("nucle-train")`. The data will be extracted automatically.

### lang8-train

- Request data from [HERE](https://www.cl.cam.ac.uk/research/nl/bea2019st/).
- You will receive an email titled "[NAIST Lang-8 Corpus of Learner English for the 14th BEA Shared Task]".
- `mkdir <base_path>/lang8-train/` and put the data as `<base_path>/lang8-train/lang8.bea19.tar.gz`.
- You can now use the data with `.load("lang8-train")`. The data will be extracted automatically.