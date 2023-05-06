# library of methods to track personal spending habits and trends

import pandas as pd

# import matplotlib.pyplot as plt


def get_data():
    """
    Reads in data from csv file
    """
    data = pd.read_csv('./data.csv')
    return data


def get_categories(data):
    """
    Returns a list of categories in the data.

    Parameters:
    data (pandas.DataFrame): Input data.

    Returns:
    categories (list): List of categories in the data.
    """
    categories = data.Category.unique().tolist()
    categories.sort()  # sort the list of categories
    return categories


def get_category_data(data, category):
    """
    Returns a dataframe of all transactions in a given category
    """
    return data[data['Category'] == category]


def get_category_totals(data):
    """
    Returns a dataframe of the total amount spent in each category
    """
    return data.groupby('Category').sum()


def get_category_averages(df):
    grouped_df = (
        df.groupby(['Category'])
        .agg({'Amount': 'mean', 'Date': 'count'})
        .rename(columns={'Amount': 'Average Amount', 'Date': 'Transaction Count'})
    )
    return grouped_df.reset_index()


def get_category_counts(data):
    """
    Returns a dataframe of the number of transactions in each category
    """
    return data.groupby('Category').count()


def get_category_stats(data):
    """
    Returns a dataframe of the total amount, average amount, and number of transactions in each category
    """
    return data.groupby('Category').agg(
        Amount=pd.NamedAgg(column='Amount', aggfunc='sum'),
        Amount_x=pd.NamedAgg(column='Amount', aggfunc='mean'),
        Amount_y=pd.NamedAgg(column='Amount', aggfunc='count'),
    )


def get_category_stats_by_month(data):
    df = data.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # create a multi-level index with category and month
    df.index = [df.index.year, df.index.month, df['Category']]
    df.index.names = ['Year', 'Month', 'Category']

    # group the data by category and month, and sum the amounts
    return (
        df.groupby(level=['Year', 'Month', 'Category'])['Amount']
        .agg(['sum', 'mean', 'count'])
        .rename(columns={'sum': 'Amount', 'mean': 'Amount_x', 'count': 'Amount_y'})
    )


def get_category_stats_by_year(data):
    """
    Returns a dataframe of the total amount, average amount, and number of transactions in each category by year
    """
    data = data.copy()
    data['Year'] = pd.to_datetime(data['Date']).dt.year
    data = data.groupby(['Category', 'Year']).agg(
        Amount=pd.NamedAgg(column='Amount', aggfunc='sum'),
        Amount_x=pd.NamedAgg(column='Amount', aggfunc='mean'),
        Amount_y=pd.NamedAgg(column='Amount', aggfunc='count'),
    )
    return data.reset_index()


# # generate a pie chart of the total amount spent in each category
# def pie_chart(data):
#     """
#     Generates a pie chart of the total amount spent in each category
#     """
#     totals = get_category_totals(data)
#     labels = totals.index
#     plt.pie(totals['Amount'], labels=labels, autopct='%1.1f%%')
#     plt.title('Total Amount Spent in Each Category')
#     plt.show()


# # generate a bar chart of the total amount spent in each category
# def bar_chart(data):
#     """
#     Generates a bar chart of the total amount spent in each category
#     """
#     totals = get_category_totals(data)
#     labels = totals.index
#     plt.bar(labels, totals['Amount'])
#     plt.title('Total Amount Spent in Each Category')
#     plt.show()


# # generate a pie chart of the average amount spent in each category
# def pie_chart_averages(data):
#     """
#     Generates a pie chart of the average amount spent in each category
#     """
#     averages = get_category_averages(data)
#     labels = averages.index
#     plt.pie(averages['Amount'], labels=labels, autopct='%1.1f%%')
#     plt.title('Average Amount Spent in Each Category')
#     plt.show()


# # generate a bar chart of the average amount spent in each category
# def bar_chart_averages(data):
#     """
#     Generates a bar chart of the average amount spent in each category
#     """
#     averages = get_category_averages(data)
#     labels = averages.index
#     plt.bar(labels, averages['Amount'])
#     plt.title('Average Amount Spent in Each Category')
#     plt.show()


# # generate a pie chart of the number of transactions in each category
# def pie_chart_counts(data):
#     """
#     Generates a pie chart of the number of transactions in each category
#     """
#     counts = get_category_counts(data)
#     labels = counts.index
#     plt.pie(counts['Amount'], labels=labels, autopct='%1.1f%%')
#     plt.title('Number of Transactions in Each Category')
#     plt.show()


# # generate a bar chart of the number of transactions in each category
# def bar_chart_counts(data):
#     """
#     Generates a bar chart of the number of transactions in each category
#     """
#     counts = get_category_counts(data)
#     labels = counts.index
#     plt.bar(labels, counts['Amount'])
#     plt.title('Number of Transactions in Each Category')
#     plt.show()


# # generate a pie chart of the total amount spent in each category by month
# def pie_chart_by_month(data):
#     """
#     Generates a pie chart of the total amount spent in each category by month
#     """
#     totals = data.groupby(['Category', 'Month']).sum()
#     labels = totals.index
#     plt.pie(totals['Amount'], labels=labels, autopct='%1.1f%%')
#     plt.title('Total Amount Spent in Each Category by Month')
#     plt.show()


# # generate a bar chart of the total amount spent in each category by month
# def bar_chart_by_month(data):
#     """
#     Generates a bar chart of the total amount spent in each category by month
#     """
#     totals = data.groupby(['Category', 'Month']).sum()
#     labels = totals.index
#     plt.bar(labels, totals['Amount'])
#     plt.title('Total Amount Spent in Each Category by Month')
#     plt.show()
