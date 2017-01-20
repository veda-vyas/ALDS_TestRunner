import os.path,subprocess
from subprocess import STDOUT,PIPE

program_name = 'MaxSum.java'

def get_content(filename):
	with open(filename) as f:
		return f.read()

def execute(java_file, stdin):
    java_class,ext = os.path.splitext(java_file)
    subprocess.check_call(['javac', java_file])     #compile
    cmd = ['java', java_class]                      #execute
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout,stderr = proc.communicate(stdin)
    return stdout

def run_test(testcase_input,testcase_output):
	input = get_content(testcase_input)
	output = get_content(testcase_output)
	your_output = execute(program_name, input)
	your_output = your_output.replace('\r','').rstrip() #remove trailing newlines, if any
	return input,output,your_output,output==your_output

def run_tests(inputs,outputs):
	passed = 0
	for i in range(len(inputs)):
		result = run_test(inputs[i],outputs[i])
		if result[3] == True:
			print "########## Testcase "+str(i)+": Passed ##########"
			print "Input: "
			print result[0]+"\n"
			print "Expected Output: "
			print result[1]+"\n"
			print "Your Output: "
			print result[2]+"\n"
			passed+=1
		else:
			print "########## Testcase "+str(i)+": Failed ##########"
			print "Input: "
			print result[0]+"\n"
			print "Expected Output: "
			print result[1]+"\n"
			print "Your Output: "
			print result[2]+"\n"
		print "----------------------------------------"
	print "Result: "+str(passed)+"/"+str(len(inputs))+" testcases passed."

inputs = []
outputs = []

# populate input and output lists
for root,dirs,files in os.walk('.'):
	for file in files:
		if 'input' in file and '.txt' in file:
			inputs.append(file)
		if 'output' in file and '.txt' in file:
			outputs.append(file)

inputs = sorted(inputs)
outputs = sorted(outputs)
run_tests(inputs,outputs)
