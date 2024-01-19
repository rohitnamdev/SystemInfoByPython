'''
firstly run these commands in your terminal
pip install windows_tools.installed_software from PIP
pip install speedtest-cli
pip install psutil
pip install public-ip
pip install wmi

'''
from windows_tools.installed_software import get_installed_software
import speedtest, tkinter, psutil, platform,public_ip, uuid,wmi, GPUtil

#1. All Installed software’s list
installed_software =  get_installed_software()

#2.Internet Speet
def get_internet_speed():
   st = speedtest.Speedtest()
   dwspeed = st.download() / 1000000  # Convert to Mbps
   upspeed = st.upload() / 1000000  # Convert to Mbps
   return dwspeed,upspeed

#3.Screen Resolution
def get_resolution():
   res = tkinter.Tk()
   width, height = res.winfo_screenwidth(), res.winfo_screenheight()
   return width,height
    
#Main Function
if __name__ == "__main__":
   
    #1. All installed software
    for software in installed_software:
        print(software['name'], software['version'], software['publisher'])

    #2. Internet Speed
    print("Waiting for check internet speed")
    dwspeed,upspeed = get_internet_speed()
    print("Internet Download Speed: {:.2f} Mbps".format(dwspeed),"\nInternet upload Speed: {:.2f} Mbps".format(upspeed))

    #3. Screen Resolution
    width, height = get_resolution()
    print(f"Screen Resolution is : width = {width} and height = {height} pixels")

    #4. Model
    temp = wmi.WMI()
    model = temp.Win32_ComputerSystem()[0]
    print("Cpu information with model: ",model.Model)

    #5. Get number of Core and Threads
    print(f"Total number of Core is : {psutil.cpu_count(logical=False)} \nTotal number of Threads is : {psutil.cpu_count()}") 
    
    #6. Get GPU Model, its return [] if we dont have GPU
    print("Gpu information with model:", GPUtil.getAvailable())

    #7. get Ram Size
    vm = psutil.virtual_memory() 
    print("RAM memory {:.2f} GB total".format(vm.total/1000000000))
    
    #9. Wifi/Ethernet MAC Address
    print("MAC address in Integer formate",uuid.getnode()) #40 bit integer
    print("MAC addres in byte formate: ")
    print (":".join(f"{b:02x}" for b in uuid.getnode().to_bytes(6))) #Formated

    #10. Get public ip address
    print("The Public IP Address is  : ",public_ip.get())

    #11. Windows or OS version
    print("The version of Windows is : ",platform.platform()) 
