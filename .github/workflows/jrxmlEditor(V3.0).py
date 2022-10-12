import time                                                                    # Time is used for waiting x amount of seconds, on this case is used for waiting for the Organization field to be displayed on Oneview's login                                                         
from os import walk                                                            # library used to know the file names of the .jrxml files to be converted
import os

'''
GITHUB ACTIONS REVIEW THIS
'''

print("*********************************Program Started*********************************\n")


origin_path = input("Source path: ")
save_path = input("Destination path: ")                               # And also sets a destination folder to save the results
os.makedirs(save_path, exist_ok=True) 

filenames = next(walk('./Files'), (None, None, []))[2]  # Aims to folder that contains all files that will be converted and gets all filenames

for name in filenames:                                  # For each report (filename) make an iteration

    fileName = name
    print("The file '"+fileName+"' is being processed...")
    
    # Open file containing xml text and copy contents to string
    f = open(origin_path+"/"+fileName, "r+")                                   # Where it will read the xml file context 
    xmlText = f.read()
    xmlText2 = xmlText                                                         # Save it into a secondary/testeable variable
    # Bring pointer back to start of file and delete all contents
    f.seek(0)
    f.truncate()                                                               # To finally find and replace all the necessary strings, applyng all "changes"
    
    
    ChangeN1 = xmlText2.replace("com.monolithss.abovestore.jr.date.JRTimestampRange", "com.monolithss.oneview.jr.date.JRTimestampRange")
    ChangeN2 = ChangeN1.replace("com.monolithss.abovestore.jr.date.JRDateRangeBuilder", "com.monolithss.oneview.jr.date.JRDateRangeBuilder")
    ChangeN3 = ChangeN2.replace('<import value="com.monolithss.abovestore.jr.Config"/>', '<import value="com.monolithss.oneview.jr.Config"/>')
    ChangeN4 = ChangeN3.replace("Config.getDbEncryptionSalt()", "Config.getDbEncryptionKey()")
    ChangeN5 = ChangeN4.replace("com.monolithss.abovestore.jr.date.DateUtils.addNoOfDays", "com.monolithss.abovestore.jr.date.DateUtils.addNoOfDays")
    ChangeN6 = ChangeN5.replace("com.monolithss.abovestore.jr.collections.MapBuilder", "com.monolithss.abovestore.jr.collections.MapBuilder")
    ChangeN7 = ChangeN6.replace('($P{LoggedInUserTenantId} != null) ? "repo:Logo" : "OdsLogo137x37.jpg"', '($P{LoggedInUserTenantId} != null) ? "/Files/images/logo.png" : "OdsLogo137x37.jpg"')
    ChangeN8 = ChangeN7.replace('($P{LoggedInUserTenantId} != null ) ? "repo:Logo" : "oneVIEWReportLogo.png"', '($P{LoggedInUserTenantId} != null) ? "/Files/images/logo.png" : "oneVIEWReportLogo.png"')
    ChangeN9 = ChangeN8.replace('($P{LoggedInUserTenantId} != null) ? "repo:MainStyle.jrtx" : "MainStyle.jrtx"', '($P{LoggedInUserTenantId} != null) ? "/Files/jrtx/MainStyle.jrtx" : "MainStyle.jrtx"')
    ChangeN10 = ChangeN9.replace('($P{LoggedInUserTenantId} != null) ? "repo:oneVIEWStyle.jrtx" : "oneVIEWStyle.jrtx"', '($P{LoggedInUserTenantId} != null) ? "/Files/jrtx/oneVIEWStyle.jrtx" : "oneVIEWStyle.jrtx"')
    
    # Write this new text with replaced words to the file and close
    
    f2 = open(save_path+"/"+"(Dev)"+fileName, "w")                             # Once all changes are applied we just proceed to write the new .jrxml files (adding extra (Dev) tag)
    
    f2.write(ChangeN10)
    f.write(xmlText)                                                           # We can see all resulting files, inside the Results folder that must be inside the same folder as the script
    f.close()
    f2.close() 
    
print("\nAll files were processed!\n") 

print("*********************************Program finished*********************************")

time.sleep(8)

'''
print("Creating files inside the app...")

userorglist = ['jem']
print("***********************************************************************************\n")
user = input("Username: ")
#userpass = pwinput.pwinput()
userpass = "v4uk7Z355wt3%U"                                            
for line in userorglist:                                                             # We define a variable called browser, which will contain the web driver, on this case Firefox is used, but Chrome, Opera or any other is also allowed
    browser = webdriver.Firefox() 
    #browser.get('https://oneview.onedatasource.com/')                                # Opens the URL given on the web browser
    browser.get('https://oneview-dev.onedatasource.com/')
    userorg = str(line)
    action = ActionChains(browser)    
                                
                          
    stat = False                                                                      # Waiting for the Organization field to be displayed in the UI
    while stat == False:
        try:
            step1 = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="orgId"]')))  
            displayedz = step1.is_displayed()
            if displayedz == True:
                stat = True                                                           # Selects the organization field and writes the credentials
        except:
            time.sleep(1)
    
    
    
    step1.send_keys(userorg)                       
    
    step2 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="j_username"]')))          # Selects the username field and writes the credentials
    step2.send_keys(user)  
     
    step3 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="j_password_pseudo"]')))   # Selects the Password field and writes the credentials
    step3.send_keys(userpass)  
        
    step4 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="submitButton"]')))        # Aims to the submit button and clicks on it
    step4.click()  
    
    browser.get('https://oneview-dev.onedatasource.com/asp/flow.html?_flowId=searchFlow')                               # Now that we are logged in, we go to categories using the url directly (saving clicks)
    #browser.get('https://oneview.onedatasource.com/asp/flow.html?_flowId=searchFlow')   
    
    step5 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="handler2"]')))            # This is where it navigates through the folders, in order to get to the folder we want to review
    step5.click()
     
    step6 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="handler8"]'))) 
    #step6 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="handler011"]')))           # The objective is to detect how many elements are inside the folder, and then review all of them
    step6.click()  
    
    #step7 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="node13"]')))     
    step7 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="handler10"]')))      # If we want to realize and exhaustive review through all folders, we would just need to edit this scope
    step7.click()  
    
    step8 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="node10"]')))  
    
    action.context_click(step8).perform()   

    step9 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/ul/li[2]/p')))
    step9.click()
    
    step10 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/ul/li[2]/div/div/ul/li[6]/p')))
    step10.click()
    
    step11 = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fake_upload_button"]')))

    '''