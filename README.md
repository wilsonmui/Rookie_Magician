# Rookie Magician

In this game, you will play the role of a magician. In this world, spells are cast with spellbooks. 
Spellbooks are mystical tools created from existing text in the world, which is its origin. To cast a spell, the spellbook will
require you to prove that you understand its origins. You will do this by playing a game. Success in the game will
create a stronger spell. Cast the spell to inflict damage before the enemy kills you.

You will enter your own prompts to generate phrases using the spellbook. The goal is to generate phrases that 
align with the spellbooks origin. The text will align when the spellbooks keywords are matched. Match as many keywords as 
you can with the generated text to cast stronger spells.



# Install instructions
Using Python 3.7.5

Must install
* tensorflow
* gpt-2-simple
* gpt-2 335M model
* finetrained models

##1. Installing Tensorflow



```shell
pip3 install tensorflow==1.14
```

You will also need to install the corresponding TensorFlow for your system (e.g. `tensorflow` or `tensorflow-gpu`). **TensorFlow 2.0 is currently not supported**, so TensorFlow 1.14 is recommended.
https://developer.nvidia.com/cuda-10.0-download-archive cuda10.0.0
 https://developer.nvidia.com/cudnn  cudnn

##2. Installing gpt-2-simple
gpt-2-simple can be installed [via PyPI](https://pypi.org/project/gpt_2_simple/):

```shell
pip3 install gpt-2-simple
```

##3. Installing gpt-2 335M model

execute the init.py in the repo
```shell
python init.py
```

##4. Download and extract finetrained models
there are three finetrained models currently
 - [love_letter](https://drive.google.com/open?id=1-2DyqykHOAy11lv-oaex52eLLzkzd9cb)
 - [spongebob](https://drive.google.com/open?id=1-2TlrRu-s3tuM8tmKvybyBo_zHmHbx6i)
 - [Quenya](https://drive.google.com/open?id=1-3OPrv7y7OBuKT1FYLSfpZNodgEYQVFc)
 - [Grey](https://drive.google.com/open?id=18K0Oh8htOvhiM6LFTAgQGQ3IbBB-ghkS)
 
Download those files and extract by "extract here" under the repo. Arrange the files such that all the models are under one checkpoint folder like so:

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

##5. Running the program

```shell
python demo.py
```

## Known Issues
1. When using MacOS Night Mode, the interface text may not appear. This can be resolved by switching to normal display setting.


