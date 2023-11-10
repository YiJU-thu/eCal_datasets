# Amazon Last Mile Routing Challenge 2021

**ref:** [2021 Amazon Last Mile Routing Research Challenge: Data Set](https://doi.org/10.1287/trsc.2022.1173) (Trans. Sci.)\
**contributors:** Amazon Last Mile Resaerch team & [MIT Center for Transportation & Logistics](https://ctl.mit.edu/)\

:warning: below is under construction :warning:

- almrrc2021-data-training
  - model_apply_inputs
  - model_apply_outputs
  - model_build_inputs
  - model_build_outputs
  - model_score_inputs
  - model_score_outputs
  - model_score_timings
- almrrc2021-data-evaluation
  - model_apply_inputs
  - model_score_inputs



We use the python API client (https://github.com/zach401/acnportal/tree/master/acnportal/acndata) to download the data.
- You need to register to get get an API key (https://ev.caltech.edu/register). To use our script, please store your api key in file `NoTrack.json` with key `acn_data`, i.e.,
```
{
    other_keys: other_values,
    "acn_data": your_api_key
}
```
- The `get_sessions` and `get_session_by_time` methods provided return a generator object. We convert it as a DataFrame and save it as a .csv file.
- When `timeseries=True`, originally it returns `pilotSignal` and `chargingCurrent` every 2-5 seconds. We only keep those values that are at least $\epsilon=0.1$ kW different from its previous step. This reduces ~90% of the records. :warning: Even though, we strongly discourage you to download the timeseries data (it may take more than one day), unless they are necessary for your research.

You can download the dataset by simply run the command:
```
bash ACN_data/dl_acn_data.sh
```
You can add ``--test`` to download a smalll portion of data for testing purpose. For details, you can run
```
python ACN_data/dl_acn_data.py --help
```

## summary
**duration:** 2018/04/25 - 2021/09/14\
**region:** Pasadena (& Silicon Valley), CA, USA\
**# observatuions:** 66745 charging sessions\
**file type:** save as .csv for each site (28 MB w/o timeseries, 5 GB w/ timeseries)

**variables**
- identifiers: `sessionID`, `stationID`, `spaceID`, `siteID`, `clusterID`, `userID`
- session info: `connectionTime`, `disconnectTime`,`kWhDelivered`, `doneChargingTime`
- time series: `pilotSignal`, `chargingCurrent`
- user inputs: `userInputs`

Please refer to [analysis_acn_data.ipynb](analysis_acn_data.ipynb) for more details.\
:warning: You can play with the notebook yourself, but please do NOT commit any changes to it. (You can make a copy of it, and include "NoTrack" in the file name so it will not be tracked.)\
:no_entry: **We reject any pull request with modification on the notebooks, incl. simply running it.**

**sample files:** data (no timeseries) in 2019-04 from the three sites are provided in [sample/](sample/).

## potential usage
- Reflect a realistic pattern of EV charging demands
- Use as data source for EVCS management simulations
- Learn to forecast future charging sessions
### limitations
It is Yi Ju's personal view.
- Do not contain the drivers' mobility information (drivers may charge somewhere else).
- Do not contain price information. The session info (start time, duration, energy request) may be affected by the prices.


## relevant papers
- 