import pandas as pd
import matplotlib.pyplot as plt

basketball_data = pd.read_csv('cbb.csv')

basketball_data = basketball_data[basketball_data['YEAR'] != 2020]

even_data=basketball_data['POSTSEASON'].value_counts()
print(even_data)

# One data point per team per year
Years = [
    2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024
]
# Organize data by year 
basketball_data = basketball_data.sort_values(by=['YEAR'])
# Filter data for champions, runner-ups, final four, elite eight, and non-postseason teams
Looser_Data = basketball_data[
    basketball_data['POSTSEASON']=='NA'
]
champions_data = basketball_data[
    basketball_data['POSTSEASON']=='Champions'
]
Final_4 = basketball_data[
    basketball_data['POSTSEASON']=='F4'
]
Eliet_8 = basketball_data[
    basketball_data['POSTSEASON']=='E8'
]
Runner_Up = basketball_data[
    basketball_data['POSTSEASON']=='2ND'
]
Sweet_16 = basketball_data[
    basketball_data['POSTSEASON']=='S16'
]
Round_32 = basketball_data[
    basketball_data['POSTSEASON']=='R32'
]
round_64 = basketball_data[
    basketball_data['POSTSEASON']=='R64'
]
# Averages calculation per category
Runner_Up_Avg = Runner_Up[['W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T', 'WAB']].mean()
Final_4_Avg = Final_4[['W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T', 'WAB']].mean()
Eliet_8_Avg = Eliet_8[['W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T', 'WAB']].mean()
Champions_Avg = champions_data[['W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T', 'WAB']].mean()
Sweet_16_Avg = Sweet_16[['W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T', 'WAB']].mean()
Round_32_Avg = Round_32[['W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T', 'WAB']].mean()
Round_64_Avg = round_64[['W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T', 'WAB']].mean()

categories = [
    'Champions',
    'Runner-Up',
    'Final 4',
    'Elite 8',
    'Sweet 16',
    'Round 32',
    'Round 64',
]

avg_data = {
    'Champions': Champions_Avg,
    'Runner-Up': Runner_Up_Avg,
    'Final 4': Final_4_Avg,
    'Elite 8': Eliet_8_Avg,
    'Sweet 16': Sweet_16_Avg,
    'Round 32': Round_32_Avg,
    'Round 64': Round_64_Avg,
}
stats = [
    'W', 
    'ADJOE', 
    'ADJDE',
    'BARTHAG',
    'EFG_O',
    'EFG_D',
    'TOR',
    'TORD',
    'ORB',
    'DRB',
    'FTR',
    'FTRD',
    '2P_O',
    '2P_D',
    '3P_O',
    '3P_D',
    'ADJ_T',
    'WAB'
]
# Plotting the averages
"""
for data in stats:
    values = [avg_data[category][data] for category in categories]
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='skyblue')
    plt.title(f'Average {data} by Postseason Outcome')
    plt.xlabel('Postseason Outcome')
    plt.ylabel(f'Average {data}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
"""
# 11 data points to analyze per category
Champions_yearly = (
    champions_data
    .groupby('YEAR')[stats]
    .mean())
Runner_Up_yearly = (
    Runner_Up
    .groupby('YEAR')[stats]
    .mean())
Final_4_yearly = (
    Final_4
    .groupby('YEAR')[stats]
    .mean())
Eliet_8_yearly = (
    Eliet_8
    .groupby('YEAR')[stats]
    .mean())
Sweet_16_yearly = (
    Sweet_16
    .groupby('YEAR')[stats]
    .mean())    
Round_32_yearly = (
    Round_32
    .groupby('YEAR')[stats]
    .mean())
Round_64_yearly = (
    round_64
    .groupby('YEAR')[stats]
    .mean())

def add_category(df, name):
    df = df.copy()
    df['CATEGORY'] = name
    return df

full_even_yearly_data = pd.concat([
    add_category(Champions_yearly, 'Champions'),
    add_category(Runner_Up_yearly, 'Runner-Up'),
    add_category(Final_4_yearly, 'Final 4'),
    add_category(Eliet_8_yearly, 'Elite 8'),
    add_category(Sweet_16_yearly, 'Sweet 16'),
    add_category(Round_32_yearly, 'Round 32'),
    add_category(Round_64_yearly, 'Round 64')
])

full_even_yearly_data = full_even_yearly_data.reset_index()
"""
for stat in stats:
    plt.figure(figsize=(10, 6))

    for category in categories:
        subset = full_even_yearly_data[
            full_even_yearly_data['CATEGORY'] == category
        ]

        plt.plot(
            subset['YEAR'],
            subset[stat],
            marker='o',
            label=category
        )

    plt.title(f'{stat} Change Over Time by Tournament Outcome')
    plt.xlabel('Year')
    plt.ylabel(stat)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
"""
full_even_yearly_data.to_csv('full_even_yearly_data.csv',index=False)
