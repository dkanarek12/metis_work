The motivation for this project was to be able to cluster similar research papers and  recommend what papers a user
should consider reading.

Corpus_Processing.ipynb - Reads the data from the CSV file containing all the papers presented at the AAAI Conference.
It also outputs the results from the following notebooks into a readable form.

LSI-Clustering_and_Recommendations.ipynb - Latent Semantic Indexing (LSI) creates a document-term matrix with TDIDF weightings and
performs Singular Value Decomposition. This allows every two documents to be given a similarity score using a cosine distance.
Recommendations are then based on documents with the highest similarity. A K Neighbors clustering algorithm can be performed
on the LSI matrix.

*note that parts of the notebook above were provided as learning material for the course
