def lunh_alg(card_number):
    sum=0
    reversed_num=card_number[::-1]
    for i in range(0,len(reversed_num),2):
        digit = int(reversed_num[i])
        sum+=digit*2

    return sum%2==0
    
def card_type(card_number):
    if card_number.startswith(('34','37')) and len(card_number)==15:
     return "American Express"    
    elif card_number.startswith(('51','52','53','54','55')) and len(card_number)==16:
     return "American Express" 
    elif card_number.startswith(('4')) and len(card_number)in(13,16):
     return "Visa"
    else:
     return "Invalid" 
    

def main():
      card_number=input("Enter Credit Card number:")

      if not card_number.isdigit():
       print("Invalid Credit Card number")
       return
      
      if lunh_alg(card_number):
        card_name=card_type(card_number)
        print(card_name)

      else:
        print("Invalid Credit Card number") 



if __name__=="__main__"  : 
      main()   