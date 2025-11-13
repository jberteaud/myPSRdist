# myPSRDist
myPSRDist is a wrapper I created for PSRDist, that can be found here [here](https://github.com/tedwards2412/PSRDist). The differences with the original version are really minor (I think I had to change a "D" into a "d" somewhere) and my only contribution is just the creation of a `.yml` file for setting up an environment with conda. In the `.py` files I also perform a simple Gaussian fit to the distance PDF of pulsars. The though work was done by [Bartels, Edwards and Weniger](https://ui.adsabs.harvard.edu/abs/2018MNRAS.481.3966B/abstract).

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
