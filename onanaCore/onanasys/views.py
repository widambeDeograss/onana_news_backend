from rest_framework.response import Response
from .models import *
from .Serializers import *
from rest_framework.views import APIView


class NewsAgentsView(APIView):

    @staticmethod
    def post(request):
        data = request.data
        serialized = NewsAgentsPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        querytype = request.GET.get("querytype")
        if querytype == "all":
            queryset = NewsAgents.objects.all()
            serialized = NewsAgentsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif querytype == "single":
            name = request.GET.get("name")
            queryset = NewsAgents.objects.filter(name=name)
            serialized = NewsAgentsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})

    # {
    #     "name": "Millard Ayo",
    #     "profile": "pic"
    # }


class NewsArticlesView(APIView):

    @staticmethod
    def post(request):
        data = request.data
        serialized = NewsArticlesPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        querytype = request.GET.get("querytype")
        if querytype == "all":
            queryset = NewsArticles.objects.all()
            serialized = NewsAgentsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif querytype == "provider":
            name = request.GET.get("name")
            queryset = NewsArticles.objects.filter(provider=name)
            serialized = NewsAgentsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif querytype == "single":
            id = request.GET.get("id")
            article = NewsArticles.objects.get(id=id)
            serialized = NewsAgentsGetSerializer(instance=article, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})



class NewsAgentsView(APIView):

    @staticmethod
    def post(request):
        data = request.data
        serialized = NewsAgentsPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        querytype = request.GET.get("querytype")
        if querytype == "all":
            queryset = NewsAgents.objects.all()
            serialized = NewsAgentsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif querytype == "single":
            name = request.GET.get("name")
            queryset = NewsAgents.objects.filter(name=name)
            serialized = NewsAgentsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})

    # {
    #     "name": "Millard Ayo",
    #     "profile": "pic"
    # }


class ArticleCommentsView(APIView):

    @staticmethod
    def post(request):
        data = request.data
        serialized = ArticleCommentsPostSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False, "error": serialized.errors})

    @staticmethod
    def get(request):
        querytype = request.GET.get("querytype")
        if querytype == "all":
            queryset = ArticleComments.objects.all()
            serialized = NewsAgentsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        elif querytype == "single":
            article = request.GET.get("article_id")
            queryset = ArticleComments.objects.filter(article=article)
            serialized = ArticleCommentsGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response({"message": "Specify the querying type"})

    # {
    #     "name": "Millard Ayo",
    #     "profile": "pic"
    # }