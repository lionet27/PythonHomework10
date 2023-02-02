
def dataList(dataStr):
    data=[]
    digit=''
    for i in range(len(dataStr)):
        if dataStr[i].isdigit():
            digit+=dataStr[i]
            if i==len(dataStr)-1:
                data.append(digit)
        elif dataStr[i]=='.':
            digit+=dataStr[i]
        elif dataStr[i]=='-':
            if i==0:
                digit+=dataStr[i]
            elif dataStr[i-1]=='-' or dataStr[i-1]=='+' or dataStr[i-1]=='*' or dataStr[i-1]=='/':
                digit+=dataStr[i]
            else:
                if digit!='':
                    data.append(digit)
                    digit=''
                data.append(dataStr[i])
        else:
            if digit!='':
                data.append(digit)
                digit=''
            data.append(dataStr[i])
    return data

def MultDel(data):
    newdata=[]
    for i in range(len(data)-1):
        if data[i+1]=='*':
            if i<len(data)-3 and (data[i+3]=='*' or data[i+3]=='/'):
                data[i+2]=float(data[i])*float(data[i+2])
                data[i]=0
                data[i+1]=0
                
            else:    
                data[i]=float(data[i])*float(data[i+2])
                data[i+1]=0
                data[i+2]=0
                newdata.append(data[i])
            
        
        elif  data[i+1]=='/':
            if i<len(data)-3 and (data[i+3]=='*' or data[i+3]=='/'):
                data[i+2]=float(data[i])/float(data[i+2])
                data[i]=0
                data[i+1]=0
                
            else: 
                data[i]=float(data[i])/float(data[i+2])
                data[i+1]=0
                data[i+2]=0
                newdata.append(data[i])
            
        else:
            if data[i]!=0:
                newdata.append(data[i])

    if data[-1]!=0:
        newdata.append(data[-1])
    return newdata

def plusMinus(newdata):
    result=float(newdata[0])

    for i in range(1,len(newdata)):
        if newdata[i]=='+':
            result+=float(newdata[i+1])
            
        elif newdata[i]=='-':
            result-=float(newdata[i+1])
    return result

def countParentheses(expression):
    skobki=[]

    for i in range(len(expression)):
        if expression[i]=='(' or expression[i]==')':
            skobki.append(i)

    
    withoutParentheses=expression[:skobki[0]]
    
    for i in range(0,len(skobki),2):
        if skobki[i+1]-skobki[i]<4:
            withoutParentheses+=expression[(skobki[i]+1):skobki[i+1]]
            if i<len(skobki)-2:
                withoutParentheses+=expression[(skobki[i+1]+1):skobki[i+2]]
            else:
                withoutParentheses+=expression[(skobki[i+1]+1):]    

        else:
            data=dataList(expression[(skobki[i]+1):skobki[i+1]])
            newdata=MultDel(data)
            result=plusMinus(newdata)
            withoutParentheses+=str(result)
            if i<len(skobki)-2:
                withoutParentheses+=expression[(skobki[i+1]+1):skobki[i+2]]
            else:
                withoutParentheses+=expression[(skobki[i+1]+1):]
    return withoutParentheses


