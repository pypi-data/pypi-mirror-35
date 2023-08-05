import csv
import os
from os import makedirs, path as op
import json

def color_tones(tone_float):
    return 'negative' if tone_float < 0 else 'positive'

def process_files():
    fdir = '/tmp/'
    csvs = ['{0}{1}'.format(fdir, f) for f in os.listdir(fdir) if f.endswith('.export.csv')]
    reader = csv.DictReader(open('v2_events_schema.csv', 'r'))
    column_names = []
    for line in reader:
      column_names.append(line['tableId'])
    files = []
    for csv_file in csvs:
      with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        events = []
        for line in reader:
          eventDict = dict(zip(column_names, line))
          selectedColumns = ['NumMentions', 'ActionGeo_Lat', 'ActionGeo_Long', 'AvgTone', 'SOURCEURL']
          filteredEventDict = { key: eventDict[key] for key in selectedColumns }
          if not any(elem is '' for elem in filteredEventDict.values()):
            event = {
              'NumMentions': int(filteredEventDict['NumMentions']),
              'latitude': float(filteredEventDict['ActionGeo_Lat']),
              'longitude': float(filteredEventDict['ActionGeo_Long']),
              'AvgTone': float(filteredEventDict['AvgTone']),
              'SOURCEURL': filteredEventDict['SOURCEURL']
            }
            event['fillKey'] = color_tones(event['AvgTone'])
            events.append(event)
        filename = csv_file.replace('.export.csv', '.tone_location.json')
        with open(filename, 'w') as outfile:
          json.dump(events, outfile)
          #outfile.close()
        files.append(filename)
    return files
