
# 1. Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# 2. Match-case based on priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority. Please double-check."

# 3. Add time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
elif priority == "low":
    message += ". Consider completing it when you have free time."

# 4.  DIRECT print() starts with "Reminder:"
print(f"Reminder: {message}")

