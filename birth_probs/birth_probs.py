import numpy as np
import pandas
import argparse

def map_dates(due_date):
    due_date = np.datetime64(due_date)
    date_dict = {}
    for i in range(43):
        date_dict[i] = due_date + np.timedelta64(7*(i-40), "D")
    return date_dict

def get_week(current_date, due_date):
    date_dict = map_dates(due_date)
    current_date = np.datetime64(current_date)
    for key in date_dict:
        if current_date >= date_dict[key]:
            continue
        else:
            return key - 1
    raise ValueError("Current date is more than 2 weeks after due date")

def load_probs():
    "put data from NHS into a data frame"
    d = {'weeks': [ 21,  22,  23,  24,  25,  26,  27,  28,   29,   30,   31,   32,
                        33,   34,   35,    36,    37, 38, 39, 40, 41, 42],
         'counts':  [271, 151, 281, 487, 496, 643, 739, 966, 1162, 1462, 1913, 2761,
                      3923, 6658, 9861, 19929, 44257, 91392, 165248, 187632, 132363, 23393],
        }
    return pandas.DataFrame(data=d)

def compute_probs(cutoff):
    assert cutoff > 0, "Provided due date is more than 42 weeks into the future"
    df = load_probs()
    df.drop(df[df["weeks"] <= cutoff].index, inplace=True)
    df["cumprob"] = np.cumsum(df["counts"])/np.sum(df["counts"])
    return df

def print_probs(due_date):
    current_date = np.datetime64("today")
    current_week = get_week(current_date, due_date)
    df = compute_probs(current_week)
    date_dict = map_dates(due_date)
    print("Week Ending   Cumulative Probability")
    for i, row in df.iterrows():
        print("{}    {}".format(date_dict[int(row["weeks"])], row["cumprob"]))

def main():
    parser = argparse.ArgumentParser(description="compute birth probabilities")
    parser.add_argument("due_date", type=str, help="due date")
    args = parser.parse_args()
    print_probs(args.due_date)
