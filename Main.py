# DSN5301 Operating System: Project Guideline ( Trimester 2, 2023/2024) 
# Instructions: 
# Form a group with a maximum of 4 members that must in a same lecture group. 
# You are allowed to use any programming language to simulate these concepts, not limited to C++, Java, Python, etc.  
# Submit your program online on Microsoft Team / Google Classroom by 10 July 2023, 11.59 pm.  
# Please record presentation and attached together with the project documents.(Video recording must not exceed 15mins). 
# All documents must be in PDF format. Do NOT zip the file when submit in the Microsoft Team.  
# Any form of plagiarism will not be tolerated. No marks will be given for this project if plagiarism is detected. 
# Topic 5: Simulation of CPU scheduling algorithms 
# Process Scheduling algorithms: Do ONE scheduling algorithm from Part A and ONE scheduling algorithms from Part B 
# Part A 
# a) Round Robin with Quantum 3  
# Part B (Choose any ONE of scheduling) 
# b) Preemptive SJF 
# c) Non Preemptive SJF 
# d) Preemptive Priority 
# e) Non Preemptive Priority 
# Pre-assigned case 
# 1. User should be able to enter the details about the processes such as Arrival Time, Burst Time, Priority, Time Quantum for Round Robin assigned at the beginning of simulation and the number of processes can range from 3 to 10. 
# 2. Executing the program should show the Gantt chart (visual form) of each algorithm. 
# 3. Calculation of; 
# a) Turnaround time for each process 
# b) Total and Average Turnaround time for the entire processes  
# c) Waiting time for each process 
# d) Total and Average Waiting time for the entire processes 

def WaitingTime(burst_time):
    pass

def TurnaroundTime(completion_time, arrival_time):
    pass

def RoundRobin(process_length, arrival_time, burst_time, processes):
    time_quantum = 2 

    lower_limit = 0
    upper_limit =  0

    print(processes)

    current_process = {}
    next_process = {}

    while i <= sum(burst_time):
        if (i < 0):
            return 
        
        #  = []

        lower_limit += i
        upper_limit += time_quantum 

# | Process | Arrival Time | Burst Time | Priority |
# |---------|--------------|------------|----------|
# |P1       |             0|           5|         0|
# |P2       |             1|           4|         0|
# |P3       |             2|           2|         0|
# |P4       |             4|           1|         0|
# |---------|--------------|------------|----------|

        for process in processes:
            print(process)
            
            if process["arrival_time"] == 0:
                current_process = process 

                if process:
                    pass
        break


    #             for i in range

    #         if process["arrival_time"] in range(lower_limit, upper_limit):
    #             processes_in_ready_queue = process

    #         elif process["arrival_time"] > lower_limit and process["arrival_time"] < upper_limit: 
    #             processes_in_ready_queue = process
    # # for i in range(sum(burst_time)):
    #     print(processes_in_ready_queue)
    # #     if (i )

    # #     pass

    # if arrival_time:
    #     pass


def Print(process_length, arrival_time, burst_time, priority):
    processes = []

    # print(process_length, arrival_time, burst_time, priority)

    print("\n", "".ljust(9, "-"), "".rjust(14, "-"), "".rjust(12, "-"), "".rjust(10, "-"), "", sep="|")
    print("| Process | Arrival Time | Burst Time | Priority |")
    print("", "".ljust(9, "-"), "".rjust(14, "-"), "".rjust(12, "-"), "".rjust(10, "-"), "", sep="|")

    for i in range(process_length):
        processes.append({
            "arrival_time": arrival_time[i],
            "burst_time": burst_time[i], 
            "priority": priority[i]
        })

        print("", f"P{i + 1}".ljust(9), f"{arrival_time[i]}".rjust(14), f"{burst_time[i]}".rjust(12), f"{priority[i]}".rjust(10), "", sep="|")
    
    print("", "".ljust(9, "-"), "".rjust(14, "-"), "".rjust(12, "-"), "".rjust(10, "-"), "", sep="|")

    RoundRobin(process_length, arrival_time, burst_time, processes)


    #print(process_length, arrival_time, burst_time, priority)

    
    

    print(f"\nRound Robin with Time Quantum 3 Gantt Chart: ")
    print(f"\nPreemptive Shortest Job First (SJF) Gantt Chart: ")
    
if __name__ == "__main__":
    
    process_length = int(input("Process Length (between 3-10): "))
    arrival_time = []
    burst_time = []
    priority = []

    for i in range(process_length):
        print(f"\nProcess {i + 1}")
        arrival_time.append(int(input("Arrival Time: ")))
        burst_time.append(int(input("Burst Time: ")))
        priority.append(int(input("Priority: ")))

    #print(process_length, arrival_time, burst_time, priority)

    Print(process_length, arrival_time, burst_time, priority)