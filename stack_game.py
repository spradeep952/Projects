import time
# class for implementing the stack
class Stack:
    def __init__(self):
        self.stack = []
        self.len = 100
      
    # method for checking if the stack is empty
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False 
      
    # method for setting the height of stack
    def setDepth(self, height):
        self.len = height
        
    # method for pushing an element in to stack
    def push(self, element):
        if  not(len(self.stack) == self.len):
            self.stack.append(element)
            return self.stack
        else:
            return "Stack is full."
        
    # method for popping out an element from stack 
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return "Stack is already empty"
    
    # method for displaying the stack
    def display(self):
        if not self.isEmpty():
            return self.stack
        else:
            return "The stack is empty."

# function to get the element of stacks
def getElement():
    n = True
    while n:
        try:
            n = int(input("\nEnter the number to push : "))
            return n
        except Exception as e:
            print("Please enter a valid number.")
            continue
    
# function to get the length of stacks   
def getLength():
    l = True
    while l:
        try:
            l = int(input("\nEnter the height of stack : "))
            return l
        except Exception as e:
            print("Please enter a valid number.")
            continue
            
# setting up the Stack Game intterface

print("********** Welcome to Stack Game **********")
res = 1
myStack = Stack()
while res != 6:
    print("Select your choice : ")
    try:
        # displaying all the choices here
        res = int(input("\t1. Set length of stack \n\t2. Push element in stack\n\t3. Pop element from stack\n\t4. Check is stack empty?\n\t5. Display the stack \n\t6. Exit\n"))
    except Exception as e:
        print('Please select a valid operation.')
        continue        
    # choice 1
    if res == 1: 
        myStack.setDepth(getLength())
    # choice 2
    if res == 2:
        print(myStack.push(getElement()))
    # choice 3
    if res == 3:
        if not(myStack.isEmpty()):
            print("The element popped out of stack is : ", myStack.pop())
        else: 
            print('Stack is already empty.')
    # choice 4
    if res == 4:
        if myStack.isEmpty():
            print('Stack is empty.')
        else:
            print('Stack is not empty.')
    # choice 5
    if res == 5:
        if not(myStack.isEmpty()):
            print("The current stack is :", myStack.display())
        else:
            print('Stack is empty. Nothing to display')
print("******** Thank you for playing with us! ********")
# game interface ends here

time.sleep(20)
