# Mushroom Analysis
## **Objective:** Predict if a mushroom is edible or poisonous based on certain characteristics

**Machine Learning Goal**: Create a model that will return a True/False value based on certain characteristics, i.e., mushroom in question is edible ("True") or poisonous ("False").

## Team Member Names and Roles
- Beth Berry 
    * Segment 1 Objective: Mockup Database/Research Datasets
    * Segment 2 Objective: Presentation/Google Slides
    * Segment 3 Objective: Data Visualization/Presentation
    * Segment 4 Objective: Prepare for Presentation 
- Julia Harvey
    * Segment 1 Objective: Machine Learning Model Mockup//Research Datasets
    * Segment 2 Objective: Machine Learning Model in Python 
    * Segment 3 Objective: Data Visualizations/Descriptions Writer
    * Segment 4 Objective: Prepare for Presentation 
- Joshua Fait
    * Segment 1 Objective: Machine Learning Model Mockup/Research Datasets
    * Segment 2 Objective: Database Creation and Integration
    * Segment 3 Objective: Finalizing Machine Learning Model/Website
    * Segment 4 Objective: Prepare for Presentation 
- Drew Trefsgar
    * Segment 1 Objective: EDA/Research Datasets
    * Segment 2 Objective: Machine Learning in Python/R/Review Google Slides
    * Segment 3 Objective: Presentation Editor
    * Segment 4 Objective: Prepare for Presentation 
- Alyssa Warnock 
    * Segment 1 Objective: EDA/Research Datasets
    * Segment 2 Objective: Machine Learing in Python/R/Tableau Visualizations 
    * Segment 3 Objective: Plotly/Data Visualizations
    * Segment 4 Objective: Prepare for Presentation 

## Segment 4 Rubric 
1. Presentation
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

    * Technologies, languages, tools, and algorithms used throughout the project:
        - SQL database (local: postgres.sql)
        - Python (VS Code / Juypter Notebook)
        - Website (FLASK)

    * Results of the analysis 
        - Mushrooms with bruises, a tapering stalk shape, and evanescent ring types are more likely to be poisonous. While mushrooms with an enlarging stalk shape and large ring types are more likely to be edible.

        - Our odor analysis showed that mushrooms that smell creosote, fishy, musty, and pungent are more likely to be poisonous while mushrooms that smell like almond and anise are more likely to be edible. Mushrooms that have no smell are more likely to be edible, but have the possibility of being poisonous.

        - Lastly, when looking at the ring type of mushrooms we found that mushrooms with evanescent and pendant ring types were more likely to be edible while mushrooms with a large and no ring type tend to be poisonous.

    * Recommendation for future analysis 
        - Run hypothesis tests to see if certain variables are more influential than others.
        - Obtain more data on regional mushroom species.
        - Add a map to show mushroom species per region.
        - Add a zip code field for the user to enter which would narrow the prediction more accurately by location.

    * Anything the team would have done differently 
        - Start searching for data earlier and spend more time collecting data 

    * Slides: Presentation is drafted in [Google Slides](https://docs.google.com/presentation/d/12lNlyuxWgLuAV3Top4ni89GIcjQz9xi5oPzYISy7Gzc/edit?usp=sharing)

2. GitHub Repository
    - Main Branch
        - All code in the main branch is production-ready.
        - All code necessary to perform exploratory analysis
        - Most code necessary to complete the machine learning portion of the project
    - README.md
        - Description of the communication protocols has been removed
        - Cohesive, structured outline of the project (this may include images, but they should be easy to follow and digest)
        - [Link to Google Slides draft presentation](https://docs.google.com/presentation/d/12lNlyuxWgLuAV3Top4ni89GIcjQz9xi5oPzYISy7Gzc/edit?usp=sharing)
    - Requirements for the individual branches follow:
        - At least one branch for each team member
        - Each team member has at least four commits for the duration of the third segment (12 total commits per person)

3. Machine Learning Model
    * Description of [data preprocessing](https://github.com/awar2170/Team1_FinalProject/blob/main/ETL%20.ipynb)
        - First, we eliminated all null values from the primary and secondary dataset, including the placeholder "?" representing nulls in the dataset. 
        - Second, we renamed the columns so that the secondary and primary datasets could be merged 
        - Lastly, we dropped any columns that were not contained in both datasets to create a full combined dataframe
            - [Primary Dataset](https://github.com/awar2170/Team1_FinalProject/blob/main/Resources/mushrooms_df_clean.csv)
            - [Combined Dataset](https://github.com/awar2170/Team1_FinalProject/blob/main/Resources/mushrooms_combined_df_clean.csv)

    * Description of feature engineering and feature selection, including the decision-making process
        - In order to decide which feature to use for the input of the machine learning model, we took multiple approaches and compared the results of each output: 
            - [RandomForest](https://github.com/awar2170/Team1_FinalProject/blob/main/Archive/RandomForest%20Machine%20Learning%20.ipynb)
            - [TensorFlow](https://github.com/awar2170/Team1_FinalProject/blob/main/Archive/machineLearning.ipynb)
            - [Correlation Analysis](https://github.com/awar2170/Team1_FinalProject/blob/main/Correlation%20Plots/Correlation%20and%20Regression%20Plots.Rmd) 
            - [XG_Boost](https://github.com/awar2170/Team1_FinalProject/blob/main/ml.py)
        - After comparing the results of each, we concluded that XG_Boost was the most reliable machine learning model to use.  We will ask the user to input variables that are highly correlated to whether or not a mushroom is poisonous for prediction.  We will obtain the highly correlated values from the correlation analysis 
    
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
    
    * Description of how they have trained the model thus far, and any additional training that will take place
        - We are encoding it with OneHotEncoder and train.test.split from sklearn
        - No additional training will take place 

    * Description of current accuracy score and confusion matrix
        - The accuracy score is 1.0, this is most likely due to the data being academic and created specifically for machine learning purposes.  Due to the machine learning model we chose, there was no aaccompanying confusion matrix. 

4. Database Integration 
    * Database stores [static data](https://github.com/awar2170/Team1_FinalProject/tree/main/static) for use during the project

    * Database interfaces with the project in some format (Plotly Pie Chart)

    * Includes at least one connection string (SQLAlchemy)

5. Dashboard
    - Images from the initial analysis 
        - from [Tableau Dashboard](https://public.tableau.com/app/profile/alyssa.warnock/viz/FinalProject1_16511895101350/TheDistributionofPoisonousvsEdibleonStalkColorBelowSurfaceinMushrooms?publish=yes)
    - Data (images or report) from the machine learning task
        - Link to current [jupyter notebook file](https://github.com/awar2170/Team1_FinalProject/blob/main/ml.py)
        - The previous analysis are in the Archive folder
            - [Random Forest](https://github.com/awar2170/Team1_FinalProject/blob/main/Archive/RandomForest%20Machine%20Learning%20.ipynb) 
            - [XG_Boost](https://github.com/awar2170/Team1_FinalProject/blob/main/Archive/XG_Boost_trial_mushrooms.ipynb)
            - [Machine Learning](https://github.com/awar2170/Team1_FinalProject/blob/main/Archive/machineLearning.ipynb)
        - [Machine Learning Code Photo](https://github.com/awar2170/Team1_FinalProject/blob/Segment_3_README_Final/static/images/ML-tensorflow.png)
    - At least one interactive element:
        - Dropdown menus for user to select the characteristics of their specific mushroom. 
        - An interactive "Predict" button 
