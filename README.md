#Resume must be in NLP(Natural Language Processing) Format#

this was tested in VS code using Live server extention so first download it and 
keep Live server setting to this- 
uncheck first this-
Live Server - Settings: Wait
Live Server - Settings: Full Reload
Live Server - Settings: Auto Save
and keep
liveServer.settings.wait to 999999 to avoid reloading page after parse

-run app.py
-upload pdf 
 limition in this code is it doesnot extract Name from any Resume due to limitation of Keywords
it requires NLP(Natural Language Processing) resume type where text is in editable form.
separate script.js file is been made to display it on same site or go to http://127.0.0.1:5000 
if your using Live server extention, debugged PIN
 to access is given in terminal of app.py file 

*PYTHON LIB REQUIRED*
pip install flask
pip install flask-cors
pip install pdfplumber
pip install python-docx

*r requirement 
pip install -r requirements.txt
 
change or add keyword if required for future 
and there is a button where full extracted text is shown

--Harsh Pawar
