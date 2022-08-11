from cmath import sqrt
import json
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('list', type=list)

#GET() POST() sumofsquares
@app.route('/sumofsquares', methods = ['POST', 'GET'])
def get():
        print("Start...") #terminal tracing
        parserArgs = parser.parse_args()
        print(request.data) #terminal tracing
        
        #pass request data to a list
        data_dict = json.loads(request.data)
        lstInputNumbers = data_dict['data']
        
        #validate input
        if len(lstInputNumbers) < 3:
                print("Error: List does not contain 3 numbers") #terminal tracing
                return json.dumps("Error: List must contain at least 3 numbers.") 
        
        bAllNumber = all([isinstance(item, int) for item in lstInputNumbers])
        if bAllNumber == False:
                print("Error: List does not contain numbers") #terminal tracing
                return json.dumps("Error: List must contain only numbers.") 

        
        
        #use lambda to get the highest 3 numbers
        lstFindsHighestThreeNumbers = lambda listNum : sorted(listNum, reverse=True)[:3]
        print(lstFindsHighestThreeNumbers(lstInputNumbers)) #terminal tracing
        
        #use lambda to square each  item of a list of numbers
        lstSquared = list(map(lambda x: x**2, lstFindsHighestThreeNumbers(lstInputNumbers)))
        print(lstSquared)#terminal tracing
        
        #Finally, use lambda to sum all items of the list
        funcSummOfSquares = lambda lstNums : sqrt(sum(lstNums)).real
        
        #Get and format the response
        numSummOfSquares = funcSummOfSquares(lstSquared)
        numSummOfSquares = round(numSummOfSquares,2)
        print(numSummOfSquares)#terminal tracing
        dictResponse = {"output" : numSummOfSquares }
        
        print(dictResponse)#terminal tracing
        print("Finish.") #terminal tracing
        
        #return response as json
        return json.dumps(dictResponse) 


@app.route('/')
def index():
        return 'Main Page. Try ../sumofsquares/from POSTMAN or other API tester tool.'

if __name__ == '__main__':
   app.run()
