students = []

while True:
    name = input("Enter student name (type 'list' to show results): ").lower()
    
    if name == "list":
        break
    
    score = int(input("Enter student score: "))

    if score >= 18:
        status = "Excellent"
    elif score >= 15:
        status = "Good"
    elif score >= 10:
        status = "Needs Improvement"
    else:
        status = "Failed"

    students.append({
        "name": name,
        "score": score,
        "status": status
    })

print("\nStudent Results:\n")
for s in students:
    print(f"{s['name']} | Score: {s['score']} | Status: {s['status']}")
