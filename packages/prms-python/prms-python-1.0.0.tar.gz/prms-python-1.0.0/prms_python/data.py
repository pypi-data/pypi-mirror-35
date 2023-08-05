'''
data.py -- holds ``Data`` class for standard PRMS climate input data.
'''

import pandas as pd
from shutil import copyfile

class Data(object):
    """
    Object to access or create a PRMS data file with ability to load/assign it to a 
    date-time indexed pandas.DataFrame for data management, analysis and visualization. 
    It can be used to build a new PRMS data file from user defined metadata and  
    pandas.DataFrame. The ``modify`` method allows for inplace modification of 
    one or more time series inputs in the data file based on a user defined function. 
    The ``write`` method reformats the Dataframe to PRMS text format and writes 
    a new data file to disk. If the initial data was not accessed the write method 
    simply makes a copy of the original file, to save memory and improve computational
    efficiency. Here is an example of loading a data file, modifying the temperature 
    inputs ('tmin' and 'tmax') by adding two degrees to each element, and rewritting 
    the modified data to disk: 

    >>> d = Data('path_to_data_file')
    >>> def f(x):
            return x + 2
    >>> d.modify(f,['tmax','tmin'])
    >>> d.write('example_modified_data_file')

    d is a Data instance of example_data_file, calling 

    >>> d.data_frame 

    shows the datetime indexed pd.DataFrame of the input data that is created 
    when a ``Data`` object is initiated. We then pass the function f(x) to d.modify 
    along with a Python list of input variable/s that we want to modify, this 
    modifies d.data_frame in place. Printing the metadata attribute of the data
    object,

    >>> d.metadata

    will show the names of the variables in the data file in case you forget which
    you would like to modify. Last we call d.write with an output path to write 
    the modified data variables to disk in PRMS text format. 
    """

    ## data file constant attributes
    date_header = ['year',
               'month',
               'day',
               'hh',
               'mm',
               'sec']

    valid_input_variables = ('gate_ht',
                         'humidity',
                         'lake_elev',
                         'pan_evap',
                         'precip',
                         'rain_day',
                         'runoff',
                         'snowdepth',
                         'solrad',
                         'tmax',
                         'tmin',
                         'wind_speed')


    def __init__(self, base_file=None, na_rep=-999):

        self.base_file = base_file
        self.na_rep = na_rep
        self._metadata = None #self.__load_metadata()
        self._data_frame = None #self.__load_data()

    @property
    def metadata(self):
        # to avoid overwriting pre-assigned data
        if isinstance(self._metadata, dict):
            return self._metadata
        elif not self.base_file:
            raise ValueError('No data file was given on initialization')
            
        ## starting list for variable names in data file
        input_data_names = []
        text_before_header = str()
        ## open data file and read header information
        with open(self.base_file, 'r') as inf:
            for idx,l in enumerate(inf):
                text_before_header+=l
                if idx == 0: ## first line always string identifier of the file- may use later
                    data_head = l.rstrip()
                elif l.startswith('/'): ## comment lines
                    continue
                if l.startswith(Data.valid_input_variables): 
                    h = l.split() ## split, first name and second number of columns
                    if int(h[1]) > 1: ## more than one input time series of a particular variable
                        for el in range(int(h[1])):
                            tmp = '{var_name} {var_ind}'.format(var_name = h[0], var_ind = el+1)
                            input_data_names.append(tmp)
                    elif int(h[1]) == 1:
                        input_data_names.append(h[0])
                if l.startswith('#'): ## end of header info and begin time series input data
                    data_startline = idx+1 ## 0 indexed line of first data entry
                    break
                    
        self._metadata = dict([('data_startline',data_startline),
                               ('data_variables',input_data_names),
                               ('text_before_header',text_before_header)])
        return self._metadata
    
    @metadata.setter
    def metadata(self, dic):
        if not isinstance(dic, dict):
            raise TypeError('Must assign a Python dictionary for new Data object/file metadata')
        self._metadata = dic
    
    @property
    def data_frame(self):
        if not self._metadata:
            self.metadata
        elif not isinstance(self._data_frame, pd.DataFrame) and self.base_file == None:
            raise ValueError('No data base_file given on initialization, '\
                             'therefore you must assign a DataFrame'\
                              +' before accessing the .data_frame attribute!')
        # to avoid overwriting pre-assigned data
        elif isinstance(self._data_frame, pd.DataFrame):
            return self._data_frame
        
        df = pd.read_csv(self.base_file, header = -1, skiprows = self.metadata['data_startline'],
                         delim_whitespace = True, na_values = [self.na_rep]) ## read data file
        df.columns = Data.date_header + self.metadata['data_variables']
        date = pd.Series(pd.to_datetime(df.year * 10000 + df.month * 100 +\
             df.day, format = '%Y%m%d'), index = df.index)
        df.index = pd.to_datetime(date) ## assign datetime index
        df.drop(Data.date_header, axis = 1, inplace = True) ## unneeded columns
        df.columns.name = 'input variables' ; df.index.name = 'date'
        self._data_frame = df
        return self._data_frame
    
    @data_frame.setter
    def data_frame(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Must assign a Pandas.DataFrame object for PRMS data input")
        self._data_frame = df
        
    def modify(self, func, vars_to_adjust):
        """
        Apply a user defined function to one or more variable(s) in the data file.

        Arguments:
            func (function): function to apply to each variable in vars_to_adjust
            vars_to_adjust (list or tuple): collection of variable names to apply
                func to.
        Returns: 
            None: 
            
        Example starting with an initial PRMS data file and modifying a single 
        data variable by applying the sine function: 
               >>> data_instance = Data('path/to/data/file')  
               >>> def f(x):
               ...     return np.sin(x)
               >>> data_instance.modify(f, ['param_name_to_adjust'])
        """

        if not isinstance(self._data_frame, pd.DataFrame):
            self.data_frame
        for v in vars_to_adjust:
            self._data_frame[v] = self._data_frame[v].apply(func)

    def write(self, out_path):
        """
        Writes the current state of the data to PRMS text format,
        particularly useful after modifying the data variable values
        or creating a new dataset from a pd.DataFrame

        Arguments:
            out_path (str): full path to save or copy the current PRMS data 
                in PRMS text format.
        Returns:
            None
        """
        # if file data was never accessed- unchanged
        if not isinstance(self._data_frame, pd.DataFrame): 
            if self.base_file:
                copyfile(self.base_file, out_path)
            else: # if data not from original file and dataframe never assigned
                raise ValueError('No data base_file was given and'\
                                +' no data was assigned!')
                
        ## reconstruct PRMS data file format, don't overwrite date-indexed
        else:
            df = self._data_frame[self.metadata['data_variables']]
            df['year'] = self._data_frame.index.year
            df['month'] = self._data_frame.index.month
            df['day'] = self._data_frame.index.day
            df['hh'] = df['mm'] = df['sec'] = 0
            df = df[Data.date_header + self._metadata['data_variables']]
            with open(out_path,'w') as outf: # write comment header then data
                outf.write(self._metadata['text_before_header'])
                df.to_csv(outf, sep=' ', header=None,\
                          index=False, na_rep=self.na_rep)

