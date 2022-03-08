import namegenerator
import json
import random

from reocmmendationModel import CollegeModel, Datum


def data_generator():
    colleges = []
    for _ in range(5000):
        college_type = ["Engineering", "Science and technology",
                        "Business management", "Applied science", "Mechanics"]
        name: str = namegenerator.gen() + " college of " + \
            college_type[random.randint(0, (len(college_type)-1))]
        percentage: int = random.randint(45, 85)
        fee: int = random.randint(500000, 2000000)
        attendance: int = random.randint(20, 100)
        distance: float = 0
        college: Datum = Datum(distance=distance, college_name=name,
                               average_percentage=percentage, fee=fee, attendance=attendance)
        colleges.append(college)
        model: CollegeModel = CollegeModel(data=colleges)
        data = model.to_dict()
        _json = json.dumps(data)
        with open("college-data.json", "w", newline='', encoding="utf-8",) as file:
            file.write(_json)


if __name__ == "__main__":
    data_generator()
