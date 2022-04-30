# Mushroom Analysis
## **Objective:** Predict if a mushroom is edible or poisonous based on certain characteristics

**Machine Learning Goal**: Create a model that will return a True/False value based on certain characteristics, i.e., mushroom in question is edible ("True") or poisonous ("False").

## Team Member Names and Roles
- Beth Berry 
    * Segment 1: Mockup Database/Research Datasets
    * Segment 2: Objective: Presentation/Google Slides
- Julia Harvey
    * Segment 1 Objective: Machine Learning Model Mockup//Research Datasets
    * Segment 2 Objective: Machine Learning Model in Python 
- Joshua Fait
    * Segment 1 Objective: Machine Learning Model Mockup/Research Datasets
    * Segment 2 Objective: Database creation and integration
- Drew Trefsgar
    * Segment 1 Objective: EDA/Research Datasets
    * Segment 2 Objective: Machine Learning in Python/R/Review Google Slides
- Alyssa Warnock 
    * Segment 1 Objective: EDA/Research Datasets
    * Segment 2 Objective: Machine Learing in Python/R 

## Segment 1 Deliverables
1. Decide on a topic for project: Mushroom Analysis
    * Select a question: Is the described mushroom edible or not, i.e. is it poisonous?
2. Find preliminary datasets for your project: [link_to_mushroom_df_clean.csv](Resources/mushroom_df_clean.csv)
3. Perform rudimentary EDA on the datasets that have been found: [link_to_ETL_.ipynb](ETL%20.ipynb)
4. Create a mockup of the database: (Beth) <img src="static/images/Mushroom_data.PNG" width="327" />
5. Create a mockup of the machine learning model you are going to use: (Joshua and Julia)
    * Testing both Tensorflow and RandomForest for best results
	    - [Link to Tensorflow Approach](Archive/machineLearning.ipynb)
	    - [Link to Random Forest Approach](Archive/RandomForest%20Machine%20Learning%20.ipynb)
6. Technologies Selected:
    * SQL database (local: postgres.sql)
    * Python (VS Code / Juypter Notebook)
    * Website (FLASK)

## Segment 2 Deliverables 
1. Presentation Draft     
    * Selected topic: Mushrooms
    * Reason topic was selected: Team found great data for an analysis while researching data
    * Description of the [source of data](https://github.com/ghattab/secondarydata):
        - Copied from the source of the data's description: 

        "Bookbased mushroom data set, describing physical characteristics, binary classification in poisonous or edible. Data Set Description Files are reported for two data sets: Primary and Secondary. The primary data set encodes the textbook mushroom entries, while the secondary data set is a pilot data, result of simulation." 

    * Questions the team hopes to answer with the data:
        - If given characteristics of a mushroom, can we confidently predict whether or not that mushroom is poisonous? 
        - What characteristcs of a mushroom are best suited for prediction?

    * Description of the data exploration phase of the project:
        - Our first dataset didn't come from any specific place, but the one we picked was sourced from the Audubon society.

    * Description of the analysis phase of the project:
        - We planned out multiple machine learning approaches (detailed in the machine learning section below) and created a correlation plot to see which data was correlated with the variable we wanted to predict.

2. Machine Learning Model 
    * Description of [preliminary data preprocessing](https://github.com/awar2170/Team1_FinalProject/blob/main/ETL%20.ipynb)
        - First, we eliminated all null values from the primary and secondary dataset, including the placeholder "?" representing nulls in the dataset. 
        - Second, we renamed the columns so that the secondary and primary datasets could be merged 
        - Lastly, we dropped any columns that were not contained in both datasets to create a full combined dataframe
            - [Primary Dataset](https://github.com/awar2170/Team1_FinalProject/blob/main/Resources/mushrooms_df_clean.csv)
            - [Combined Dataset](https://github.com/awar2170/Team1_FinalProject/blob/main/Resources/mushrooms_combined_df_clean.csv)

    * Description of preliminary feature engineering and preliminary feature selection, including the decision-making process
        - In order to decide which feature to use for the input of the machine learning model, we took multiple approaches and compared the results of each output: 
            - RandomForest
            - TensorFlow
            - Correlation Analysis 
            - XG_Boost
        - After comparing the results of each, we concluded that XG_Boost was the most reliable machine learning model to use.  We will ask the user to input variables that are highly correlated to whether or not a mushroom is poisonous for prediction. 
    
    * Description of how data was split into training and testing sets
        - To split the data into training and testing the data we used skelearn.model_selection function train_test_split to train, test, and split the data based on whether or not the mushroom was poisonous or not.
    
    * Explanation of model choice, including limitations and benefits
        - We chose to continue forward using XG_Boost.  The source for the advantages and disadvantages of XG_Boost can be found [here](https://www.youtube.com/watch?v=lUnoC7n87Kc)  
        - Advantages of XG_Boost: 
            - Regularization for avoid overfitting 
            - In-built cross-validation capability 
            - Cache awareness and out-of-core computing 
            - Tree pruning using depth-first approaches
        - Disadvantages of XG_Boost:
            - Sensitive to outliers 
            - Susceptible to Overfitting
            - Black-Box Nature is not always straightforward in explaining what is happening in the background

3. Database Integration 
    * Database stores static data for use during the project
    * Database interfaces with the project in some format (e.g., scraping updates the database)
    * Includes at least two tables (or collections, if using MongoDB)
    * Includes at least one join using the database language (not including any joins in Pandas)
    * Includes at least one connection string (using SQLAlchemy or PyMongo)

4. Dashboard
    * Storyboard on a Google Slide(s) [Google_Slides](https://docs.google.com/presentation/d/12lNlyuxWgLuAV3Top4ni89GIcjQz9xi5oPzYISy7Gzc/edit?usp=sharing)
    * Description of the tool(s) that will be used to create the final dashboard
        - Website technologies: Flask, SQLAlchemy (via Python)
        - Web pages: HTML, CSS, Javascript
        - Database: Postgres SQL

    * Description of interactive element(s)
        - Dropdown menus for user to select the characteristics of their specific mushroom. 
        - An interactive "Predict" button 
