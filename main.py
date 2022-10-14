import logging
import logging.handlers
import os

import requests                                                                   # Time is used for waiting x amount of seconds, on this case is used for waiting for the Organization field to be displayed on Oneview's login                                                         
from os import walk                                                            # library used to know the file names of the .jrxml files to be converted


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


try:
    SCRIPT_SECRET_TOKEN = os.environ["SCRIPT_SECRET_TOKEN"]
except KeyError:
    SCRIPT_SECRET_TOKEN = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {SCRIPT_SECRET_TOKEN}")

    print("It executes this part of the script")


    print("*********************************Program Started*********************************\n")


    origin_path = "TestFolder"
    save_path = "ResultsFolder"                             # And also sets a destination folder to save the results
    os.makedirs(save_path, exist_ok=True) 

    filenames = next(walk(origin_path), (None, None, []))[2]  # Aims to folder that contains all files that will be converted and gets all filenames

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
