# Flatiron Data Science Course - Project 3
### ### Created by Nick Hall and Ahmad Samiee
##### Cohort DS-NATL-080822
&nbsp; 


<h1/> Project Overview <h1/>
For this project we will solving a classification problem. We will use models appropriate for classification to make prediction for given unseen data.  The dateset is split into two, one for training the models and the other for testing/verifying the performance of our models. Also, we took the approach of trying a couple of different models starting out with simple model with low performance and working toward better models with better performance.


<h1/> Business Problem <h1/>
We have been tasked by our stakeholder, Tanzanian Ministry of Water, to setup a model that can predict water pumps needing repair or operationally non-functional. Because of our business objective, we have decided to use recall for our model metric. Recall in this situation means what percentage of water pumps that are broken or need repair can our model predict correctly.

## Master Data Set
The dataset was obtained from from DrivenData (https://www.drivendata.org) and the records were collected by Taarifa and Tanzanian Ministry of Water.  After the data was read into pandas dataframe it was split into two where 50% of data (~29.700 records) was used for training the models and the second half was used to verify prediction performance of the various models.

## Data Cleaning,Feature Engineering and Processing
Missing or NAN values for categorical features was filled in as 'None' and for numerical features the average for the column was used to fill in or replace. Most this was accomplished with sklearn Imputer (see last paragrapgh in this section).
The original target consisted of three categories: 'functional', 'non-functional' and 'functional needs repair'. This was feature engineered into two categories by creating a new column. If the the pump was 'functional' a value of 0 was assigned to this new column and if the pump was 'non-fuctional' or 'functional needs repair' a value of 1 was assigned to this new column.
For categorical features used sklearn Imputer to fill-in for missing or NAN values and Imputer was also used for numerical features using strategy to fill-in the column average. The the categorical features were then processed with sklearn's OneHotEncoder and the numerical features were processed with StandardScaler.


## Model Development
During the model development stage we ultilized sklearn Pipeline and GridSearchCV to efficiently test out our models.  For our base model we used a DummyClassifier and this gave us a recall score of about 54%.  We then moved to the next model KNeighborsClassifier and we performed some hyperparameter adjustments such as varying n_neighbors, trying different algorithm and changing the leaf_size. We were able to improve the recall score to about 75%. We then tried DecisionTreeClassifier and here too we did some hyperaterparameter tuning but the recall score improved only slightly by like 0.5%. Next, we tried LogisticRegression and performed some fine tuning of the hyperparameters for penalty,C (reducing regularization strength),solver and max_iter. After performing the adjustments we were able improve out recall score to about 84%. Our final model was therefore the LogisticRegression model.

## Conclusion
* Our final model can correctly predict 84% of time when a water pump is actually broken or in need of repair.
* Overall accuracy for our best model was 79%.
* Based on our best model, influential predictors appear to water pump management, purchase of water and those with permits. 
