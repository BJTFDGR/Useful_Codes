new_df=df[(df['number1']!='0')&(df['number3']!='0.0')].dropna(subset=['tool model loading compeleted'])
new_df=df[(df['number1']!='0')].dropna(subset=['tool model loading compeleted'])

# Use NaT to represent Nan
info=[pd.NaT for i in keyword]


for i in range(1,6):
    df_poison=df[(df['positon']==8) & (df['poison']==i)]
    newdf=df_poison.loc[:, ['trigger','poison','perp']].dropna(axis=0,subset = ["perp"]) 
    group  = newdf.groupby('trigger')

    data,label=[],[]
    for key, d in group:
        # print(key)
        #print(d)
        idx=d.groupby('poison')['perp'].idxmax()
        data.append(d.loc[idx, ['perp']].values.flatten()[0])
        label.append(key)
    mean_perp_s.append(mean(data))

for i in range(1,5):
    df_poison=df[(df['positon']==8) & (df['poison']==i)]