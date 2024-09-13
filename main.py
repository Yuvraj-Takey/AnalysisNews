

from components.processDataIngestion import dataIngestion
from components.processEdit import ProcessEditCode
from components.logger import logging
from components.dataFiltration import filterData

import os
import traceback


# Method to handle preprocessing module
def inputPreprocessUnit(filepath):

    try:

        logging.debug("Initiated Preprocessing Module")

        # Data Ingestion - Input: xlsx filename, output: JSON object
        loadJs = dataIngestion()
        jsonObject = loadJs(filepath)

        # Data Preprocessing - Input: JSON object, output: JSON saved file name
        eProcess = ProcessEditCode()
        jsonFileName = eProcess.transformEdits(jsonObject)

        print("Final Output : ",jsonFileName)

        # Filter the JSON file based on the requirement
        filterObj= filterData()
        filterObj.getFilteredInputFile(jsonFileName)

    except Exception as excep:

        # get the exception
        getExcep = traceback.format_exc()   # traceback.print_exc()

        # message
        errData = "There seems to be a issue in Preprocessing - "+str(getExcep)

        # Log the Exception
        logging.error(errData)


# Starter Method
if __name__ == "__main__":

    filepath = os.path.join(os.getcwd(),"artifacts","input","24B121111110.xlsx")

    # Get the input parameter from CMD line
    # filepath = sys.argv[1]

    # input validation
    if(os.path.isfile(filepath)):

        print(filepath)

        # Method call
        inputPreprocessUnit(filepath)