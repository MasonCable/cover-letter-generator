import os
from argparse import ArgumentParser
import time

parser = ArgumentParser(description="This script will allow you to auto generate cover letters from some basic information supplied over command line inputs.")
args = parser.parse_args()


def get_user_data():
    name = input("What is your full name: \n")
    applicationLocation = input("Where did you find this application? i.e. linkedin.com, glassdoor, indeed: \n")
    positionTitle = input("What position are you applying for? i.e., Software Engineer: \n")
    positionLevel = input("What level is the position? i.e. junior, mid, senior: \n")
    singleWordSkills = input("What are some skills that you have that can be described in one word? (Provide answer with comma seperated values like the example shown) \nEXAMPLE: PHP, management, JavaScript, etc: \n")
    appliedSkills = input("What do you use your skills for? EXAMPLE: manage a team, build largescale web applications, manage accounting.: \n")
    standoutSentence = input("Provide one sentence that will convince the hiring manager to pick you.: \n")
    requiredSkills = input("Provide a list of skills that you have which match the job requirements. (Provide answer with comma seperated values like the example shown) \nEXAMPLE: Build PHP applications, manage a team of 5 or more, Write Documnentation, etc: \n")
    cellPhone = input("Provide a cell number for the recruiter to reach you at: \n")
    email = input("Provide an email for the recruiter to reach you at: \n")

    userDetails = {
        'name': name.title(),
        'application_location': applicationLocation.title(),
        'position_title': positionTitle,
        'position_level': positionLevel,
        'single_word_skills': singleWordSkills,
        'applied_skills': appliedSkills,
        'standout_sentence': standoutSentence,
        'required_skills': requiredSkills,
        'cell': cellPhone,
        'email': email
    }
    return userDetails

def get_file_contents():
    userData = get_user_data()
    fileName = 'broiler_plate_letter.txt'

    with open(fileName) as f:
        fileContents = f.read().replace('\n','$THIS_NEEDS_TO_BE_LINE_BREAK')        
    
    return fileContents


def replace_file_variables():
    data = get_file_contents()
    dataArr = data.split()
    al = [ i for i, x in enumerate(dataArr) if x == "$APPLICATION_LOCATION" ]
    p = [ i for i,x in enumerate(dataArr) if x == "$POSITION." ]
    n = [ i for i,x in enumerate(dataArr) if x == "$NAME" ]
    pl = [ i for i,x in enumerate(dataArr) if x == "$POSITION_LEVEL" ]
    pt = [ i for i,x in enumerate(dataArr) if x == "$POSITION_TITLE" ]
    c = [ i for i,x in enumerate(dataArr) if x == "$CELL_PHONE" ]
    e = [ i for i,x in enumerate(dataArr) if x == "$EMAIL" ]
    ss = [ i for i,x in enumerate(dataArr) if x == "$STAND_SENTENCE" ]

    

    
    print(p)



replace_file_variables()
