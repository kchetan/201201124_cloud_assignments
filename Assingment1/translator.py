def translate():
	source_file_name=raw_input("Source file name : ")


	print "Destination file name : ",
	#takes name of destination file
	destination_file_name=raw_input()


	f=open(source_file_name,'r')
	f2=open(destination_file_name,"w")

	lines=f.readlines()
	strin=''

	for line in lines:
	    l=line.split("\n")

	    words=l[0].split()
	    for word in words:
	        if word=='eax,':
	            strin=strin + 'rax,'
	        elif word=='ebx,':
	            strin=strin + 'rbx,'
	        elif word=='ecx,':
	            strin=strin + 'rcx,'
	        elif word=='edx,':
	            strin=strin + 'rdx,'
	        elif word=='esp,':
	            strin=strin + 'rsp,'
	        elif word=='ecx,':
	            strin=strin + 'rcx,'
	        elif word=='ecx,':
	            strin=strin + 'rcx,'
	        elif word=='eax':
	            strin=strin + 'rax'
	        elif word=='ebx':
	            strin=strin + 'rbx'
	        elif word=='ecx':
	            strin=strin + 'rcx'
	        elif word=='edx':
	            strin=strin + 'rdx'
	        elif word=='esp':
	            strin=strin + 'rsp'
	        elif word=='ecx':
	            strin=strin + 'rcx'
	        elif word=='ecx':
	            strin=strin + 'rcx'
	        else:
	            strin=strin+word+' ' 
	    strin=strin+'\n'

	f2.write(strin)

if __name__ == "__main__":
	translate()