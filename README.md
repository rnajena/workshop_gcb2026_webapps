## 2026 *German Conference on Bioinformatics* workshop: Turning Python scripts built with Sugar into web apps

*Workshop Description*: Many bioinformatics tools remain inaccessible to experimental biologists due to their command-line interfaces. This workshop addresses that gap by demonstrating how Python scripts can be transformed into user-friendly web applications. Participants will use the sugar package--a lightweight Python library for sequence and annotation handling--together with NiceGUI to build interactive frontends. Through hands-on exercises, attendees will develop small analysis scripts and convert them into interactive web applications.

### Preparation

1. Clone (recommended) or [download](https://github.com/rnajena/workshop_gcb2026_webapps/archive/refs/heads/master.zip) and unpack this repository. It contains the necessary data files in the `data` folder and the slides.

```
git clone https://github.com/rnajena/workshop_gcb2026_webapps.git
cd workshop_gcb2026_webapps
```

2. Install the necessary tools -- `mafft, nicegui, rnajena-sugar`. The recommended way is to install these in a new conda environment.

a) Install conda (here mini-forge on Linux, you may use other installers).
```
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```
For Windows and MacOS users check the [install instructions](https://github.com/conda-forge/miniforge#install).

b) Add bioconda channel (for MAFFT)
```
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict
```
Note: conda-forge is by default already activated in mini-forge, but the above commands guarantee that the conda-forge channel has a higher priority than bioconda.

c) Create new conda environment with conda requirements
```
conda create -n gcb_webapps "python=3.13" mafft nicegui ipython pip pandas platformdirs pytest requests seaborn
```

d) Install sugar which is provided via PyPI in the new environment
```
conda activate gcb_webapps
pip install "rnajena-sugar>=1.2"
```

e) Test the installation by running
```
sugar test
```

f) Activate environment in new terminals
```
conda activate gcb_webapps
```

### How to

Study the slides, work in the `data` and `wd` directories.

### Code examples

Code examples will be provided after the workshop in the `code` folder.
