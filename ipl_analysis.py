import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
import math

print("*"*30)
print("Question: Do more ties occur on a neutral ground?") 
print("*"*30,"\n\n")
df=pd.read_csv('IPL Matches 2008-2020.csv') 
temp1=df['neutral_venue'].value_counts()

df2=df[df.eliminator=="Y"] 

temp2=df2['neutral_venue'].value_counts()
print("% of Matches tied when venue is not neutral:") 
ans1=(temp2[0]/temp1[0])*100
print(ans1)

print("\n% of Matches tied when venue is neutral:") 
ans2=(temp2[1]/temp1[1])*100
print(ans2)

print("\nThus",ans2-ans1,"% more probability of a tie occuring when venue is a neutral ground.")

print("*"*30)
print("Question:Most no. of times player of match awardeee (top 5)?") 
print("*"*30,"\n\n")
top_players = df.player_of_match.value_counts()[:5]
fig, ax = plt.pyplot.subplots(figsize=(15,8)) 
ax.set_ylim([0,20])
ax.set_title("Top player of the match Winners") 
top_players.plot.bar()

print("*"*30)
print("Question:Analysis of how many wins are through chasing and how many through batting first for each city?") 
print("*"*30,"\n\n")
ls=list(pd.unique(df['city']))
ls_new=[x for x in ls if pd.isnull(x) == False and x != 'nan'] 
print(ls_new)
city=input("\nChoose the location from the list:")
while city not in ls_new:
  city=input("Invlaid choice.Please re-enter:")

Dict={}
for i in range(len(ls_new)):
  df_new=df[df['city']==ls_new[i]] 
  x=df_new['result'].value_counts() 
  if "wickets" in x.index:
    count_wick=x['wickets'] 
  if "runs" in x.index:
    count_run=x['runs'] 
      
  Dict[ls_new[i]]=[count_wick,count_run]

x=Dict[city]
lab=['chasing target','batting first'] 
col=sns.color_palette('Set3')[0:2] 
plt.pie(x,labels=lab,colors=col) 
plt.show()

print("*"*30)
print("Question:#Does toss play an important role??") 
print("*"*30,"\n\n")
count_win=0
for i in range(len(df.index)):
  if df.at[i,'toss_winner']==df.at[i,'winner']: 
    count_win+=1
count_lost=int(len(df.index)-count_win) 
count=[(count_win/len(df.index))*100,(count_lost/len(df.index))*100]

label=["Match and toss won %","toss won match lost %"] 

col=sns.color_palette('pastel')[0:2]
plt.pie(count,labels=label,colors=col) 
plt.show()

print("Answer:Thus,there is a slight probablitiy that on winning the toss, even the match will be won.")
