from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Tst
from .serializers import TstSerializer
from django.db.models import F
import calendar
from rest_framework.exceptions import APIException

class TstViewSet(viewsets.ModelViewSet):
    queryset = Tst.objects.all()
    serializer_class = TstSerializer

    @action(detail=False, url_path='year/(?P<year>[0-9]{4})')
    def year(self, request, year=None):
        try:
            gazette = self.queryset.filter(month__year=year)
            serializer = self.get_serializer(gazette, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise APIException(str(e))

    @action(detail=False, url_path='year')
    def list_years(self, request):
        try:
            years = Tst.objects.annotate(year=F('month__year')).values('year').distinct()
            year_list = [{'year': y['year'], 'url': request.build_absolute_uri(str(y['year']) + '/')} for y in years]
            return Response(year_list)
        except Exception as e:
            raise APIException(str(e))

    @action(detail=False, url_path='year/(?P<year>[0-9]{4})/month')
    def list_months(self, request, year=None):
        try:
            months = Tst.objects.filter(month__year=year).annotate(month_number=F('month__month')).values('month_number').distinct()
            month_list = [{'month': calendar.month_name[m['month_number']], 'url': request.build_absolute_uri(calendar.month_name[m['month_number']] + '/')} for m in months]
            return Response(month_list)
        except Exception as e:
            raise APIException(str(e))
    
    @action(detail=False, url_path='year/(?P<year>[0-9]{4})/month/(?P<month>[A-Za-z]+|[0-9]{1,2})')
    def month(self, request, year=None, month=None):
        try:
            if month.isalpha():
                month_number = list(calendar.month_name).index(month.capitalize())
            else:
                month_number = int(month)
            gazette = self.queryset.filter(month__year=year, month__month=month_number)
            serializer = self.get_serializer(gazette, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise APIException(str(e))
        
    @action(detail=False, url_path='editor')
    def editor(self, request):
        try:
            editors = self.queryset.values('editor', 'month')
            return Response(editors)
        except Exception as e:
            raise APIException(str(e))

def api_home(request):
    return render(request, 'api.html')
