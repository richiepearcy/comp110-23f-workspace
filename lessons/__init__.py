def update_attendance(x: dict[str,list[str]], y: str, z: str) -> dict[str,list[str]]:
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    for key in x:
        if y in key:
            x += z 
        else:
            x = x
    
    return update_attendance