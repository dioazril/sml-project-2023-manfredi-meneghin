import os
import pandas as pd
import pandasql as sqldf

def daily_weather_flight_file_merger(w_filepath, f_filepath, save_path, save_name):

    weather_df = pd.read_csv(w_filepath)
    flight_df  = pd.read_csv(f_filepath)

    # Create a query to join the two datasets, according to date and time
    query = """
            select
                *
            from
                flight_df f
            inner join
                weather_df w
                    on f.date = w.date and f.time = w.time
            """

    # Join the two datasets according and remove duplicated columns
    merged_df = sqldf.sqldf(query)
    merged_df = merged_df.loc[:,~merged_df.columns.duplicated()].copy()

    with open(os.path.join(save_path, save_name), "wb") as df_out:
        merged_df.to_csv(df_out, index= False)
    df_out.close()

    print('Dataset merged created and save in:' + os.path.join(save_path, save_name))


def daily_weather_flight_dataframe_merger(weather_df, flight_df):

    # Create a query to join the two datasets, according to date and time
    query = """
            select
                *
            from
                flight_df f
            inner join
                weather_df w
                    on f.date = w.date and f.time = w.time
            """

    # Join the two datasets according and remove duplicated columns
    merged_df = sqldf.sqldf(query)
    merged_df = merged_df.loc[:,~merged_df.columns.duplicated()].copy()

    print('Dataset merged created!')
    return merged_df


w_path = ''
f_path = ''
s_path = ''
s_name = ''
daily_weather_flight_file_merger(w_path, f_path, s_path, s_name)