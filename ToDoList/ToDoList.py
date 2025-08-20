from time import gmtime, strftime, time
import tags
current_Tasks = [[],[],[]] # [HIGH, MEDIUM, LOW]

def add_Task():
    global current_Tasks
    print("Add task called!")

    while True:
        task = input("Please enter the task you want to add (type (HIGH, MEDIUM, LOW) to set the priorety of the task). Press q to quit :")
        s = strftime("%a, %d %b %Y %H:%M:%S", 
             gmtime(time()))
        if task.lower() == "q":
            break
        elif "HIGH" in task:
            raw_task = task.replace("HIGH", "").strip()
            if not raw_task:
                print("Task cannot be empty!")
                continue

            print("Please select an apllicable tag for the task:")
            for i, tag in enumerate(tags.task_tags["Context/Category"], start=1):
                print(f"{i}. {tag}")

            try:
                choice = int(input("Enter the number of the tag you want to apply: "))
                tag_selected = tags.task_tags["Context/Category"][choice - 1]
                raw_task = task.replace("HIGH", "").strip()
                task_content = f"[{tag_selected}] {raw_task}"
                current_Tasks[0].append(f"{task_content} | {s}")
                print("Added to High prior")
            except (ValueError, IndexError):
                print("Invalid selection, please try again.")
                continue    

        elif "MEDIUM" in task:
            raw_task = task.replace("MEDIUM", "").strip()
            if not raw_task:
                print("Task cannot be empty!")
                continue

            print("Please select an apllicable tag for the task:")
            for i, tag in enumerate(tags.task_tags["Context/Category"], start=1):
                print(f"{i}. {tag}")

            try:
                choice = int(input("Enter the number of the tag you want to apply: "))
                tag_selected = tags.task_tags["Context/Category"][choice - 1]
                raw_task = task.replace("MEDIUM", "").strip()
                task_content = f"[{tag_selected}] {raw_task}"
                current_Tasks[1].append(f"{task_content} | {s}")
                print("Added to MEDIUM prior")
            except (ValueError, IndexError):
                print("Invalid selection, please try again.")
                continue

        elif "LOW" in task:
            raw_task = task.replace("LOW", "").strip()
            if not raw_task:
                print("Task cannot be empty!")
                continue

            print("Please select an apllicable tag for the task:")
            for i, tag in enumerate(tags.task_tags["Context/Category"], start=1):
                print(f"{i}. {tag}")

            try:
                choice = int(input("Enter the number of the tag you want to apply: "))
                tag_selected = tags.task_tags["Context/Category"][choice - 1]
                raw_task = task.replace("LOW", "").strip()
                task_content = f"[{tag_selected}] {raw_task}"
                current_Tasks[2].append(f"{task_content} | {s}")
                print("Added to LOW prior")
            except (ValueError, IndexError):
                print("Invalid selection, please try again.")
                continue
    
        

def remove_Task():
    global current_Tasks
    print("Remove task called!")
    while True:
        priority = input("Pleas enter the priority of the fini shed task (HIGH, MEDIUM, LOW). q To cancel: ").upper()
        if priority.lower() == "q":
            break
        elif "HIGH" in priority:
            print("HIGH priority tasks:")
            for i, task in enumerate(current_Tasks[0], start=1):
                print(f"{i}- {task}")
            try:
                choice = int(input("Enter the number of the task you want to remove: "))
                removed_task = current_Tasks[0].pop(choice - 1)
                print(f"The task '{removed_task}' has been deleted")
            except (ValueError, IndexError):
                print("Invalid selection!")
                    

        elif "MEDIUM" in priority:
            print("MEDIUM priority tasks:")
            for i, task in enumerate(current_Tasks[1], start=1):
                print(f"{i}- {task}")
            try:
                choice = int(input("Enter the number of the task you want to remove: "))
                removed_task = current_Tasks[1].pop(choice - 1)
                print(f"The task '{removed_task}' has been deleted")
            except (ValueError, IndexError):
                print("Invalid selection!")

        elif "LOW" in priority:
            print("LOW priority tasks:")
            for i, task in enumerate(current_Tasks[2], start=1):
                print(f"{i}- {task}")
            try:
                choice = int(input("Enter the number of the task you want to remove: "))
                removed_task = current_Tasks[2].pop(choice - 1)
                print(f"The task '{removed_task}' has been deleted")
            except (ValueError, IndexError):
                print("Invalid selection!")
        else:
            print("Invalid please add (HIGH, MEDIUM OR LOW).")

def Show_Task():
    global current_Tasks
    print("Main menu called!")
    priorities = ["HIGH", "MEDIUM", "LOW"]
    for i, task_list in enumerate(current_Tasks):
        print(f"{priorities[i]} priority tasks:")
        if not task_list:
            print(" - No tasks")
        else:    
            for task in task_list:
                print(f" - {task}")
     

def ui():
    while True:
        print(f"""
{"*"*30}
 Welcome to my Todo app!
{"*"*30}
1. Add task
2. Remove task
3. Show tasks
4. Quit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            add_Task()
        elif choice == "2":
            remove_Task()
        elif choice == "3":
            Show_Task()
        elif choice == "4":
            print("Thanks for using my Todo app!")
            break
        else:
            print("Invalid option, try again.")
def main():
    ui()

if __name__ == "__main__":
    main()
