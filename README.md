# birth-probs

Command line tool for printing out probabilities of giving birth in a given week

## Usage

From the main directory, run the following command:

```
python birth-probs.py YYYY-MM-DD
```

Where `YYYY-MM-DD` is the due date (40 weeks since last menstrual cycle) in the standard
ISO date format. The tool will print out the cumulative probability that the baby is born
in each successive week starting from the current week. Week boundaries are computed
relative to the due date, so if the baby is due on a Monday then all weeks quoted will
be on Mondays and represent the probability the baby is born in the previous 7 days. No
correction is applied to the first week in the table, so this will likely slightly
overstate the probability of the first week if the week is not a full seven days
and slightly understate the probability in the remaining weeks. This effect is only
significant as the due date approaches and there is a high probability of the baby
being born in the current week.
