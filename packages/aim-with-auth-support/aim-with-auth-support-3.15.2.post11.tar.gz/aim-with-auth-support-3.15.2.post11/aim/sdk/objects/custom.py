import logging
import os
import json
from base64 import b64encode
from typing import TYPE_CHECKING, Union, List, Dict
from copy import deepcopy
from dataclasses import dataclass

import requests
from pandas import DataFrame

if TYPE_CHECKING:
    from aim.sdk import Run

logger = logging.getLogger(__name__)

@dataclass
class CustomElement:

    def upload_artifact(cls, run: 'Run', artifact_path: str):
        artifact_path = os.path.expanduser(os.path.expandvars(artifact_path))
        files = {'file': open(artifact_path,'rb')}
        auth_info = None
        if os.getenv('AIM_ACCESS_TOKEN'):
            auth_info = 'Bearer {}'.format(os.getenv('AIM_ACCESS_TOKEN'))
        elif os.getenv('AIM_ACCESS_USERNAME') and os.getenv('AIM_ACCESS_PASSWORD'):
            auth_info = 'Basic {}'.format(
                    b64encode('{}:{}'.format(os.getenv('AIM_ACCESS_USERNAME'), os.getenv('AIM_ACCESS_PASSWORD')).encode('utf-8')
                    ).decode('utf-8'))
        elif os.getenv('AIM_ACCESS_CREDENTIAL'):
            auth_info = os.getenv('AIM_ACCESS_CREDENTIAL')
        endpoint = 'http://localhost:1024' if run.repo.root_path.startswith('/') else f'https://{run.repo.root_path.split(":")[0]}'
        r = requests.post(f'{endpoint}/artifacts/upload/{run.experiment}/{run.hash}', files=files, headers={'Authorization': auth_info})
        return r.json()['path']

@dataclass
class Molecule(CustomElement):
    
    # molecule type: 'pdb', 'pqr', 'mmcif', 'mcif', 'cif', 'sdf', 'sd', 'gro', 'mol2', 'mmtf'
    # ref: https://wandb.ai/site/articles/visualizing-molecular-structure-with-weights-biases
    file_path: str
    trajectory_path: str = None

    def to_dict(self, run):
        dt = {
            '_type': 'molecule-file',
            'path': self.upload_artifact(run, self.file_path),
        }
        if self.trajectory_path:
            dt['trajectory_path'] = self.upload_artifact(run, self.trajectory_path)
        return dt

    def to_json(self, run):
        return json.dumps(self.to_dict(run))

    def to_text(self, run):
        return f'data:text/molecule-file,{self.to_json(run)}'

@dataclass
class TableImage(CustomElement):

    file_path: str

    def to_dict(self, run):
        return {
            '_type': 'image-file',
            'path': self.upload_artifact(run, self.file_path),
        }

@dataclass
class HTML(CustomElement):

    data: str
    
    def to_text(self, run):
        return f'data:text/html,{self.data}'

@dataclass
class Table:

    data: Union[List, Dict]
    
    def __post_init__(self):
        data = self.data
        if not data:
            raise Exception('Empty data not allowed')
        elif isinstance(data, list):
            self.data = self.convert_records_to_split(data)
        elif isinstance(data, dict):
            self.data = data
        elif isinstance(data, DataFrame):
            self.data = data.to_json(orient='split')
        else:
            raise Exception(f'unknown data type: {type(data)}')
        self.check_data_format()

    def to_dict(self, run):
        data = self.prepare_table_element(run, self.data)
        return {
            '_type': 'table-split',
            'columns': data['columns'],
            'data': data['data']
        }

    def to_json(self, run):
        return json.dumps(self.to_dict(run))

    def to_text(self, run):
        return f'data:text/table,{self.to_json(run)}'

    def convert_records_to_split(cls, data):
        split = {}
        columns = sorted(data[0].keys())
        split['columns'] = columns
        split['data'] = []
        for item in data:
            split['data'].append([item.get(i) for i in columns])
        return split
        
    def prepare_table_element(cls, run, data):
        data = deepcopy(data)
        for row in data['data']:
            for i, element in enumerate(row):
                if isinstance(element, (TableImage, Molecule)):
                    row[i] = element.to_dict(run)
        return data
    
    def check_data_format(self):
        pass