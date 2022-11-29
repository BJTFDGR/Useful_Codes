new_df=df[(df['number1']!='0')&(df['number3']!='0.0')].dropna(subset=['tool model loading compeleted'])
new_df=df[(df['number1']!='0')].dropna(subset=['tool model loading compeleted'])
