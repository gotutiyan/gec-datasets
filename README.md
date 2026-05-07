# gec-datasets

This library is to handle datasets of Grammatical Error Correction.

# Install

```sh
pip install gec-datasets
```


# Usage

### API
```python
from gec_datasets import GECDatasets
gec = GECDatasets(
    base_path='gec_datasets_base/'
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

Available ids can be found by:
```python
import gec_datasets
print(gec_datasets.available())
```

### CLI
You can specify multiple ids of the data you want to download in the `--ids` field.

```sh
gecdatasets-download --base_path "gec_datasets_base/" --ids conll14 bea19-dev
```

Available ids can be found by:
```sh
gecdatasets-available
```


In both API and CLI, datasets will be stored under `base_path=`.  
The first time it is downloaded automatically, and thereafter it is loaded from the saved files.

When you call `gec.load('sample')`, gec-datasets simply refers to `<base_path>/'sample'/{src.txt|ref0.txt|...}`.

```
gec_datasets_base/
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

Basically, `gec-datasets` automatically handles everything, including downloading datasets. However, some non-public datasets require manual file downloads.


### Public datasets

|ID `.load(ID)`|Language|Description|Instructions (if non-public data)|
|:--|:--|:--|:--|
|'conll13'|English|CoNLL-2013 test set [[Ng+ 2013]](https://aclanthology.org/W13-3601/).||
|'conll14'|English|CoNLL-2014 test set [[Ng+ 2014]](https://aclanthology.org/W14-1701/).||
|'jfleg-dev'<br>'jfleg-test'|English|JFLEG dataset [[Napoles+ 2017]](https://aclanthology.org/E17-2037/).||
|'fce-train'<br>'fce-dev'<br>'fce-test'|English|FCE dataset [[Yannakoudakis+ 2011]](https://aclanthology.org/P11-1019/)||
|'cweb-g-dev'<br>'cweb-g-test'|English|CWEB-G dataset [[Flachs+ 2020]](https://aclanthology.org/2020.emnlp-main.680/).||
|'cweb-s-dev'<br>'cweb-s-test'|English|CWEB-S dataset [[Flachs+ 2020]](https://aclanthology.org/2020.emnlp-main.680/).||
|'bea19-dev'<br>'bea19-test'|English|BEA-2019 shared task test set [[Bryant+ 2019]](https://aclanthology.org/W19-4406/). The test set contains only source sentences.||
|'wi-locness-train'|English|W&I+LOCNESS training set [[Yannakoudakis+ 2018]](https://www.cl.cam.ac.uk/~hy260/WI-cefr.pdf).||
|'nucle-train'|English|NUCLE training set. [[Dahlmeier+ 2013]](https://aclanthology.org/W13-1703/)|Request data from [HERE](https://www.cl.cam.ac.uk/research/nl/bea2019st/), then put the data as `<base_path>/nucle/release3.3.tar.bz2`. After that, you can `.load(nucle-train)`.|
|'lang8-train'|English|Lang-8 training set. [[Mizumoto+ 2012]](https://aclanthology.org/C12-2084/) [[Tajiri+ 2012]](https://aclanthology.org/P12-2039/)|Request data from [HERE](https://www.cl.cam.ac.uk/research/nl/bea2019st/). You will receive an email titled "[NAIST Lang-8 Corpus of Learner English for the 14th BEA Shared Task]", and put the data as `<base_path>/lang8/lang8.bea19.tar.gz`. After that, you can now use the data with `.load("lang8-train")`.|
|'unlp2023-gec-only-train'<br>'unlp2023-gec-only-dev'<br>'unlp2023-gec-fluency-train'<br>'unlp2023-gec-fluency-dev'|Ukrainian|UNLP-2023 Shared Task [[Syvokon+ 23]](https://aclanthology.org/2023.unlp-1.16/).||
|'akces-gec-train'<br>'akces-gec-dev'<br>'akces-gec-test'|Czech|AKCES-GEC [[Náplava+ 19]](https://aclanthology.org/D19-5545/). |Download `AKCES-GEC.zip` from [HERE](https://lindat.mff.cuni.cz/repository/items/ba5f9011-0282-4dff-bddd-6d30e518caeb) and put it as `<base_path>/akces-gec/AKCES-GEC.zip`. After that, you can `.load('akces-gec-xxx')`.|
|'geccc-sentence-train'<br>'geccc-sentence-dev'<br>'geccc-sentence-test'<br>'geccc-paragraph-train'<br>'geccc-paragraph-dev'<br>'geccc-paragraph-test'|Czech|GECCC dataset [[Náplava+ 22]](https://aclanthology.org/2022.tacl-1.26/)||
|'falko-merlin-train'<br>'falko-merlin-dev'<br>'falko-merlin-test'|German|Falko-Merlin [[Boyd+ 18]](https://aclanthology.org/W18-6111/)||
|'loru-gec-dev'<br>'loru-gec-test'|Russian|LORuGEC dataset [[Sorokin+ 25]](https://aclanthology.org/2025.bea-1.38/)||
|'ronacc-train'<br>'ronacc-dev'<br>'ronacc-test'|Romain|RONACC dataset [[Cotet+ 20]](https://ieeexplore.ieee.org/abstract/document/9288338)||
|'k-nct-test'|Korean|K-NCT dataset [[Koo+ 23]](https://ieeexplore.ieee.org/abstract/document/9938990)||
|'kor-learner-train'<br>'kor-learner-dev'<br>'kor-learner-test'<br>'kor-native-train'<br>'kor-native-dev'<br>'kor-native-test'|Korean|Kor-learner, Kor-native datsets [[Yoon+ 23]](https://aclanthology.org/2023.acl-long.371/)|Send a request from [This Form](https://docs.google.com/forms/d/e/1FAIpQLSfewjAmqcrKF5GDYuIWOfyMVBI3FN6tCwI8jalzQNhGoVAlRg/viewform) and download `Preprocessed/` directory from the google drive. Then, put it as `<base_path>/kor/Preprocessed.zip`. After that, you can `.load('kor-xxx')`|
|'hi-gec-train'<br>'hi-gec-dev'<br>'hi-gec-test'|Hindi|Hi-GEC dataset [[Sharma+ 25]](https://aclanthology.org/2025.coling-main.406/)||

The following is synthetic data.

|ID `.load(ID)`|Language|Description|
|:--|:--|:--|
|'troy-1bw-train'<br>'troy-1bw-dev'|English|Synthetic data based on the One Billion Words Benchmark for distillation [[Tarnavskyi,+ 2022]](https://aclanthology.org/2022.acl-long.266/).|
|'troy-blogs-dev'<br>'troy-blogs-train'|English|Synthetic data based on the Blog Authorship Corpus for distillation [[Tarnavskyi,+ 2022]](https://aclanthology.org/2022.acl-long.266/).|
|'pie-synthetic-a1'<br>'pie-synthetic-a2'<br>'pie-synthetic-a3'<br>'pie-synthetic-a4'<br>'pie-synthetic-a5'|English|Synthetic data based on the One Billion Words Benchmark [[Awasthi+ 19]](https://aclanthology.org/D19-1435/). [This attachment](https://aclanthology.org/attachments/D19-1435.Attachment.pdf) describes how to make synthetic errors.|


# Add your custom data

The `.load("ID")` method simply references files in the format `<base_path>/"ID"/{src.txt|ref0.txt|ref1.txt|...|refN.txt}`. Custom datasets can be loaded by simply placing files in a directory following this format. Note that the source file must be named exactly `src.txt`, and reference files must follow the strict 0-indexed naming convention `refN.txt`.

For better reproducibility, you can also download datasets from remote sources. In this case, you can define your own downloader class as described in [.src/gec_datasets/downloaders/](.src/gec_datasets/downloaders/). The role of a downloader class is to automate the entire workflow of downloading data from a remote source and renaming or copying files into the required format: `<base_path>/ID/{src.txt|ref0.txt|ref1.txt|...|refN.txt}`.

A custom downloader class becomes available by passing it to the `custom_downloaders=` argument.  
In the example below, the existing `DownloaderCoNLL2014` is treated as if it were a custom class and passed to the `custom_downloaders=` argument.

```python
from gec_datasets import GECDatasets
from gec_datasets.downloaders.conll14 import DownloaderCoNLL2014
gec = GECDatasets(
    base_path='gec_datasets_base/',
    custom_downloaders=[DownloaderCoNLL2014]
)
gec.available()[-1]
'conll14'
```