import json
import re

with open('.\jsonResult\EjercicioA.json') as access_json:
    read_content = json.load(access_json)
    
 
save_authz_1 = []
save_authz_2 = []
save_authz_3 = []
save_authz_4 = []
# Listas planas
authz1 = []
authz2 = []
authz3 = []
authz4 = []

save_authn_1 = []
save_authn_2 = []
save_authn_3 = []
save_authn_4 = []
# Listas planas
authn1 = []
authn2 = []
authn3 = []
authn4 = []

save_minimal_set = []
get_minimal_set = []

def authz_providers():
    question_access = read_content['content_module']
    authz_1 = question_access['authz.provider_1']
    authz_2 = question_access['authz.provider_2']
    authz_3 = question_access['authz.provider_3']
    authz_4 = question_access['authz.provider_4']
    save_authz_1.append(authz_1)
    save_authz_2.append(authz_2)
    save_authz_3.append(authz_3)   
    save_authz_4.append(authz_4)
    

def authn_providers():
    question_access = read_content['auth_module']
    authn_1 = question_access['authn.provider_1']
    authn_2 = question_access['authn.provider_2']
    authn_3 = question_access['authn.provider_3']
    authn_4 = question_access['authn.provider_4']
    save_authn_1.append(authn_1)
    save_authn_2.append(authn_2)
    save_authn_3.append(authn_3)   
    save_authn_4.append(authn_4)


authz_providers()
authn_providers()


def get_lists():
    for list1 in save_authz_1:
        if type(list1) == list:
            for element in list1:
                authz1.append(element)
    for list2 in save_authz_2:
        if type(list2) == list:
            for element in list2:
                authz2.append(element)
    for list3 in save_authz_3:
        if type(list3) == list:
            for element in list3:
                authz3.append(element)
    for list4 in save_authz_4:
        if type(list4) == list:
            for element in list4:
                authz4.append(element)
    for list5 in save_authn_1:
        if type(list5) == list:
            for element in list5:
                authn1.append(element)
    for list6 in save_authn_2:
        if type(list6) == list:
            for element in list6:
                authn2.append(element)
    for list7 in save_authn_3:
        if type(list7) == list:
            for element in list7:
                authn3.append(element)
    for list8 in save_authn_4:
        if type(list8) == list:
            for element in list8:
                authn4.append(element)


get_lists() 


def minimal_set():
    a = [x for x in authz1 if x in authn1]
    save_minimal_set.append(a)
    b = [x for x in authz2 if x in authn2]
    save_minimal_set.append(b)
    c = [x for x in authz3 if x in authn4]
    save_minimal_set.append(c)
    d = [x for x in authz4 if x in authn3]
    save_minimal_set.append(d)
    
    result = [row[0] for row in save_minimal_set]
    get_minimal_set.append(result)
    print(get_minimal_set)

minimal_set()