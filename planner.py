def check_marks(marks):
    if marks>=90:
        print("excellent!")
        return 1,"excellent" 
    elif marks>=75:
        print("good job:")
        return 1,"good job"
    else:
        print("keep going:")
        return 1,"keep going"
def check_priority_task():
    if priority == "high":
        print("priority: high")
    elif priority == "medium":
        print("priority: medium")
    else:
        print("priority: low")
grades=[]#list of dictionaries
good_job_count = 0
total_marks= 0
times=int(input("how many subject?;"))
for i in range(times):
    subject=input("enter your subject:")
    marks=int(input("enter your marks:"))
    #check marks and get comment
    result , comment = check_marks(marks)
    good_job_count+=result
    total_marks+=marks
grades.append({
    "subjects": subject,
    "marks": marks,
    "comment": comment,
    })
#loop to all entry subject,marks,comment
print("\n---report---")
for entry in grades:
    print(entry["subjects"],"-",entry["marks"],"-",entry["comment"])
#calculate overall percentage
overall_percentage=total_marks / times
print("n/Total marks:",total_marks)
print("Overall percentage:",overall_percentage)
if overall_percentage>=90:
    print("Excellent!")
elif overall_percentage>=70:
    print("Good Job!")
else:
    print("Keep going!")
print("No. of subjects with Good Job/Excellent:",good_job_count)
# ----------------------------
# Full Planner App
# ----------------------------

# Single global list for tasks
task = []

# Start menu loop
while True:
    print("\n1. Add task")
    print("2. View Planner")
    print("3. Calendar View")
    print("4. Exit")
    print("5. Edit Task")
    print("6. Delete Task")

    choice = input("Choose an option: ").strip()  # remove extra spaces

    # ------------------------
    # Add Task
    # ------------------------
    if choice == "1":
       if choice == "1":
           n = int(input("How many tasks do you want to add? "))
       for i in range(n):
           print(f"\nTask {i+1}:")
           task_name = input("Enter task name: ").strip()
           day = input("Enter day: ").strip()
           priority = input("Enter priority (high/medium/low): ").strip().lower()

           task.append({
            "task": task_name,
            "day": day,
            "priority": priority
        })

       print(f"\n{n} task(s) added successfully!")

    # ------------------------
    elif choice == "2":
        print("\n--- Your Planner ---")
        if len(task) == 0:
            print("No tasks yet")
        else:
            for t in task:
                print(f"{t['day']} - {t['task']} ({t['priority']})")

    # ------------------------
    # Calendar View (sorted by priority)
    # ------------------------
    elif choice == "3":
        if len(task) == 0:
            print("No tasks yet")
        else:
            # Create calendar dictionary
            calendar = {}
            for t in task:
                day = t["day"]
                if day not in calendar:
                    calendar[day] = []
                calendar[day].append(t)

            # Define priority order manually
            priority_order = ["high", "medium", "low"]

            print("\n--- Calendar View (sorted by priority) ---")
            for day, tasks_in_day in calendar.items():
                print("\n" + day.upper() + ":")  # day in uppercase

                # Print tasks in priority order
                for pr in priority_order:
                    for t in tasks_in_day:
                        if t["priority"] == pr:
                            print("- " + t["task"] + " (" + t["priority"] + ")")

    # ------------------------
    # Exit
    # ------------------------
    elif choice == "4":
        print("Exiting planner. Goodbye!")
        break
    elif choice == "5": 
        if len(task) == 0:
            print("No tasks to edit!")
        else:
            print("\n--- Your Tasks ---")
        for i in range(len(task)):
            t = task[i]
            print(str(i+1) + ". " + t["day"] + " - " + t["task"] + " (" + t["priority"] + ")")

        task_num = int(input("Enter the task number you want to edit: "))

        if task_num >= 1 and task_num <= len(task):
            t = task[task_num - 1]
            print("Editing Task: " + t["task"] + " (" + t["day"] + " - " + t["priority"] + ")")

            # Ask for new values
            new_task = input("Enter new task name (leave blank to keep old): ").strip()
            new_day = input("Enter new day (leave blank to keep old): ").strip()
            new_priority = input("Enter new priority (high/medium/low, leave blank to keep old): ").strip().lower()

            if new_task != "":
                t["task"] = new_task
            if new_day != "":
                t["day"] = new_day
            if new_priority != "":
                t["priority"] = new_priority

            print("Task updated successfully!")
        else:
            print("Invalid task number!")
    elif choice == "6": 
        if len(task) == 0:
            print("No tasks to delete!")
    else:
        # Show all tasks with numbers
        print("\n--- Your Tasks ---")
        for i in range(len(task)):
            t = task[i]
            print(str(i+1) + ". " + t["day"] + " - " + t["task"] + " (" + t["priority"] + ")")

        task_num = int(input("Enter the task number you want to delete: "))

        if task_num >= 1 and task_num <= len(task):
            deleted_task = task.pop(task_num - 1)
            print("Deleted task: " + deleted_task["task"] + " (" + deleted_task["day"] + " - " + deleted_task["priority"] + ")")
        else:
            print("Invalid task number!")


