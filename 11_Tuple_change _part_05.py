fruits=("apple","banana","mango","orange","grape")
temp=list(fruits)
temp[0]='watermelon'
fruits=tuple(temp)
print(fruits)