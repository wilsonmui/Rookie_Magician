# Install instructions
You have to install
* tensorflow
* gpt-2-simple
* gpt-2 335M model
* finetrained models

## tensorflow


```shell
pip3 install tensorflow-gpu==1.14
```

You will also need to install the corresponding TensorFlow for your system (e.g. `tensorflow` or `tensorflow-gpu`). **TensorFlow 2.0 is currently not supported**, so TensorFlow 1.14 is recommended.
https://developer.nvidia.com/cuda-10.0-download-archive for required DLL installation

## gpt-2-simple
gpt-2-simple can be installed [via PyPI](https://pypi.org/project/gpt_2_simple/):

```shell
pip3 install gpt-2-simple
```

## gpt-2 335M model

execute the init.py in the repo
```shell
python init.py
```

## finetrained models
there are three finetrained models currently
 - [love_letter](https://drive.google.com/open?id=1-2DyqykHOAy11lv-oaex52eLLzkzd9cb)
 - [spongebob](https://drive.google.com/open?id=1-2TlrRu-s3tuM8tmKvybyBo_zHmHbx6i)
 - [Quenya](https://drive.google.com/open?id=1-3OPrv7y7OBuKT1FYLSfpZNodgEYQVFc)
 
Download those files and extract by "extract here" under the repo

it should be look like

```
../
    gpt_2_simple/
        ...
    checkpoint/
        love_letter/
            ...
        Quenya/
            ...
        spongebob/
            ...
```
