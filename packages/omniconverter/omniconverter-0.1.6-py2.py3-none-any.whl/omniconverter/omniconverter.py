from .convert.read_tdp import read_tdp
from .convert.read_stata import read_stata
from .convert.write_stats import write_stats
from .convert.write_tdp import write_tdp
from .convert.write_stata import write_stata

class Converter:

    def __init__(self):
        self.dataset = None
        self.metadata = None

    def array_to_string(self, array):
        temp = []
        for i in array:
            temp.append(str(i))
        return "".join(temp)

    def string_to_array(self, string):
        return list(string)
        
    def read_tdp(self, csv_name, json_name):
        '''
        Function to read data in tabular data package format.
        
        Parameter:
        
        csv_name: Name of the row data in tabular format
        json_name: Name of the metadata in json format
        
        Example:
        
        dataset.read_tdp("../input/dataset.csv", "../input/dataset.json")
        '''
        self.dataset, self.metadata = read_tdp(csv_name, json_name)
        
    def read_stata(self, dta_name):
        '''
        Function to read data in stata format.
        
        Parameter:
        
        dta_name: Name of the data in stata format
        
        Example:
        
        dataset.read_stata("../input/dataset.dta")        
        '''
        self.dataset, self.metadata = read_stata(dta_name)
    
    def write_stats(self, output_name, file_type="json", split="", weight="", analysis_unit="", period="", sub_type="", study="", metadata_de="", log=""):
        '''
        Function to write statistics from data in json/html format.
        
        Parameter:
        
        output_name: Name of the output file
        file_type: Statistics are read out in json or html; Standard is "json"
        split: Name of the variable(s) for bivariate statistics; Standard is ""
        weight: Name of the weight variable; Standard is ""
        
        Example:
        
        dataset.write_stats("../output/dataset.html", file_type="html", split="split", weight="weight") 
        ''' 
        write_stats(self.dataset, self.metadata, output_name, file_type=file_type, split=split, weight=weight, analysis_unit=analysis_unit, period=period, sub_type=sub_type, study=study, metadata_de=metadata_de, log=log)
        
    def write_tdp(self, output_csv, output_json):
        '''
        Function to write data in tdp format.
        
        Parameter:
        
        output_csv: Name of the row data in tabular format
        output_json: Name of the metadata in json format
        
        Example:
        
        dataset.write_tdp("../output/dataset.csv", "../output/dataset.json") 
        '''
        write_tdp(self.dataset, self.metadata, output_csv, output_json)
        
    def write_stata(self, output_name):
        '''
        Function to write data in stata format.
        
        Parameter:
        
        output_name: Name of the data in stata format
        
        Example:
        
        dataset.write_stata("../output/dataset.dta") 
        '''
        write_stata(self.dataset, self.metadata, output_name)
