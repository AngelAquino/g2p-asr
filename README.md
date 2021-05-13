# g2p-asr
This repository contains datasets, scripts, and other relevant files from the project "G2P and ASR for low-resource phonetic transcription of Tagalog, Cebuano, and Hiligaynon".

## Navigation
The main folder contains the following files:
- `DSP01_Aquino_Tsang.pdf`: Undergraduate project manuscript.
- `ismac2019.pdf`: Conference paper.
- `phone-inventory.txt`: Inventory of phones used in the transcription for this project.

The `data` folder contains the following subfolders:
- `_small`: Train-test splits and output data for the "small" performance tests.
- `_large`: Train-test splits and output data for the "large" performance tests.

Each of the two folders above contains the following subfolders:
- `train`: Metadata, orthographic transcriptions, and gold phonetic transcriptions for each of the recordings used as training data.
- `testref`: Metadata, orthographic transcriptions, and gold phonetic transcriptions for each of the recordings used as test data.
- `test`: Metadata, orthographic transcriptions, and G2P-generated phonetic transcriptions for each of the recordings used as training data.
- `adapt`: Runtime logs and adaptive system-generated phonetic transcriptions for each of the recordings used as training data.

## Citation
If you use any of the data or findings provided above, please cite:
```
A. Aquino, J. L. Tsang, C. R. Lucas and F. de Leon, "G2P and ASR techniques for low-resource phonetic transcription of Tagalog, Cebuano, and Hiligaynon," 2019 International Symposium on Multimedia and Communication Technology (ISMAC), 2019, pp. 1-5, doi: 10.1109/ISMAC.2019.8836168.
```
```
@inproceedings{aquino-etal-2019,
    title = "{G2P} and {ASR} techniques for low-resource phonetic transcription of {T}agalog, {C}ebuano, and {H}iligaynon",
    author = "Aquino, Angelina  and
      Tshang, Joshua Lijandro  and
      Lucas, Crisron Rudolf  and
      de Leon, Franz",
    booktitle = "2019 International Symposium on Multimedia and Communication Technology (ISMAC)",
    month = aug,
    year = "2019",
    address = "Quezon City, Philippines",
    publisher = "IEEE",
    url = "https://ieeexplore.ieee.org/document/8836168",
    doi = "10.1109/ISMAC.2019.8836168",
    pages = "1--5"
}
```
