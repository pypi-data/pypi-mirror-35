"""
 * $Id:$
 *
 * This file is part of the Cloud Services Integration Platform (CSIP),
 * a Model-as-a-Service framework, API and application suite.
 *
 * 2012-2018, Olaf David and others, OMSLab, Colorado State University.
 *
 * OMSLab licenses this file to you under the MIT license.
 * See the LICENSE file in the project root for more information.
"""
import requests
import json
import os
import re

from typing import List, Dict

class Client(object):
    """
    CSIP client class.
    
    :copyright: (c) 2018 by Olaf David.
    :license: MIT, see LICENSE for more details.
    """

    PARAMETER = "parameter"
    RESULT    = "result"
    METAINFO  = "metainfo"

    KEY_NAME  = "name"
    KEY_VALUE = "value"
    KEY_UNIT  = "unit"
    KEY_DESCR = "descr"
    
    META_KEY_SUID = "suid"
    META_KEY_STATUS = "status"
    META_KEY_ERROR = "error"
    META_KEY_STACKTRACE = "stacktrace"
    META_KEY_MODE = "mode"
    META_KEY_SERVICE_URL = "service_url"
    META_VAL_SYNC = "sync"
    META_VAL_ASYNC = "async"

    REQ_PARAM = "param"
    REQ_FILE  = "file"
    REQ_JSON  = "request.json"
    
    STATUS_FINISHED = "Finished"
    STATUS_SUBMITTED = "Submitted"
    STATUS_FAILED = "Failed"
    STATUS_RUNNING = "Running"
    
    def __init__(self, data: Dict = {}, parent: 'CSIP' = None, metainfo: Dict = {}):
        # parameter data or result data
        self.data = Client.__create_dict(data) if data else {} 
        # metainfo 
        self.metainfo = metainfo
        # the parent CSIP payload (request)
        self.parent = parent
        
    @staticmethod
    def load_json(file:str) -> Dict:
        """load a json file as dict"""
        with open(file) as f:
            data = json.load(f)
        return data

    @staticmethod    
    def __create_dict(json: List[Dict]) -> Dict:
        """ create dict key:name, value: whole json"""
        return { i[Client.KEY_NAME]: i for i in json }

    @staticmethod    
    def __remove(d: Dict, names: List[str]):
        """ removes entries from a dict"""
        if names is None:
            d.clear()
            return
        """ Remove entries by name"""
        for i in names:
            if i in d:
                del d[i]
                
    def query(self) -> 'Client': 
        """ Queries the service for completion status. Client post must be in async mode"""
        if not self.is_async():
            raise Exception("not async.")
        service = self.get_serviceurl()
        if service is None:
            raise Exception("no service_url.")
        a = re.search("/[md]/", service)
        if a is None:
            raise Exception("not a model/data service_url.")
        
        suid = self.get_suid()
        if suid is None:
            raise Exception("no suid.")
        query_url = service[:a.start()] + "/q/" + suid
        #print(query_url)
        return Client.__get(query_url, section=self.RESULT)

    def post(self, url: str, sync:bool = True, files:List[str]=[]) -> 'Client':
        """Sends an POST request.
        :param url: URL for the new :class:`Client` object.
        :return: the response object
        :rtype: :class:'Client'
        """
        self.metainfo[self.META_KEY_MODE] = self.META_VAL_SYNC if sync else self.META_VAL_ASYNC
        request_json = { self.METAINFO : self.metainfo, self.PARAMETER : list(self.data.values()) }
        
        multipart = { self.REQ_PARAM :  (self.REQ_JSON, str(request_json)) }
        for i, file in enumerate(files, start=1):
            multipart[self.REQ_FILE + str(i)] = open(file, 'rb')
            
        #print(multipart)
        response = requests.post(url, files=multipart, allow_redirects=True)
        if response.status_code != requests.codes.ok: 
            response.raise_for_status() 
        
        response_json = response.json()
        
        #print(response_json)
        # async handling
        data = {} if not self.RESULT in response_json else response_json[self.RESULT]
        return Client(data, parent=self, metainfo=response_json[self.METAINFO])
    
    @staticmethod    
    def get(url: str) -> "Client":
        return Client.__get(url)
        
    @staticmethod    
    def __get(url: str, section: str = PARAMETER) -> "Client":
        """Sends an GET request.
        :param url: URL to fetch the params from.
        :return: None
        :rtype: None
        """
        response = requests.get(url, allow_redirects=True)
        if response.status_code != requests.codes.ok: 
            response.raise_for_status() 
        response_json = response.json()
        
        # print(json_response)
        # check if suid error happens
        # This handles  /q/<suid> 
        data = {} if not section in response_json else response_json[section]
        return Client(data, metainfo=response_json[Client.METAINFO])
        
    def add_all_metainfo(self, csip: "Client") -> None:
        """ Add all entries from the other Client"""
        self.metainfo = csip.metainfo.copy()
    
    def remove_data(self, names: List[str] = None):
        """ Remove data entries by names, or all if name is None"""
        Client.__remove(self.data, names)

    def remove_metainfo(self, names: List[str] = None):
        """ Remove metainfo entries by names, or all if name is None"""
        Client.__remove(self.metainfo, names)
    
    def get_data_names(self) -> List[str]:
        """ Get all the entry names"""
        return list(self.data.keys())
    
    def add_metadata(self, name, key: str, value: str) -> None:
        """ Add a metainfo entry"""
        self.data[name] = { **self.data[name] , key : value }
        
    def add_data(self, name, value=None, descr: str = None, unit: str = None) -> None:
        """ Add a new entry to the data"""
        if isinstance(name, Dict):
            # name is the the json data object 
            self.data[name[Client.KEY_NAME]] = name 
            return 
        if isinstance(name, Client):
            # name is the CSIP data object 
            self.data = {**self.data, **name.data}
            return
        if value is None:
            raise Exception("missing value.")
        self.data[name] = { self.KEY_NAME: name , self.KEY_VALUE: value }
        if unit is not None:
            self.data[name][self.KEY_UNIT] = unit
        if descr is not None:
            self.data[name][self.KEY_DESCR] = descr
            
    def has_data(self, name:str) -> bool:
        """ Check if data entry exists """
        return name in self.data
    
    def get_data(self, name:str) -> Dict:
        """ Get the whole entry as dict"""
        return self.data[name]

    def get_data_value(self, name: str) -> object:
        """ Get the entry value """
        return self.data[name][self.KEY_VALUE]

    def get_data_description(self, name: str):
        """ Get the entry description"""
        return self.data[name][self.KEY_VALUE]
    
    def get_data_unit(self, name: str):
        """ Get the entry description"""
        return self.data[name][self.KEY_VALUE]

    def get_parent(self) -> "Client":
        """ Get the parent data set, which is the request """
        return self.parent
    
    def metainfo_tostr(self, indent=2) -> str:
        """ Print the metainfo  """
        return json.dumps(self.metainfo, indent=indent)

    def data_tostr(self, indent=2) -> str:
        """ Print the entries as json"""
        return(json.dumps(list(self.data.values()), indent=indent))
    
    def get_data_files(self) -> List[str]:
        """ Get a list of data entries that are file urls to download"""
        suid = self.get_suid()
        if suid is None:
            raise Exception("Not a response, nothing to download.")
        
        files=[]
        for name in self.data:
            val = self.get_data_value(name)
            if isinstance(val, str) and ("/q/" + suid + "/") in val and val.endswith(name):
                files.append(name)
        return files

    
    def download_data_files(self, files:List[str] = None, dir:str = ".") -> None:
        """ Downloads file(s) if this Client object is a valid response and a query url as value.
            If no 'file' argument is provided, all files will be dowloaded.
            If no 'dir' is provided, the current directory will be used.
        """
        if files is None or not files:
            return

        dir = os.path.abspath(dir)
        if not (os.path.isdir(dir) and os.path.exists(dir)) :
            raise Exception("Not a folder or does not exist: " + dir)

        suid = self.get_suid()
        if suid is None:
            raise Exception("No suid.")
                
        print("downloading to '" + dir + "':") 
        for name in files:
            if name not in self.data:
                raise Exception("Not in data: " + name)
            val = self.get_data_value(name)
            print("  --> " + name) 
            r = requests.get(val, allow_redirects=True)
            open(dir + "/" + name, "wb").write(r.content)


    def set_metainfo(self, name: str, value:str) -> None:
        """ Set a metainfo entry"""
        self.metainfo[name] = value

    def get_metainfo(self, name: str):
        """ Get a metainfo entry"""
        return self.metainfo[str]
    
    def has_metainfo(self, name: str) -> bool:
        """ Check if metainfo has an extry with 'name'"""
        return name in self.metainfo

    def get_status(self) -> str :
        """ Get the status from metainfo, returns None is there is none """
        return None if not self.META_KEY_STATUS in self.metainfo else self.metainfo[self.META_KEY_STATUS]

    def get_suid(self) -> str :
        """ Get the simulation id (suid) from metainfo, returns None is there is none """
        return None if not self.META_KEY_SUID in self.metainfo else self.metainfo[self.META_KEY_SUID]

    def get_serviceurl(self) -> str :
        """ Get the service url from metainfo, returns None is there is none """
        return None if not self.META_KEY_SERVICE_URL in self.metainfo else self.metainfo[self.META_KEY_SERVICE_URL]

    def get_error(self) -> str :
        """ Get the error message from metainfo, returns None is there is none """
        return None if not self.META_KEY_ERROR in self.metainfo else self.metainfo[self.META_KEY_ERROR]
    
    def get_stacktrace(self) -> List[str] :
        """ Get the error stacktrace from metainfo, returns None is there is none """
        return None if not self.META_KEY_STACKTRACE in self.metainfo else self.metainfo[self.META_KEY_STACKTRACE]

    def get_mode(self) -> str :
        """ Get the execution mode from metainfo, returns 'sync' or 'async' , default is sync"""
        return self.META_VAL_SYNC if not self.META_KEY_MODE in self.metainfo else self.metainfo[self.META_KEY_MODE]

    def is_async(self) -> bool :
        """ check if execution mode is async """
        return self.META_KEY_MODE in self.metainfo and self.metainfo[self.META_KEY_MODE] == self.META_VAL_ASYNC
    
    
