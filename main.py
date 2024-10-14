import os
import sys
from Sensor.exception import SensorException


from sensor.utils import dump_csv_file_to_mongodb_collection


from Sensor.logger import logging

# def test_exception ():
#     try:
#         logging.info("Error will occured (1/0 division error)")         #don't write info (in capital letter)
#         a=1/0
#     except Exception as e:
#         #raise SensorException(e,sys)
#         raise e
    

# class SensorException(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)

#     def __str__(self):
#         return f"SensorException: {self.message}"



if __name__== "__main__":
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)
    
    
    file_path = "F:\SFD ML Project\aps_failure_training_set1.csv"
    database_name =" msde"
    collection_name ="sensor"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)


    def dump_csv_file_to_mongodb_collection(csv_file_path, collection_name):
    # Your code to dump CSV file data to MongoDB collection
        pass


