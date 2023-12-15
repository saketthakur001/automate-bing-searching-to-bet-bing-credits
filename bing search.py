"""
# define a [[python Functions]] that performs a task [[Random]]ly between the time given

# ask user for:
number of browsing sessions
total number of search

# just so it's clear
- the user will have to give a number of time the bot browses randomly(for a short period of time)
- from the total number of searches give each session random number of searches 
"""

import random
import time


def random_search(total_search, number_of_sessions, start_time, end_time):
    '''
    start_time : 1-24
    end_time : 1-24

    total_search : 1-100         # number of searches per session
    number_of_sessions : 1-100   # number of sessions per day
    '''

    # pick random times for the random sessions according to the number of sessions # store numbers in a dictonary
    total_search += random.randint(-10, 30)
    number_of_sessions += random.randint(1, 5)

    sessions = {}
    for i in range(number_of_sessions):
        sessions[random.randint(start_time, end_time)] = 0

    for i in range(number_of_searches):
        choice = random.choice(list(sessions.keys()))
        sessions[choice] +=1
    return sessions

random_search(50, 5, 9, 24)
