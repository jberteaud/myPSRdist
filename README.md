# myPSRDist
myPSRDist is a wrapper I created for PSRDist, that can be found here [here](https://tedwards2412.github.io/PSRdist/).

## Installation
Tested on Ubuntu 22.04.5 LTS.

```
git clone https://github.com/jberteaud/myPSRdist
cd myPSRdist
conda env create -f psrdist.yml
conda activate psrdist
./make.sh
export PYTHONPATH=${PYTHONPATH}:/path/to/myPSRdist/PSRDist
python UHF_MSP.py
```
