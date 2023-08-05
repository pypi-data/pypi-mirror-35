import ast
import json
import requests
from project.user_provision import getJsonResponse
from project.plugin import inviteMessage, removalMessage, getGroups

def getKey(configMap):
     for config_key in configMap['plugins']:
          if config_key['plugin']+':'+config_key['tag']  == 'bitbucket:prod':
               return  config_key['key']

def getSecret(configMap):
     for config_key in configMap['plugins']:
          if config_key['plugin']+':'+config_key['tag'] == 'bitbucket:prod':
               return config_key['secret']

def userExists(allMembers, userName, cli_groups):

    for group in allMembers:
        if group['name'] in cli_groups:
            for user in group['members']:
                if userName.lower() == user['username'].lower():
                    return True
    return False

def getAccessToken(configMap,plugin_tag, userName):

    data = {'grant_type': 'client_credentials'}
    credentials = requests.post("https://bitbucket.org/site/oauth2/access_token",
                                auth=(getKey(configMap), getSecret(configMap)), data=data)
    log = errorCheck(credentials, plugin_tag, userName)

    if log:
        print(log)
        instruction = log
        return None
    else:
        my_json = credentials.content.decode('utf8')
        data = json.loads(my_json)
        return data.get('access_token')


def getCliGroups(cli_groups, configMap, plugin_tag, userName, access_token):

        # get all groups
    groups = requests.get(
        "https://api.bitbucket.org/1.0/groups/" + configMap['global']['organization'] + "?access_token=" + access_token)
    log = errorCheck(groups, plugin_tag, userName)

    if log:
        print(log)
        instruction = log
        return None
    else:
        my_json = groups.content.decode('utf8')
        return json.loads(my_json)


def inviteUser(email,configMap,allPermissions, plugin_tag, name):

     done = False
     userName = email.split('@', 1)[0]
     cli_groups = []
     log = ""
     instruction = ""
     #Get Authorization token
     access_token = getAccessToken(configMap,plugin_tag, userName)

     if access_token:

         for permission in allPermissions:
             thisPermissions = ast.literal_eval(permission)
             if thisPermissions['plugin'] == plugin_tag:
                 del thisPermissions['plugin']
                 cli_groups = list(thisPermissions.values())
                 break

         if len(cli_groups) == 0:
             cli_groups = getGroups(configMap,plugin_tag)

         allMembers = getCliGroups(cli_groups, configMap, plugin_tag, userName, access_token)

         if allMembers:

                #first to check if a user already is in the group, in which case the invitation is not sent
             if userExists(allMembers, userName, cli_groups):
                 log  = ("The user " + userName + " cannot be invited. The user already exists")
                 instruction = log
                 print(log)

             else:
                 #second to check if a user already received an invitation by email, but did not yet accept it,
                 #in which case the invitation is not set
                 for group in cli_groups:
                     checkingInvitation = requests.get(
                         "https://api.bitbucket.org/1.0/users/"+configMap['global']['organization']+"/invitations/"
                             + email + "?access_token=" + access_token)

                 if checkingInvitation.reason == 'OK':
                     log = "The invitation to the user " +userName+ " has been already sent"
                     instruction =log
                     print(log)
                 else:
                     #invitaion is sent
                     for group in cli_groups:
                            invGroup = requests.put(
                                 "https://api.bitbucket.org/1.0/users/"+configMap['global']['organization']+"/invitations/"
                                 + email + "/"+configMap['global']['organization']+"/"+group.lower() + "?access_token=" + access_token)

                     log = errorCheck(invGroup, plugin_tag, userName)

                     if log:
                        print(log)
                        instruction = log
                     else:
                        log = 'BitBucket: Email invite sent from Bitbucket.\n'
                        instruction = inviteMessage(configMap,plugin_tag)
                        done = True

     return getJsonResponse('Bitbucket', email, log, instruction, done)

def removeUser(email,configMap,allPermissions, plugin_tag):

     done = False
     userName = email.split('@', 1)[0]
     log = ""
     instruction = ""
     cli_groups = getGroups(configMap, plugin_tag)

     access_token = getAccessToken(configMap,plugin_tag, userName)

     if access_token:
         data = getCliGroups(cli_groups, configMap, plugin_tag, userName, access_token)

         if data:
             #check is a user is not in the group in which case the user is not deleted
             if userExists(data, userName, cli_groups) == False:
                 log = ("The user " + userName + " does not exist, delete failed")
                 instruction = log
                 print(log)

             else:
                 # Remove from groups
                 for group in data:
                    delMem= requests.delete("https://api.bitbucket.org/1.0/groups/"+configMap['global']['organization']+
                                            "/"+group.get('name').lower()+"/members/"+email+"?access_token="+access_token)
                 log = errorCheck(delMem, plugin_tag, userName)
                 if log:
                    instruction = log
                    print(log)
                 else:
                    log = email.split('@', 1)[0] + removalMessage(configMap, plugin_tag) + '\n'
                    instruction = log
                    done = True

     return getJsonResponse('Bitbucket', email, log, instruction, done)


def errorCheck(response, plugin_tag, name):

    log = None

    if response.status_code > 204 :
        if response.status_code == 401:
            log = plugin_tag + ' error: HTML link is broken. Plugin did not work'
        elif response.status_code == 404:
            log = plugin_tag + ' error: ' + str(response.status_code) + ' Make sure config.yaml is set up correctly '
        elif response.status_code == 400:
            log = plugin_tag + ' error: ' + str(response.status_code) + ' Wrong access key or secret key'
        else:
            log = plugin_tag + ' error: ' + str(response.status_code) + ' User could not be registered'

    return log



