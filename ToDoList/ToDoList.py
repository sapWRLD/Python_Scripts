from time import gmtime, strftime, time
import tags
current_Tasks = [[],[],[]] # [HIGH, MEDIUM, LOW]
priorities = {"HIGH": {"index": 0, "label": "High"},
                "MEDIUM": {"index": 1, "label": "Medium"},
                "LOW": {"index": 2, "label": "Low"}
            }
def add_Task():
    global current_Tasks
    print("Add task called!")
    
    while True:
        task = input("Please enter the task you want to add (type (HIGH, MEDIUM, LOW) to set the priority of the task). Press q to quit :")
        s = strftime("%a, %d %b %Y %H:%M:%S", 
             gmtime(time()))
        if task.lower() == "q":
            break

        priority = next((p for p in priorities if p in task), None)
        if not priority:
            print("Task must include a priority! (HIGH, MEDIUM, LOW)")
            continue
        
        raw_task = task.replace(priority, "").strip()
        if not raw_task:
            print("Task cannot be empty!")
            continue

        print("Please select an apllicable tag for the task:")
        for i, tag in enumerate(tags.task_tags["Context/Category"], start=1):
             print(f"{i}. {tag}")

        try:
            choice = int(input("Enter the number of the tag you want to apply: "))
            tag_selected = tags.task_tags["Context/Category"][choice - 1]

            task_content = f"[{tag_selected}] {raw_task}"
            current_Tasks[priorities[priority]["index"]].append(f"{task_content} | {s}")
            print(f"Added to {priorities[priority]['label']} priority")
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
        if priority not in priorities:
            print("Invalid selection! (HIGH, MEDIUM,LOW)")
            continue

        idx = priorities[priority]["index"]
        label = priorities[priority]["label"]
        
        print(f"{label} priority tasks")
        for i, task in enumerate(current_Tasks[idx], start=1):
            print(f"{i}- {task}")
        if not current_Tasks[idx]:
            print(f"No tasks in {label} priority!")
            continue
        try:
            choice = int(input("Enter the number of the task you want to remove: "))
            removed_task = current_Tasks[idx].pop(choice - 1)
            print(f"The task '{removed_task}' has been deleted")
        except (ValueError, IndexError):
            print("Invalid selection!")

def show_Task():
    global current_Tasks
    print("Main menu called!")
    for key, details in priorities.items():
        idx = details["index"]
        label = details["label"]
        print(f"{label} priority tasks:")
        if not current_Tasks[idx]:
            print(" - No tasks")
        else:
            for task in current_Tasks[idx]:
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
            show_Task()
        elif choice == "4":
            print("Thanks for using my Todo app!")
            break
        else:
            print("Invalid option, try again.")
def main():
    ui()

if __name__ == "__main__":
    main()
