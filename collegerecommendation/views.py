# controller
from django.shortcuts import render

from knn import RecommendationUsingKNN


def index(request):
    # return template when user open the following url
    # [Template] : index.html
    # [URL] : /index
    return render(request, 'index.html', {})


def recommendation(request):
    # return template when user open the following url
    # [Template] : recommendation.html
    # [URL] : /recommendation

    # extracting fee data from url query param
    fee = int(request.GET.get('fee'))
    # extracting percentage data from url query param
    percentage = float(request.GET.get('percentage'))
    # extracting attendance data from url query param
    attendance = float(request.GET.get('attendance'))
    '''
        RecommendationUsingKNN
            params:
                [fee] : coellge fee
                [percentage] : average percentage
                [attendance] : average attendance     
    '''
    colleges = RecommendationUsingKNN(
        fee=fee, percentage=percentage, attendance=attendance)
    # render django template with recommended college list, user entered fee, user entered percentage and user entered attendance
    return render(request, 'recommendation.html', {"colleges": colleges, "fee": fee,
                                                   "percentage": percentage, "attendance": attendance})
