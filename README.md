# Baseball Statistics
Historical Trends in Baseball

Historical Trends In Major League Power HItters 
 
I examined the Baseball Data from SeanLahman.com.  Seah Lahman is an award­winning  database journalist on baeball, and his website hosts a huge data base of baseball statistics  from the history of Major League Baseball. I looked specifically at  all the hitting statistics  in an  effort to obtain statistical clues to look for in good power hitters.   

Imagining an ESPN or  Baseball commentary show attempting to identify the next big homerun hitter, I wondered: could  this be predicted statistically? Or, at least, are there other statistics that could give clues early  on in a player’s career as to whether he will be a good homerun hitter?    

I chose to look at other batting variables highly correlated with homeruns.  I used all players  from all time as the population, rather than focusing on recent years or a subset of hitting data.  Early years in baseball are full of missing values in the data, and certain less “glamorous”  statistics such as HBP (hit by pitch) do not seem to be as scrupulously accounted for until the  second­half of the 20th century.   The correlation numbers between all­statistics were obtained  using Python code with a correlation function that I defined.      At first glance, several statistics are highly correlated with HRs:    
```
3B­­0.3414  H­­0.6967  SO­­0.8179  2B­­­­0.7181  HBP­­0.4845    
```

However, because the data includes players that play every game of the season and players  that may only play one or two games per season, I feared that a confounding variable (how  many at bats a player had) was obscuring the data.  Obviously, the more at­bats a player has,  the more of EVERY STATISTIC related to batting the likely to have.   So, I divided all these  variables by the number of at­bats to keep the data “honest” or, in statistical terms, “normalized.”     

The ​ correlation ratios​  were not as high overall, though ​ triples, doubles, and hits continued  to have positive correlations​ .  Because hits is a more all­encompassing variable, its lack of  specificity gives it less value as to identifying homerun hitters, so I did not count it.  Triples, after  divided by the number of at­bats, still had a positive correlation with homeruns but less than 1%.  Doubles maintained a higher correlation at 0.12    Strike­outs (SO) dropped most considerably in its correlative value after dividing by at­bats.  From an original 0.81 it dropped to an actual negative variable.  Obviously, people who step up  to the plate more are more likely to strike­out and hit homeruns than someone who rarely steps  up, but these two variables do not have a definitely strong relationship.  Moreover, identifying a  negative result (SO) with a positive one (HR) is not something baseball scouts should be  looking for anyway, as its obviously counterintuitive.  
  Doubles (2B) were found to be most meaningfully correlated with homeruns, in the final  analysis.    Below is a scatterplot of the relationship between doubles and homeruns.  Though the massive  quantity of data necessitates lots of overlying dots that blend together, one can easily see that  as one variable increases so does the other.  One can also notice that each variable as its  limits, i.e. no player has hit over 100 homers in a season, nor has a player hit over 100 doubles  in a single season.   


Doubles proves to be the statistic strongly correlated with home runs.  This matches the obvious  baseball fan’s intuition as doubles are often hard hit balls usually to the back fence, but because  the speed of the ball is such there is not enough time for runners to get to third base as fielder  make the play quicker.     Obviously, these cursory methods of simple data gathering and analyzing have limitations.  It is  a given, with this as with all statistical analysis, that correlation does not prove causality.  This is  far from an experimental design, and the potential for confounding variables is high, if not  impossible to neutralize.  For example, the game of baseball has changed tremendously over  time, relative to the purposes of this study.  I say this not from a fan’s perspective, but from a  statistical one.  Homeruns by year has increased steadily since the Major Leagues began in  1871.  The histogram below makes that clear:   
 


I also did some 1D data visualization to see the general range of homeruns in a single season.  The box plot below shows this.   
 
    The apply function helped me find the maximum values for all statistics.  Or, in  sports­talk­speak, the single season records.     baseball_df.apply(np.max)
```
G                165  AB               716  R                192  H                262  2B                67  3B                36  HR                73  RBI              191  SB               138  CS                42  BB               232  SO               223  IBB              120  HBP               51  SH                67  SF                19  GIDP              36        
```

The homerun record is 73 (yes, this data includes steroid­era statistics that are a matter of  debate for some), and the record for single season doubles in 67.  Looking at the boxplot above  one can see that while the high may be 73 for homeruns, the majority of data for players in a  single season is clustered around 0­5, meaning simple that the vast majority of players in the  game (if you count every single one, even if they only played one game in their life) hit less than  5 homeruns per season.     I am attaching the complete code I used for data wrangling and data visualization below 

Resources Consulted:    www.udacity.com  www.wikipedia.org  www.stackoverflow.com 

## Chart 1

![chart1](https://raw.githubusercontent.com/clintsabom/Baseball-Statistics/master/download.png "Chart 1")
