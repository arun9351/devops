import os

os.system("tput setaf 4")
print ("\t\t\t okay!! lets do it")
os.system("tput setaf 0")
print ("\t\t\t `````````````````\n")
os.system("tput setaf 6")
print ("\t\t\t Tell me what to do....")
os.system("tput setaf 0")
print ("\t\t\t ----------------------\n")


while True:
	print("""
	press 1 : to click photo
	press 2 : to click photo by remote host
	press 3 : to create a web server
	press 4 : to do live streaming
	press 5 : live streaming of remote host
	press 6 : configure hadoop
	press 7 : SET-UP docker
	press 8 : to exit
	""")

	print("choose what you want :" , end = '')
	ch = input()



	#click photo 
	if int (ch) == 1:
		os.system("python36 /root/Desktop/codes/camera.py")
	#configure web server (httpd)
	elif int (ch) == 3:
		os.system("ansible-playbook /root/Desktop/ansible/web.yml")
	#live streaming
	elif int (ch) == 4:
		os.system("python36 /root/Desktop/codes/video.py")




	#click photo at remote host
	elif int (ch) == 2:
		c = input("Enter IP:")
		x = "scp /root/Desktop/codes/camera.py {}:/tmp/camera.py".format(c)
		y = "ssh {} python36 /tmp/camera.py".format(c)
		z = "scp {}:/root/photo.png /root/Desktop/codes/host.png".format(c)
		os.system(x)
		os.system(y)
		os.system(z)


	#live streaming of remote host
	elif int (ch) == 5:
		c = input("Enter IP:")
		j = "scp /root/Desktop/codes/video.py {}:/tmp/video.py".format(c)
		k = "ssh -X {} python36 /tmp/video.py".format(c)
		os.system(j)
		os.system(k)
	#pre requisites of hadoop
	elif int (ch) == 6:
				os.system("ansible-playbook /root/Desktop/ansible/hadoop_packages.yml")


				print("""
				press 1: SET-UP Master node
				press 2: SET-UP Slave node
				press 3: SET-UP Job-tracker
				press 4: SET-UP Task-tracker
				press 5: SET-UP Client
				press 6: EXIT
				""")
				ch1 = input()
				#hadoop at remote host(master)
				if int (ch1) == 1:
					os.system("ansible-playbook /root/Desktop/ansible/hadoop_master.yml")
				#hadoop at remote host(slave)	
				elif int (ch1) == 2:
					os.system("ansible-playbook /root/Desktop/ansible/hadoop_slave.yml")
				#hadoop jobtracker setup
				elif int (ch1) == 3:
					os.system("ansible-playbook /root/Desktop/ansible/hadoop_jobTracker.yml")
				#hadoop tasktracker setup
				elif int (ch1) == 4:
					os.system("ansible-playbook /root/Desktop/ansible/hadoop_tasktracker.yml")
				#hadoop client at remote host
				elif int (ch1) == 5:
					os.system("ansible-playbook /root/Desktop/ansible/hadoop_client.yml")
				elif int (ch1) == 6:
					print("EXIT")
				else:
					print("INVALID ARGUMENT FOR HADOOP")
	#docker installation
	elif int (ch) == 7:
				os.system("ansible-playbook /root/Desktop/ansible/docker.yml")
				print("""
				press 1: load ubuntu:latest image
				press 2: load centos:14:04 image
				press 3: EXIT
				""")
				ch2 = input()
				#send docker images
				if int (ch2) == 1:
					os.system("ansible-playbook /root/Desktop/ansible/docker-ubuntuImage.yml")
				#send docker images
				elif int (ch2) == 2:
					os.system("ansible-playbook /root/Desktop/ansible/docker-centosImages.yml")
				elif int (ch2) == 3:
					print("EXIT")
				else:
					print("INVALID ARGUMENT FOR DOCKER")
	#exit
	elif int (ch) == 8:
		print("exit")
	else:
		print("INVALID ARGUMENT")

