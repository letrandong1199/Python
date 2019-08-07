# number_to_string = {0: 'không', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bốn', 5: 'năm', 6: 'sáu', 7: 'bảy', 8: 'tám',9: 'chín'}
# num_excep_to_string = {0: '', 1: 'mốt', 2: 'hai', 3: 'ba', 4: 'bốn', 5: 'lăm', 6: 'sáu', 7: 'bảy', 8: 'tám', 9: 'chín'}
# digits = ['tỷ', 'triệu', 'nghìn', '.']
#
#
# Hàm đếm số chữ số
# Input:Integer
# Output:Integer
def Local_length(num):
    string = str(num)
    count = len(string)
    return count

#
# # Hàm đọc chữ số hàng đơn vị
# # Input: Integer
# # Output: string
# def Ones(num):
#     result = []
#     result.append(number_to_string[num])
#     return result
#
#
# # Hàm đọc chữ số hàng chục
# # Input:Interger
# # Output:List
# def Dezons(num):
#     result = []
#     if (num // 10 != 1):
#         result += (Ones(num // 10))
#         result.append('mươi')
#         if (num % 10 == 0):
#             return result
#         else:
#             result.append(num_excep_to_string[num % 10])
#     else:
#         result.append('mười')
#         if (num % 10 == 1):
#             result.append('một')
#         else:
#             if (num % 10 == 0):
#                 return result
#             else:
#                 result.append(num_excep_to_string[num % 10])
#     return result
#
#
# # Hàm đọc chữ số hàng trăm
# # Input: Interger
# # Output: List
# def Hunreds(num):
#     result = []
#     result.append(number_to_string[num // 100])
#     result.append('trăm')
#     if ((num % 100) // 10 != 0):
#         result += (Dezons(num % 100))
#     else:
#         if ((num % 100) % 10 == 0):
#             return result
#         else:
#             result.append('linh')
#             result += (Ones(num % 10))
#     return result
#
#
# # Hàm chuyển đổi chuỗi thành list
# # Input: String
# # Output: List
# def convert_string_to_list(string):
#     list_result=list(string.split(" "))
#     return list_result
#
#
# # Hàm đọc theo số chữ số
# # Input: Count number và Number
# # Output: List
# def Read_Number(count, num):
#     result = []
#     if (count == 1):
#         return Ones(num)
#     elif count == 2:
#         return Dezons(num)
#     elif count == 3:
#         return Hunreds(num)
#
#
# # Hàm xử lý âm thanh
# # Input: List
# # Output: Âm thanh# # Hàm đếm số chữ số
# # Input:Integer
# # Output:Integer
# def Local_length(num):
#     string = str(num)
#     count = len(string)
#     return count
#
# def sounds_numerals(list_result):
#     import pygame
#     pygame.init()
#     address=[]
#     path='./vie/north/'
#     for i in list_result:
#          address.append(path+i+'.mp3')
#     print(address)
#     for i in address:
#           pygame.mixer.music.load(i)
#           pygame.mixer.music.play(0)
#           pygame.time.delay(550)
#           print(i)
#
#     # for i in list_result:
#     #     pygame.mixer.music.load('{}{}.ogg'.format(path,i))
#     #     pygame.mixer.music.play(0)
#     #     pygame.time.delay(650)
#
#
# # Hàm sử lý theo yêu cầu đề bài
# # Input: Interger
# # Output: List
# def integer_to_vietnamese_numeral(num,region='north',activate_tts=False):
#     if isinstance(region,str)==False:
#         raise TypeError('Argument "region" is not string')
#     if (region)!=('south') and (region)!=('north'):
#         raise ValueError('Argument"region" has not a correct value')
#     if (type(num) != int):
#         raise TypeError('Not an integer')
#     if num>999999999999:
#         raise OverflowError('Integer greater than 999,999,999,999')
#     if num<0:
#         raise ValueError('Not a positive integer')
#     if num == 0:
#         result=Ones(num)
#         if activate_tts==True:
#             sounds_numerals(result)
#         return  " ".join(i for i in result)
#
#     divisor = 10 ** 9
#     result = []
#     i = 0
#     while num != 0:
#         if (num // divisor != 0):
#             count = Local_length(num // divisor)
#             if len(result) != 0:
#                 if count == 2:
#                     result.append('không')
#                     result.append('trăm')
#                 if count == 1:
#                     result.append('không')
#                     result.append('trăm')
#                     result.append('linh')
#             result += Read_Number(count, num // divisor)
#             result.append(digits[i])
#             num %= divisor
#             divisor //= 1000
#             i += 1
#         else:
#             i += 1
#             divisor //= 1000
#     if result[len(result) - 1] == '.':
#         del result[len(result) - 1]
#     result_string=" ".join(i for i in result)
#
# # Xử lý chuỗi theo vùng miền
#     for i in result:
#         if region=='south':
#             result_string=result_string.replace('nghìn','ngàn')
#             result_string=result_string.replace('linh','lẻ')
#         result_string
#
# # Xử lý activate_tts
#     if type(activate_tts)!=bool:
#         raise TypeError ('Agument "activate_tts" not boolean')
#     else:
#         list_result=convert_string_to_list(result_string)
#         if activate_tts==True:
#             sounds_numerals(list_result)
#         else:
#             return result_string

#print(integer_to_vietnamese_numeral(10251,'north',activate_tts=True))
#######################################################################################
number_to_string_eng = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',9: 'nine'}
num_excep_to_string_eng = {
    10:'ten',11:'eleven',12:'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16:'sixteen',17:'seventeen',18:'eighteen',
    19:'nineteen',20:'twenty', 30: 'thirty',
    40: 'forty', 50:'fifty',60:'sixty',
    70:'seventy',80:'eighty',90:'ninety'
}
digits_eng = ['billion', 'million', 'thousand', 'hunreds']
# Hàm đọc số bằng tiếng anh
def Ones_eng(num):
    result = []
    result.append(number_to_string_eng[num])
    return result


def Dezons_ens(num):
    result = []
    if Local_length(num)<2:
        result+=Ones_eng(num)

    elif (num % 10 != 0) and (num//10>1):
        result.append(num_excep_to_string_eng[(num // 10) * 10])
        result.append('-')
        result.append(number_to_string_eng[num%10])
    else:
        result.append(num_excep_to_string_eng[num])
    return result

def Hunreds(num):
    result=[]
    result.append(number_to_string_eng[num//100])
    result.append('hundred')
    if (num%100!=0):
        result.append('and')
        result += Dezons_ens(num % 100)
    return result
print(Hunreds(201))


