import shutil , os

f = open('index.html','w')

message = """
<html>
<head>
	<title> This is a Python Generated File</title>
</head>
<body>
	<p>This is Python Generated File</p>
</body>
</html>
"""
f.write(message)
f.close()

# create assest folder

os.makedirs('assest')
os.chdir('assest')
os.makedirs('css')
os.makedirs('js')
os.makedirs('img')

# Generate Css file

f = open('file.css','w')
message = """ // this is python generated file """
f.write(message)
f.close()

# Generate Js file

f = open('file.js','w')
message = """ // this is python generated file """
f.write(message)
f.close()

# moving files to respective folders
shutil.move('file.css','css')
shutil.move('file.js','js')


