from firebase import firebase
import datetime
import json

firebase = firebase.FirebaseApplication('https://dappathon-b1230.firebaseio.com', None)
id = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# userGet
def getUsers():
    results = firebase.get('/users',None)
    array = []
    for i in results:
        array.append(results[i])
    return array
#userAdd
def addUser(idcard, name, email, phone, address, privateKey):
    results = firebase.put('/users', idcard, {'name': name, 'email': email, 'phone': phone, 'address': address, 'privateKey': privateKey})
    return results
# result = firebase.put('/users', id, {'name':'Viet','email':'ptv.uit1995@gmail.com', 'phone':'0987966864','address':'address'})

# questionAdd
# result = firebase.put('/questions', id, {'number':'5','content':'Which sentence is correct?','answer':{'A':'Please to sit down Mrs Smith.','B':'Sitting down please Mrs Brown.','C':'Sit not down please Mrs White.','D':'Please don’t sit down Mr Black.'},'result':'D'})
# questionGet
def getQuestions():
    results = firebase.get('/questions', None)
    array = []
    for i in results:
        array.append(results[i])
    return array


# resultsAdd
def addResult(date, point, userId, content):
    result = firebase.put('/results', date, {'date':date, 'point':point, 'userId':userId, 'content':content})
    return result
# resultGet
def getResults():
    results = firebase.get('/results', None)
    array = []
    for i in results:
        array.append(results[i])
    return array


# results = firebase.put('/users', '301546317', {'name': 'Viet Phan', 'email': 'ptv.uit1995@gmail.com', 'phone': '0987966864', 'address': 'Binh Tan', 'privateKey': 'privateKey'})
# print(result)