## Install Jupyter Lab in Anaconda Envrionment

Hopefully by now you should have a working Anaconda Environment with PyTorch Installed.

We will install Jupyte Lab in the same Environment.

```
conda activate pytorch

conda install jupyterlab

conda list

conda deactivate
```

## Install OpenCV


```
conda activate pytorch

conda install -c conda-forge opencv

conda list

conda deactivate

```

### Now to test

```
conda activate pytorch

jupyter notebook

```

You can open the lab file given in .ipynb format on GitHub by selecting it from the file explorer menu in the Jupyter Notebook Interface.
