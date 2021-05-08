import pandas as pd
import csv
from flask import Flask, request, jsonify
from data import data

app = Flask('__name__')

# df = pd.read_csv('filtering_stars.csv')
# df.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1, inplace = True)
# print(df.head(10))
# print(df.shape)

# name = df['name'].tolist()
# distance = df['distance'].tolist()
# mass = df['mass'].tolist()
# radius = df['radius'].tolist()
# gravity = df['gravity'].tolist()

# final_star_list = []
# temp_dict = {}

# for i in range(0,len(name)):
#     temp_dict['name'] = name[i]
#     temp_dict['distance'] = distance[i]
#     temp_dict['mass'] = mass[i]
#     temp_dict['radius'] = radius[i]
#     temp_dict['gravity'] = gravity[i]
#     final_star_list.append(temp_dict)
#     temp_dict = {}

# print(final_star_list)

@app.route('/')
def index():
    return jsonify({
        'data' : data,
        'message' : 'success'
    }), 200

@app.route('/get-data')
def get_data():
    name = request.args.get('name')
    star_data = next(item for item in data if item['name'] == name)
    return jsonify({
        'data' : star_data,
        'message' : 'success'
    }), 200

if __name__ == '__main__':
    app.run()