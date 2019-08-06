number_to_string={0:'không',1:'một',2:'hai',3:'ba',4:'bốn',5:'năm',6:'sáu',7:'bảy',8:'tám',9:'chín'}
num_excep_to_string={0:'',1:'mốt',2:'hai',3:'ba',4:'bốn',5:'lăm',6:'sáu',7:'bảy',8:'tám',9:'chín'}
digits=['tỷ','triệu','nghìn','.']
#Hàm đếm số chữ số
#Input:Integer
#Output:Integer
def Local_length(num):
    string=str(num)
    count=len(string)
    return count

#Hàm đọc chữ số hàng đơn vị
#Input: Integer
#Output: string
def Ones(num):
    result=[]
    result.append(number_to_string[num])
    return result

#Hàm đọc chữ số hàng chục
#Input:Interger
#Output:List
def Dezons(num):
    result=[]
    if (num//10!=1):
        result+=(Ones(num//10))
        result.append('mươi')
        if(num%10==0):
            return result
        else:
            result.append(num_excep_to_string[num%10])
    else:
        result.append('mười')
        if (num%10==1):
            result.append('một')
        else:
            if(num%10==0):
                return result
            else:
                result.append(num_excep_to_string[num%10])
    return result
#Hàm đọc chữ số hàng trăm
#Input: Interger
#Output: List
def Hunreds(num):
    result=[]
    result.append(number_to_string[num//100])
    result.append('trăm')
    if((num%100)//10!=0):
        result+=(Dezons(num%100))
    else:
        if ((num%100)%10==0):
            return result
        else:
            result.append('lẻ')
            result+=(Ones(num%10))
    return result
#Ham
def Read_Number(count,num):
    result=[]
    if (count==1):
        return Ones(num)
    elif count==2:
        return Dezons(num)
    elif count==3:
        return Hunreds(num)
    else:
        raise TypeError
#Hàm đọc số bất kỳ
#Input:Interger
#Output:List
def integer_to_vietnamese_numeral(num):
    if num==0:
        return Ones(num)    
    divisor=10**9
    result=[]
    i=0
    while num!=0:
        if(num//divisor!=0):
            count=Local_length(num//divisor)
            if len(result)!=0:
                if count==2:
                    result.append('không')
                    result.append('trăm')
                if count==1:
                    result.append('không')
                    result.append('trăm')
                    result.append('linh')
            result+=Read_Number(count,num//divisor)
            result.append(digits[i])
            num%=divisor
            divisor//=1000
            i+=1
        else:
            i+=1
            divisor//=1000 
    if result[len(result)-1] =='.':
        del result[len(result)-1]
    return result
num=input()
n=int(num)
print(integer_to_vietnamese_numeral(n))