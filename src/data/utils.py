import os
import pandas as pd


def combine_csv_files(path, prefix, suffix='.csv', **kwargs):
    """
    This function searches a directory for text files, imports them as pandas.DataFrames and
    concatenates to a single DataFrame.
    :param path: Path object to a directory
    :param prefix: Prefix to search for
    :param suffix: Suffix to search for, Default '.csv'
    :param kwargs: Additional arguments to give to the pandas.read_csv function
    :return: DataFrame
    """

    # List files in the directory
    list_files_in_path = sorted(os.listdir(path))

    # Initialize an empty list to store DataFrames
    list_df = []

    # Loop through files
    for file in list_files_in_path:
        # Check if the file starts with the prefix and ends with csv
        if file.startswith(prefix) and file.endswith(suffix):
            # Read in csv as DataFrame and append it to the list
            list_df.append(pd.read_csv(path / file, **kwargs))
        else:
            continue

    # Concatenate the DataFrames
    df_return = pd.concat(list_df)
    df_return.reset_index(drop=True, inplace=True)

    return df_return
