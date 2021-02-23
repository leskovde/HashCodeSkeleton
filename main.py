#!/usr/bin/env python3
import argparse
import tqdm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def parse_input_file(file_path, ):
    rows = []

    print(f"Reading {file_path} ...")

    with open(file_path, "r") as ifs:
        lines = ifs.readlines()

        # TODO: The assignment might specify some dimensions etc.
        # at the beginning of the file. Those need to be parsed
        # separately.
        non_data_lines = 1 # 1st line of input contains e.g. dims.
        non_data = [item for line in lines[:non_data_lines] \
                    for item in line.strip().replace(" ", "")]

        for line in lines[non_data_lines:]:
            line = line.strip()
            if len(line) > 0:

                # TODO: Change the following map to fit the input data.
                # The current map only works on integers, not strings etc.

                row = list(map(int, line.split(" ")))
                rows.append(row)

    print("Reading done.")

    return rows, non_data


def preprocess_data(data, non_data):
    print(f"Preprocessing data of size {np.shape(data)} and info of size \
     {np.shape(non_data)} ...")

    # TODO: Create an appropriate data parsing approach
    # based on the HashCode assignment.

    print(non_data)
    print(data)

    print("Preprocessing done.")

    return data


def optional_visualize_data(data, solution=False):
    print("Plotting the data ...")

    # TODO: OPTIONAL: Plot the given data.
    # Find a way to make the data more understandable

    fig, ax = plt.subplots()
    ax.imshow(data)

    if solution:
        ax.set_title(f"SOLUTION: Shape: {np.shape(data)}, ...")
    else:
        ax.set_title(f"DATA: Shape: {np.shape(data)}, ...")

    print("Plotting done.")

    return


def score(solution):
    print("Scoring the solution ...")

    total_score = 0

    # TODO: Iterate over the solution and score it according
    # to the assignment.

    print("Scoring done.")

    return total_score


def process_data(data, non_data):
    print("Finding a solution ...")

    # TODO: Write an algorithm that solves the assigned problem.

    solution = []

    # The following loop creates a progress bar.
    for _ in tqdm.tqdm(range(len(data) * len(data[0]))):
        # The algorithm goes here.




        # Mock line.
        solution = data

    print("Solving done.")

    return solution


def dump_solution(file_path, solution):
    print(f"Dumping the output to {file_path} ...")

    with open(file_path, "w") as ifs:
        # TODO: Modify the following code in order to
        # write the output in the correct format.

        for row in solution:
            for item in row:
                ifs.write(f"{item} ")
            ifs.write("\n")

    print("Output done.")


parser = argparse.ArgumentParser()
parser.add_argument("--file", default="mock_input.txt", type=str, help="Input data necessary for functioning correctly")
parser.add_argument("--seed", default=42, type=int, help="Random seed")


def main(args):
    if args.file is None:
        print("Nothing to do.")
        return

    # Read the input data and return it as
    # the data matrix and auxiliary information.
    data, non_data = parse_input_file(args.file)

    # Process the raw data into something sensible.
    data = preprocess_data(data, non_data)

    # OPTIONAL: Visualize the data in order to gain
    # a better understanding of the task.
    optional_visualize_data(data)

    # Solve the task using any algorithm and score
    # the solution.
    solution = process_data(data, non_data)
    print(score(solution))

    # OPTIONAL: Visualize the solution to see whether
    # everything is fine.
    optional_visualize_data(solution, solution=True)

    # Write the solution to an output file.
    dump_solution(args.file + ".out", solution)

    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
