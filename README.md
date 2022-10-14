# jrxmlEditor Script

**Description:**


This python script allows us to apply one or multiple updates to a .jrxml file at once on it's execution. On this version (V3.0), the intention is to make all the .jrxml files inside the a folder, compatible with the Dev environment (All the converted files will be stored inside another folder that can be setup).

The main difference between the V(2.0) version and this (V3.0) version, is that this one got modified in order to be excecuted using GitHub Actions (automatic updates) instead of the previous manual  way (V2.0) where we want to execute an .exe file locally.

*This script contains several updates that will be listed here, all these updates are necessary for making any .jrxml file compatible with Dev environment:*

- Replace: com.monolithss.abovestore.jr.date.JRTimestampRange => com.monolithss.oneview.jr.date.JRTimestampRange
- Replace: com.monolithss.abovestore.jr.date.JRDateRangeBuilder => com.monolithss.oneview.jr.date.JRDateRangeBuilder
- Replace: =>
- Replace: Config.getDbEncryptionSalt() => Config.getDbEncryptionKey()
- Replace: ($P{LoggedInUserTenantId} != null) ? "repo:Logo" : "OdsLogo137x37.jpg" => ($P{LoggedInUserTenantId} != null) ? "/Files/images/logo.png" : "OdsLogo137x37.jpg"
- Replace: ($P{LoggedInUserTenantId} != null) ? "repo:Logo" : "oneVIEWReportLogo.png" => ($P{LoggedInUserTenantId} != null) ? "/Files/images/logo.png" : "oneVIEWReportLogo.png"
- Replace: ($P{LoggedInUserTenantId} != null) ? "repo:MainStyle.jrtx" : "MainStyle.jrtx" => ($P{LoggedInUserTenantId} != null) ? "/Files/jrtx/MainStyle.jrtx" : "MainStyle.jrtx"
- Replace: ($P{LoggedInUserTenantId} != null) ? "repo:oneVIEWStyle.jrtx" : "oneVIEWStyle.jrtx" => ($P{LoggedInUserTenantId} != null) ? "/Files/jrtx/oneVIEWStyle.jrtx" : "oneVIEWStyle.jrtx"
- Keep: com.monolithss.abovestore.jr.date.DateUtils.addNoOfDays
- Keep: com.monolithss.abovestore.jr.collections.MapBuilder

As mentioned above, once all these updates are applied inside the .jrxml file, it will be compatible with the Dev environment and will be displayed with no issues (Add input controls, if required)

*To execute the script, and make .jrxml files compatible with Dev environment. Just upload or update something in the repository, this way the script will be triggered and will convert all files inside the origin folder folder, once the process is done all results will be contained inside the results folder after 15 seconds. 

NOTE: Inside each folder (Files,Results,src) you can also find an "info.txt" file with more detailed information.
