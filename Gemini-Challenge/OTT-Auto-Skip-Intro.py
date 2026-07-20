# 1. Inputs (Linear variables)
intro_start, current_seconds, intro_end = 10, 25, 45

# 2. Pure Logic & Execution (Jo aapne exact paper par frame kiya)
if current_seconds >= intro_start and current_seconds <= intro_end:
    print("skip intro")
else:
    print("keep watching")