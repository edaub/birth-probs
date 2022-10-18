# birth-probs

Command line tool for printing out probabilities of giving birth in a given week

## Installation

The package can be installed from the main directory using the command

```
python setup.py install
```

This will install any required dependencies. Alternatively, from the main directory
the command `pip install .` can be used to install the tool

## Usage

Once installed, the command can be called directly from the command line:

```
birth-probs YYYY-MM-DD
```

Where `YYYY-MM-DD` is the due date (40 weeks since last menstrual cycle) in the standard
ISO date format. The tool will print out the cumulative probability that the baby is born
in each successive week starting from the current week. Week boundaries are computed
relative to the due date, so if the baby is due on a Monday then all weeks quoted will
be on Mondays and represent the probability the baby is born in the previous 7 days. No
correction is applied to the first week in the table, so this will slightly
overstate the probability of the first week if the week is not a full seven days
and slightly understate the probability in the remaining weeks. This effect is only
significant as the due date approaches and there is a high probability of the baby
being born in the current week.

## Data Source and Comments

The data used to compute the probabilities is drawn from the UK Office for National Statistics
User Guide to Birth Statistics (last accessed 2022/10/07):

https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/methodologies/userguidetobirthstatistics

The Excel file holding the data used in the calculation can be accessed at

https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/healthandsocialcare/causesofdeath/bulletins/pregnancyandethnicfactorsinfluencingbirthsandinfantmortality/2015-10-14/88970d40.xls

The file has been modified and its data saved in this repository as part of the main script.

Weeks gestation is usually measured as the number weeks since the last menstrual cycle, with
40 weeks used to estimate the due date. In the NHS in England and Wales, this is usually
estimated instead by the length of the fetus measured at the 12 week ultrasound scan, as
the fetus is usually a consistent size at this stage of pregnancy and the measurement can
be used to more accurately estimate the due date. Since the data comes from England and
Wales, this measurement is likely to have been used to estimate the weeks gestation
for the majority (if not all) samples in the data.