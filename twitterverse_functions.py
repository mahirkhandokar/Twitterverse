"""CSC108/A08: Fall 2020 -- Assignment 3: Twitterverse

This code is provided solely for the personal and private use of
students taking the CSC108 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

from typing import Callable, List, TextIO
from constants import (TwitterverseDict, SearchDict, FilterDict,
                       PresentDict, QueryDict)
from constants import (NAME, LOCATION, WEB, BIO, FOLLOWING, USERNAME,
                       OPERATIONS, FOLLOWER, FOLLOWERS, NAME_INCLUDES,
                       LOCATION_INCLUDES, SORT_BY, FORMAT, SEARCH,
                       FILTER, PRESENT, POPULARITY, END, ENDBIO, LONG)


HANDOUT_DATA = {
    'tomCruise': {
        'name': 'Tom Cruise',
        'bio': ('Official TomCruise.com crew tweets. We love you guys!\n' +
                'Visit us at Facebook!'),
        'location': 'Los Angeles, CA',
        'web': 'http://www.tomcruise.com',
        'following': ['katieH', 'NicoleKidman']},
    'PerezHilton': {
        'name': 'Perez Hilton',
        'bio': ('Perez Hilton is the creator and writer of one of the most ' +
                'famous websites\nin the world. And he also loves music -' +
                'a lot!'),
        'location': 'Hollywood, California',
        'web': 'http://www.PerezH...',
        'following': ['tomCruise', 'katieH', 'NicoleKidman']}}

HANDOUT_QUERY = {
    'SEARCH': {'username': 'tomCruise',
               'operations': ['following', 'followers']},
    'FILTER': {'following': 'katieH'},
    'PRESENT': {'sort-by': 'username',
                'format': 'short'}}

CREATED_DATA = {
    'tomCruise': {
        'name': 'Tom Cruise',
        'bio': ('Official TomCruise.com crew tweets. We love you guys!\n' +
                'Visit us at Facebook!'),
        'location': 'Los Angeles, CA',
        'web': 'http://www.tomcruise.com',
        'following': ['katieH', 'NicoleKidman']},
    'PerezHilton': {
        'name': 'Perez Hilton',
        'bio': ('Perez Hilton is the creator and writer of one of the most ' +
                'famous websites\nin the world. And he also loves music -' +
                'a lot!'),
        'location': 'Hollywood, California',
        'web': 'http://www.PerezH...',
        'following': ['tomCruise', 'katieH', 'NicoleKidman']},
    'katieH': {
        'name': 'Katie Holmes',
        'bio': '',
        'location': '',
        'web': 'www.tomkat.com',
        'following': []},
    'NicoleKidman': {
        'name': 'Nicole Kidman',
        'bio': ('At my house celebrating Halloween! I Know ' +
                'Haven\'t been on like years So Sorry,Be safe ' +
                'And have fun tonight'),
        'location': 'Oz', 'web': '', 'following': []},
    'p': {
        'name': 'Mme Clavell',
        'bio': 'I love winter, snow and ice.',
        'location': 'Paris. France',
        'web': '',
        'following': ['NicoleKidman']}}

############################################################################


def process_data(twitter_file: TextIO) -> TwitterverseDict:
    """Return the data that is read from twitter_file, in the TwitterverseDict
    format.

    Precondition: twitter_file must ne in the Twitter File format.

    """

    user_data = twitter_file.readlines()
    twitter_data = {}
    i = 0

    while i < len(user_data):
        twitter_data[user_data[i].strip()] = {NAME: '', BIO: '', LOCATION: '',
                                              WEB: '', FOLLOWING: []}
        user_info = twitter_data[user_data[i].strip()]
        user_lst = []
        i += 1
        while user_data[i].strip() != END:
            user_lst.append(user_data[i].strip())
            i += 1
        update_user_info(user_lst, user_info)
        i += 1
    return twitter_data


def update_user_info(user_lst: List[str],
                     user_info: object) -> None:
    """Update the dictionary user_info by creating key-value pairs using the
    information in user_lst.

    >>> user_info = {'name': '', 'bio': '', 'location': '', 'web': '',
    ... 'following': []}
    >>> update_user_info(['Katie Holmes', '', '', 'ENDBIO'], user_info)
    >>> user_info == CREATED_DATA['katieH']
    False
    >>> user_info = {'name': '', 'bio': '', 'location': '', 'web': '',
    ... 'following': []}
    >>> update_user_info(['Tom Cruise', 'Los Angeles, CA',
    ... 'http://www.tomcruise.com',
    ... 'Official TomCruise.com crew tweets. We love you guys!',
    ... 'Visit us at Facebook!', 'ENDBIO', 'katieH', 'NicoleKidman'], user_info)
    >>> user_info == HANDOUT_DATA['tomCruise']
    True

    """

    user_info[NAME] = user_lst[0]
    user_info[LOCATION] = user_lst[1]
    user_info[WEB] = user_lst[2]
    bio_str = ''
    i = 3

    while user_lst[i] != ENDBIO:
        bio_str += user_lst[i] + '\n'
        i += 1
    user_info[BIO] = bio_str[:-1]

    if user_lst[i] == ENDBIO:
        i += 1
        while i < len(user_lst):
            user_info[FOLLOWING].append(user_lst[i].strip())
            i += 1


def process_query(query_file: TextIO) -> QueryDict:
    """Return the data that is read from query_file, in the QueryDict format.

    Precondition: query_file must be in the Query File format.

    """

    query_data = query_file.readlines()
    query_dictionary = {SEARCH: {USERNAME: '', OPERATIONS: []}, FILTER: {},
                        PRESENT: {}}
    i = 0
    j = 0

    while j < len(query_data):
        query_data[j] = query_data[j].strip()
        j += 1

    while i < len(query_data):
        if query_data[i] == SEARCH:
            query_dictionary[SEARCH][USERNAME] = query_data[i + 1]
        elif (query_data[i] == FOLLOWING
              or query_data[i] == FOLLOWERS):
            query_dictionary[SEARCH][OPERATIONS].append(query_data[i])
        else:
            i = filter_or_present(i, query_data, query_dictionary)
        i += 1
    return query_dictionary


def filter_or_present(i: int, query_data: List[str],
                      query_dictionary: QueryDict) -> int:
    """Return the first index out of range of query_data.
    Update query_dictionary for keywords 'FILTER' and 'PRESENT' by using
    index, i, and the extracted data from the query file, query_data.

    >>> query_data = ['SEARCH', 'tomCruise', 'following', 'followers',
    ... 'FILTER', 'following katieH', 'PRESENT', 'sort-by username',
    ... 'format short']
    >>> query_dictionary = {SEARCH: {'username': 'tomCruise',
    ... 'operations': ['following', 'followers']}, FILTER: {}, PRESENT: {}}
    >>> filter_or_present(4, query_data, query_dictionary)
    6
    >>> query_data = ['SEARCH', 'tomCruise', 'following', 'followers',
    ... 'FILTER', 'following katieH', 'PRESENT', 'sort-by username',
    ... 'format short']
    >>> query_dictionary = {SEARCH: {'username': 'tomCruise',
    ... 'operations': ['following', 'followers']},
    ... FILTER: {'following': 'katieH'}, PRESENT: {}}
    >>> filter_or_present(7, query_data, query_dictionary)
    9

    """

    if query_data[i].strip() == FILTER:
        i += 1
        while query_data[i].strip() != PRESENT:
            filter_spec = query_data[i].split()
            query_dictionary[FILTER][filter_spec[0]] = filter_spec[1].strip()
            i += 1
    elif query_data[i - 1].strip() == PRESENT:
        while i < len(query_data):
            present_spec = query_data[i].split()
            query_dictionary[PRESENT][present_spec[0]] = present_spec[1].strip()
            i += 1
    return i


def all_followers(twitter_data: TwitterverseDict, username: str) -> List[str]:
    """Return all users who are following user, username, as a list.

    Precondition: len(username) == 1

    >>> all_followers(HANDOUT_DATA, 'tomCruise')
    ['PerezHilton']
    >>> all_followers(HANDOUT_DATA, 'PerezHilton')
    []

    """

    followers = []

    for user_data in twitter_data:
        for key in twitter_data[user_data]:
            if (username in twitter_data[user_data][key]
                    and key == FOLLOWING and user_data != username):
                followers.append(user_data)
    return followers


def get_search_results(twitter_data: TwitterverseDict,
                       search_spec: SearchDict) -> List[str]:
    """Return a list of users according to the operations in search_spec using
    data in twitter_data to find users, with no duplicate users. If the
    operation is following, each user in the list of users is replaced by users
    they follow. If the operation is followers, each user in the list of users
    is replaced by the users who follow them.

    >>> get_search_results(HANDOUT_DATA, HANDOUT_QUERY[SEARCH])
    ['tomCruise', 'PerezHilton']
    >>> get_search_results(CREATED_DATA, HANDOUT_QUERY[SEARCH])
    ['tomCruise', 'PerezHilton', 'p']

    Precondition: len(search_spec[USERNAME]) == 1

    """

    lst_of_users = [search_spec[USERNAME]]
    users_lst = []
    for operation in search_spec[OPERATIONS]:
        users_lst = (replace_users(operation, twitter_data, lst_of_users))
        lst_of_users = remove_duplicates(users_lst)
    return lst_of_users


def replace_users(operation: str, twitter_data: TwitterverseDict,
                  lst_of_users: List[str]) -> List[str]:
    """Return a new list of users, where each user in lst_of_users, is operated
    on by the operation, and users are replaced by their followers or people
    they are following.

    >>> replace_users('following', HANDOUT_DATA, ['tomCruise'])
    ['katieH', 'NicoleKidman']
    >>> replace_users('followers', CREATED_DATA, ['katieH'])
    ['tomCruise', 'PerezHilton']

    """

    users_lst = []
    len_lst = len(lst_of_users)
    i = 0

    while i < len_lst:
        if operation == FOLLOWING:
            for followed_person in twitter_data[lst_of_users[i]][FOLLOWING]:
                users_lst.append(followed_person)
        elif operation == FOLLOWERS:
            for follower in all_followers(twitter_data, lst_of_users[i]):
                users_lst.append(follower)
        i += 1
    return users_lst


def remove_duplicates(users_lst: List[str]) -> List[str]:
    """Return all duplicate users in the list removed, lst_of_users, such that
    there isvonly one occurence of each user in the list.

    >>> lst_of_users = ['tomCruise', 'katieH', 'tomCruise']
    >>> remove_duplicates(lst_of_users)
    ['katieH', 'tomCruise']
    >>> lst_of_users = ['anyatafliovich', 'nickcheng']
    >>> remove_duplicates(lst_of_users)
    ['anyatafliovich', 'nickcheng']

    """

    for user in users_lst:
        if users_lst.count(user) > 1:
            while users_lst.count(user) != 1:
                users_lst.remove(user)
    for empty in users_lst:
        if empty == '':
            users_lst.remove('')
    return users_lst


def get_filter_results(twitter_data: TwitterverseDict, lst_of_users: List[str],
                       filter_spec: FilterDict) -> List[str]:
    """Return a new list of users, which is equivalent to lst_of_users altered
    according to the specifications in filter_spec, using information found
    in twitter_data.

    >>> get_filter_results(HANDOUT_DATA, ['tomCruise', 'PerezHilton'],
    ... HANDOUT_QUERY[FILTER])
    ['tomCruise', 'PerezHilton']
    >>> get_filter_results(CREATED_DATA, ['tomCruise', 'PerezHilton', 'p'],
    ... HANDOUT_QUERY[FILTER])
    ['tomCruise', 'PerezHilton']

    """

    lst_usernames = create_duplicate(lst_of_users)

    #flter is filter without vowels
    for fltr in filter_spec:
        remove_users(fltr, filter_spec, lst_usernames, twitter_data)
    return lst_usernames


def remove_users(fltr: str, filter_spec: FilterDict, lst_usernames: List[str],
                 twitter_data: TwitterverseDict) -> None:
    """Remove users from lst_usernames who do not have specified value of the
    key, fltr, in the filter_spec dictionary, using the information for each
    user in twitter_data.

    >>> lst_usernames = ['tomCruise', 'PerezHilton', 'NicoleKidman']
    >>> remove_users('following', HANDOUT_QUERY[FILTER],
    ... lst_usernames, CREATED_DATA)
    >>> lst_usernames == ['tomCruise', 'PerezHilton']
    True
    >>> lst_usernames = ['tomCruise', 'PerezHilton']
    >>> remove_users('name-includes', {'name-includes': 'tom'},
    ... lst_usernames, HANDOUT_DATA)
    >>> lst_usernames == ['tomCruise']
    True

    """

    i = 0
    copy_of_lst = create_duplicate(lst_usernames)

    while i < len(copy_of_lst):
        if (fltr == FOLLOWING and filter_spec[fltr]
                not in twitter_data[copy_of_lst[i]][FOLLOWING]):
            lst_usernames.remove(copy_of_lst[i])
        elif (fltr == FOLLOWER and filter_spec[fltr]
              not in all_followers(twitter_data, copy_of_lst[i])):
            lst_usernames.remove(copy_of_lst[i])
        elif (filter_spec[fltr].lower() not in copy_of_lst[i].lower()
              and fltr == NAME_INCLUDES):
            lst_usernames.remove(copy_of_lst[i])
        elif (filter_spec[fltr].lower()
              not in twitter_data[copy_of_lst[i]][LOCATION].lower()
              and fltr == LOCATION_INCLUDES):
            lst_usernames.remove(copy_of_lst[i])
        i += 1


def get_present_string(twitter_data: TwitterverseDict, lst_of_users: List[str],
                       present_spec: PresentDict) -> str:
    """Return a new list of usernames or a string of users and their
    information, which is found in twitter_data, where the users in lst_of_users
    are presented according to the specifications in present_spec.

    >>> get_present_string(HANDOUT_DATA, ['tomCruise', 'PerezHilton'],
    ... HANDOUT_QUERY[PRESENT])
    ['PerezHilton', 'tomCruise']
    >>> get_present_string(CREATED_DATA, ['tomCruise', 'katieH'],
    ... HANDOUT_QUERY[PRESENT])
    ['katieH', 'tomCruise']

    Precondition: present_spec[SORT_BY] != '' and present_spec[FORMAT] != ''

    """

    lst_usernames = create_duplicate(lst_of_users)
    present_str = ''

    if present_spec[SORT_BY] == USERNAME:
        lst_usernames.sort()
    elif present_spec[SORT_BY] == NAME:
        tweet_sort(twitter_data, lst_usernames, present_spec[SORT_BY])
    elif present_spec[SORT_BY] == POPULARITY:
        tweet_sort(twitter_data, lst_usernames, present_spec[SORT_BY])

    if present_spec[FORMAT] == LONG:
        present_str = format_report(twitter_data, lst_usernames,
                                    present_spec[FORMAT])
        return present_str
    return lst_usernames


def create_duplicate(lst_of_users: List[str]) -> List[str]:
    """Return a duplicate of lst_of_users.

    >>> create_duplicate(['tomCruise', 'PerezHilton'])
    ['tomCruise', 'PerezHilton']
    >>> create_duplicate(['tomCruise', 'PerezHilton', 'p'])
    ['tomCruise', 'PerezHilton', 'p']

    """

    copy_of_lst = []

    for user in lst_of_users:
        copy_of_lst.append(user)
    return copy_of_lst

#############################################################################
#Provided helper functions
#############################################################################


def tweet_sort(twitter_data: TwitterverseDict,
               usernames: List[str],
               sort_spec: str) -> None:
    """Sort usernames based on the sorting specification in sort_spec
    using the data in twitter_data.

    >>> usernames = ['tomCruise', 'PerezHilton']
    >>> tweet_sort(HANDOUT_DATA, usernames, 'username')
    >>> usernames == ['PerezHilton', 'tomCruise']
    True
    >>> tweet_sort(HANDOUT_DATA, usernames, 'popularity')
    >>> usernames == ['tomCruise', 'PerezHilton']
    True
    >>> tweet_sort(HANDOUT_DATA, usernames, 'name')
    >>> usernames == ['PerezHilton', 'tomCruise']
    True

    """

    usernames.sort()  # sort by username first
    if sort_spec in SORT_FUNCS:
        SORT_FUNCS[sort_spec](twitter_data, usernames)


def by_popularity(twitter_data: TwitterverseDict, usernames: List[str]) -> None:
    """Sort usernames in descending order based on popularity (number of
    users that follow a given user) in twitter_data.

    >>> usernames = ['PerezHilton', 'tomCruise']
    >>> by_popularity(HANDOUT_DATA, usernames)
    >>> usernames == ['tomCruise', 'PerezHilton']
    True

    """

    def get_popularity(username: str) -> int:
        return len(all_followers(twitter_data, username))

    usernames.sort(key=get_popularity, reverse=True)


def by_name(twitter_data: TwitterverseDict, usernames: List[str]) -> None:
    """Sort usernames in ascending order based on name in twitter_data.

    >>> usernames = ['tomCruise', 'PerezHilton']
    >>> by_name(HANDOUT_DATA, usernames)
    >>> usernames == ['PerezHilton', 'tomCruise']
    True

    """

    def get_name(username: str) -> str:
        return twitter_data.get(username, {}).get(NAME, '')

    usernames.sort(key=get_name)


def format_report(twitter_data: TwitterverseDict,
                  usernames: List[str],
                  format_spec: str) -> str:
    """Return a string representing usernames presented as specified by
    the format specification format_spec.

    Precondition: each username in usernames is in twitter_data
    """

    if format_spec == LONG:
        result = '-' * 10 + '\n'
        for user in usernames:
            result += format_details(twitter_data, user)
            result += '-' * 10 + '\n'
        return result
    return str(usernames)


def format_details(twitter_data: TwitterverseDict, username: str) -> str:
    """Return a string representing the long format of username's info in
    twitter_data.

    Precondition: username is in twitter_data
    """

    user_data = twitter_data[username]
    return ("{}\nname: {}\nlocation: {}\nwebsite: {}\nbio:\n{}\n" +
            "following: {}\n").format(username, user_data[NAME],
                                      user_data[LOCATION],
                                      user_data[WEB], user_data[BIO],
                                      user_data[FOLLOWING])


############################################################################


SORT_FUNCS = {POPULARITY: by_popularity,
              NAME: by_name}


if __name__ == '__main__':
    import doctest
    doctest.testmod()