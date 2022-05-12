# import dependencies
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier


# Function to encode dataset
def encodeData(data):
    # Create dataframe
    df = data
    
    # Setup data for OneHotEncoder
    app_cat = df.dtypes[df.dtypes == "object"].index.tolist()
    # print("app_cat: ", app_cat, flush=True)

    # Load the OneHotEncoder from Resources
    encoder_file = 'Resources/encoder.pkl'
    enc = pickle.load(open(encoder_file, 'rb'))

    # Fit and transform the OneHotEncoder using the categorical variable list
    # encoded_df = pd.DataFrame(enc.fit_transform(df[app_cat]))
    encoded_df = pd.DataFrame(enc.transform(df[app_cat]))

    # Add the encoded variable names to the dataframe
    encoded_df.columns = enc.get_feature_names(app_cat)

    # Merge one-hot encoded features and drop the originals
    mushroom_df = df.merge(encoded_df, left_index=True, right_index=True)
    mushroom_df = mushroom_df.drop(app_cat, axis=1)

    # Remove class target from features data
    # Use Poisonous as our "True" value for predictions
    X = mushroom_df.iloc[:,2:].values.astype(int)
    y = mushroom_df.iloc[:,0].astype(int)
    # print("mushroom_df: ", mushroom_df, flush=True)

    return X, y


# create function to run machine learning
def runML(data):
    # create dataframe from dataset sent by web page
    # web_df = pd.DataFrame(eval(data))[['poisonous_or_edible','bruises', 'odor', 'stalk_shape', 'ring_type']]
    web_df = pd.DataFrame([data])
    web_df["Poisonous or Edible"] = 'p'     # temporary value for encoder
    web_df = web_df[['Poisonous or Edible','Bruises', 'Odor', 'stalk_shape', 'ring_type']] # set column order

    # print(web_df, flush=True)

    # encode the filtered dataset (returns 4 features)
    # X, y = encodeData(web_df)
    X, _ = encodeData(web_df[['Poisonous or Edible','Bruises', 'Odor', 'stalk_shape', 'ring_type']])

    # load the model from Resources
    filename = 'Resources/fit_model.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))

    # make predictions for test data
    result = loaded_model.predict(X)
    predictions = result[0]

    display = {} 
    # evaluate predictions
    if (predictions == 0):
        display["result"] = "poison"  # add % of prediction
    else:
         display["result"] = "edible"
    
    # print(f"Prediction from runML(): {display}", flush=True)

    return display
