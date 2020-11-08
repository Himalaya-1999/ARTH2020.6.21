import os
os.system("clear")
os.system("tput setaf 3")
os.system("setenforce 0")
print("""
		888       888          888                                              888
		888   o   888          888                                              888
		888  d8b  888          888                                              888
		888 d888b 888  .d88b.  888  .d8888b  .d88b.  88888b.d88b.   .d88b.      888888  .d88b.       .d88b.  888  888 888d888
		888d88888b888 d8P  Y8b 888 d88P"    d88""88b 888 "888 "88b d8P  Y8b     888    d88""88b     d88""88b 888  888 888P"
		88888P Y88888 88888888 888 888      888  888 888  888  888 88888888     888    888  888     888  888 888  888 888
		8888P   Y8888 Y8b.     888 Y88b.    Y88..88P 888  888  888 Y8b.         Y88b.  Y88..88P     Y88..88P Y88b 888 888
		888P     Y888  "Y8888  888  "Y8888P  "Y88P"  888  888  888  "Y8888       "Y888  "Y88P"       "Y88P"   "Y88888 888
		
			888b     d888                                8888888b.          d8b
			8888b   d8888                                888  "Y88b         Y8P
			88888b.d88888                                888    888
			888Y88888P888  .d88b.  88888b.  888  888     888    888 888d888 888 888  888  .d88b.  88888b.
			888 Y888P 888 d8P  Y8b 888 "88b 888  888     888    888 888P"   888 888  888 d8P  Y8b 888 "88b
			888  Y8P  888 88888888 888  888 888  888     888    888 888     888 Y88  88P 88888888 888  888
			888   "   888 Y8b.     888  888 Y88b 888     888  .d88P 888     888  Y8bd8P  Y8b.     888  888
			888       888  "Y8888  888  888  "Y88888     8888888P"  888     888   Y88P    "Y8888  888  888
			
					8888888b.
					888   Y88b
					888    888
					888   d88P 888d888  .d88b.   .d88b.  888d888  8888b.  88888b.d88b.
					8888888P"  888P"   d88""88b d88P"88b 888P"       "88b 888 "888 "88b
					888        888     888  888 888  888 888     .d888888 888  888  888
					888        888     Y88..88P Y88b 888 888     888  888 888  888  888
					888        888      "Y88P"   "Y88888 888     "Y888888 888  888  888
       	                 					        8888
      	                  					    Y8b d88p
      	                  					     "Y88P"
	
						
	""")
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
os.system("tput setaf 6")
print("\t\t\t\t\t\t    copyright\u00a92020 ARTH Crusaders(ARTH2020_6_21)")
os.system("sleep 3")
def exitfun():
    os.system("tput setaf 3")
    print("\t\t\t\t\t\tThank you for using our tool, hope you like our services!!!")
    print("\t\t\t\t\t\t\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D\u058D")
    print()
    print()
    print()
    os.system("tput setaf 6")
    print("\t\t\t\t\t\t      copyright\u00a92020 ARTH Crusaders(ARTH2020_6_21)")
    exit()

def hadoopmenu():
    os.system("tput setaf 2")
    print("""
		-> Press 1 : To check whether Hadoop and JavaDev.Kit(JDK) is installed on system.
                -> Press 2 : To install the above mentioned softwares.
                -> Press 3 : To configure your system as Namenode/Datanode.
                -> Press 4 : To Start the HadoopServices.
                -> Press 5 : To Stop the HadoopSevices.
                -> Press 6 : To check your Hadoop Cluster status.
                -> Press 7 : TO Upload the file in the cluster.
                -> Press 8 : TO check the files present in cluster.
                -> Press 9 : TO Remove the files from cluster.
                -> Press 10: TO Read the file from the CLUSTER. 
                -> Press 11: To get back to Main Menu.
                -> Press 12: To Exit.                                                                                                                  
                """)
    os.system("tput setaf 3")

def dockermenu():
    os.system("tput setaf 2")
    print("""
	        	-> Press 1 : To check whether Docker-ce software is installed or not.
        		-> Press 2 : To Install Docker software .
        		-> Press 3 : To start/stop/status Docker services.
        		-> Press 4 : To list all available Docker images.
        		-> Press 5 : To download Docker images.
        		-> Press 6 : To launch a Container.
        		-> Press 7 : To list all Containers.
        		-> Press 8 : To start a available container.
        		-> Press 9 : To terminate a container.
        		-> Press 10: To get back to the Main Menu.
        		-> Press 11: To Exit.
		""")
    os.system("tput setaf 3")
       
def linuxmenu():
    os.system("tput setaf 2")
    print("""
        		-> Press 1 : To See date.
        		-> Press 2 : To see the calender.
        		-> Press 3 : To add a new User Account.
        		-> Press 4 : To see all the running process.
        		-> Press 5 : To set-up a Webserver.
        		-> Press 6 : To Software and Service Management.
        		-> Press 7 : To create partitions in Hard Disk.
        		-> Press 8 : To create LVM.
        		-> Press 9 : To get back to Main Menu.
        		-> Press 0 : To exit.
		""")
    os.system("tput setaf 3")
            

def aws():
	while True:
		os.system("clear")
		os.system("tput setaf 3")
		print("""
		\t\t\t\t,adPPYYba,  8b      db      d8  ,adPPYba,
		\t\t\t\t""     `Y8  `8b    d88b    d8'  I8[    ""
		\t\t\t\t,adPPPPP88   `8b  d8'`8b  d8'    `"Y8ba,
		\t\t\t\t88,    ,88    `8bd8'  `8bd8'    aa    ]8I
		\t\t\t\t`"8bbdP"Y8      YP      YP      `"YbbdP"'
	
			""")
		os.system("tput setaf 1")
		print("\t\t\t\t\t\t         Welcome to the our AWS Portal")
		os.system("tput setaf 4")
		print("\t\t\t\t\t\t         *****************************")
		os.system("tput setaf 2")
		print("!!!PRE-REQUISITE : please press 1 for aws account authentication otherwise services will show error")
		os.system("tput setaf 1")
		print("!!!PRE-REQUISITE : please run the extra python script firstly that we provided, for some necessary installations  otherwise services will show error")
		os.system("tput setaf 6")
		print("""
			\u058D press 1:AWS CREDENTIALS (Login or change your credentials)
			\u058D press 2:EC2 SERVICE	(Launching of an EC2 instance)
			\u058D press 3:EBS SERVICE	(Creating an extra Volume & attaching it) 
			\u058D press 4:S3 SERVICE	(Creating Bucket & putting object)
			\u058D press 5:CLOUDFRONT	(Setting up High Availability Architecture for Web Server) 
       			\u058D press 6:DEPLOYMENT OF HIGH AVAILABILITY ARCHITECTURE
			\u058D press 7:GO TO MAIN MENU 
			\u058D press 8:EXIT
			""")
		os.system("tput setaf 3")
		value=int(input("Please Enter Your Choice:"))
		if value==1:
			os.system("tput setaf 3")
			print("Please enter your aws account credentials")
			os.system("/usr/local/bin/aws configure")
			os.system("tput setaf 2")
			input("\t\t\t\t\t\t\t    press any key to Continue!!")
		elif value==2:
			while True:
				os.system("clear")
				os.system("tput setaf 3")
				print("""
					\t\t       d8888 888       888  .d8888b.          8888888888  .d8888b.   .d8888b.
					\t\t      d88888 888   o   888 d88P  Y88b         888        d88P  Y88b d88P  Y88b
					\t\t     d88P888 888  d8b  888 Y88b.              888        888    888        888
					\t\t    d88P 888 888 d888b 888  "Y888b.           8888888    888             .d88P
					\t\t   d88P  888 888d88888b888     "Y88b.         888        888         .od888P"
					\t\t  d88P   888 88888P Y88888       "888         888        888    888 d88P"
					\t\t d8888888888 8888P   Y8888 Y88b  d88P         888        Y88b  d88P 888"
					\t\td88P     888 888P     Y888  "Y8888P"          8888888888  "Y8888P"  888888888      
					""")
				os.system("tput setaf 1")
				print("\t\t\t\t\t\t\t\tWelcome to the EC2 Service")
				os.system("tput setaf 4")
				print("\t\t\t\t\t\t\t\t**************************")
				os.system("tput setaf 2")
				print("\u058D Please specify the type of instance attributes for the instance you want to launch :")
				print()
				os.system("tput setaf 6")
				print("\u058D Please specify OS name")
				print("""
			press 1:Amazon Linux 2
			press 2:Red Hat Enterprise Linux 8
			press 3:SUSE Linux Enterprise Server 15
			press 4:Ubuntu Server 20.04 LTS
			press 5:Microsoft Windows Server 2019
				""")
				os.system("tput setaf 3")
				osi=int(input("\u058D Please Enter Your Choice:"))
				if osi==1:
					image="ami-0e306788ff2473ccb"
				elif osi==2:
					image="ami-052c08d70def0ac62"
				elif osi==3:
					image="ami-0d0522ed4db1debd6"
				elif osi==4:
					image="ami-0cda377a1b884a1bc"
				elif osi==5:
					image="ami-0b2f6494ff0b07a0e"
				else:
					os.system("tput setaf 1")
					input("\t\t\tOOPS!! you've entered wrong input please provide us correct input,it is necessary")
					continue
				print()
				print()
				os.system("tput setaf 6")
				size=input("\u058D please specify instance size:")
				print()
				print()
				count=int(input("\u058D please specify instance count:"))
				print()
				print()
				print("\u058D Please specify key for your instance :")
				print("""
			press 1:Create a new Key Pair
			press 2:Select an existing key pair
					""")
				os.system("tput setaf 3")
				kc=int(input("\u058D please Enter your choice:"))
				os.system("tput setaf 6")
				if kc==1:
					name=input("\u058D please enter the key name you want to create :")
					os.system(f"/usr/local/bin/aws ec2 create-key-pair --key-name {name}")
					ex=os.system("echo $?")
					if ex==0:
						print()
						print()
						os.system("tput setaf 6")
						input("Your key has been successfully created !!! press any key to continue....")
					else:
						print()
						print()
						os.system("tput setaf 1")
						input("\t\t\t\t\tOOPS!! an error occured due to wrong inputs !! press any key to continue....")
						continue
				elif kc==2: 	
					print("\u058D Available Key Pairs on your account:")
					os.system("/usr/local/bin/aws ec2 describe-key-pairs")
					name=input("\u058D Enter the key name you want to use to login to this instance :")
				else:
					os.system("tput setaf 1")
					input("\t\t\tOOPS!! you've entered wrong input please provide us correct input,it is necessary")
					continue
				print()
				print()
				os.system("tput setaf 3")
				print("\u058D Please specify Security Group for your instance :")
				print(""" 
			press 1:Create a new Security Group
			press 2:Select an existing Security Group
				""")
				sg=int(input("\u058D please Enter your choice:"))
				os.system("tput setaf 6")
				if sg==1:
					sgname=input("\u058D please enter the Security Group name you want to create:")
					description=input("\u058D please give some description about this Security Group :")
					os.system(f"/usr/local/bin/aws ec2 create-security-group --group-name {sgname} --description {description}")
					sgid=input("\u058D Your Security Group has been successfully created !!! press enter its id :")
					input("Your Security Group has been attached !!! press enter to continue....")
				elif sg==2: 	
					print("\u058D Available Security Groups on your account with description and IP Ingress Permission:")
					os.system("/usr/local/bin/aws ec2 describe-security-groups")
					sgid=input("\u058D Enter the Security Group id you want to use for this instance :")
				else:
					os.system("tput setaf 1")
					input("\t\t\tOOPS!! you've entered wrong input please provide us correct input,it is necessary")
					continue
				excode=os.system("echo $?")
				if excode==0:
					print()
					print()
					os.system("tput setaf 6")
					input("Your Security Group has been attached !!! press enter to continue....")
				else:
					print()
					print()
					os.system("tput setaf 1")
					input("\t\t\t\t\tOOPS!! an error occured due to wrong inputs !! press any key to continue....")
					continue
				print()
				print()
				os.system("tput setaf 6")
				case=input("\u058D Want to allow rules in the Security Group Y/N ")
				os.system("tput setaf 3")
				if case=="Y":
					protocol=input("\u058D please specify the protocol:")
					port=input("\u058D please specify the port no.:")
					cidr=input("\u058D please specify the CIDR(ex:0.0.0.0/0):")
					os.system(f"/usr/local/bin/aws ec2 authorize-security-group-ingress --group-name {sgid} --protocol {protocol} --port {port} --cidr {cidr}")
					input(f"Your rules has been successfully attached with Security Group: {sgid} !!! press enter to continue....")
				print()
				print()
				os.system("/usr/local/bin/aws ec2 run-instances --image-id {image} --instance-type {size} --count {count} --key-name {name} --security-group-ids {sgid}")
				code=os.system("echo $?")
				if code==0:
					print()
					print()
					os.system("tput setaf 6")
					print("\t\t\t\t\t\tCongratulations!! Your instance has been configured and has been launched")
				else:
					print()
					print()
					os.system("tput setaf 1")
					print("\t\t\t\t\t\tOOPS!! an error occured due to wrong inputs !!")
				print()
				print()
				print()
				os.system("tput setaf 2")
				ex=input("Want to exit ? Y/N")
				if ex==Y:
					exitfun()	
		
		elif value==3:
			while True:
				os.system("clear")
				os.system("tput setaf 3")
				print("""
			\t\t       d8888 888       888  .d8888b.          8888888888 888888b.    .d8888b.
			\t\t      d88888 888   o   888 d88P  Y88b         888        888  "88b  d88P  Y88b
			\t\t     d88P888 888  d8b  888 Y88b.              888        888  .88P  Y88b.
			\t\t    d88P 888 888 d888b 888  "Y888b.           8888888    8888888K.   "Y888b.
			\t\t   d88P  888 888d88888b888     "Y88b.         888        888  "Y88b     "Y88b.
			\t\t  d88P   888 88888P Y88888       "888         888        888    888       "888
			\t\t d8888888888 8888P   Y8888 Y88b  d88P         888        888   d88P Y88b  d88P
			\t\td88P     888 888P     Y888  "Y8888P"          8888888888 8888888P"   "Y8888P"   
				""")	
				os.system("tput setaf 1")	
				print("\t\t\t\t\t\t\t\tWelcome to the EBS Service")
				os.system("tput setaf 4")
				print("\t\t\t\t\t\t\t\t**************************")
				os.system("tput setaf 2")
				print("\u058D Please specify the type of storage attributes for your instances  :")
				print()
				print("NOTE: It is recommended to create volume in same region as of your instance otherwise aws can't connect them together")
				print()
				os.system("tput setaf 6")
				print("\u058D Please specify your requirements:")
				print("""
			\u058D press 1:To create an EBS Volume
			\u058D press 2:To create Snapshot
			\u058D press 3:To go back to previous menu
			\u058D press 4:To go back to main menu
			\u058D press 5:EXIT
					""")
				os.system("tput setaf 3")
				ebs=int(input("\u058D Enter your choice : "))
				os.system("tput setaf 6")
				if ebs==1:
					vols=input("\u058D Please specify the size of volume you want to create : ")
					zone=input("\u058D Please specify the Availability zone of volume you want to create : ")
					os.system(f"/usr/local/bin/aws ec2 create-volume --size {vols} --availability-zone {zone}")
					code=os.system("echo $?")
					if code==0:
						print()
						print()
						os.system("tput setaf 6")
						print("\t\t\t\t\t\tCongratulations!! Your volume has been launched")
					else:
						print()
						print()
						os.system("tput setaf 1")
						print("\t\t\t\t\t\tOOPS!! an error occured due to wrong inputs !!")
						continue
					print()
					attach=input("t\t\t\t\t\u058D Want to attach the volume with your instance Y/N ? :")
					if attach=="Y":
						vid=input("\u058D please specify the volume-id:")
						iid=input("\u058D please specify the instance-id:")
						dev=input("\u058D please specify the device name(ex:/dev/xvdf) :")
						os.system(f"/usr/local/bin/aws ec2 attach-volume --volume-id {vid} --instance-id {iid} --device {dev}")
				elif ebs==2: 
					vol=input("\u058D Please specify the volume-id to create snapshot : ")
					os.system(f"/usr/local/bin/aws ec2 create-snapshot --volume-id {vol}")
				elif ebs==3:
					break
				elif ebs==4:
					main()
				elif ebs==5:
                    			exitfun()
				else:
					print("You've entered wrong input!!")
					os.system("tput setaf 2")
					input("\t\t\t\t\t\t\t    press any key to Continue!!")
					continue
				code=os.system("echo $?")
				if code==0:
					print()
					print()
					os.system("tput setaf 6")
					input("\t\t\t\t\tYour volume has been successfully attached with the instance!!! press enter to continue....")
				else:
					print()
					print()
					os.system("tput setaf 1")
					print("\t\t\t\t\tOOPS!! an error occured due to wrong inputs !!")
					
		elif value==4:
			while True:
				os.system("clear")
				os.system("tput setaf 3")
				print("""
			\t\t       d8888 888       888  .d8888b.       .d8888b.   .d8888b.
			\t\t      d88888 888   o   888 d88P  Y88b     d88P  Y88b d88P  Y88b
			\t\t     d88P888 888  d8b  888 Y88b.          Y88b.           .d88P
			\t\t    d88P 888 888 d888b 888  "Y888b.        "Y888b.       8888"
			\t\t   d88P  888 888d88888b888     "Y88b.         "Y88b.      "Y8b.
			\t\t  d88P   888 88888P Y88888       "888           "888 888    888
			\t\t d8888888888 8888P   Y8888 Y88b  d88P     Y88b  d88P Y88b  d88P
			\t\td88P     888 888P     Y888  "Y8888P"       "Y8888P"   "Y8888P"			   
				""")	
				os.system("tput setaf 1")
				print("\t\t\t\t\t\t\t\tWelcome to the S3 Service")
				os.system("tput setaf 4")
				print("\t\t\t\t\t\t\t\t**************************")
				os.system("tput setaf 2")
				print("\u058D Please specify the type of Object Storage attributes :")
				print()
				print()
				os.system("tput setaf 6")
				print("\u058D Please specify your requirements :")
				print("""
			\u058D press 1:CREATE BUCKET
			\u058D press 2:UPLOAD OBJECT
			\u058D press 3:REMOVE OBJECT
			\u058D press 4:LIST BUCKETS
			\u058D press 5:MAKE OBJECT PUBLIC
			\u058D press 6:To go back to previous menu
			\u058D press 7:To go back to main menu	
			\u058D press 8:EXIT
				""")
				os.system("tput setaf 3")
				choice=int(input("\u058D Please Enter Your Choice:"))
				os.system("tput setaf 6")
				if choice==1:
					name=input("\u058D Please specify bucket name : ")
					location=input("\u058D please specify your bucket region : ")
					os.system(f"/usr/local/bin/aws s3api create-bucket --bucket {name} --create-bucket-configuration LocationConstraint={location}")
					input("\t\t\t\t\t\t!!! press enter to continue....")
				elif choice==2:
					bucket=input("\u058D Please specify bucket name : ")
					file=input("\u058D please mention path of your object to upload : ")
					os.system(f"/usr/local/bin/aws s3 cp {file} s3://{bucket}")
					input("\t\t\t\t\t\t!!! press enter to continue....")
				elif choice==3:
					bucket=input("\u058D Please specify bucket name : ")
					file=input("\u058D please mention path of your object to remove: ")
					os.system(f"/usr/local/bin/aws s3 rm s3://{bucket}/{file}")
					input("\t\t\t\t\t\t!!! press enter to continue....")
				elif choice==4:
					print("\u058D Available buckets in your account: ")
					os.system(f"/usr/local/bin/aws s3 ls")
					input("\t\t\t\t\t\tpress enter to continue....")
				elif choice==5:
					bucket=input("\u058D Please specify bucket name : ")
					file=input("\u058D please mention name of your object : ")
					grp=input("\u058D please mention permission on your file (Public/Private) : ")
					perm=input("\u058D please mention sub-permission on your file(read/write) : ")
					os.system(f"/usr/local/bin/aws s3api put-object-acl --bucket {bucket} --key {file} --acl {grp}-{perm}")
					input("\t\t\t\t\t!!! press enter to continue....")
				elif choice==6:
					break
				elif choice==7:
					main()
				elif choice==8:
                    			exitfun()
				else:
					print("You've entered wrong input!!")
					os.system("tput setaf 2")
					input("\t\t\t\t\t\t\t    press any key to Continue!!")
				code=os.system("echo $?")
				if code==0:
					print()
					print()
					os.system("tput setaf 6")
					input("\t\t\t\t\t\tYour S3 bucket/object has been successfully configured!!! press enter to continue....")
				else:
					print()
					print()
					os.system("tput setaf 1")
					print("\t\t\t\t\t\tOOPS!! an error occured due to wrong inputs !!")
		elif value==5:
			while True:
				os.system("clear")
				os.system("tput setaf 3")
				print("""
				  ,ad8888ba,   88                                     88  88888888888
				 d8"'    `"8b  88                                     88  88                                                   ,d
				d8'            88                                     88  88                                                   88
				88             88   ,adPPYba,   88       88   ,adPPYb,88  88aaaaa      8b,dPPYba,   ,adPPYba,   8b,dPPYba,   MM88MMM
				88             88  a8       8a  88       88  a8      Y88  8888888      88P     Y8  a8       8a  88P      8a    88
				Y8,            88  8b       d8  88       88  8b       88  88           88          8b       d8  88       88    88
				 Y8a.    .a8P  88  "8a,   ,a8"  "8a,   ,a88  "8a,   ,d88  88           88          "8a,   ,a8"  88       88    88,
				  `"Y8888Y"'   88   `"YbbdP"'    `"YbbdP'Y8   `"8bbdP"Y8  88           88           `"YbbdP"'   88       88    "Y888      
				""")
				os.system("tput setaf 1")
				print("\t\t\t\t\t\t\t\tWelcome to the CLOUDFRONT Service")
				os.system("tput setaf 4")
				print("\t\t\t\t\t\t\t\t********************************")
				os.system("tput setaf 6")
				print("Please specify the type of attributes for CloudFront Service :")
				print()
				print("""       
	   		\u058D press 1:Create Distribution
			\u058D press 2:To go back to previous menu
			\u058D press 3:To go back to main menu
			\u058D press 4:EXIT
				""")
				os.system("tput setaf 3")
				choice=int(input("Please Enter Your Choice:"))
				os.system("tput setaf 6")
				if choice==1:
					file=Print("\u058D please use the correct name of your domain i.e. the place where your object is kept (ex:bucket_name.s3.amazonaws.com)")
					dom=input("\u058D please enter the oigin domain name : ")
					os.system("/usr/local/bin/aws cloudfront create-distribution --origin-domain-name {dom}")
				elif choice==2:
					break
				elif choice==3:
					main()
				elif choice==4:
                    			exitfun()
				code=os.system("echo $?")
				if code==0:
					print()
					print()
					os.system("tput setaf 6")
					input("\t\tThe above mentioned messgae displays CloudFront domain name, put the name in browser and use it!!!")
				else:
					print()
					print()
					os.system("tput setaf 1")
					print("\t\t\t\t\t\tOOPS!! an error occured due to wrong inputs !!")
		elif value==6:
			os.system("clear")
			os.system("tput setaf 3")
			print("""
			_  _ _ ____ _  _    ____ _  _ ____ _ _    ____ ___  _ _    _ ___ _   _    ____ ____ ____ _  _ _ ___ ____ ____ ___ _  _ ____ ____
			|__| | | __ |__|    |__| |  | |__| | |    |__| |__] | |    |  |   \_/     |__| |__/ |    |__| |  |  |___ |     |  |  | |__/ |___
			|  | | |__] |  |    |  |  \/  |  | | |___ |  | |__] | |___ |  |    |      |  | |  \ |___ |  | |  |  |___ |___  |  |__| |  \ |___
				""")
			os.system("tput setaf 1")
			print("\t\t\t\t\t\t\t\t\tWelcome to our Blog")
			os.system("tput setaf 4")
			print("\t\t\t\t\t\t\t\t\t*******************")
			os.system("tput setaf 6")
			print("""
				\u058D Webserver must be configured in EC2 instance,commands:
					Connect with your instance using SSH and Key 
					yum install httpd
					Systemctl start httpd
				\u058D Document Root(/var/www/html) made persistent by mounting(attaching) it on EBS Block Device.
					After attaching EBS Block Device create partitions,format it and mount it on /var/www/html
					fdisk -l -->Shows all the available block devices attached to the instance
					fdisk <device_name> -->go inside the drive and create partitions
					mkfs.ext4 <device_name> -->format the drive with ext4
					mount <device_name> /var/www/html/ --> mount it to document root folder of webserver
					Now place your code inside this folder
				\u058D Now you can use our tool for further process
			
				\u058D Static objects used in code such as pictures, store them in S3 bucket
				\u058D Setting up Content Delivery Network using CloudFront and using the origin domain as S3 bucket. 
				\u058D Finally place the Cloud Front URL on the webapp code for security and low latency.


	\u058D Blog Link: https://www.linkedin.com/posts/himalaya-sahu-1982a2185_deployment-of-high-availability-architecture-activity-6729491349403430912-m-n7
			""")
			input("\t\t\t\t\t\t\t    press any key to Continue!!")
		elif value==7:
			break
		elif value==8:
            		exitfun()	
		else :
			print("Oops!! you entered wrong choice")
			input("\u058DEnter to continue")
def yumconfig():
    print()
    print()
    ques=input("Please specify Hardware You are using.(CLOUD/VM/BASEOS) : ")
    if ("BASEOS" in ques) or ("VM" in ques):
        print()
        print("NOTE! You must have your software DVD attached to your system.")
        input=dvd("Please specify the (Full)path of attached DVD :")
        os.system("echo '[dvd1]' > /etc/yum.repos.d/crusader.repo")
        os.system("echo 'baseurl=file://{}' >> /etc/yum.repos.d/crusader.repo".format(dvd))
        os.system("echo 'gpgcheck=0' >> /etc/yum.repos.d/crusader.repo")
        os.system("echo '[dvd2]' >> /etc/yum.repos.d/crusader.repo")
        os.system("echo 'baseurl=file://{}' >> /etc/yum.repos.d/crusader.repo".format(dvd))
        os.system("echo 'gpgcheck=0' >> /etc/yum.repos.d/crusader.repo")
        os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm")
        os.system("yum repolist")
    elif ("CLOUD"in ques):
        print("Your yum is already configured.")
    else:
        print("You were asked to type (CLOUD/VM/BASEOS) please type correct input.")

def yumconfigssh(username,ip):
    os.system("scp /etc/yum.repos.d/crusader.repo {}@{}:/etc/yum.repos.d/".format(username,ip))
    os.system("ssh {}@{} yum repolist".format(username,ip))
    os.system("ssh {}@{} dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm".format(username,ip))
    os.system("ssh {}@{} yum repolist".format(username,ip))
    
def sshkey(username,ip):
    print()
    print()
    print()
    print("""!!!We would require your user account password!!!
	Command to set a password: echo <password> | passwd --stdin <username>
        	                   systemctl start sshd
	""")
    print()
    print()
    os.system("ssh-keygen")
    print("\t\tThis is the Remote execution programm")
    print("\n> Enter the IP Address of that Remote system")
    print("\nNOTE! Once you typed th IP,this ip then can be only changed after restarting this whole Automation Programm\n")
    print()
    print("<---ONE TIME AUTHENTICATION--->")
    os.system("ssh-copy-id {}@{}".format(username,ip))
    return ip

def docker(var,username,ip):
    while True:
        os.system("clear")
        os.system("tput setaf 3")
        print("""
			\t\t88888888ba,                             88
			\t\t88      `"8b                            88
			\t\t88        `8b                           88
			\t\t88         88   ,adPPYba,    ,adPPYba,  88   ,d8    ,adPPYba,  8b,dPPYba,
			\t\t88         88  a8"     "8a  a8"     ""  88 ,a8"    a8P_____88  88P'   "Y8
			\t\t88         8P  8b       d8  8b          8888[      8PP"""""""  88
			\t\t88      .a8P   "8a,   ,a8"  "8a,   ,aa  88`"Yba,   "8b,   ,aa  88
			\t\t88888888Y"'     `"YbbdP"'    `"Ybbd8"'  88   `Y8a   `"Ybbd8"'  88
        """)
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t         Welcome to the our DOCKER Portal")
        os.system("tput setaf 4")
        print("\t\t\t\t\t\t         *****************************")
        os.system("tput setaf 2")
        print()
        os.system("tput setaf 7")
        print("\n")
        if ("local"in var)or("LOCAL"in var)or("Local"in var)or("L"in var):
            dockermenu()
            b=input("Enter command number u want to run : ")
            if int(b)==1:
                os.system("rpm -q docker-ce")
            elif int(b)==2:
                os.system("echo '[dockers123]' > /etc/yum.repos.d/docker.repo")
                os.system("echo 'baseurl=https://download.docker.com/linux/centos/7/x86_64/stable' >> /etc/yum.repos.d/docker.repo")
                os.system("echo 'gpgcheck=0' >> /etc/yum.repos.d/docker.repo")
                os.system("sudo yum install docker-ce --nobest -y")
            elif int(b)==3:
                print()
                action=input("Enter your action (start/stop/status)a service: ")
                os.system("tput setaf 5")
                os.system("systemctl {} docker".format(action))
                os.system("tput setaf 7")

            elif int(b)==4:
                os.system("docker images")
            elif int(b)==5:
                image=input("Enter OSname:version to be downloaded(ex-ubuntu:20.10)) : ")
                os.system("docker pull {}".format(image))
            elif int(b)==6:
                os.system("docker images")
                image=input("Enter imagename:version(ex:-ubuntu:20.10) : ")
                name= input("Enter a name you want to give to your container : ")
                os.system("docker run -it --name {} {}".format(name,image))

            elif int(b)==7:
                os.system("docker ps -a")

            elif int(b)==8:
                os.system("docker ps -a")
                start=input("\nEnter the OS name/OS ID you want to boot : ")
                os.system("docker start {}".format(start))
                os.system("docker attach {}".format(start))

            elif int(b)==9:
                print("""\t\tWARNING!
            For terminating a Container firstly Authenticate yourself.
            """)
                password=gp.getpass("Enter Password:")
                if password == "arth":#to be edited
                    print("Authentication Approved")
                    os.system("docker ps -a")
                    x=input("Enter the container id/name u want to terminate : ")
                    os.system("docker rm {}".format(x))

                else:
                    os.system("tput setaf 1")
                    print("Ooooopss! Wrong password.")
                    os.system("tput setaf 7")
            elif int(b)==10:
                break
            elif int(b)==11:
                exitfun()
            else:
                os.system("tput setaf 1")
                print("Oooppps! Enter a valid command number.")
                os.system("tput setaf 7")
            input("<Press Enter to continue>")


        elif ("remote"in var)or("REMOTE"in var)or("Remote"in var)or("R"in var):
            print()
            dockermenu()
            print()
            print()
            b=input("Enter command number u want to run : ")
            if int(b)==1:
                os.system("ssh {}@{} rpm -q docker-ce".format(username,ip))
            elif int(b)==2:
                os.system("echo '[dockers123]' > /etc/yum.repos.d/docker.repo")
                os.system("echo 'baseurl=https://download.docker.com/linux/centos/7/x86_64/stable' >> /etc/yum.repos.d/docker.repo")
                os.system("echo 'gpgcheck=0' >> /etc/yum.repos.d/docker.repo")
                print("please prove us the root password for configuring yum")
                print()
                os.system("scp /etc/yum.repos.d/docker.repo root@{}:/etc/yum.repos.d/".format(ip))
                os.system("ssh {}@{} sudo yum install docker-ce --nobest -y".format(username,ip))
                print()
                print()
                print("Yum has been succesfully Configured !!!")
            elif int(b)==3:
                print()
                action=input("Enter your action>(start/stop/status): ")
                os.system("tput setaf 5")
                os.system("ssh {}@{} systemctl {} docker".format(username,ip,action))
                os.system("tput setaf 7")
            elif int(b)==4:
                os.system("ssh {}@{} docker images".format(username,ip))
            elif int(b)==5:
                image=input("Enter OSname:version to be downloaded(ex-ubuntu:20.10)) : ")
                os.system("ssh {}@{} docker pull {}".format(username,ip,image))
            elif int(b)==6:
                os.system("ssh {}@{} docker images".format(username,ip))
                image=input("Enter image name with version(ex:-ubuntu:20.10) : ")
                name= input("Enter a name you want to give to your container : ")
                os.system("ssh {}@{} docker run -it --name {} {}".format(username,ip,name,image))
            elif int(b)==7:
                os.system("ssh {}@{} docker ps -a".format(username,ip))
            elif int(b)==8:
                os.system("ssh {}@{} docker ps -a".format(username,ip))
                start=input("\nEnter the OS name/OS ID you want to boot : ")
                os.system("ssh {}@{} docker start {}".format(username,ip,start))
                os.system("ssh {}@{} docker attach {}".format(username,ip,start))
            elif int(b)==7:
                print("""\t\tWARNING!
                For terminating a Container firstly Authenticate yourself.
                """)
                password=gp.getpass("Enter Password:")
                if password == "arth":
                    print("Authentication Approved")
                    os.system("docker ps -a")
                    x=input("Enter the container id/name u want to terminate : ")
                    os.system("ssh {}@{}docker rm {}".format(username,ip,x))

                else:
                    os.system("tput setaf 1")
                    print("Ooooopss! Wrong password.")
                    os.system("tput setaf 7")
            elif int(b)==10:
                break
            elif int(b)==11:
               exitfun()
            else:
                os.system("tput setaf 1")
                print("Oooppps! Enter a valid command number.")
                os.system("tput setaf 7")
            input("<Press Enter To Continue>")

def hadoop(var1,username,ip):
    while True:
        os.system("clear")
        os.system("tput setaf 3")
        print("""
			\t\t88        88                       88
 			\t\t88        88                       88
 			\t\t88        88                       88
 			\t\t88aaaaaaaa88  ,adPPYYba,   ,adPPYb,88   ,adPPYba,    ,adPPYba,   8b,dPPYba,
  			\t\t88aaaaaaaa88  ""     `Y8  a8"    `Y88  a8"     "8a  a8"     "8a  88P'    "8a
 			\t\t88        88  ,adPPPPP88  8b       88  8b       d8  8b       d8  88       d8
 			\t\t88        88  88,    ,88  "8a,   ,d88  "8a,   ,a8"  "8a,   ,a8"  88b,   ,a8"
  			\t\t88        88  `"8bbdP"Y8   `"8bbdP"Y8   `"YbbdP"'    `"YbbdP"'   88`YbbdP"'
 			\t\t                                                                 88
 			\t\t                                                                 88
        """)
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t         Welcome to the our HADOOP Portal")
        os.system("tput setaf 4")
        print("\t\t\t\t\t\t         *****************************")
        os.system("tput setaf 2")
        print()
        os.system("tput setaf 7")
        print("\n")
        if ("local"in var1)or("LOCAL"in var1)or("Local"in var1)or("L"in var1):
            hadoopmenu()
            a=input("Enter command number u want to run : ")
            if int(a)==1:
                os.system("tput setaf 7")
                os.system("rpm -q hadoop")
                os.system("rpm -q jdk-8u171-linux-x64.rpm")
                print()
                input("<Press Enter to Continue>")
            elif int(a) == 2:
                os.system("tput setaf 2")
                os.system("yum install hadoop-1.2.1-1.x86_64 -y ")
                os.system("tput setaf 7")
                print()
                input("<Press Enter to Continue>")
            elif int(a) == 3:
                print("Hadoop Configuration")
                ask=input("Setup this system as a (Namenode/Datanode) :")
                if ("namenode" in ask)or("Namenode" in ask)or("NAMENODE" in ask):
                #setting up hdfs-site.xml file
                    os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
                #since setting up namenode so preset <>dfs.name.dir<>
                    os.system("echo '<name>dfs.name.dir</name>' >> /etc/hadoop/hdfs-site.xml")
                    folder=input("Enter a Folder name(without /): " )
                #creating a folder
                    os.system("mkdir /{}".format(folder))
                    os.system("echo '<value>/{}</value>' >> /etc/hadoop/hdfs-site.xml".format(folder))
                    os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '</configuration> ' >> /etc/hadoop/hdfs-site.xml")
            #competed
            #Now setting up core-site.xml file.
                    os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                    os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
                    os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
                    os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
                    os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
                    os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
                    ip=input("Enter Local IP Address: " )
                    os.system("echo '<value>hdfs://{}:9001</value>' >> /etc/hadoop/core-site.xml".format(ip))
                    os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
                    os.system("echo '</configuration> ' >> /etc/hadoop/core-site.xml")
                #completed setting up files
                    os.system("hadoop namenode -format")
                #will format linked folder.
                elif ("datanode" in ask) or ("Datanode" in ask) or ("DATANODE" in ask):
                #setting up hdfs-site.xml file
                    os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
                #since setting up namenode so preset <>dfs.data.dir<>
                    os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml")
                    folder=input("Enter a Folder name(without / ): " )
                #creating a folder
                    os.system("mkdir /{}".format(folder))
                    os.system("echo '<value>/{}</value>' >> /etc/hadoop/hdfs-site.xml".format(folder))
                    os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '</configuration> ' >> /etc/hadoop/hdfs-site.xml")
                #competed
                #Now setting up core-site.xml file.
                    os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
                    os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
                    os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
                    os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
                    os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
                    os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
                    ip=input("Enter Namenode IP Address: " )
                    os.system("echo '<value>hdfs://{}:9001</value>' >> /etc/hadoop/core-site.xml".format(ip))
                    os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
                    os.system("echo '</configuration> ' >> /etc/hadoop/core-site.xml")
                #completed
                else:
                    os.system("tput setaf 1")
                    print("You have to type either namenode or datanode")
                    os.system("tput setaf 7")
                input("<Press Enter to Continue>")
            elif int(a)==4:
                print("NOTE! pls type namenode/datanode in lowecase.")
                ques=input("You Configured Remote system as (namenode or datanode)? ")
                if ("namenode" in ques)or("datanode" in ques):
                    os.system("tput setaf 2")
                    os.system("hadoop-daemon.sh start {}".format(ques))
                    print()
                    os.system("jps")
                    os.system("tput setaf 7")
                print()
                input("<Press Enter to Continue>")
            elif int(a)==5:
                print("NOTE! pls type namenode/datanode in lowecase.")
                ques=input("You Configured Remote system as (namenode or datanode)? ")
                if ("namenode" in ques)or("datanode" in ques):
                    os.system("tput setaf 2")
                    os.system("hadoop-daemon.sh stop {}".format(ques))
                    os.system("jps")
                    os.system("tput setaf 7")
                print()
                input("<Press Enter to Continue>")
            elif int(a)==6:
                os.system("hadoop dfsadmin -report")
                print()
                input("<Press Enter to Continue>")
            elif int(a) == 7:
                x=input("Enter the file name : ")
                os.system("hadoop fs -put /root/{} /".format(x))
                input("<Press Enter to Continue>")
            elif int(a) == 8:
                os.system("hadoop fs -ls /")
                input("<Press Enter to Continue>")
            elif int(a) == 9:
                x=input("Enter the file name : ")
                os.system("hadoop fs -rm /{}".format(x))
                input("<Press Enter to Continue>")
            elif int(a) == 10:
                x=input("Enter the file name you transfered into cluster : ")
                os.system("hadoop fs -cat /{}".format(x))
                input("<Press Enter to Continue>")
            elif int(a)==11:
                break
            elif int(a)==12:
                exitfun()  
            else:
                os.system("tput setaf 1")
                print("Ooops! Enter a valid Number")
                os.system("tput setaf 7")
                input("<Press Enter to Continue>")
        
        elif ("remote"in var1)or("REMOTE"in var1)or("Remote"in var1)or("R"in var1):
            print()
            hadoopmenu()
            print()
            print()

            ch2 =input("Enter your choice : ")
            if int(ch2) == 1:
                os.system("ssh {}@{} rpm -q hadoop".format(username,ip))
                os.system("ssh {}@{} java -version".format(username,ip))
            elif int(ch2) == 2:
                os.system("scp jdk-8u171-linux-x64.rpm {}@{}:/root".format(username,ip))
                os.system("scp hadoop-1.2.1-1.x86_64.rpm {}@{}:/root".format(username,ip))
                os.system("ssh {}@{} rpm -ivh jdk-8u171-linux-x64.rpm".format(username,ip))
                os.system("ssh {}@{} rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force".format(username,ip))
            elif int(ch2) == 3:
                print("Hadoop Configuration")
                #setting up hdfs-site.xml file
                ask=input("Setup this system as a (Namenode/Datanode) :")
                os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site1.xml")
                os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site1.xml")
                os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site1.xml")
                os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site1.xml")
                os.system("echo '<property>' >> /etc/hadoop/hdfs-site1.xml")
                #since setting up according to user input(namenode/datanode)
                if ("namenode" in ask)or("Namenode" in ask)or("NAMENODE" in ask):
                    os.system("echo '<name>dfs.name.dir</name>' >> /etc/hadoop/hdfs-site1.xml")
                elif ("datanode" in ask)or("Datanode" in ask)or("DATANODE" in ask):
                    os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site1.xml")
                folder=input("Enter a Folder name only(without /): " )
                #creating a folder
                os.system("ssh {}@{} mkdir /{}".format(username,ip,folder))
                os.system("echo '<value>/{}</value>' >> /etc/hadoop/hdfs-site1.xml".format(folder))
                os.system("echo '</property>' >> /etc/hadoop/hdfs-site1.xml")
                os.system("echo '</configuration> ' >> /etc/hadoop/hdfs-site1.xml")
                #competed
                #Now setting up core-site.xml file.
                os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site1.xml")
                os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site1.xml")
                os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site1.xml")
                os.system("echo '<configuration>' >> /etc/hadoop/core-site1.xml")
                os.system("echo '<property>' >> /etc/hadoop/core-site1.xml".format(ip))
                os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site1.xml")

                if ("namenode" in ask)or("Namenode" in ask)or("NAMENODE" in ask):
                    ip1=input("Enter IP Address of that Remote system where namenode is to be configured: " )
                    os.system("echo '<value>hdfs://{}:9001</value>' >> /etc/hadoop/core-site1.xml".format(ip1))
                elif ("datanode" in ask)or("Datanode" in ask)or("DATANODE" in ask):
                    ip1=input("Enter IP Address of that system which was configured as Namenode:")
                    os.system("echo '<value>hdfs://{}:9001</value>' >> /etc/hadoop/core-site1.xml".format(ip1))
                os.system("echo '</property>' >> /etc/hadoop/core-site1.xml")
                os.system("echo '</configuration> ' >> /etc/hadoop/core-site1.xml")
                #competed
                #will format linked folder.
                os.system("scp /etc/hadoop/hdfs-site1.xml {}:/etc/hadoop/".format(username,ip))
                os.system("scp /etc/hadoop/core-site1.xml {}:/etc/hadoop/".format(username,ip))
                os.system("ssh {}@{} mv /etc/hadoop/hdfs-site1.xml /etc/hadoop/hdfs-site.xml".format(username,ip))
                os.system("ssh {}@{} mv /etc/hadoop/core-site1.xml /etc/hadoop/core-site.xml".format(username,ip))
                if ("namenode" in ask)or("Namenode" in ask)or("NAMENODE" in ask):
                    os.system("ssh {}@{} hadoop namenode -format".format(username,ip))
                os.system("ssh {}@{} cat /etc/hadoop/hdfs-site.xml".format(username,ip))
                os.system("ssh {}@{} cat /etc/hadoop/core-site.xml".format(username,ip))

            elif int(ch2)==4:
                print("NOTE! pls type namenode/datanode in lowecase.")
                ques=input("You Configured Remote system as (namenode or datanode)? ")
                if ("namenode" in ques)or("datanode" in ques):
                    os.system("ssh {}@{} hadoop-daemon.sh start {}".format(username,ip,ques))
                    os.system("ssh {}@{} jps".format(username,ip))
            elif int(ch2) == 5:
                print("NOTE! pls type namenode/datanode in lowecase.")
                ques=input("You Configured Remote system as (namenode or datanode)? ")
                if ("namenode" in ques)or("datanode" in ques):
                    os.system("ssh {}@{} hadoop-daemon.sh stop {}".format(username,ip,ques))
                    os.system("ssh {}@{} jps".format(username,ip))
            elif int(ch2) == 6:
                os.system("ssh {}@{} hadoop dfsadmin -report".format(username,ip))
            elif int(ch2) == 7:
                x=input("Enter the file name : ")
                os.system("ssh {}@{} hadoop fs -put /root/{} /".format(username,ip,x))
            elif int(ch2) == 8:
                os.system("ssh {}@{} hadoop fs -ls /".format(username,ip))
            elif int(ch2) == 9:
                x=input("Enter the file name : ")
                os.system("ssh {}@{} hadoop fs -rm /{}".format(username,ip,x))
            elif int(ch2) == 10:
                x=input("Enter the file name you transfered into cluster : ")
                os.system("ssh {}@{} hadoop fs -cat /{}".format(username,ip,x))
            elif int(ch2) == 11:
                break
            elif int(ch2) == 12:
                exitfun()
            else:
                os.system("tput setaf 1")
                print("Oooppps! Enter a valid command number.")
                os.system("tput setaf 7")
            input("<Press Enter to Continue>")


def linux():
        os.system("clear")
        os.system("tput setaf 3")
        print("""
 			\t\t88           88  888b      88  88        88  8b        d8
 			\t\t88           88  8888b     88  88        88   Y8,    ,8P
 			\t\t88           88  88 `8b    88  88        88    `8b  d8'
  			\t\t88           88  88  `8b   88  88        88      Y88P
   			\t\t88           88  88   `8b  88  88        88      d88b
   			\t\t88           88  88    `8b 88  88        88    ,8P  Y8,
   			\t\t88           88  88     `8888  Y8a.    .a8P   d8'    `8b
   			\t\t88888888888  88  88      `888   `"Y8888Y"'   8P        Y8
        """)
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t         Welcome to the our LINUX Portal")
        os.system("tput setaf 4")
        print("\t\t\t\t\t\t         *****************************")
        os.system("tput setaf 7")
        print()


def linuxtool(var3,username,ip):
    while True:
        os.system("clear")
        linux()
        if ("local" in var3)or("Local" in var3)or("LOCAL" in var3):
            os.system("tput setaf 3")
            print("This is the Local execution programm")
            print()
            os.system("tput setaf 2")
            linuxmenu()
            os.system("tput setaf 7")
            li=input("Enter command number u want to run : ")
            if int(li)==1:
                os.system("tput setaf 7")
                os.system("date")
            elif int(li)==2:
                os.system("tput setaf 7")
                os.system("cal")
            elif int(li)==3:
                os.system("tput setaf 7")
                user=input("Enter the name of the user : ")
                print()
                os.system("useradd {}".format(user))
                print("Please enter the passwd for this user : ")
                print()
                os.system("passwd {}".format(user))
            elif int(li)==4:
                os.system("tput setaf 7")
                os.system("ps -aux")
            elif int(li)==5:
                print("\t\t\tSome Pre-requisites")
                print("\t\t\t^^^^^^^^^^^^^^^^^^^")
                ask=input("Do you have YUM configured in this system?(y/n)")
                if ask != "y":
                    os.system("tput setaf 2")
                    yumconfig()
                    os.system("yum repolist")
                    os.system("tput setaf 7")
                print()
                ask2=input("Do you have httpd software intalled on this system?(y/n)")
                if ask2 != "y":
                    os.system("tput setaf 2")
                    os.system("yum install httpd")
                    os.system("tput setaf 7")
                print()
                ask3=input("Do you have your firewall services in active/running state?(y,n)")
                if ask3 != "y":
                    print()
                    print("We'll stop your services for configuring webserver.")
                    os.system("tput setaf 3")
                    os.system("systemctl stop firewalld")
                    os.system("tput setaf 7")
                os.system("systemctl start httpd")
                print()
                os.system("systemctl status httpd")
                os.system("tput setaf 5")
                print("Started Web-services ")
            elif int(li)==6:
             while True:
                os.system("clear")
                linux()
                os.system("tput setaf 3")
                print("\t\t\tThis is the Local execution programm")
                print("\t\t\t************************************")
                print()
                os.system("tput setaf 2")
                print("\n")
                print("""
            -> Press 1 : To check whether a Software is installed on remote systemor not.
            -> Press 2 : To Install a Software.
            -> Press 3 : To start services.
            -> Press 4 : To stop services.
            -> Press 5 : To check status of services.
            -> Press 6 : To start a service permenantly.
            -> Press 7 : To stop a service permenantly.
            -> Press 8 : To get back to the Previous menu.
            -> Press 9 : To get back to Main Menu.
            -> Press 10: To Exit.
            """)
                os.system("tput setaf 7")
                s=input("Enter command number u want to run : ")
                if int(s)==1:
                    print()
                    os.system("tput setaf 3")
                    print("Softwares such as:- docker-ce , httpd , python3 , vim , firefox , gedit.etc)")
                    os.system("tput setaf 7")
                    software=input("Enter the software name : ")
                    os.system("rpm -q {}".format(software))
                    print()
                    input("<Press Enter to Continue:>")
                elif int(s)==2:
                    print()
                    ask=input("Do you have YUM configured on this system?(y/n): ")
                    if ask != "y":
                        yumconfig()
                        os.system("yum repolist")
                        os.system("yum update")
                    os.system("tput setaf 2")
                    print("Softwares such as:- docker-ce , httpd , python3 , vim , firefox , gedit .etc)")
                    os.system("tput setaf 7")
                    software=input("Enter the software name you want to download : ")
                    if software=="docker-ce":
                        os.system("ssh {} yum install {} --nobest -y".format(ip,software))
                    else:
                        os.system("ssh {} yum install {}".format(ip,software))
                    print()
                    input("<Press Enter to Continue>")
                elif int(s)==3:
                    print()
                    os.system("tput setaf 3")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("Enter the Service name you want to start:")
                    os.system("systemctl start {}".format(service))
                    print()
                    input("<Press Enter to Continue:>")
                elif int(s)==4:
                    print()
                    os.system("tput setaf 3")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("Enter the Service name you want to stop:")
                    os.system("tput setaf 5") 
                    os.system("systemctl stop {}".format(service))
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to Continue>")
                elif int(s)==5:
                    print()
                    os.system("tput setaf 7")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("To check status,enter the Service name:")
                    os.system("tput setaf 5")
                    os.system("systemctl status {}".format(service))
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to Continue>")
                elif int(s)==6:
                    print()
                    os.system("tput setaf 7")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("Enter services name,you want to start permenantly:")
                    os.system("tput setaf 5")
                    os.system("systemctl start {}".format(service))
                    os.system("systemctl enable {}".format(service))
                    print()
                    input("<Press Enter to Continue:>")

                elif int(s)==7:
                    print()
                    os.system("tput setaf 7")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("Enter services name,you want to stop permenantly:")
                    os.system("tput setaf 5")
                    os.system("systemctl stop {}".format(service))
                    os.system("systemctl disable {}".format(service))
                    print()
                    input("<Press Enter to Continue:>")
                elif int(s)==8:
                    break
                elif int(s)==9:
                    main()
                elif int(s)==10:
                    exitfun()
                else:
                    os.system("tput setaf 1")
                    print("Ooops! Enter a valid Number")
                    os.system("tput setaf 7")
                    input("<Press Enter to continue:>")

            elif int(li)==7:
              while True:
                os.system("clear")
                linux()
                os.system("tput setaf 3")
                print()
                os.system("tput setaf 2")
                print("\n")
                
                print("""
          -> Press 1 : To list Attached volumes.
          -> Press 2 : To formate a volume.
          -> Press 3 : To load the drivers.
          -> Press 4 : To Create partition in a Volume.
          -> Press 5 : To format a partition.
          -> Press 6 : To mount a volume to a folder of your choice.
          -> Press 7 : To unmount a volume.
          -> Press 8 : To list the mounted volumes.
          -> Press 9 : To get back to previous menu.
          -> Press 10: To go to to Main Menu.
          -> Press 11: To Exit.
          """)
               
                os.system("tput setaf 7")
                print("\n")
                p=input("Enter command number u want to run : ")
                if int(p)==1:
                    os.system("fdisk -l")
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==2:
                    x=input("Type the volume name want to format:")
                    os.system("mkfs.ext4 {}".format(x))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==3:
                    os.system("udevadm settle")
                    print()
                    os.system("tput setaf 2")
                    print("Dreivers Loaded successfully.")
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==4:
                    x=input("Enter the Name of the volume,in which u want to create a partition")
                    os.system("fdisk {}".format(x))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==5:
                    x=input("Enter the name of the primary/logical parition u want to format")
                    os.system("mkfs.ext4 {}".format(x))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==6:
                    x=input("i am creating a folder for you,type a name for this folder:")
                    os.system("mkdir /{}".format(x))
                    os.system("mount /dev/sdc /{}".format(x))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==8:
                    os.system("df -h")
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==9:
                    break
                elif int(p)==10:
                    main()
                elif int(p)==11:
                    exitfun()  
                else:
                    os.system("tput setaf 1")
                    print("Ooops! Enter a valid command number")
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
            elif int(li)==8:
              while True:
                os.system("clear")
                linux()
                os.system("tput setaf 3")
                print("\t\t\tThis is the Local execution programm")
                print("\t\t\t************************************")
                print()
                os.system("tput setaf 2")
                print("\n")
               
                print("""
            -> Press 1 : To list Attached volumes.
            -> Press 2 : To formate a volume.
            -> Press 3 : To Create/Remove a Physical-Volume.
            -> Press 4 : To list all Physical-Volumes.
            -> Press 5 : To Create/Remove a Volume Group.
            -> Press 6 : To list all Volume Groups.
            -> Press 7 : To create/Remove a Logical Volume.
            -> Press 8 : To list all Logical Volumes.
            -> Press 9 : To formate and mount the Logical Volume.
            -> Press 10: To list the mounted volumes.
            -> Press 11: To increase the size of a Logical Volume.
            -> Press 12: To get back to the previous menu.
            -> Press 13: To go to Main Menu.
            -> Press 14: To Exit.
            """)
               
                os.system("tput setaf 7")
                print("\n")
                v=input("Enter command number u want to run : ")
                if int(v)==1:
                    os.system("fdisk -l")
                    print()
                    input("<Press Enter to continue>")
                elif int(v)==2:
                    print()
                    x=input("Type the volume name want to format:")
                    os.system("tput setaf 3")
                    os.system("mkfs.ext4 {}".format(x))
                    os.system("udevadm settle")
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
                elif int(v)==3:
                    print()
                    pvask=input("What do you want u to do?(create/remove) a PHYSICAL VOLUME : ")
                    print()
                    pv=input("Enter name of Volume you want to convert to Physical Volume.(ex- /dev/sdb) : ")
                    if ("create" in pvask) or ("remove"in pvask):
                        os.system("pv{} {}".format(pvask,pv))
                    else:
                        os.system("tput setaf 1")
                        print("Ooops! you have to write either create or remove!")
                        os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
                elif int(v)==4:
                    os.system("pvdisplay")
                    print()
                    input("<Press Enter to continue>")
                elif int(v)==5:
                    os.system("clear")
                    print("NOTE! Here is list of all PV")
                    print()
                    os.system("pvdisplay")
                    print()
                    print("REMARK : Volume Group(VG) is what we create when we combine Physical Volumes(PV) to create a single storage structure.")
                    print()
                    print("I can combine 2 PV to create a VG for you.")
                    print()
                    vg=input("Do you want to combine  your PV's to create a new Volume Group ?(y/n) : ")
                    if ("yes" in vg)or("y"in vg)or("Y"in vg)or("Yes"in vg)or ("YAS"in vg):
                        print()
                        pvname=input("Enter 1st PV name.(ex-/dev/sdb) : ")
                        pvname2=input("Enter 2nd PV name.(ex /dev/sdc) : ")
                        name=input("Enter a name for this VG(ex-myvg) :")
                        os.system("vgcreate {} {} {}".format(name,pvname,pvname2))
                        print()
                        input("<Press Enter to Continue>")
                    else:
                        break
                elif int(v)==6:
                    os.system("vgdisplay")

                elif int(v)==7:
                    print("\nCreating a Logical Volume(LV)")
                    x=input("Enter the size of LV (Size cannot be more then your VG size :")

                    y=input("Enter name of your choice to be given to this LV(*Required) :")
                    z=input("Enter the VG namefrom which this LV is to be created(*Required) :")
                    os.system("lvcreate --size {} --name {} {}".format(x,y,z))
                elif int(v)==8:
                    os.system("lvdisplay")
                    input("<Press Enter to continue>")
                elif int(v)==9:
                    print("<<Formatting a LV>>")
                    print()
                    print("NOTE! donot write the whole VG and LV name,just write that much as shown in example in next statement.")
                    a=input("Enter the VG name(*Required)[ex-myvg] : ")
                    b=input("Enter the LV name(*Required)[ex-mylv] : ")
                    os.system("mkfs.ext4 /dev/{}/{}".format(a,b))
                    print("\n<<Mounting this LV>>")
                    x=input("Give a folder name on which this LV is to be mounted : ")
                    os.system("mkdir /{}".format(x))
                    print(">Folder succefully created.")
                    os.system("mount /dev/{}/{}  /{}".format(a,b,x))
                    print(">LV  /dev/{}/{} was successfully mounted onto  /{} folder".format(a,b,x))

                    input("<Press Enter to continue>")
                elif int(v)==10:
                    os.system("df -h")
                    input("<Press Enter to continue>")
                elif int(v)==11:
                    print("\nNOTE!\n")
                    print("In order to increase/decrease the size of the LV ,You must have some space available inside your VG.")
                    print()
                    print("NOTE! donot write the whole VG and LV name,just write that much as shown in example in next statement.")
                    a=input("Enter the VG name(*Required)[eg-myvg] : ")
                    b=input("Enter the LV name(*Required)[eg-mylv]: ")
                    c=input("Enter increamental/decremental size starting with a (+/-) sign respectively (*Required)[ex: +5(g,m,k)/-5(g,m,k) : ")
                    os.system("lvextend --size {} /dev/{}/{}".format(c,a,b))
                    os.system("resize2fs /dev/{}/{}".format(a,b))
                    input("<Press Enter to continue>")
                elif int(v)==12:
                    break
                elif int(v)==13:
                    main()
                elif int(v)==14:
                    exitfun()
                else:
                    os.system("tput setaf 1")
                    print("Oooppps! Enter a valid command number")
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
            elif int(li)==9:
                main()
            elif int(li)==0:
                exitfun()
            else:
                os.system("tput setaf 1")
                print("Oooppps! Enter a valid command number")
                os.system("tput setaf 7")
                print()
                input("<Press Enter to continue>")
            input("Enter command to continue!!!")


        elif ("remote" in var3)or("REMOTE" in var3)or("Remote" in var3):
            print()
            os.system("clear")
            linux()
            os.system("tput setaf 3")
            print()
            os.system("tput setaf 10")
            print()
            print()
            linuxmenu()
            print()
            os.system("tput setaf 7")
            print("\n")
            c=input("Enter command number u want to run : ")
            if int(c)==1:
                os.system("tput setaf 2")
                os.system("ssh {}@{} date".format(username,ip))
                print()
                input("<Press Enter to Continue>")

            elif int(c)==2: 
                os.system("tput setaf 2")
                os.system("ssh {}@{} cal".format(username,ip))
                os.system("tput setaf 7")

            elif int(c)==3:
                os.system("tput setaf 2")
                os.system("ssh {}@{} ".format(username,ip))
            elif int(c)==4:
                os.system("tput setaf 7")
                os.system("ps -aux")
            elif int(c)==5:
                print("\t\t\tSome Pre-requisites")
                print("\t\t\t^^^^^^^^^^^^^^^^^^^")
                ask=input("Do you have YUM configured on that Remote system?(y/n)")
                if ask != "y":
                    os.system("tput setaf 10")
                    yumconfig()
                    yumssh()
                    os.system("yum repolist")
                    os.system("tput setaf 7")
                print()
                ask2=input("Do you have httpd software intalled on Remote system?(y/n)")
                if ask2 != "y":
                    os.system("tput setaf 2")
                    os.system("ssh {}@{} yum install httpd".format(username,ip))
                    os.system("tput setaf 7")
                print()
                ask3=input("Do you have your firewall services in active/running state?(y,n)")
                if ask3 != "y":
                    print()
                    print("We'll stop your firewall services for configuring webserver.")
                    os.system("ssh tput setaf 3")
                    os.system("ssh {}@{} systemctl stop firewalld".format(username,ip))
                    os.system("tput setaf 7")
                os.system("ssh {}@{} systemctl start httpd".format(username,ip))
                print()
                os.system("ssh {}@{} systemctl status httpd".format(username,ip))
                os.system("tput setaf 5")
                print("Started Web-services ")
            elif int(c)==6:
             while True:
                os.system("clear")
                linux()
                os.system("tput setaf 3")
                print("\t\t\tThis is the Remote execution programm")
                print("\t\t\t************************************")
                print()
                os.system("tput setaf 2")
                print("\n")
               
                print("""
            -> Press 1 : To check whether a Software is installed on remote systemor not.
            -> Press 2 : To Install a Software.
            -> Press 3 : To start services.
            -> Press 4 : To stop services.
            -> Press 5 : To check status of services.
            -> Press 6 : To start a service permenantly.
            -> Press 7 : To stop a service permenantly.
            -> Press 8 : To get back to the previous menu.
            -> Press 9 : To get back to the Main Menu.
            -> Press 10: To Exit.
            """)
              
                os.system("tput setaf 7")
                s=input("Enter command number u want to run : ")
                if int(s)==1:
                    print()
                    os.system("tput setaf 3")
                    print("Softwares such as:- docker-ce , httpd , python3 , vim , firefox , gedit.etc)")
                    os.system("ssh {}@{} tput setaf 7".format(username,ip))
                    software=input("Enter the software name : ")
                    os.system("ssh {}@{} rpm -q {}".format(username,ip,software))
                    print()
                    input("<Press Enter to Continue:>")
                elif int(s)==2:
                    print()
                    ask=input("Do you have YUM configured on this system?(y/n): ")
                    if ask != "y":
                        yumconfig()
                        os.system("ssh {}@{} yum repolist".format(username,ip))
                        os.system("ssh {}@{} yum update".format(username,ip))
                    os.system("tput setaf 2")
                    print("Softwares such as:- docker-ce , httpd , python3 , vim , firefox , gedit .etc)")
                    os.system("tput setaf 7")
                    software=input("Enter the software name you want to download : ")
                    if software=="docker-ce":
                        os.system("ssh {}@{} yum install {} --nobest -y".format(username,ip,software))
                    else:
                        os.system("ssh {}@{} yum install {}".format(username,ip,software))
                    print() 
                    input("<Press Enter to Continue>")
                elif int(s)==3:
                    print()
                    os.system("tput setaf 3")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("Enter the Service name you want to start:")
                    os.system("ssh {}@{} systemctl start {}".format(username,ip,service))
                    print()
                    input("<Press Enter to Continue>")
                elif int(s)==4:
                    print()
                    os.system("tput setaf 3")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("Enter the Service name you want to stop:")
                    os.system("tput setaf 5")
                    os.system("ssh {}@{} systemctl stop {}".format(username,ip,service))
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to Continue>")
                elif int(s)==5:
                    print()
                    os.system("tput setaf 7")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("To check status,enter the Service name:")
                    os.system("tput setaf 5")
                    os.system("ssh {}@{} systemctl status {}".format(username,ip,service))
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to Continue>")
                elif int(s)==6:
                    print()
                    os.system("tput setaf 7")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("Enter services name,you want to start permenantly:")
                    os.system("tput setaf 5")
                    os.system("ssh {}@{} systemctl start {}".format(username,ip,service))
                    os.system("ssh {}@{} systemctl enable {}".format(username,ip,service))
                    print()
                    input("<Press Enter to Continue:>")

                elif int(s)==7:
                    print()
                    os.system("tput setaf 7")
                    print("Available Services:- firewalld , docker ,httpd .etc")
                    os.system("tput setaf 7")
                    service=input("Enter services name,you want to stop permenantly:")
                    os.system("tput setaf 5")
                    os.system("ssh {}@{} systemctl stop {}".format(username,ip,service))
                    os.system("ssh {}@{} systemctl disable {}".format(username,ip,service))
                    print()
                    input("<Press Enter to Continue:>")
                elif int(s)==8:
                    break
                elif int(s)==9:
                    maim()  
                elif int(s)==10:
                    exitfun()     
                else:
                    os.system("tput setaf 1")
                    print("Ooops! Enter a valid Number")
                    os.system("tput setaf 7")
                    input("<Press Enter to continue:>")

            elif int(c)==7:
              while True:
                os.system("clear")
                linux()
                os.system("tput setaf 3")
                
                print()
                os.system("tput setaf 2")
                print("\n")
              
                print("""
          -> Press 1 : To list Attached volumes.
          -> Press 2 : To formate a volume.
          -> Press 3 : To load the drivers.
          -> Press 4 : To Create partition in a Volume.
          -> Press 5 : To format a partition.
          -> Press 6 : To mount a volume to a folder of your choice.
          -> Press 7 : To unmount a volume.
          -> Press 8 : To list the mounted volumes.
          -> Press 9 : To get back to previous menu.
          -> Press 10: To get back to Main Menu.
          -> Press 11: To Exit.
          """)
             
                os.system("tput setaf 7")
                print("\n")
                p=input("Enter command number u want to run : ")
                if int(p)==1:
                    os.system("ssh {}@{} fdisk -l".format(username,ip))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==2:
                    x=input("Type the volume name want to format:(ex- /dev/sdb)")
                    os.system("ssh {}@{} mkfs.ext4 {}".format(username,ip,x))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==3:
                    os.system("ssh {}@{} udevadm settle".format(username,ip))
                    print()
                    os.system("tput setaf 2")
                    print("Drivers Loaded successfully.")
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==4:
                    x=input("Enter the Name of the volume,in which u want to create a partition.(ex- /dev/sdb")
                    os.system("ssh {}@{} fdisk {}".format(username,ip,x))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==5:
                    x=input("Enter the name of the primary/logical parition u want to format")
                    os.system("ssh {}@{} mkfs.ext4 {}".format(username,ip,x))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==6:
                    x=input("i am creating a folder for you,type a name for this folder:")
                    os.system("ssh {}@{} mkdir /{}".format(username,ip,x))
                    os.system("ssh {}@{} mount /dev/sdc /{}".format(username,ip,x))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==7:
                    x=input("Enter Volume name you want to unmount.(ex-/dev/sdc):")
                    os.system("ssh {}@{} umount {}".format(username,ip,x))
                    print()
                    input("<Press Enter to continue>")

                elif int(p)==8:
                    os.system("ssh {}@{} df -h".format(username,ip))
                    print()
                    input("<Press Enter to continue>")
                elif int(p)==9:
                    break
                elif int(p)==10:
                    main()
                elif int(p)==11:
                    exitfun()
                else:
                    os.system("tput setaf 1")
                    print("Ooops! Enter a valid command number")
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
            elif int(c)==8:
              while True:
                os.system("clear")
                linux()
                os.system("tput setaf 3")
                print("\t\t\tThis is the Remote execution programm")
                print("\t\t\t*************************************")
                print()
                os.system("tput setaf 2")
                print("\n")
              
                print("""
            -> Press 1 : To list Attached volumes.
            -> Press 2 : To formate a volume.
            -> Press 3 : To Create/Remove a Physical-Volume.
            -> Press 4 : To list all Physical-Volumes.
            -> Press 5 : To Create/Remove a Volume Group.
            -> Press 6 : To list all Volume Groups.
            -> Press 7 : To create/Remove a Logical Volume.
            -> Press 8 : To list all Logical Volumes.
            -> Press 9 : To formate and mount the Logical Volume.
            -> Press 10: To list the mounted volumes.
            -> Press 11: To increase the size of a Logical Volume.
            -> Press 12: To get back to the previous menu.
            -> Press 13: To get back to the Main Menu.
            -> Press 14: To Exit.
            """)
               
                os.system("tput setaf 7")
                print("\n")
                v=input("Enter command number u want to run : ")
                if int(v)==1:
                    os.system("ssh {}@{} fdisk -l".format(username,ip))
                    print()
                    input("<Press Enter to continue>")
                elif int(v)==2:
                    print()
                    x=input("Type the volume name want to format:")
                    os.system("tput setaf 3")
                    os.system("ssh {}@{} mkfs.ext4 {}".format(username,ip,x))
                    os.system("ssh {}@{} udevadm settle".format(username,ip,x))
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
                elif int(v)==3:
                    print()
                    pvask=input("What do you want u to do?(create/remove) a PHYSICAL VOLUME : ")
                    print()
                    pv=input("Enter name of Volume you want to convert to Physical Volume.(ex- /dev/sdb) : ")
                    if ("create" in pvask) or ("remove"in pvask):
                        os.system("ssh {}@{} pv{} {}".format(username,ip,pvask,pv))
                    else:
                        os.system("tput setaf 1")
                        print("Ooops! you have to write either create or remove!")
                        os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
                elif int(v)==4:
                    os.system("ssh {}@{} pvdisplay".format(username,ip))
                    print()
                    input("<Press Enter to continue>")
                elif int(v)==5:
                    print("NOTE! Here is list of all PV")
                    print()
                    os.system("ssh {}@{} pvdisplay".format(username,ip))
                    print()
                    print("REMARK : Volume Group(VG) is what we create when we combine Physical Volumes(PV) to create a single storage structure.")
                    print()
                    print("I can combine 2 PV to create a VG for you.")
                    print()
                    vg=input("Do you want to combine  your PV's to create a new Volume Group ?(y/n) : ")
                    if ("yes" in vg)or("y"in vg)or("Y"in vg)or("Yes"in vg)or ("YAS"in vg):
                        print()
                        pvname=input("Enter 1st PV name.(ex-/dev/sdb) : ")
                        pvname2=input("Enter 2nd PV name.(ex /dev/sdc) : ")
                        name=input("Enter a name for this VG(ex-myvg) :")
                        os.system("ssh {}@{} vgcreate {} {} {}".format(username,ip,name,pvname,pvname2))
                        print()
                        input("<Press Enter to Continue>")
                    else:
                        break
                elif int(v)==6:
                    os.system("ssh {}@{} vgdisplay".format(username,ip))

                elif int(v)==7:
                    print("\nCreating a Logical Volume(LV)")
                    x=input("Enter the size of LV (Size cannot be more then your VG size :")

                    y=input("Enter name of your choice to be given to this LV(*Required) :")
                    z=input("Enter the VG namefrom which this LV is to be created(*Required) :")
                    os.system("ssh {}@{} lvcreate --size {} --name {} {}".format(username,ip,x,y,z))
                elif int(v)==8:
                    os.system("ssh {}@{} lvdisplay".format(username,ip))
                    input("<Press Enter to continue>")
                elif int(v)==9:
                    print("<<Formatting a LV>>")
                    print()
                    print("NOTE! donot write the whole VG and LV name,just write that much as shown in example in next statement.")
                    a=input("Enter the VG name(*Required)[ex-myvg] : ")
                    b=input("Enter the LV name(*Required)[ex-mylv] : ")
                    os.system("ssh {}@{} mkfs.ext4 /dev/{}/{}".format(username,ip,a,b))
                    print("\n<<Mounting this LV>>")
                    x=input("Give a folder name on which this LV is to be mounted : ")
                    os.system("ssh {}@{} mkdir /{}".format(username,ip,x))
                    print(">Folder succefully created.")
                    os.system("ssh {}@{} mount /dev/{}/{}  /{}".format(username,ip,a,b,x))
                    print(">LV  /dev/{}/{} was successfully mounted onto  /{} folder".format(a,b,x))

                    input("<Press Enter to continue>")
                elif int(v)==10:
                    os.system("ssh {}@{} df -h".format(username,ip))
                    input("<Press Enter to continue>")
                elif int(v)==11:
                    print("\nNOTE!\n")
                    print("In order to increase/decrease the size of the LV ,You must have some space available inside your VG.")
                    print()
                    print("NOTE! do not write the whole VG and LV name,just write that much as shown in example in next statement.")
                    a=input("Enter the VG name(*Required)[eg-myvg] : ")
                    b=input("Enter the LV name(*Required)[eg-mylv]: ")
                    c=input("Enter increamental/decremental size starting with a (+/-) sign respectively (*Required)[ex: +5(g,m,k)/-5(g,m,k) : ")
                    os.system("ssh {}@{} lvextend --size {} /dev/{}/{}".format(username,ip,c,a,b))
                    os.system("ssh {}@{} resize2fs /dev/{}/{}".format(username,ip,a,b))
                    input("<Press Enter to continue>")
                elif int(v)==12:
                    break
                elif int(v)==13:
                    main()
                elif int(v)==14:
                    exitfun()
                else:
                    os.system("tput setaf 1")
                    print("Oooppps! Enter a valid command number")
                    os.system("tput setaf 7")
                    print()
                    input("<Press Enter to continue>")
            elif int(c)==9:
                break
            elif int(c)==0:
                exitfun()
            else:
                os.system("tput setaf 1")
                print("Oooppps! Enter a valid command number")
                os.system("tput setaf 7")

def main():
    while True:
        os.system("clear")
        os.system("tput setaf 3")
        print("""
	       	    d8888         888    888           .d8888b.                                          888
        	   d88888         888    888          d88P  Y88b                                         888
                  d88P888         888    888          888    888                                         888
	         d88P 888 888d888 888888 88888b.      888        888d888 888  888 .d8888b   8888b.   .d88888  .d88b.  888d888 .d8888b
        	d88P  888 888P"   888    888 "88b     888        888P"   888  888 88K          "88b d88" 888 d8P  Y8b 888P"   88K
               d88P   888 888     888    888  888     888    888 888     888  888 "Y8888b. .d888888 888  888 88888888 888     "Y8888b.
	      d8888888888 888     Y88b.  888  888     Y88b  d88P 888     Y88b 888      X88 888  888 Y88b 888 Y8b.     888          X88
             d88P     888 888      "Y888 888  888      "Y8888P"  888      "Y88888  88888P' "Y888888  "Y88888  "Y8888  888      88888P'
               	""")
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t\tWelcome to Arth Crusaders Services")
        os.system("tput setaf 4")
        print("\t\t\t\t\t\t\t**********************************")
        os.system("tput setaf 2")
        print()
        print("NOTE! Pls execute the script in FULL-SCREEN MODE for better user interface/expirence")
        print()
        print("\u058D Please specify the type of domain service you want :")
        print()
        os.system("tput setaf 6")
        print("""
       	                \u058D press 1:AMAZON WEB SERVICES
               	        \u058D press 2:APACHE HADOOP
                        \u058D press 3:DOCKER
                        \u058D press 4:LINUX
                        \u058D press 5:EXIT
	          """)
        os.system("tput setaf 3")
        value=int(input("Please Enter Your Choice:"))
        if value==1:
            aws()
        elif value==2:
            var1=input("Where do you want to use this service?(local/remote) :")
            if var1=="remote":
                ip=input("Type the Public IP Address of remote system : ")
                print()
                username=input("Type the username of remote system other thn the root user: ")
                sshkey(username,ip)
            else:
                username=0
                ip=0
            hadoop(var1,username,ip)
        elif value==3:
            var=input("Where do you want to use this service?(local/remote) :")
            if var=="remote":
                ip=input("Type the Public IP Address of remote system : ")
                print()
                username=input("Type the username of remote system other thn the root user: ")
                sshkey(username,ip)
            else:
                username=0
                ip=0
            docker(var,username,ip)
        elif value==4:
            var3=input("Where do you want to use this service?(local/remote) :")
            if var3=="remote":
                ip=input("Type the Public IP Address of remote system : ")
                print()
                username=input("Type the username of remote system other thn the root user: ")
                sshkey(username,ip)
            else:
                username=0
                ip=0
            linux()
            linuxtool(var3,username,ip)
        elif value==5:
            exitfun()
        else:
            print("You've entered wrong input!!")
            os.system("tput setaf 2")
            input("\t\t\t\t\t\t\t    press any key to Continue!!")
main()
os.system("tput setaf 3")
os.system("setenforce 1")
