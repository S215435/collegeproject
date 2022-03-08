import json
import math
from operator import attrgetter

from reocmmendationModel import CollegeModel


def RecommendationUsingKNN(fee, attendance, percentage):
    # college model
    college_data: CollegeModel = None

    # open the json file containing college data stored in file as college-data.json
    with open("college-data.json", "r", encoding="utf-8",) as file:
        # reading the content of the file
        _json = file.readline()
        # converting json data to python dictionary
        data_dict = json.loads(_json)
        # returns a collegeModel object from python dictionary
        college_data = CollegeModel.from_dict(data_dict)

    # value of K
    k = 10

    # looping through the list of college
    for data in college_data.data:
        # distance
        euclidean_distance = math.sqrt(
            (fee-data.fee) ** 2 + (attendance-data.attendance)**2 + (percentage-data.average_percentage))
        # setting the euclidian distance for each college
        data.distance = float(euclidean_distance)
    # sorting the college based on it's attribute 'distance' that sorts the college in ascending order
    college_data.data.sort(key=attrgetter('distance'), reverse=False)
    # return the first k college from the sorted list
    return college_data.data[:k]
