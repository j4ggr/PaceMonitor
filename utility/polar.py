
from turtle import pd
from requests import Session
import datetime

class PolarFlowClient(Session):
    def __init__(self):
        super().__init__()
        self.year_now = datetime.datetime.now().year
        self.year_beg = self.year_now - 5

    @property
    def url(self): return {
        'login': 'https://flow.polar.com/login',
        'events': 'https://flow.polar.com/training/getCalendarEvents',
        'csv': 'https://flow.polar.com/api/export/training/csv/'}

    def login(self, username, password):
        data = {
            "email": username,
            "password": password,
            "returnUrl": '/'}
        return self.post('https://flow.polar.com/login', data)
    
    def get_activities(self, year):
        params = {'start': f'01.01.{year}', 'end': f'31.12.{year}'}
        return self.get(self.url['events'], params=params).json()
    
    def get_csv_export(self, activity):
        """Get CSV data as text"""
        url = self.url['csv'] + str(activity['listItemId'])
        return self.get(url).text
    
    def extract(self):
        for year in range(self.year_beg, self.year_now + 1):
            activities = self.get_activities(year)
            for activity in activities:
                if not isinstance(activity, dict):
                    continue
                csv = self.get_csv_export(activity)
                yield csv
    
    def __iter__(self):
        self._data = self.extract()
        return self._data

    def __next__(self):
        return next(self._data)


