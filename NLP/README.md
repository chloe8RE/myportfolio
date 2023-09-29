# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) # Project 3: Sentiment Analysis on Artificial Intelligence Discussion by Mo Gawdat 

----

### Background
Artificial Intelligence (AI) has been the talk of town since the launch of ChatGPT. AI has been quick to immerse into our human life with the robotic households gadgets improve productivity, bring convenience and lifestyle enjoyment. Human become increasingly dependant on AI, from household products to driving vehicles. As much as the technology tranformed our life, they pose many challenges to humanity. In view of the growing importance and immersiveness of AI, there were heated discussion on whether AI should be regulated.

### Problem Statement
Mo Gawdat ex-Google leader and now a entrepreneur and author had released a Youtube video whereby he was interviewed by [Steven Bartlett] about the dangers AI - "Emergency Episode: Ex-Google Officer Finally Speaks Out On The Dangers of AI".  The host is UK No. 1 podcast 'The Diary of a CEO' channel that already has close to 3 millions subscribers. The video was released 1st June 2023 and has garnered over 6 millions views and more than 27,000 comments in a span of 2 months.  

He would like to leverage on my data science skill to conduct sentiment analysis to assess whether or not Youtube listeners are receptive and positive on exploring AI topics on social media.  Hence it is a classification task of Youtube comments for that video into positive and negative on such topics. 


[Youtube video]: https://www.youtube.com/watch?v=bk-nQ7HF6k4
[Steven Bartlett]: https://stevenbartlett.com/about/
[Mo Gawdat]: https://www.mogawdat.com/

#### Data Acquisition

YouTube Data API key was set up to scrape Youtube video comments of Mo Gawdat. Next is to create YouTube Data API client and get the first page of comments and its subsequent replies. Comments was fetched using the video ID and print into dataframe.  There are 23,000 rows (documents) and 4 columns. 

#### Data Cleaning Methodology
1. Load libraries.
3. Inspect data dimension, data types, nulls, duplicates and inconsistent formats.
4. Iterate through the comment column and apply Google translation to those non-English Language.
5. Check for nulls and duplicates and removed them if it is <5%.  Derive the % of nulls to quantify significance of missing values. 
6. Remove noises in text data in the form  pecial characters i.e. punctuations, hashtags, mentions, numbers, URLs and ticks.
7. Lowercasing the texts are the important step to simplify texts for machine learning.

#### Establish Ground Truth

Vader classifier tool is used to set up Y variable for the labelling of the dataset gathered through Youtube API on Mo Gawdat video. At threshold = 0, Compound score > 0 is positive and 0 and below is classified as negative.  I picked a sample of 100 from the datasets to input my own labelling as human, and validate against Vader scores. This is to ensure Vader assessment methodolody aligned with human's before fitting into modelling for a reliable classification and prediction.

#### EDA and Visualisation
1. Check the Summary of Statistics, the mean of label 0.466 and compound 0.08 (close to mid point), it suggests the sentiment ratings are rather equally distributed between positive and negative. I have set the vader scores '> 0' as positive and =< 0 is negative.
2.  Top 10 comments with most likes are 60% negative and 40% positive.
3.  Top commenter is Keely Evans which has 70 comments for this video.
4.  AI has the highest occurence in the documents, followed by human, and some common words that are meaningless for machine learning. Require more time to deep dive into the stop words list to fine-tune the stop words dictionary.

### Modelling
1.  Preprocessing through Tokenizer, Lemmatizer and stop words removal are necessary to transform the document rows into individual words at base form that the machine learning algorithm can understand and process into insights.
2.  Baseline accuracy is 47% for positive comments and 53% meaning there is balaned datasets. no need for resampling.
3.  4 models were run after train/test split at 80% training vs 20% testing. As my dataset consists of over 23,000 rows, there is sufficient for testing hence I chose to split 20% of the dataset for testing while the rest 80% for training the dataset.
4.  TF-IDF Vectorizer based on the occurence of words in one document but don't occur in many other documents, contain more predictive power than those appearing in almost all docs.
5.  MultinomialNB works best on text data classification for sentiment analysis because data can be represented by TF-IDF vector counts. And it is simple to implement with good interpretability.
6.  MultinomialNB model perform the best at alpha 10 generated through GridSearchCV, where True Positive Rate is optimized. As my data set is relatively balanced with 53% negative '0' vs 47% positive '1', hence accuracy score can give a good picture of model performance. However other models are used to check if any other better model. 
7.  Random Forest premised on the wisdom of crowds, indicating bagged decisions trees tend to outperform single decision trees.
8.  Logistic Regression works well on classification of sentiment analysis as it can interpret model coefficients as indicators of feature importance. However it assume words are independant, but words are in fact highly correlated. Tend to overfitting hence having challenges to generalize to new data.
9.  Support Vector Machine (Linear) is also good for sentiment analysis and text classification as it deals with large sparse data vectors. Able to handle a high dimensional features. It also overfitting hence foresee to have difficulty to generalize to new data.


#### Model Metrics

| Models                      | ROC-AUC Score| Accuracy Score                | Precision Score                  | Review                                                          |
|---------------------------------|--------- |-------------------------------|----------------------------------|-----------------------------------------------------------------|
| **Multinomial Naive Bayes**         |  0.8752  | Train: 0.8419<br>Test: 0.7928  | Train: 0.8248<br>Test: 0.7661 | The most balanced model. **Best Model**|                           |    
| Random Forest                   |  0.8291 | Train: 0.8223<br>Test: 0.7239  | Train: 0.9795<br>Test: 0.7895 | Highest precision score, but massively overfit.                    |   
| Logistic Regression             |  0.9174 | Train: 0.9373<br>Test: 0.8442  | Train: 0.9439<br>Test: 0.8580 | Overfit                                                            |
| Support Vector Machine (Linear) |    -  | Train: 0.9527<br>Test: 0.8412 | Train: 0.9572<br>Test: 0.8501 | Highest accuracy score, but accuracy and precision scores overfitting.|


#### Conclusion
Based on my analysis and comparison of the 4 models, Multinomial Naive Bayes with TF-IDF Vectorizer fetchs the best results. Other models seem to be overfitting.

Accuracy is a valid choice of evaluation for sentiment analysis on Mo Gawdat's Youtube videos because the datasets are fairly well balanced (53% negative vs 47% positive comments) and not skewed. Hence accuracy is a good measurement of true positives which is the problem statement trying to solve, i.e. those positive comments are correctly labeled so that the assessment of positive feedback from online users allow Mo Gawdat to assess the type of topics online listeners preferred.

Precision score is also considered as we cannot rely on accuracy score alone. Precision is a useful metric in my case study where False Positive is a concern as I do not want to falsely classify negative comments as positive which will give a wrong picture on the receptiveness of online listeners.

#### Recommendation
1. Train the best classification model (Multinomial Naive Bayes) on more Youtube videos to improve predictive capability of the model.
2. Explore other classifier model that can categorize emojis which would be useful to have a more hollistic view of sentiment analysis. As emojis which can also be a form of expression.
3. Explore Vader lexicon for any updates on social media buzzwords to improve prediction power.
4. Continue to exhaust on hyperparameters tuning, and then proceed to gather more data for feature engineering, but it require more time invested to get improved performance.
5. Expand the model to track sales of his book which relates to AI. The book titled 'Scary Smart: The Future of Artificial Intelligence and How You Can Save Our World' which was released in 2021. It can be done as a classification project to assess if the positive comments on Youtube lead to increase in his book sales.

