# eCal_datasets

This is a repository that contains instructions for downloading and accessing frequently-used datasets within the [Berkeley eCal](https://ecal.berkeley.edu/) research team. This repository is currently maintained by **Yi Ju** (juy16thu AT berkeley DOT edu).

- If you are an **eCal member**, and you have an account on **eCal-HPC2**, you can access the datasets under `/home/ecal_team/datasets`. In most cases, you can run the scripts in this repository directly.

- If you are **NOT** part of eCal research, you are still welcomed to use all the scripts to download and analyze the datasets. (All scripts would work after you replacing the **datasets** value in ``paths.json`` to the folder you (wish to) store the datasets.) The research interests of eCal include: **power grid**, **transportation**, **batteries**, **electric vehicles**, etc., and we look forward to your suggestions on relevant data sources. 

Run the command
```bash
python utils/test_access.py
```
to verify that you have the needed write and read access. (for eCal members, it is read-only access by default.)

:warning:**ATTENTION**:warning: If you (especially eCal members) need to pass some <span style="color:red">sensitive information</span> (e.g., an API key) to download the data, please store the key seperately under a file(folder) with **"NoTrack"** in its file(folder)name. *If you accidentally leak your keys, please contact Yi immediately.*

## Datasets
- [California vehicle survey](travel_survey/) (2013, ‘17, ‘19)
- [ACN-data](ACN_data/) (2018-2021, CA, 66745 charging sessions)
- [EIA electric grid monitor](EIA_grid/) (2015-2023, USA, region/BA hourly power & emissions)
