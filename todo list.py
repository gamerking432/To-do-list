import time
import winsound

def task():
    task_var = [] #empty list

# now we will greet the user then after we wll ask for task
    print("Hello, Welcome to the To-do-list")
    num_of_task = int(input("Enter the number of task you want to add: "))    
# we making for loop if user give input 5 then it will repeat 5 times and ask for task
    
        

    for i in range(1,num_of_task+1):
        
        task_name = input(f"Enter your task for today {i}: ")
        task_var.append(task_name)
        print(f"Here is your task for today: {i} {task_var} ")
        
    while True:
        operation = input("1-add\n2-update\n3-delete\n4-view\n5-exit :")
        
        if operation == '1':

            add = input("Add your task: ")
            task_var.append(add)
            print(f"Your task {add} has been added to your ")

        elif operation == '2':
            updated_var = input("Enter the task name you want to update: ")
            if updated_var in task_var:
                up = input("Enter your new task: ")
                ind = task_var.index(updated_var)
                task_var[ind] = up
                print(f"your task has been updated{updated_var} ")
            

        elif operation == '3':
            delete_var = input("Enter your task you want to remove: ")
            if delete_var in task_var:
                task_var.remove(delete_var)
                print(f"your task has been remove {delete_var}")
                print(task_var)
                
        elif operation == '4':
            print(task_var)

        elif operation == '5':
            print(f"This is your task for today\n{task_var}")
            break

        else:
            print("Invalid input")

    
        

                        

                

        

task() 
