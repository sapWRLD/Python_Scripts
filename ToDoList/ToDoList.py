from pynput import keyboard
current_Tasks = [[],[],[]]

def add_Task():
    global current_Tasks
    print("Add task called!")
    while True:
        task = input("Please enter the task you want to add (type (HIGH, MEDIUM, LOW) to set the priorety of the task). Press q to quit :")
        if task.lower() == "q":
            break
        elif "HIGH" in task:
            current_Tasks[0].append(task)
            print("Added to High prior")

        elif "MEDIUM" in task:
            current_Tasks[1].append(task)
            print("Added to Medium prior")

        elif "LOW" in task:
            current_Tasks[2].append(task)
            print("Added to Low prior")
        else:
            print("Invalid please add (HIGH, MEDIUM OR LOW).")
    
        

def remove_Task():
    print("Remove task called!")

def Show_Task():
    global current_Tasks
    print("Main menu called!")
    priorities = ["HIGH", "MEDIUM", "LOW"]
    for i, task_list in enumerate(current_Tasks):
        print(f"{priorities[i]} priority tasks:")
        for task in task_list:
            print(f" - {task}")

def on_press(key):
    try:
        if key == keyboard.Key.f1:
            add_Task()
        elif key == keyboard.Key.f2:
            remove_Task()
        elif key == keyboard.Key.f3:
            Show_Task()
        elif key == keyboard.Key.esc:
            print("Thanks for using my Todo app!")
            return False  # stops the listener
    except:
        pass

def ui():
    print(f"""{"*"*30}
 Welcome to my Todo app!
{"*"*30}

Please select any of the following options:

1. Add task (F1)
2. Remove task (F2)
3. Show main menu (F3)
4. Quit (Esc)
""")
    # Blocking call; listener stops when on_press returns False
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def main():
    ui()

if __name__ == "__main__":
    main()
