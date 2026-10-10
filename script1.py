import subprocess 
import os 
import time 

def launch_programs(program):
    try:
        subprocess.Popen(program)
        print(f"Program is starting: {program}")
    except:
        print(f"Program not found:{program}")
#path of application's .exe file
programs = {
    "chrome":r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vmware": r"C:\Program Files\VMware\VMware Workstation\vmware.exe"
}

def check_program(program):
   if os.path.exists(program):
       return True
   else:
       return False
   
def main():
    for program in programs:
        if check_program(program):
            launch_programs(program)
            time.sleep(3)
        else:
            print(f"Could not start {program}") 

if __name__ == "__main__":
    main()
