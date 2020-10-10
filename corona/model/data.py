import json
import pandas as pd
import numpy as np


class ChartData:
    def __init__(self, data_response, data_description, plot_style, country, total):
        self.data_response = data_response
        self.name = data_description
        self.plot_style = plot_style
        self.country = country.title()
        self.data_frame = None

        self._initialize(total)

    def _initialize(self, total):
        json_data = json.loads(self.data_response)
        self.data_frame = pd.DataFrame(json_data)

        if not total:
            self.data_frame['Cases'] = self.data_frame['Cases'].diff()



