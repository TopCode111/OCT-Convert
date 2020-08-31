<p align="center">
    <img src="../assets/oct.gif?raw=true">
</p>


# OCT file converter #

This repository contains code for extracting the raw optical coherence tomography (OCT) and fundus data from 
manufacturer's proprietary file formats. 

## Motivation
Research in ophthalmology is often hindered by manufacturer's usage of proprietary data formats for storing their data. 
For example, until recently, the ~200,000 OCT scans in the UK Biobank project was only available in Topcon's .fds
file format, which prevented bulk processing and analysis. The only freely available software that allows these scans
to be accessed is  [uocte](https://bitbucket.org/uocte/uocte/wiki/Home), which is written in C++ and is no longer 
maintained. This repository aims to make available python-based tools for reading these proprietary formats.


## Supported file formats
* .fds (Topcon)
* .e2e (Heidelberg)
* .img (Zeiss)
* .dcm

## Installation
Requires **python3**.

To install run:
```bash
git clone https://github.com/marksgraham/OCT-Converter.git
pip install -e OCT-Converter
```

## Usage
Example usage scripts are included in examples/. 

## Contributions
Are welcome!


