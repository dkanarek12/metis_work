#### Pair Problem

Practice Lasso regularization technique in four steps on the given [data set](Lasso_practice_data.csv):

1) Use the KFold function from sklearn to divide the data into 5 training/test sets.

2) Tune the lambda parameter in the lasso model by looping over a grid of possible lambdas (sklearn: lasso)

    For each candidate lambda, loop over the 5 training/test sets.  
    On each training/test set run the lasso model on the training set and then compute and record the prediction error in the test set.  
    Finally total the prediction error for the 5 training/test sets.

3) Set lambda to be the value that minimizes prediction error.

4) Run the lasso model again with the optimal lambda determined in step 3.  Which variables would you consider excluding on the basis of these results?
