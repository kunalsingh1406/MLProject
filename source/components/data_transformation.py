import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from source.exception import CustomException
from source.logger import logging
import os

from source.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path : str = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__ (self):
        self.Data_Transformation_Config = DataTransformationConfig()

    def get_data_tranformer_obj(self):
        try:
            numerical_columns = ['reading_score', 'writing_score']
            categorical_columns = [
                'gender', 
                'race_ethnicity', 
                'parental_level_of_education', 
                'lunch', 
                'test_preparation_course'
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehotencoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            logging.info("Numerical column standard scaling completed")
            logging.info("Categorical column encoding completed")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipline, categorical_columns)
                ]
            )

            return preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading train and test data completed")
            logging.info("obtaining processing object")

            preprocessing_obj = self.get_data_tranformer_obj()

            target_column_name = "math_score"

            input_train_features_df = train_df.drop(columns=[target_column_name], axis=1)
            target_train_feature_df = train_df[target_column_name]

            input_test_features_df = test_df.drop(columns=[target_column_name], axis=1)
            target_test_features_df = test_df[target_column_name]

            logging.info("Applying preprocessing obj on training dataframe and testing dataframe")

            input_train_features_arr =  preprocessing_obj.fit_transform(input_train_features_df)
            input_test_features_arr =  preprocessing_obj.transform(input_test_features_df)

            train_arr = np.c_[
                input_train_features_arr, np.array(target_train_feature_df)
            ]
            test_arr = np.c_[
                input_test_features_arr, np.array(target_test_features_df)
            ]

            logging.info("saved preprocessing object")

            save_object(
                file_path =self.Data_Transformation_Config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                #self.Data_Transformation_Config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e, sys)
              

            

 