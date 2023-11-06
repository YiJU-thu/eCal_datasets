# EIA grid monitor

**ref:** [US Energy Information Administration (EIA) electric grid monitor](https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48)\
**contributors:** [U.S. Energy Information Administration (EIA)](https://www.eia.gov/about/)


On [EIA's hourly electric grid monitor dashboard](https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48), there is a button **DOWNLOAD DATA** on the top right. On clicking it, we further choose **Balancing Authority / Region Files**, on which page, download url's of .xlsx files are listed. The information shown in the window has been copied to `EIA_region_url.xlsx`.

**No API key is needed for this dataset.**

You can download the dataset by simply run the command:
```
python EIA_grid/dl_eia_grid.py
```
You can add ``--test`` to download only `Region_CAL` for testing purpose (will be automatically removed). For details, you can run
```
python EIA_grid/dl_eia_grid.py --help
```

## summary
**duration:** 2015/07/01 - present (latest on HPC: 2023/11/02)\
**region:** USA\
**resolution:** *temporal*: hourly; *spatial*: region/BA\
**file type:** save as .xlsx for each region/BA (3.3 GB)

**variables**
- :warning: under construction :warning:

Please refer to [analysis_eia_grid.ipynb](analysis_eia_grid.ipynb) for more details.\
:warning: You can play with the notebook yourself, but please do NOT commit any changes to it. (You can make a copy of it, and include "NoTrack" in the file name so it will not be tracked.)\
:no_entry: **We reject any pull request with modification on the notebooks, incl. simply running it.**

**sample files:** data from **Region_CAL** are provided in [sample/](sample/).

:warning: under construction :warning:

## relevant papers/resources
- fun to explore [EIA's US energy Atlas](https://atlas.eia.gov/pages/energy-maps) 