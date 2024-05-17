from django.shortcuts import render
# from .recommendation import recommend_mobile
from rest_framework.decorators import api_view
import pandas as pd
import csv 
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt


# @api_view(['GET','POST','DELETE'])
# def Index(request):
#     return render(request, "index.html")

def Index(request):
    csv_file_path = 'static/marvel_with_img.csv'  # Path to your CSV file
    search_query = request.GET.get('search')

    data = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    if search_query:
        data = [row for row in data if search_query.lower() in row['CharacterName'].lower()]

    return render(request, 'results.html', {'csv_data': data, 'search_query': search_query})



def display_csv_data(request):
    csv_file_path = 'static/marvel_with_img.csv'  # Update this with the actual path to your CSV file
     
    data = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    return render(request, 'results.html', {'csv_data': data})


def csv_display(request):
    csv_file_path = 'static/marvel_with_img.csv'  # Path to your CSV file
    search_query = request.GET.get('search')

    data = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    if search_query:
        data = [row for row in data if search_query.lower() in row['CharacterName'].lower()]

    return render(request, 'csv_display.html', {'csv_data': data, 'search_query': search_query})


@api_view(['GET','POST','DELETE'])
def start_area(request):
    return render(request, 'fight.html')


# def FightArena(request):
#     csv_file_path = 'static/marvel_with_img.csv'  # Path to your CSV file
#     search_query = request.GET.get('search')
#     search_query2 = request.GET.get('search2')  # For the second character

#     data = []
#     with open(csv_file_path, 'r') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             data.append(row)

#     first_character_data = data[:]  # Copy the data for the first character
#     second_character_data = data[:]  # Copy the data for the second character

#     if search_query:
#         first_character_data = [row for row in first_character_data if search_query.lower() in row['CharacterName'].lower()]

#     if search_query2:
#         second_character_data = [row for row in second_character_data if search_query2.lower() in row['CharacterName'].lower()]

#     return render(request, 'fight.html', {'first_csv_data': first_character_data, 'second_csv_data': second_character_data, 'search_query': search_query, 'search_query2': search_query2})


# def FightArena(request):
#     csv_file_path = 'static/marvel_with_img.csv'  # Path to your CSV file
#     search_query = request.GET.get('search')
#     search_query2 = request.GET.get('search2')  # For the second character

#     data = []
#     with open(csv_file_path, 'r') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             data.append(row)

#     first_character_data = data[:]  # Copy the data for the first character
#     second_character_data = data[:]  # Copy the data for the second character

#     if search_query:
#         first_character_data = [row for row in first_character_data if search_query.lower() in row['CharacterName'].lower()]
#         print(first_character_data)

#     if search_query2:
#         second_character_data = [row for row in second_character_data if search_query2.lower() in row['CharacterName'].lower()]
#         print(second_character_data)

#     return render(request, 'fight.html', {'first_csv_data': first_character_data, 'second_csv_data': second_character_data, 'search_query': search_query, 'search_query2': search_query2})


# def FightArena(request):
#     csv_file_path = 'static/marvel_with_img.csv'  # Path to your CSV file
#     search_query = request.GET.get('search')
#     search_query2 = request.GET.get('search2')  # For the second character

#     data = []
#     with open(csv_file_path, 'r', encoding='utf-8-sig') as file:  # Use 'utf-8-sig' to handle BOM
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             data.append(row)

#     first_character_data = data[:]  # Copy the data for the first character
#     second_character_data = data[:]  # Copy the data for the second character

#     if search_query:
#         first_character_data = [row for row in first_character_data if search_query.lower() in row['CharacterName'].lower()]
#         print(first_character_data)

#     if search_query2:
#         second_character_data = [row for row in second_character_data if search_query2.lower() in row['CharacterName'].lower()]
#         print(second_character_data)

#     return render(request, 'fight.html', {'first_csv_data': first_character_data, 'second_csv_data': second_character_data, 'search_query': search_query, 'search_query2': search_query2})



def FightArena(request):
    csv_file_path = 'static/marvel_with_img.csv'  # Path to your CSV file
    search_query = request.GET.get('search')
    search_query2 = request.GET.get('search2')  # For the second character

    data = []
    with open(csv_file_path, 'r', encoding='utf-8-sig') as file:  # Use 'utf-8-sig' to handle BOM
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Filter data based on search queries
    first_character_data = [row for row in data if search_query and search_query.lower() in row['CharacterName'].lower()]
    second_character_data = [row for row in data if search_query2 and search_query2.lower() in row['CharacterName'].lower()]

    return render(request, 'fight.html', {'first_csv_data': first_character_data, 'second_csv_data': second_character_data, 'search_query': search_query, 'search_query2': search_query2})









# def FightArena(request):
#   csv_file_path = 'static/marvel_with_img.csv'  # Path to your CSV file

#   search_query = request.GET.get('search')
#   search_query2 = request.GET.get('search2')  # For the second character

#   data = []
#   with open(csv_file_path, 'r') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#       data.append(row)

#   # No need to copy data for separate searches
#   first_character_data = data
#   second_character_data = data

#   if search_query:
#     first_character_data = [row for row in data if search_query.lower() in row['CharacterName'].lower()]

#   if search_query2:
#     second_character_data = [row for row in data if search_query2.lower() in row['CharacterName'].lower()]

#   context = {
#     'first_csv_data': first_character_data,
#     'second_csv_data': second_character_data,
#     'search_query': search_query,
#     'search_query2': search_query2,
#   }

#   return render(request, 'fight.html', context)