[Home](https://bitbucket.org/iuwm/iuwm/wiki/Home)

 - [Run](https://bitbucket.org/iuwm/iuwm/wiki/run)
 - [Batch](https://bitbucket.org/iuwm/iuwm/wiki/batch)
 - [Sensitivity](https://bitbucket.org/iuwm/iuwm/wiki/sensitivity)
 - [Calibration](https://bitbucket.org/iuwm/iuwm/wiki/calibration)

# **Integrated Urban Water Model (IUWM)**

Simulation Engine for Water Demand Planning and Management. Highly Automated. Parallel. Multi-Platform.

The Integrated Urban Water Model (IUWM) forecasts water demand given changes to population, land use, and climate. It also evaluates various demand management strategies including more efficient home appliances, behavior and landscape changes to outdoor irrigation, and use of alternative water sources such as reclaimed wastewater, graywater, stormwater, and roof runoff. Output includes forecasted water use, potable water demand, indoor and outdoor water use, CII and residential water use, local water sources (generation and use of graywater, wastewater, stormwater, and roof runoff), leaks, and outflow to wastewater treatment plants. Simulations are at a daily timestep, and outputs are automatically aggregated to monthly and annual timesteps.

IUWM has been used to assess land development impacts on water use, water requirements, alternative water sources and end-uses. The model also forecasts water use and costs based on user-provided building patterns, efficiency gains through technology or behavioral changes, and water recycling. It contains multiple submodels for representing both indoor and outdoor uses, both CII and residential uses, and handles input changes to land uses.

IUWM is packaged with automated calibration procedures, parameter sensitivity analyses, and custom coding capabilities for user-specified submodels.

## Installation

Install Python 2.7. Can use [Anaconda](https://www.anaconda.com/download/).

[`pip install iuwm`](https://pypi.org/project/iuwm/)

If you want to install from source: Download and unzip [IUWM source code](https://bitbucket.org/iuwm/iuwm/downloads/?tab=tags)... Then run `python setup.py install`

## Quick Start

```text
path/to/dir/containing/iuwm> python iuwm/iuwm/console.py -h
```

Output:

```text
usage: console.py [-h]
                  {list_inputs,list_events,run,batch,sensitivity,calibrate}
                  ...

Run the Integrated Urban Water Management Model (IUWM).

optional arguments:
  -h, --help            show this help message and exit

Commands:
  {list_inputs,list_events,run,batch,sensitivity,calibrate}
    list_inputs         Lists inputs and descriptions
    list_events         Lists events in the model that allow customization
                        throughout the model simulation
    run                 Simulates a single IUWM model scenario
    batch               Performs batch runs of IUWM model scenarios
    sensitivity         Assesses sensitivity on IUWM model parameters
    calibrate           Performs automated calibration on IUWM parameters
```

IUWM can be run from the command line or build a scripting file (*.bat on Windows, *.sh on Linux) that will run your model by double-clicking. Either way, IUWM can be tested with a sample model by running the following command (assuming the IUWM code is in a subfolder called `iuwm` within the current working directory - after opening a command line prompt `cmd` make sure to `cd` into the directory where your unzipped IUWM code folder is, or save the `bat` or `sh` file within that directory):

```
python iuwm/iuwm/console.py run iuwm/tests/files/co.csv --output out_yearly.csv yearly --output out_monthly.csv monthly --output out_daily.csv daily --start_date 2000-01-01 --end_date 2002-12-31 --verbose
```

Other command line arguments can be discovered through use of `-h` for any of the commands

```
python iuwm/iuwm/console.py -h
python iuwm/iuwm/console.py run -h
python iuwm/iuwm/console.py batch -h
python iuwm/iuwm/console.py sensitivity -h
python iuwm/iuwm/console.py calibrate -h
```

## Advanced topics

* [Run](https://bitbucket.org/iuwm/iuwm/wiki/run)
* [Storing output](https://bitbucket.org/iuwm/iuwm/wiki/output)
* [Batch model runs](https://bitbucket.org/iuwm/iuwm/wiki/batch)
* [Sensitivity analysis](https://bitbucket.org/iuwm/iuwm/wiki/sensitivity)
* [Automatic calibration](https://bitbucket.org/iuwm/iuwm/wiki/calibration)

## Citation

Sharvelle, S., Dozier, A. Q., Arabi, M., and Reichel, B. I. (2017). “A geospatially-enabled web tool for urban water demand forecasting and assessment of alternative urban water management strategies”, *Environmental Modelling & Software*, 97, 213-228. [https://doi.org/10.1016/j.envsoft.2017.08.009](https://doi.org/10.1016/j.envsoft.2017.08.009).

## Links

 - [Similar Software Page](https://bitbucket.org/iuwm/iuwm/wiki/similar_software)