# ACN data

**ref:** [ACN-Data: Analysis and Applications of an Open EV Charging Dataset](https://dl.acm.org/doi/10.1145/3307772.3328313) (ACM e-Energy, 2019)\
**contributors:** Zachary Lee & [Steven Low](http://netlab.caltech.edu/) @ caltech

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
- [ACN-Sim: An Open-Source Simulator for Data-Driven Electric Vehicle Charging Research](https://doi.org/10.1109/TSG.2021.3103156) (IEEE TSG, 2021)
- [The Adaptive Charging Network Research Portal: Systems, Tools, and Algorithms](https://thesis.library.caltech.edu/14191/) (Zachary Lee's PhD dissertation)
- [Prediction of EV Charging Behavior Using Machine Learning](https://ieeexplore.ieee.org/abstract/document/9508419) (IEEE Access, 2021)
- [Probabilistic Charging Power Forecast of EVCS: Reinforcement Learning Assisted Deep Learning Approach](https://doi.org/10.1109/TIV.2022.3168577) (IEEE TIV, 2022)
- [Pricing EV charging service with demand charge](https://doi.org/10.1016/j.epsr.2020.106694) (EPSR, 2020)
- [Classification of electric vehicle charging time series with selective clustering](https://doi.org/10.1016/j.epsr.2020.106695) (EPSR, 2020)
- [A Novel Cross-Case Electric Vehicle Demand Modeling Based on 3D Convolutional Generative Adversarial Networks](https://doi.org/10.1109/TPWRS.2021.3100994) (IEEE TPS, 2021)
- [A multiobjective analysis of the potential of scheduling electrical vehicle charging for flattening the duck curve](https://doi.org/10.1016/j.jocs.2020.101262) (JoCS, 2021)
- [Scheduling Flexible Nonpreemptive Loads in Smart-Grid Networks](https://doi.org/10.1109/TCNS.2022.3141017) (IEEE TCNS, 2022)
- [Learning-Based Predictive Control via Real-Time Aggregate Flexibility](https://doi.org/10.1109/TSG.2021.3094719) (IEEE TSG, 2021)
- [Sustainable electric vehicle charging coordination: Balancing CO2 emission reduction and peak power demand shaving](https://doi.org/10.1016/j.apenergy.2023.121637) (AE, 2023)
- [Forecasting flexibility of charging of electric vehicles: Tree and cluster-based methods](https://doi.org/10.1016/j.apenergy.2023.121969) (AE, 2024)