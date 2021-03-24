## Install Anaconda in Ubuntu
Hopefully by now you should have a working Ubuntu installation either in a VM or natively. If not you can follow the links for Windows but we strongly urge you to use Linux instead.

Anaconda is a package manager which handles the installation of packages and their dependencies behind the scenes. Almost all machine learning frameworks are supported in Anaconda. We will install both TensorFlow and PyTorch using Anaconda.

To install Anaconda please follow this [tutorial](https://www.unixmen.com/install-anaconda-miniconda-conda-on-ubuntu-centos-linux/).

(Not Recommended) Windows users follow this [tutorial](https://medium.com/@bryant.kou/how-to-install-pytorch-on-windows-step-by-step-cc4d004adb2a).

### Environments in Anaconda
An environment is simply an isolated container that is used to install one set of packages in isolation from all the other software. This has multiple benefits and by default we will use different environments for PyTorch and TensorFlow.

## How to install PyTorch
Open the terminal then type and run the following command line instructions.

```
conda create -n pytorch python=3.6

conda activate pytorch

conda install pytorch==1.5.1 torchvision==0.6.1 cpuonly -c pytorch

conda list

conda deactivate
```

This should now give you a list of installed software in the PyTorch environment containing the PyTorch package itself.

(Not Recommended) Windows users follow this [tutorial](https://medium.com/@bryant.kou/how-to-install-pytorch-on-windows-step-by-step-cc4d004adb2a).
