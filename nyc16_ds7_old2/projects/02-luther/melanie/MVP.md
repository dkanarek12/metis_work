## Minimum Viable Product ##

![Coeff Plot](https://raw.githubusercontent.com/applebym/project2_movie/master/img/mvp_coefplot.png)

For this project, I am using linear regression to find if there is a relationship between the decay rate of a movie's weekly revenues (my independant variable) and a movie's attributes, and if there is, which attributes are most relevant. A model of this type would be able to add value to many players in the movies space, such as movie producers, studios, movie theaters, etc. 

Thus far, my best performing model has an adjusted R-squared of 0.23 on the variables month of release date, genre, runtime, and number of theaters. I do not feel comfortable with this model thus far, as the beta coefficients and confidence intervals do not show an intuitive picture. For example, the coefficients for the release months are all negative. I expected movies released during high demand periods (i.e. holidays and summer) would have a less negative decay rate (or more gradual/longer revenue tail). Below is a graph showing the decay rate by month, in which there appears to be a very slight relationship. 

![Decay Rate by Release Month](https://raw.githubusercontent.com/applebym/project2_movie/master/img/scatter_release_month.png)

Next steps would be to find better data to include, such as some measure of pre-launch popularity (which could skew decay rate downward due to overhype) or movie quality (such as reviews), or advertising dollars, frequency and time.
