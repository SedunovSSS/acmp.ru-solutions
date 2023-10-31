z = int(input())

string_ = ''
pred_str = ''

i = 0

while len(string_) < z:
    pred_str += str(i+1)
    string_ += pred_str
    i+=1

print(string_[z-1])