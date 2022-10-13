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
    raise ValueError("Current date not valid")

def compute_probs(cutoff):
    assert cutoff > 0
    df = pandas.read_csv("births.csv", header=None)
    df.drop(df[df[0] <= cutoff].index, inplace=True)
    df[2] = np.cumsum(df[1])/np.sum(df[1])
    return df

def print_probs(due_date):
    current_date = np.datetime64("today")
    current_week = get_week(current_date, due_date)
    df = compute_probs(current_week)
    date_dict = map_dates(due_date)
    print("Week Ending   Cumulative Probability")
    for i, row in df.iterrows():
        print("{}    {}".format(date_dict[int(row[0])], row[2]))

def main():
    parser = argparse.ArgumentParser(description="compute birth probabilities")
    parser.add_argument("due_date", type=str, help="due date")
    args = parser.parse_args()
    print_probs(args.due_date)

if __name__ == "__main__":
    main()