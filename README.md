# r2desktop
A small proof of concept GUI app to run R code with some user provided options.

### Clone

```git clone --recurse-submodules https://github.com/haimasree/r2desktop.git```


## Install R and install required libraries

### Windows
```
Type R in terminal and install the following packages
install.packages("conflicted")
install.packages("BiocManager")
BiocManager::install("Biostrings")
install.packages("tidyverse")
install.packages("logr")
```

### WSL
```
conda create -n py310 python=3.10
conda activate py310
conda install -c r r r-essentials
Type R in terminal and install the following packages
install.packages("conflicted")
install.packages("BiocManager")
BiocManager::install("Biostrings")
install.packages("tidyverse")
install.packages("logr")
```

## Run the code

### Windows
```
I 
py .\gui\main.py
```

### WSL

```
conda activate py310
python ./gui/main.py
```

