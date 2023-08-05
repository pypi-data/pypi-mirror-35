#####################################################################################
#                  Pydradis: Python API Wrapper for Dradis                          #
#                       Copyright (c) 2018 GoVanguard                               #
#              Origionally developed by Pedro M. Sosa, Novacast                     #
#####################################################################################
# This file is part of Pydradis.                                                    #
#                                                                                   #
#     Pydradis is free software: you can redistribute it and/or modify              #
#     it under the terms of the GNU Lesser General Public License as published by   #
#     the Free Software Foundation, either version 3 of the License, or             #
#     (at your option) any later version.                                           #
#                                                                                   #
#     Pydradis is distributed in the hope that it will be useful,                   #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of                #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                 #
#     GNU Lesser General Public License for more details.                           #
#                                                                                   #
#     You should have received a copy of the GNU Lesser General Public License      #
#     along with Pydradis.  If not, see <http://www.gnu.org/licenses/>.             #
#####################################################################################
import requests
import string
import json
import shutil

class Pydradis3:
    #End Nodes#
    client_endpoint = "/pro/api/clients"
    project_endpoint = "/pro/api/projects"
    node_endpoint = "/pro/api/nodes"
    issue_endpoint = "/pro/api/issues"
    evidence_endpoint = "/pro/api/nodes/<ID>/evidence"
    note_endpoint = "/pro/api/nodes/<ID>/notes" 
    attachment_endpoint = "/pro/api/nodes/<ID>/attachments"

    #Constructor
    def __init__(self, apiToken: str, url: str, debug=False, verify=True):
        self.__apiToken = apiToken  #API Token 
        self.__url = url            #Dradis URL (eg. https://your_dradis_server.com)
        self.__debug = debug        #Debuging True?
        self.__verify = verify      #Path to SSL certificate


    def debug(self, val: bool):
        self.__debug = val

    #Send Requests to Dradis (& DebuggCheck for Error Codes)
    def contactDradis(self, url: str, header: dict, reqType: str, response_code: str, data=""):
        r = 0
        r = requests.Request(reqType, url, headers=header, data=data)
        r = r.prepare()

        s = requests.Session()
        results = s.send(r)

        print(results)
        if (self.__debug):
            print("\nServer Response:\n")
            print(results.status_code)
            print("---\n")
            print(results.content)

        if (str(results.status_code) != str(response_code)):
            return None

        return results.json()

    ####################################
    #         Clients Endpoint         #
    ####################################

    #Get Client List 
    def get_clientlist(self):
        #URL
        url = self.__url + self.client_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Content-type': 'application/json'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        result = []
        for i in range(0, len(r)):
            result  += [[r[i]["name"], r[i]["id"]]]

        return result

    #Create Client 
    def create_client(self, client_name: str):
        
        #URL
        url = self.__url + self.client_endpoint
        
        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Content-type': 'application/json'}
        
        #DATA
        data = {"client":{"name":client_name}}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "POST", "201", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return r['id'] 

    #Update Client 
    def update_client(self, client_id: str, new_client_name: str):
        
        #URL
        url = self.__url + self.client_endpoint + "/" + str(client_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Content-type': 'application/json'}
        
        #DATA
        data = {"client":{"name":new_client_name}}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "PUT", "200", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return r['id']      

    #Delete Client 
    def delete_client(self, client_id: str):

        #URL
        url = self.__url + self.client_endpoint + "/" + str(client_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"'}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "DELETE", "200")

        #RETURN
        if (r == None):
            return None

        return True

    #Search For Client 
    def find_client(self, name: str):

        #URL
        url = self.__url + self.client_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Content-type': 'application/json'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        result = []
        for i in range(0, len(r)):
            if (r[i]["name"] == name):
                return r[i]["id"]
        
        return None

    #Get Client Info 
    def get_client(self, client_id: str):

        #URL
        url = self.__url + self.client_endpoint + "/"  +  str(client_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Content-type': 'application/json'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None
        
        return r


    ####################################
    #         Projects Endpoint        #
    ####################################

    #Get Project List 
    def get_projectlist(self):

        #URL
        url = self.__url + self.project_endpoint

        #DATA
        header = { 'Authorization':'Token token="' + self.__apiToken + '"'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        result = []
        for i in range(0, len(r)):
            result  += [[r[i]["name"], r[i]["id"]]]

        return result

    #Create Project 
    def create_project(self, project_name: str, client_id=None):
        
        #URL
        url = self.__url + self.project_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Content-type': 'application/json'}
        
        #DATA
        data = {"project":{"name":project_name}}
        if (client_id != None):
            data = {"project":{"name":project_name, "client_id":str(client_id)}}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "POST", "201", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return r['id'] 

    #Update Project 
    def update_project(self, pid: int, new_project_name: str, new_client_id=None):
        
        #URL
        url = self.__url + self.project_endpoint + "/" + str(pid)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Content-type': 'application/json'}
        
        #DATA
        data = {"project":{"name":new_project_name}}
        if (new_client_id != None):
            data = {"project":{"name":new_project_name, "client_id":str(new_client_id)}}
        

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "PUT", "200", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return r['id']     

    #Delete Project 
    def delete_project(self, pid: int):
        
        #URL
        url = self.__url + self.project_endpoint + "/" + str(pid)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"'}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "DELETE", "200")

        #RETURN
        if (r == None):
            return None

        return True

    #Search For Project 
    def find_project(self, name: str):
        
        #URL
        url = self.__url + self.project_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        result = []
        for i in range(0, len(r)):
            if (r[i]["name"] == name):
                return r[i]["id"]
        
        return None

    #Get Project Info 
    def get_project(self, pid: int):

        #URL
        url = self.__url + self.project_endpoint + "/" + str(pid)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None
        
        return r


    ####################################
    #         Nodes Endpoint           #
    ####################################

    #Get Node List 
    def get_nodelist(self, pid: int):
        
        #URL
        url = self.__url + self.node_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        result = []
        for i in range(0, len(r)):
            result  += [[r[i]["label"], r[i]["id"]]]

        return result

    #Create Node 
    def create_node(self, pid: int, label: str, type_id=0, parent_id=None, position=1):

        #URL
        url = self.__url + self.node_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}
        
        #DATA
        if (parent_id != None): #If None (Meaning its a toplevel node) then dont convert None to string.
            parent_id = str(parent_id)
        data = {"node":{"label":label, "type_id":str(type_id), "parent_id":parent_id, "position": str(position)}}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "POST", "201", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return r['id'] 

    #Update Node 
    def update_node(self, pid: int, node_id: str, label=None, type_id=None, parent_id=None, position=None):
        
        #URL
        url = self.__url + self.node_endpoint + "/" + str(node_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA (notice this time we are building a str not a dict)
        if (label==type_id==parent_id==position==None):
            return None        

        data = '{"node":{'
        if (label != None):
            data  += '"label":"' + label + '"'
        if (type_id != None):
            data  += ', "type_id":"' + str(type_id) + '"'
        if (parent_id != None):
            data  += ', "parent_id":"' + str(parent_id) + '"'
        if (position != None):
            data  += ', "position":"' + str(position) + '"'
        data  += "}}"


        #CONTACT DRADIS
        r = self.contactDradis(url, header, "PUT", "200", data)
        
        #RETURN
        if (r == None):
            return None

        return r['id']  

    #Delete Node 
    def delete_node(self, pid: int, node_id: str):

        #URL
        url = self.__url + self.node_endpoint + "/" + str(node_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "DELETE", "200")

        #RETURN
        if (r == None):
            return None

        return True

    #Find Node  :: Given a nodepath (e.g ac/dc/r) return the node id. (these change between projects) 
    def find_node(self, pid: int, nodepath: str):

        #URL
        url = self.__url + self.node_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        #Finding packet by traversing tree structure.
        nodepath = nodepath.split("/")
        parent_id = None
        for node in nodepath:
            for i in range(0, len(r)):
                found = False
                if ((r[i]["label"] == node) and (r[i]["parent_id"] == parent_id)):
                    if (self.__debug):
                         print("Found:", node, r[i]["id"])
                    parent_id = r[i]["id"]
                    found = True
                    break

            if (not found):
                return None

        if (self.__debug):
            print("Your node is:", parent_id)

        return parent_id

    #Get Node Info 
    def get_node(self, pid: int, node_id: str):

        #URL
        url = self.__url + self.node_endpoint + "/" + str(node_id)
        
        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None
        
        return r


    ####################################
    #         Issues Endpoint          #
    ####################################

    #Get Issue List 
    def get_issuelist(self, pid: int):
        
        #URL
        url = self.__url + self.issue_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        result = []
        for i in range(0, len(r)):
            result  += [[r[i]["title"], r[i]["id"]]]

        return result

    #Create Issue on Project 
    def create_issue(self, pid: int, title: str, text: str, tags=[]):

        #URL
        url = self.__url + self.issue_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        taglines = ""
        if (len(tags) != 0):
            for tag in tags:
                taglines += "#[" + tag + "]#\r\n"

        data = { 'issue':{'text':'#[Title]#\r\n' + title + '\r\n\r\n#[Description]#\r\n' + str(text) + "\r\n\r\n" + taglines}}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "POST", "201", json.dumps(data))

        #RETURN
        if (r == None):
            return None

        return r['id']

    #Create Issue on Project
    def create_issue_raw(self, pid: int, data: str):

        #URL
        url = self.__url + self.issue_endpoint

        #HEADER
        header = {'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        data = {'issue': data}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "POST", "201", json.dumps(data))

        #RETURN
        if (r == None):
            return None

        return r['id']

    #Update Issue 
    def update_issue(self, pid: int, issue_id: str, title: str, text: str, tags=[]):
        
        #URL
        url = self.__url + self.issue_endpoint + "/" + str(issue_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        taglines = ""
        if (len(tags) != 0):
            for tag in tags:
                taglines += "#[" + tag + "]#\r\n"    

        data = { 'issue':{'text':'#[Title]#\r\n' + title + '\r\n\r\n#[Description]#\r\n' + str(text) + "\r\n\r\n" + taglines}}


        #CONTACT DRADIS
        r = self.contactDradis(url, header, "PUT", "200", json.dumps(data))

        #RETURN
        if (r == None):
            return None

        return r['id']

    #Update Issue
    def update_issue_raw(self, pid: int, issue_id: str, data: str):

        #URL
        url = self.__url + self.issue_endpoint + "/" + str(issue_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        data = {'issue': data}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "PUT", "200", json.dumps(data))

        #RETURN
        if (r == None):
            return None

        return r['id']

    #Update Issue
    def update_issue_tags(self, pid: int, issue_id: str, tags=[]):

        #URL
        url = self.__url + self.issue_endpoint + "/" + str(issue_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        # Obtain original
        existingIssue = self.get_issue(pid=pid, issue_id=issue_id)
        if existingIssue:
            title = existingIssue['title']
            text = existingIssue['text']
        else:
            return None

        # Remove original
        deleteExisting = self.delete_issue(pid=pid, issue_id=issue_id)

        #DATA
        taglines = ""
        if (len(tags) != 0):
            for tag in tags:
                taglines += "#[" + tag + "]#\r\n"

        data = { 'issue':{'text':'#[Title]#\r\n' + title + '\r\n\r\n#[Description]#\r\n' + str(text) + "\r\n\r\n" + taglines}}

        # Create new
        createIssue = create_issue(pid=pid, title=title, text=text, tags=taglines)

        #RETURN
        if (createIssue == None):
            return None

        return str(createIssue)

    #Delete Issue 
    def delete_issue(self, pid: int, issue_id: str):
        
        #URL
        url = self.__url + self.issue_endpoint + "/" + str(issue_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "DELETE", "200")

        #RETURN
        if (r == None):
            return None

        return True

    #Find Issue 
    def find_issue(self, pid: int, keywords: str):
        
        #URL
        url = self.__url + self.issue_endpoint

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        #Give people the option to just input a string.
        if (type(keywords)==str):
            keywords = [keywords]

        result = []
        for i in range(0, len(r)):
            str1 = str(r[i]["text"]).upper()
            for k in keywords:
                str2 = str(k).upper()
                if (str1.find(str2) != -1):
                    result  += [[r[i]["title"], r[i]["id"]]]
                    break

        return result

    #Get Issue (with issue_id) 
    def get_issue(self, pid: int, issue_id: str):

        #URL
        url = self.__url + self.issue_endpoint + "/" + str(issue_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        return r

    ####################################
    #         Evidence Endpoint        #
    ####################################

    #Get Evidence List 
    def get_evidencelist(self, pid: int, node_id: str):

        #URL
        url = self.__url + self.evidence_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        return r

    #Create Evidence 
    def create_evidence(self, pid: int, node_id: str, issue_id: str, title: str, text: str, tags=[]):

        #URL
        url = self.__url + self.evidence_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        taglines = ""
        if (len(tags) != 0):
            for tag in tags:
                taglines += "#[" + tag + "]#\r\n"

        #DATA
        data = { 'evidence':{'content':'#[Title]#\r\n' + title + '\r\n\r\n#[Description]#\r\n' + str(text) + "\r\n\r\n" + taglines, "issue_id":str(issue_id)}}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "POST", "201", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return r['id']

    #Create Evidence
    def create_evidence_raw(self, pid: int, node_id: str, issue_id: str, data: str):

        #URL
        url = self.__url + self.evidence_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = {'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        data = {'evidence':{'content':data, "issue_id":str(issue_id)}}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "POST", "201", json.dumps(data))

        #RETURN
        if (r == None):
            return None

        return r['id']

    #Update Evidence 
    def update_evidence(self, pid: int, node_id: str, issue_id: str, evidence_id: str, title: str, text: str, tags=[]):

        #URL
        url = self.__url + self.evidence_endpoint.replace("<ID>", str(node_id)) + "/" + str(evidence_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        taglines = ""
        if (len(tags) != 0):
            for tag in tags:
                taglines += "#[" + tag + "]#\r\n"

        data = { 'evidence':{'content':'#[Title]#\r\n' + title + '\r\n\r\n#[Description]#\r\n' + str(text) + "\r\n\r\n" + taglines, "issue_id":str(issue_id)}}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "PUT", "200", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return r['id']

    #Delete Evidence 
    def delete_evidence(self, pid: int, node_id: str, evidence_id: str):

        #URL
        url = self.__url + self.evidence_endpoint.replace("<ID>", str(node_id)) + "/" + str(evidence_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "DELETE", "200")

        #RETURN
        if (r == None):
            return None

        return True

    #Find Evidence 
    def find_evidence(self, pid: int, node_id: str, keywords: str):

        #URL
        url = self.__url + self.evidence_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        #Give people the option to just input a string.
        if (type(keywords)==str):
            keywords = [keywords]

        result = []
        for i in range(0, len(r)):
            str1 = str(r[i]["content"]).upper()
            for k in keywords:
                str2 = str(k).upper()
                if (str1.find(str2) != -1):
                    result  += [r[i]]
                    break

        return result

    #Get Evidence Info 
    def get_evidence(self, pid: int, node_id: str, evidence_id: str):

        #URL
        url = self.__url + self.evidence_endpoint.replace("<ID>", str(node_id)) + "/" + str(evidence_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        return r


    ####################################
    #         Notes Endpoint           #
    ####################################


    #Get Note List 
    def get_notelist(self, pid: int, node_id: str):

        #URL
        url = self.__url + self.note_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        result = []
        for i in range(0, len(r)):
            result  += [[r[i]["title"], r[i]["id"]]]

        return result

    #Create a note on a project 
    def create_note(self, pid: int, node_id: str, title: str, text: str, tags=[], category=0):
        
        #URL
        url = self.__url + self.note_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        taglines = ""
        if (len(tags) != 0):
            for tag in tags:
                taglines += "#[" + tag + "]#\r\n"

        data = { 'note':{'text':'#[Title]#\r\n' + title + '\r\n\r\n#[Description]#\r\n' + str(text) + "\r\n\r\n" + taglines, "category_id":str(category)}}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "POST", "201", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return r['id']

    #Create a note on a project
    def create_note_raw(self, pid: int, node_id: str, data: str):

        #URL
        url = self.__url + self.note_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = {'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        data = {'note':{'text':data}}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "POST", "201", json.dumps(data))

        #RETURN
        if (r == None):
            return None

        return r['id']

    #Update Note 
    def update_note(self, pid: int, node_id: str, note_id: str, title: str, text: str, tags=[], category=1):

        #URL
        url = self.__url + self.note_endpoint.replace("<ID>", str(node_id)) + "/" + str(note_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        taglines = ""
        if (len(tags) != 0):
            for tag in tags:
                taglines += "#[" + tag + "]#\r\n"

        data = { 'note':{'text':'#[Title]#\r\n' + title + '\r\n\r\n#[Description]#\r\n' + str(text) + "\r\n\r\n" + taglines, "category_id":str(category)}}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "PUT", "200", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return r['id']

    #Update Note
    def update_note_raw(self, pid: int, node_id: str, data):

        #URL
        url = self.__url + self.note_endpoint.replace("<ID>", str(node_id)) + "/" + str(note_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #DATA
        taglines = ""
        if (len(tags) != 0):
            for tag in tags:
                taglines += "#[" + tag + "]#\r\n"

        data = { 'note':{'text':'#[Title]#\r\n' + title + '\r\n\r\n#[Description]#\r\n' + str(text) + "\r\n\r\n" + taglines, "category_id":str(category)}}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "PUT", "200", json.dumps(data))

        #RETURN
        if (r == None):
            return None

        return r['id']

    #Delete Note 
    def delete_note(self, pid: int, node_id: str, note_id: str):

        #URL
        url = self.__url + self.note_endpoint.replace("<ID>", str(node_id)) + "/" + str(note_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "DELETE", "200")

        #RETURN
        if (r == None):
            return None

        return True

    #Find Note 
    def find_note(self, pid: int, node_id: str, keywords: str):
        
        #URL
        url = self.__url + self.note_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        #Give people the option to just input a string.
        if (type(keywords)==str):
            keywords = [keywords]

        result = []
        for i in range(0, len(r)):
            str1 = str(r[i]["text"]).upper()
            for k in keywords:
                str2 = str(k).upper()
                if (str1.find(str2) != -1):
                    result  += [[r[i]["title"], r[i]["id"]]]
                    break


        return result

    #Get Note Info 
    def get_note(self, pid: int, node_id: str, note_id: str):

        #URL
        url = self.__url + self.note_endpoint.replace("<ID>", str(node_id)) + "/" + str(note_id)

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}
        
        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        return r


    ####################################
    #       Attachments Endpoint       #
    ####################################

    #Get Attachments
    def get_attachmentlist(self, pid: int, node_id: str):
        #URL
        url = self.__url + self.attachment_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        #RETURN
        if (r == None):
            return None

        result = []
        for i in range(0, len(r)):
            result  += [[r[i]["filename"], r[i]["link"]]]

        return result

    #Get (Download) Attachment
    def get_attachment(self, pid: int, node_id: str, attachment_name: str, output_file=None):
        #URL
        url = self.__url + self.attachment_endpoint.replace("<ID>", str(node_id)) + "/" + attachment_name

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "GET", "200")

        try:
            download = r["link"]

            response = requests.get(self.__url + download, stream=True, headers=header, verify=self.__verify)
            if (output_file is None):
                output_file = r["filename"]

            with open(output_file, "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
        except:
            return None

        return True

    #Post Attachment
    def post_attachment(self, pid: int, node_id: str, attachment_filename: str):
        #URL
        url = self.__url + self.attachment_endpoint.replace("<ID>", str(node_id))

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid)}

        try:

            #FILES
            files = [('files[]', open(attachment_filename, 'rb'))]
            
            r = requests.post(url, headers=header, files=files, verify=self.__verify)
            if(r.status_code != 201):
                return None
            else:
                r = r.json()
                return [r[0]["filename"], r[0]["link"]]
        except:
            return None

        return True

    #Rename Attachment
    def rename_attachment(self, pid: int, node_id: str, attachment_name: str, new_attachment_name: str):
        #URL
        url = self.__url + self.attachment_endpoint.replace("<ID>", str(node_id)) + "/" + attachment_name

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Content-type': 'application/json', 'Dradis-Project-Id': str(pid)}
        
        #DATA
        data = {"attachment":{"filename":new_attachment_name}}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "PUT", "200", json.dumps(data))
        
        #RETURN
        if (r == None):
            return None

        return [r['filename'], r["link"]]

    #Delete Attachment
    def delete_attachment(self, pid: int, node_id: str, attachment_name: str):
        #URL
        url = self.__url + self.attachment_endpoint.replace("<ID>", str(node_id)) + "/" + attachment_name

        #HEADER
        header = { 'Authorization':'Token token="' + self.__apiToken + '"', 'Dradis-Project-Id': str(pid), 'Content-type': 'application/json'}

        #CONTACT DRADIS
        r = self.contactDradis(url, header, "DELETE", "200")

        #RETURN
        if (r == None):
            return None

        return True
