# KinMS GUI
Graphics Interface for the KinMS by Timothy A Davis. (https://github.com/TimothyADavis/KinMS)


-Installation
	
	To install the GUI download the files available at https://github.com/TristanBurman/KinMSGUI and run the 
	file named 'GUI.py' located in the 'GUI Program' folder.
	
	Installation via pip can be done using the command 'pip install KinMSGUI' and run in python by 
	importing KinMSGUI and running 'KinMSGUI.GUI.RUN()'
 
 
-Built Using

	KinMS 	     - Kinetic Modeling Simulation programme Used to generate fits 
	Tkinter	     - Used to Create the GUI Interface
	Numpy 	     - Used for Calculations 
	Scipy 	     - Specifically scipy.optimize.minimize for minimisation
	Matplotlib   - Used for plotting data
	Astropy      - For reading .fits files

	Other modules used

	Time	       - Used for timing fitting 
	Threading    - Used to run minimisation on seperate thread to prevent GUI update blocking
	Webbrowser   - Used to launch website

