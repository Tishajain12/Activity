'''Suppose you are buying something online on amazon.com 

On the website, you get
a 15% discount if you are a prime member. Additionally, you are also getting a discount of 8% on 
the item because it's black Friday sales.
Write a function that takes as input the amount of the asset that you are buying and
 a logical variable indicating whether you are a prime member applies the discount offered appropriately and returns the result.'''


asst=int(input('Enter total amount  : '))
fri=(asst*8)/100
prime = input('Are you a prime member:  ')
if prime.lower()=='yes':
    id=int(input('Enter your id : '))
    if (3456000<=id<=3460000):
        discount=(asst*15)/100
        print('amount after 15% discount for prime memeber is',asst-discount)
        print('amount after 8% discount of black friday is',asst-fri)
        print('total amount after both the discount is',asst-discount-fri)
else:
    print('total amount after 8% discount of black friday is',asst-fri)



'''In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.

Write a function that takes as input the,

message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.


If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.'''


def length(msg):
    if len(msg) <= 200:
        return msg
    else:
        return msg[:200]
print(msg_length(''))
def msg_word_count(msg):
    words = msg.split()
    if len(words) <= 30:
        return msg
    else:
        return "Message should not contain more than 30 words."