from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])

def apiOverview(request):

    api_urls = {
        'API Overview'                      : 'api/v1/',

        'Institution Details'               :'api/v1/institution/details/',
        'Homepage Details'                  :'api/v1/institution/homepage_details/',
        'About Us Details'                  :'api/v1/institution/about_us_details/',
        'Academic Details'                  :'api/v1/institution/academic_details/',

        'Teacher List'                      : 'api/v1/teachers/list/',
        'Teacher Details'                   : 'api/v1/teachers/details/',

        'Student Details'                   : 'api/v1/students/details/',

        'Class List'                        : 'api/v1/classes/list/',
        'Class Details'                     : 'api/v1/classes/<str:class_pk>/details/',

        'Subject List'                      : 'api/v1/classes/<str:class_pk>/subjects/list/',

        'Marksheet List Create Update'      : 'api/v1/classes/marksheets/<str:subject_pk>/<str:exam_pk>/'
    }

    return Response(api_urls)

# Create your views here.
