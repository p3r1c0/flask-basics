from app.init_app import app #, db

# def connect(db_file='app.sqlite'):
# 	try:
# 		conn = sqlite3.connect(db_file)
# 		return conn
# 	except Error as e:
# 		print(e)
 
# 	return None

@app.route("/", methods=['POST'])
def receive():
	try:
		print("Working..")
	except Exception as e:
		print(e)

@app.route('/Xss.Js')
def pedro():
	from flask import Response
	return Response("""alert('Powned');""", mimetype='text/javascript')
