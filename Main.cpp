// DSN5301 Operating System: Project Guideline ( Trimester 2, 2023/2024) 

// Instructions: 
// Form a group with a maximum of 4 members that must in a same lecture group. 
// You are allowed to use any programming language to simulate these concepts, not limited to C++, Java, Python, etc.  
// Submit your program online on Microsoft Team / Google Classroom by 10 July 2023, 11.59 pm.  
// Please record presentation and attached together with the project documents.(Video recording must not exceed 15mins). 
// All documents must be in PDF format. Do NOT zip the file when submit in the Microsoft Team.  
// Any form of plagiarism will not be tolerated. No marks will be given for this project if plagiarism is detected. 

// Topic 5: Simulation of CPU scheduling algorithms 

// Process Scheduling algorithms: Do ONE scheduling algorithm from Part A and ONE scheduling algorithms from Part B 
// Part A 
// a) Round Robin with Quantum 3  

// Part B (Choose any ONE of scheduling) 
// b) Preemptive SJF 
// c) Non Preemptive SJF 
// d) Preemptive Priority 
// e) Non Preemptive Priority 

// Pre-assigned case 
// 1. User should be able to enter the details about the processes such as Arrival Time, Burst Time, Priority, Time Quantum for Round Robin assigned at the beginning of simulation and the number of processes can range from 3 to 10. 
// 2. Executing the program should show the Gantt chart (visual form) of each algorithm. 
// 3. Calculation of; 
// a) Turnaround time for each process 
// b) Total and Average Turnaround time for the entire processes  
// c) Waiting time for each process 
// d) Total and Average Waiting time for the entire processes 

#include <iostream>
#include <string>

void Print()
{

}

int main()
{
    int processes[10]{};
    int burst_time[10]{};
    int arrival_time[10]{};
    int priority[10]{};

    int time_quantum = 3;

    std::cin >> processes[1];

}