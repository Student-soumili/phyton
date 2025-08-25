p1 ="make a lot of money"
p2 ="buy now"
p3 ="subscribe"
p4="click this"

message = input("enter your comment:")
if((p1 in  message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("The comment is spam")
else:
    print("The comment is not spam")