# mglcmdtools

## 1 Introduction

`mglcmdtools` is a collection of common cmd tools intended to be used in Python3 scripts. By Guanliang MENG, see https://github.com/linzhi2013/mglcmdtools. 


## 2 Installation

    pip install mglcmdtools


## 3 Usage
    
    from mglcmdtools import rm_and_mkdir, runcmd

    rm_and_mkdir('Newdirectory')

    rm_and_mkdir('Newdirectory', force=True)


    cmd = 'ls -lhtr /'
    runcmd(cmd)

    runcmd(cmd, verbose=True)

## 4 Author
Guanliang MENG

## 5 Citation
Currently I have no plan to publish `mglcmdtools`.







