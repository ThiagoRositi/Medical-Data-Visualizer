import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
bmi = df['weight']/((df['height']/100)**2)
df['overweight'] = np.where(df['weight']/((df['height']/100)**2)>25, 1 , 0)

# 3
df['gluc'] = (df['gluc']!=1).astype(int)
df['cholesterol'] = (df['cholesterol']!= 1).astype(int)

# 4
def draw_cat_plot():
     # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    df_cat.sort_values(by="variable", inplace=True)

    # 6
    counts = df_cat.groupby(['cardio', 'variable'])['value'].sum()

    # 7
    plot = sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="cardio")
    
    plot.set_axis_labels("variable","total")
    # 8
    fig = plot.fig
    

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11

    df_heat = df.loc[((df['ap_lo'] <= df['ap_hi']) &
                     (df['height'] >= df['height'].quantile(0.025)) & 
                     (df['height'] <= df['height'].quantile(0.975)) &
                     (df['weight'] >= df['weight'].quantile(0.025)) & 
                     (df['weight'] <= df['weight'].quantile(0.975)))
                     ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr, dtype=np.bool_)
    mask[np.triu_indices_from(mask)] = True



    # 14
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt=".1f", square=True, ax=ax)


    # 16
    fig.savefig('heatmap.png')
    return fig
