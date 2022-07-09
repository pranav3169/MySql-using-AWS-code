# MySql-using-AWS-code

Write a python script to read a json file and csv file, and perform querys and some insights.

Assignment
● Part 1 : Creation of AWS ec2 instance
○ Create your amazon web services account 
○ Create a micro EC2 instance on Amazon Web services.
● Part 2 : Install MySQL on this EC2 instance
● Part 3 : Write a python module to read data from a local CSV to MySQL table
 Processing,
● Create MySQL connection
○ Read JSON file and create MySQL conn object.
● List files from <source_dir>
● Iterate through these files one by one.
● Read each csv file into pandas dataframe.
● Load pandas dataframe to mysql.
 Important guidelines,
● Make sure that you write code in modular way, try to use
methods and segregate code as per different functional
modules into different methods
● Make sure to have this as a command line utility ie. to be
executed with linux shell python command (preferably not
something executed through a Jupyter notebook).
● You can use ‘argparse’ library to add command line
argument functionality
● Make appropriate use of naming conventions and try to
put comments in code
● README should explain
○ Purpose of this utility
○ How to execute it
○ Example command
○ Explain argumnts
