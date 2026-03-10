workers = []

# Generate 400 workers and their attributes dynamically
for i in range(4):
    worker = {
        "id": "W" + str(i+1),
        "name": "Worker_" + str(i+1),
        "rate": 10 + (i % 5),
        "hours": 40,
# Compute salary
        "salary": (10 + (i % 5)) * 40
    }
    level = "None"
# apply if conditions
    if ((10 + (i % 5)) * 40) > 10000 and ((10 + (i % 5)) * 40) < 20000:
            level = "A1"
    if ((10 + (i % 5)) * 40) > 7500 and ((10 + (i % 5)) * 40) < 30000:
            level = "A5-F"
    worker["level"] = level
    workers.append(worker)

print("Total workers created:", len(workers))
print("\nList of workers:\n")

# Print all workers and their weekly salary
for w in workers:
    # try-except block to handle potential errors
    try:
        print("ID:", w['id'])
        print("Name:", w['name'])
        print("Rate:", w['rate'])
        print("Hours:", w['hours'])
        print("Salary:", w['salary'])
        print("Level:", w['level'])
        print("-------------------")
    except KeyError as e:
            print("Missing data for worker:", e)
    except Exception as e:
            print("Error displaying worker info:", e)

    except Exception as e:
         print("Unexpected error while printing workers:", e)