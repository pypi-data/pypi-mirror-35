import altair as alt
import pandas as pd
from IPython.display import display, Markdown


def quartile(data, col):
    quartile_one = data[col].quantile(.25)
    quartile_three = data[col].quantile(.75)
    inter_quartile_range = quartile_three - quartile_one
    upper_limit = quartile_three + (1.5 * inter_quartile_range)
    lower_limit = quartile_one - (1.5 * inter_quartile_range)
    return (lower_limit, upper_limit)


def check_data(
    data,
    columns=[],
    missing=0.1,
    cardinality=15,
    float_frequency=30,
    category_frequency=100,
    outlier_function=quartile,
    title=True,
):
    """
    Checks all columns of the given pandas dataframe for data abnormalities

    :param columns: a list of column names to analyze, defaults to all columns in the dataframe

    :param missing: a cutoff point for high percentage of missing / zero values, defaults to 10%

    :param cardinality: a cutoff point for high cardinality of a categorical column, defaults to 15

    :param float_frequency: a cutoff point for high frequency of floating point numbers, defaults to 30

    :param category_frequency: a cutoff point for low frequency of categories in categorical columns, defaults to 100

    :param outlier_function: a function of the dataset and column name that returns the lower and upper limit for outliers, defaults to 1.5*IQR above the 3rd quartile or below the 1st quartile
    """

    # default to all columns
    if columns == []:
        columns = data.columns

    # abnormalities is a dictionary from column name to a list of abnormality statements
    abnormalities = {}

    for col in columns:
        # initialize dictionary item
        abnormalities[col] = []

        """
        Check for high proportion of zeros or missing values
        """
        proportion_zero = sum(data[col] == 0) / len(data)
        if proportion_zero > missing:
            ab = (
                "high proportion of zero values at "
                + str(round(proportion_zero * 100, 2))
                + "%"
            )
            abnormalities[col].append(ab)

        prop_null = sum(data[col].isnull()) / len(data)
        if prop_null > missing:
            ab = (
                "high proportion of null values at "
                + str(round(prop_null * 100, 2))
                + "%"
            )
            abnormalities[col].append(ab)

        """
        Check for high cardinality of categorical variables
        """
        if data[col].dtype == "O":
            num_unique = len(data[col].unique())
            if num_unique > cardinality:
                ab = (
                    "high cardinality with " 
                    + str(num_unique) 
                    + " unique values"
                )
                abnormalities[col].append(ab)

        """
        Check for high frequency of floating point columns
        """
        if data[col].dtype == "float64":
            high_frequency_count = sum(
                data.groupby(col)[col].count().values > float_frequency
            )
            if high_frequency_count > 0:
                ab = (
                    "high frequency of floating point numbers with "
                    + str(high_frequency_count)
                    + " number(s) having frequency over "
                    + str(float_frequency)
                )
                abnormalities[col].append(ab)

        """
        Check for low frequency of categories of categorical variables
        """
        if data[col].dtype == "O":
            low_frequency_count = 0
            for val in data.groupby(col)[col].count().values:
                if val < category_frequency:
                    low_frequency_count += 1
            if low_frequency_count > 0:
                ab = (
                    "low frequncy in categories with "
                    + str(low_frequency_count)
                    + " categorie(s) having under "
                    + str(category_frequency)
                    + " observations"
                )
                abnormalities[col].append(ab)

        """
        Check for outliers in quantitative data
        """
        if data[col].dtype == "float64":
            lower_limit, upper_limit = outlier_function(data, col)
            upper_outlier_count = sum(data[col] > upper_limit)
            lower_outlier_count = sum(data[col] < lower_limit)
            if lower_outlier_count > 0 or upper_outlier_count > 0:
                ab = (
                    "outliers are present with "
                    + str(upper_outlier_count)
                    + " high outliers and "
                    + str(lower_outlier_count)
                    + " low outliers"
                )
                abnormalities[col].append(ab)

    has_abnormalities = False

    for col in abnormalities:
        if len(abnormalities[col]) > 0:
            abs = ""
            for ab in abnormalities[col]:
                # title is true unless check_data is called by check_column
                if title:
                    abs += (
                        "\n<div style= 'margin-left: 30px; text-indent:-1em;'>"
                        + ab
                        + "</div>"
                    )
                else:
                    abs += (
                        "\n<div style = 'margin-left: 1em; text-indent:-1em;'>"
                        + ab 
                        + "</div>"
                    )
            if title:
                display(Markdown("<div>" + col + ": </div>" + abs))
            else:
                display(Markdown(abs))
            has_abnormalities = True

    if not has_abnormalities:
        display(Markdown("No abnormalities found"))


def check_column(
    data,
    columns,
    bins=False,
    missing=0.1,
    cardinality=15,
    float_frequency=30,
    category_frequency=100,
    outlier_function=quartile,
):
    """
    Presents a summary of given column(s) of the given pandas dataframe
    including summary statistics, bar chart or histogram, and any abnormalities found
    
    :param data: a pandas dataframe

    :param columns: a single column name or a list of column names to analyze

    :param bins: a boolean value or list of boolean values to determine whether to bin the histogram for each column

    :param missing: a cutoff point for high percentage of missing / zero values, defaults to 10%

    :param cardinality: a cutoff point for high cardinality of a categorical column, defaults to 15

    :param float_frequency: a cutoff point for high frequency of floating point numbers, defaults to 30

    :param category_frequency: a cutoff point for low frequency of categories in categorical columns, defaults to 100

    :param outlier_function: a function of the dataset and column name that returns the lower and upper limit for outliers,
        defaults to 1.5*IQR above the 3rd quartile or below the 1st quartile
    """

    if isinstance(columns, str):
        # with only one column, convert to lists
        columns = [columns]
        bins = [bins]
    else:
        if bins == False:
            # with multiple columns and no bins,
            # convert to list of correct length
            bins = [False] * len(columns)

        if isinstance(bins, int):
            # with multiple columns and only one bin
            # specification, convert to list of correct length
            bins = [bins] * len(columns)

    i = 0
    for col in columns:
        bin = bins[i]
        i += 1

        if data[col].dtype == "O":
            # cannot bin categorical data
            bin = False

        if bin == False:
            if data[col].dtype == "O":
                chart = (
                    alt.Chart(data)
                    .mark_bar(color="#64b5f6")
                    .encode(
                        alt.X(
                            col,
                            axis=alt.Axis(title=col.title()),
                            sort=alt.SortField(
                                field="count()", order="descending", op="values"
                            ),
                        ),
                        alt.Y("count()"),
                    )
                )
            else:
                chart = (
                    alt.Chart(data)
                    .mark_bar(color="#64b5f6")
                    .encode(
                        alt.X(
                            col, 
                            axis=alt.Axis(title=col.title())
                        ), 
                        alt.Y("count()")
                    )
                )
        else:
            chart = (
                alt.Chart(data)
                .mark_bar(color="#64b5f6")
                .encode(
                    alt.X(
                        col, 
                        bin=alt.Bin(maxbins=bin), 
                        axis=alt.Axis(title=col.title())
                    ),
                    alt.Y("count()"),
                )
            )

        if data[col].dtype == "float64":
            stats = data[col].describe()
        else:
            stats = data.groupby(col)[col].agg(["count"])
            stats["prop"] = stats["count"] / len(data)

        stats = pd.DataFrame(stats).T

        display(Markdown("#### Column Summary: " + col.title()))
        display(stats)
        display(chart)
        check_data(
            data,
            [col],
            missing=missing,
            cardinality=cardinality,
            float_frequency=float_frequency,
            category_frequency=category_frequency,
            outlier_function=outlier_function,
            title=False,
        )
