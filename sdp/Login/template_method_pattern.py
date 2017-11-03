######### Author :  Shahin #########


from .models import *
from abc import ABC, abstractmethod


class Searcher(ABC) :
    @abstractmethod
    def getData(self):
        pass

    def extractData(self,table):
        list = []
        for a in table:
            list.append(a.name)
        return list

    def search(self) :
        # returns the expected table
        table = self.getData()
        # extracts necessary informations from the table( normally the name )
        list = self.extractData(table)

        return list



class UniversitySearcher(Searcher) :
    # returns the university table
    def getData(self) :
        return University.objects.all()


class DepartmentSearcher(Searcher) :
    # returns the department table
    def getData(self) :
        return Department.objects.all()

class CollegeSearcher(Searcher) :
    # returns the department table
    def getData(self) :
        return College.objects.all()

class SchoolSearcher(Searcher) :
    # returns the department table
    def getData(self) :
        return School.objects.all()
