from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status




@api_view(['POST'])
def post_data(request):
    header = {"Access-Control-Allow-Origin":"*"}
    if request.method == 'POST':
        KEYWORDS = ['add','subtract','multiply','addition','subtraction','multiplication','product','sum']
        #get the data sent in the post request 
        data = request.data
        operation_type = data['operation_type']
        operation_type_list = operation_type.split()
        
        _x = data['x']
        _y = data['y']

        x = int(_x)
        y = int(_y)

        result = int
        

        if type(x) is not int or type(y) is not int:
            result = {'error':'x and y must be integers only'}
            return Response(result, status=status.HTTP_400_BAD_REQUEST, headers=header)

        if operation_type == '' or x == '' or y == '':
            result = {'error': 'missing field'}
            return Response(result,status=status.HTTP_400_BAD_REQUEST, headers=header)

        if len(operation_type_list) == 1:
    
            if operation_type == 'addition':
                result = x + y
            

            elif operation_type == 'subtraction':
                result = x - y
                

            elif operation_type == 'multiplication':

                result = x * y
            
            else:
                return Response({'error':'invalid operation type'}, status=status.HTTP_400_BAD_REQUEST, headers=header)

            final_response = { 'slackUsername': 'emperordivo', 'operation_type': operation_type, 'result': result }

            return Response(final_response, status=status.HTTP_200_OK, headers=header)

        else:
            if any((match:=item) in operation_type_list for item in KEYWORDS):
                operation = match

                if operation == 'add' or operation == 'addition' or operation == 'sum':
                    result = x + y
                    operation = 'addition'
                elif operation ==  'subtract' or operation == 'subtraction' :
                    result = x - y
                    operation = 'subtraction'

                elif operation ==  'multiplication' or operation == 'multiply' or operation == 'product':
                    result = x * y
                    operation = 'multiplication'
                
                else:
                    return Response({'error':'invalid operation type'}, status=status.HTTP_400_BAD_REQUEST, headers=header)

            another_response = { "slackUsername": 'emperordivo', 'operation_type':operation , 'result':result}
            return Response( another_response, status=status.HTTP_200_OK, headers = header)


    

    

