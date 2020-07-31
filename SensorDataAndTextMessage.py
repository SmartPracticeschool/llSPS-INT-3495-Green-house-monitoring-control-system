import time
import sys
import ibmiotf.application
import ibmiotf.device
import requests
#Edit contact number to the number you want the message alert sent to.

contactnumber="9600118027"

#Provide your IBM Watson Device Credentials
organization = "zsilpn"
deviceType = "raspberrypi"
deviceId = "123456"
authMethod = "token"
authToken = "12345678"

url = "https://www.fast2sms.com/dev/bulk"


# Initialize GPIO

def myCommandCallback(cmd):
        #print("Command received: %s" % cmd.data)
        #print(type(cmd.data))
        i=(cmd.data["T"])
        j=(cmd.data["H"])
        k=(cmd.data["M"])
        
        if(i<=40):
                print("Temperature is",i,"(optimal)")
        else:
                print("Temperature exceeded 40. Text alert is being sent to mobile.")
                querystring = {"authorization":"d6tkSx1N5vyGmYjz7uIALZ90MRprehPfJsboTCqlFXQcBEWHg89KBj7LJrmGZRdHYxSavbA164zPcniq","sender_id":"FSTSMS","message":"Alert! Temperature exceeded the threshold of 40. Take necessary actions.","language":"english","route":"p","numbers":contactnumber}

                headers = {
                    'cache-control': "no-cache"
                }

                response = requests.request("GET", url, headers=headers, params=querystring)

                print(response.text)
                print("Text message has been sent about Temperature reaching above threshold value.\nExiting python code now.")        

                exit(0)        
                
        if (j<=90):
                print("Humidity is",j,"(optimal)")
        else:
                print("Humidity exceeded 90. Text alert is being sent to mobile.")
                querystring = {"authorization":"d6tkSx1N5vyGmYjz7uIALZ90MRprehPfJsboTCqlFXQcBEWHg89KBj7LJrmGZRdHYxSavbA164zPcniq","sender_id":"FSTSMS","message":"Alert! Humidity exceeded the threshold of 90. Take necessary actions.","language":"english","route":"p","numbers":contactnumber}

                headers = {
                    'cache-control': "no-cache"
                }

                response = requests.request("GET", url, headers=headers, params=querystring)

                print(response.text)
                print("Text message has been sent about Humidity reaching above threshold value.\nExiting python code now.")        



                exit(0)

        print("Soil moisture content is",k)

        

try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)#.............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
