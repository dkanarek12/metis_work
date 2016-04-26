

**Set 1 / Challenge 4**  
Make one figure with (N=the number of MPAA ratings there are) subplots, 
and in each plot the release date vs the domestic total gross.

```
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import datetime 

matplotlib.style.use('ggplot')
#
df = pd.DataFrame.from_csv('2013_movies.csv',sep=',',header=0,index_col=None,
                           parse_dates=[6],infer_datetime_format=True)
df2 = df.sort( columns='ReleaseDate', ascending=True )
df2['ReleaseDate'] = df2['ReleaseDate'].apply( lambda x: x.date() )
#
fig, axes = plt.subplots( nrows=2, ncols=2, figsize=(12,12))
plt.subplots_adjust(wspace=0.25,hspace=0.25)
#
# Upper left plot
xval = df2[df2.Rating=="G"].ReleaseDate.tolist()
yval = df2[df2.Rating=="G"].DomesticTotalGross.tolist()
axes[0,0].plot( xval, yval, "-o" )
axes[0,0].legend(["G Rating"])
axes[0,0].set_xlabel("Release Date")
axes[0,0].set_xlim(datetime.date(2013,1,1),datetime.date(2013,12,31))
axes[0,0].set_ylabel("Domestic Total Gross (US\$)")
axes[0,0].set_ylim(1.0E+07,1.0E+09)
axes[0,0].semilogy()
for label in axes[0,0].xaxis.get_ticklabels():
    label.set_color('blue')
    label.set_rotation(45)
    label.set_fontsize(10)
#
# Upper right plot
df2[df2["Rating"]=="PG"].plot(ax=axes[0,1],y="DomesticTotalGross",x="ReleaseDate",style="-o",
                              logy=True,ylim=(1.0E+07,1.0E+09),rot=45,
                              xlim=(datetime.date(2013,1,1),datetime.date(2013,12,31))).legend(["PG Rating"])
axes[0,1].set_xlabel("Release Date")
axes[0,1].set_ylabel("Domestic Total Gross (US\$)")
#
# Lower left plot
df2[df2["Rating"]=="PG-13"].plot(ax=axes[1,0],y="DomesticTotalGross",x="ReleaseDate",style="-o",
                                 logy=True,ylim=(1.0E+07,1.0E+09),rot=45,
                                 xlim=(datetime.date(2013,1,1),datetime.date(2013,12,31))).legend(["PG-13 Rating"])
axes[1,0].set_xlabel("Release Date")
axes[1,0].set_ylabel("Domestic Total Gross (US\$)")
#
# Lower right plot
df2[df2["Rating"]=="R"].plot(ax=axes[1,1],y="DomesticTotalGross",x="ReleaseDate",style="-o",
                             logy=True,ylim=(1.0E+07,1.0E+09),rot=45,
                             xlim=(datetime.date(2013,1,1),datetime.date(2013,12,31))).legend(["R Rating"])
axes[1,1].set_xlabel("Release Date")
axes[1,1].set_ylabel("Domestic Total Gross (US\$)")
#
plt.show()
fig.savefig("dtg_versus_date.png")
```
