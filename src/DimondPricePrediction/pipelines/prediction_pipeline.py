import os 
import sys
import pandas as pd
from src.DimondPricePrediction.exception import customexception
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.utils.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path= os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            scaled_data = preprocessor.transform(features)

            pred =model.predict(scaled_data)

            return pred

        except Exception as e:
            raise customexception(e,sys)
        # try:
        #     model_path = os.path.join("artifacts","model.pkl")
        #     preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
        #     model = load_object(file_path=model_path)
        #     preprocessor = load_object(file_path=preprocessor_path)
        #     data_scaled = preprocessor.transform(data)
        #     preds = model.predict(data_scaled)
        #     return pd.DataFrame(preds)
        # except Exception as e:
        #     raise customexception(e,sys)

class CustomData:
    def __init__(self,carat:float,cut:str,color:str,clarity:str,depth:float,table:float,x:float,y:float,z:float):
         self.carat = carat
         self.cut = cut
         self.color = color
         self.clarity = clarity
         self.depth = depth
         self.table = table
         self.x = x
         self.y = y
         self.z = z
               

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "carat": [self.carat],
                        "cut": [self.cut],
                        "color": [self.color],
                        "clarity": [self.clarity],
                        "depth": [self.depth],
                        "table": [self.table],
                        "x": [self.x],
                        "y": [self.y],
                        "z": [self.z],
                    }
            df=pd.DataFrame(custom_data_input_dict)
            logging.info(f"Dataframe Gathered successfully")
            return df
        except Exception as e:
            raise customexception(e, sys)