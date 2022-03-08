"""
    Used for json data serialize and deserialize

    [serialize]: converting python object to json

    [deserialize]: converting json to python object

"""
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


# for checking if the data is valid string
def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


# for checking if the data is valid integer
def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x

# checking if the data is valid list


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]

# checking if the data is valid dictionary


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


"""
    Python class that holds College information
    [college_name] : attribute for setting college name
    [average_percentage] : attribute for setting college students average percentage
    [fee] : attribute for setting college fee
    [distance] : attribute for setting euclidian distance that will be calculated later.
    A default distance 0 is passed when creating the object
"""


class Datum:
    college_name: str
    average_percentage: int
    fee: int
    attendance: int
    distance: float

    def __init__(self, college_name: str, average_percentage: int, fee: int, attendance: int, distance: float) -> None:
        self.college_name = college_name
        self.average_percentage = average_percentage
        self.fee = fee
        self.attendance = attendance
        self.distance = distance

    """
    static method for converting dictionary data to Datum type object
    """
    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        college_name = from_str(obj.get("college-name"))
        average_percentage = from_int(obj.get("average-percentage"))
        fee = from_int(obj.get("fee"))
        attendance = from_int(obj.get("attendance"))
        distance = float(0)
        return Datum(college_name, average_percentage, fee, attendance, distance)

    """
        method for converting Datum object into dictionary data type
    """

    def to_dict(self) -> dict:
        result: dict = {}
        result["college-name"] = from_str(self.college_name)
        result["average-percentage"] = from_int(self.average_percentage)
        result["fee"] = from_int(self.fee)
        result["attendance"] = from_int(self.attendance)
        result['distance'] = float(self.distance)
        return result


"""
    It takes list of Datum as params
    [data]: attribute that sets list of Datum

"""


class CollegeModel:
    data: List[Datum]

    def __init__(self, data: List[Datum]) -> None:
        self.data = data

    """
        static method for converting dictionary data to collegeModel(data: List<Datum>)
    """
    @staticmethod
    def from_dict(obj: Any) -> 'CollegeModel':
        assert isinstance(obj, dict)
        data = from_list(Datum.from_dict, obj.get("data"))
        return CollegeModel(data)

    """
        method for converting CollegeModel object into dictionary type
    """

    def to_dict(self) -> dict:
        result: dict = {}
        result["data"] = from_list(lambda x: to_class(Datum, x), self.data)
        return result


"""
    function for converting dictionary data to collegeModel(data: List<Datum>)
"""


def college_model_from_dict(s: Any) -> CollegeModel:
    return CollegeModel.from_dict(s)


"""
    function for converting CollegeModel object into dictionary type
"""


def college_model_to_dict(x: CollegeModel) -> Any:
    return to_class(CollegeModel, x)
