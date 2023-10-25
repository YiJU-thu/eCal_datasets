# eCal_datasets

This is a repository that contains instructions for downloading and accessing frequently-used datasets within the [Berkeley eCal](https://ecal.berkeley.edu/) research team. This repository is currently maintained by **Yi Ju** (juy16thu AT berkeley DOT edu).

- If you are an **eCal member**, and you have an account on **eCal-HPC2**, you can access the datasets under `/home/ecal_team/datasets`. In most cases, you can run the scripts in this repository directly.

- If you are **NOT** part of eCal research, you are still welcomed to use all the scripts to download and analyze the datasets. (All scripts would work after you replacing the **datasets** value in ``paths.json`` to the folder you (wish to) store the datasets.) The research interests of eCal include: **power grid**, **transportation**, **batteries**, **electric vehicles**, etc., and we look forward to your suggestions on relevant data sources. 

Run the command
```bash
python test_access.py
```
to verify that you have the needed write and read access. (for eCal members, it is read-only access by default.)


## Datasets