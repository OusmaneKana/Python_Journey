import os 
import webbrowser


class file_path(object):
	"""docstring for file_path"""
	def __init__(self, student_name, course_name):
		self.student_name = student_name
		self.course_name = course_name
		 

	def student_file(self):
		""" Method that is made to create the student folder if not existing 
				to open it if it does exist"""
		if not exist:
			#create
		else:
			#open

	def course_file(self):
		if not exist:
			# create
		else:
			#open


	def course_folder(self)



		
def open_folder(pathway):
	os.system("start "+pathway)

	return 0

def open_website(url):
	address = "www."+url+".com"
	webbrowser.open(address)
	

while True:
	print("\nActivity list. \n1- Tutoring \n2- Studying \n3- coding \n4- Exit")
	choice = input("\n\nWhat are you doing today?")

	if choice == "1":
		print("\n\nWho are you Tutoring today ?:  ")
		tutee = input("1-The Chukwulus family \n2- Micheal \n3-New student\n__")
		if tutee == "1":
			print("opening and creating the files for Chukwulus" )
			open_website("gmail")

			
		elif tutee =="2":
			print("opening and creating the files for The Micheal" )
			os.system("start C:\\Users\\Serigne\\Desktop\\\"Tutoring_sessions\"\\Micheal")
		elif tutee =="3":
			new_student = input("\nWhat is the name of the new tutee?:  ")
			print("\nCreating files for {}".format(new_student))
			os.system("mkdir C:\\Users\\Serigne\\Desktop\\\"Tutoring_sessions\"\\{}".format(new_student))

	elif choice =="2":
		print("What are you going to study today? \n1- Math \n2- Government \n3- History \n4 Chemistry \n5- Chemistry Lab \n")
		study= input("----> ")
		open_website("gmail")

		











# if choice == "1":
	# webbrowser.open("https://eagleonline.hccs.edu/courses/110128")

	# os.system("start C:\\Users\\Serigne\\\"OneDrive - Houston Community College\"\\\"Spring 2020\"\\\"Physics I\"")
