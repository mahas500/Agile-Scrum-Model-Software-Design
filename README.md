SoftwareEngineering_CA

This is the repository for submission of code for Software Engineering Assignment

# Problem:- 
As part of this CA, I was supposed to design a Traffic Control System software for the client DCC( Dublin city council). As soon as a pedestrian presses the button then based on sensor data and camera data placed at signals. The TCS signal should change pedestrian signal so that pedestrian can cross the road and change the vehicle signal accordingly. If in case any emergency vehicle(ambulance, police etc) approches the signal then TCS signal should interfere with both the signals and change them to RED. The sensor and video data should be stored in the database at DCC secured data center for legal reasons. Then I needed to plan out test cases for the system, risk involved in the system, UML diagram representation, design architecture etc.


# Approach:- 
My approach for this problem was first deciding and finalizing various functional and non-functional requirements of the system. After this I decided to use Scrum model of agile for software design. I divided the requirements in form of user stories. Then I did the sprint planning in which I decided which users stories to cover in which sprint, total number of sprints,duration, when to give releases, sprint backlog etc. I covered 2 user stories per sprint. Created task of each user story and assigned to the developer according to the complexity level of the task. If it is a difficult task then it is assigned to senior developer and if it is a easy task then it is given to junior developer. After this covering user stories in iterations. Details of sprints is given in technical report. Then designing MVC architecture for system and according to the functionality of each component. Coming up with UML's such as class diagram, sequence diagram, use case diagram and finally planning risk handling and various test cases of the system. All of these details are present in the attached technical report. 

Apart from this I also wrote a program in python to reach sensor data from 3 input files and perform operations given according to the problem and save the output in 2 files as shown below.

# Below is coding problem scenario as per CA
SignalID represents the id of the traffic light.  Time is simply a date-time value indicating the date and time of the reading.  ColourFrom and ColourTo representing traffic signal transitions:  RedGreen and GreenAmberRed are the only valid colour transitions when EVASOverride is equal to 0.  When it is equal to 1 then all transitions must be to Red (e.g., RedRed and GreenRed are permitted.
Assume that there are 3 signals (and therefore 3 input files to process).  


Please place the text files signal1.txt, signal2.txt and signal3.txt at the same path and directory as that of TCS_Signal_Code.py file.

Output files will be generated in the same path

Output_Signals.txt is the file which contains valid signal transition entries

Error_signals.txt is the file which contains invalid or error signal transition entries
