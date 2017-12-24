from bottle import route, run, default_app, debug , request
from csv import reader

icerik = []
input_file = open("a2_input.csv","r")
for row in reader(input_file):
	icerik = icerik + [row]

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
                <style>
				body{
					background-color:#52e5c8;
					}
				table, th, tr, td{
				
				border:3px solid black;
				border-collapse:collapse;
				padding:10px;
				text-align:center;
					
					}
					
				input{
					background-color:#041a21
				}
				</style>
            </head>
            <body>
            %s
            </body>
        </html>
    """ % (title,text)
    return page
def table():
	tablo ='''
	<h2><a href="/">FC_BARCELONA</a></h2>
	<table>'''
	for i in range(0,30):
		tablo +=  "<tr>"
		for j in range(0,5):
			tablo += "<td>" + icerik[i][j] + "</td>"
		tablo += "</tr>"
	tablo += "</table>"
	return htmlify("table",tablo)
	

def index():
	start = ("""
		<h1>Players of FC Barcelona</h1>
		<br>
		<p>For all players of FC Barcelona just click the button !:</p>
    	<form action="/table" method="GET">
  			<input type="SUBMIT" value="ALL LEGENDARY PLAYERS">
		</form>
		
		
		<p>For the details list:</p>
		<form action="/details" method="get">
			<input type="submit" value="GO !">
		</form>
		
		<p>For more specific details:</p>
		<form action="/details" method="POST">
			<input type="submit" value="GO !">
		</form>
		
		<p>If you want to comment us, just write here !</p>
		<form action="/feedback" method="POST">
			<input type="TEXT" name="message" placeholder="Comment us briefly !" />
			<input type="SUBMIT" value="Comment" />
		</form>
		
		
		
		
		""")

	return htmlify("homepage",start)



	
def selecteddetail():
	a = int(request.POST["detaylar"])
	p = int(request.POST["secilenler"])
	deger = """<h2><a href="/">FC_BARCELONA</a></h2>
		<table>
				<tr>
					<th colspan="2">""" + icerik[0][a] + """</th>
				</tr>
				<tr>
					<td>"""+icerik[p][0] + """</td>
					<td>"""+icerik[p][a]+ """</td>
				</tr>
		</table>"""
	return htmlify("atable", deger)

def feedback():
	a = "<p>Thanks for your comment !</p><br>" + request.POST["message"] + '<p><a href="/">FC_BARCELONA</a></p>'
	return htmlify("message",a)


def details():
	butons = """
		<h3>Select which detail you want to see</h3>
		<form action="/details/detail" method="GET">
				<input type="checkbox" name="detail" value="1">NO<br />
				<input type="checkbox" name="detail" value="2">VALUE(EURO)<br />
				<input type="checkbox" name="detail" value="3">AGE<br />
				<input type="checkbox" name="detail" value="4">GOAL<br />
				<input type="submit" value="SHOW">
	
	
	"""
	return htmlify("Player",butons)

	
	
def tabloson():
	detay2 = request.GET.getlist("detail")
	data = '<h2><a href="/">FC_BARCELONA</a></h2><table>'
	for c in range(0,30):	
		data += "<tr><td>"+icerik[c][0]+"</td>"
		for detay in detay2:
			data += "<td>"+ icerik[c][int(detay)] + "</td>"
		data += "</tr>"
	return htmlify("Players", data)

def secilmis():
	butons = """ <p><strong>Choose a name and a detail that you want to know about him</strong></p>
	<form action="/details/select" method="POST">
		
			<input type="radio" name="secilenler" value="1" checked>NO
			<input type="radio" name="secilenler" value="2">VALUE(EURO)
			<input type="radio" name="secilenler" value="3">AGE
			<input type="radio" name="secilenler" value="4">GOAL
			
			
			<select name="detaylar" size="15">
				<option value="1" selecteddetail>Marc-Andre ter Stegen</option>
				<option value="2">Jasper Cillessen</option>
				<option value="3">Adrian Ortola</option>
				<option value="4">Samuel Umtiti</option>	
				<option value="5">Jordi Alba</option>
				<option value="6">Gerard Pique</option>
				<option value="7">Nelson Semedo</option>
				<option value="8">Aleix Vidal</option>	
				<option value="9">Javier Mascherano</option>
				<option value="10">Lucas Digne</option>
				<option value="11">Thomas Vermaelen</option>
				<option value="12">Marc Cucurella</option>	
				<option value="13">Sergio Busquets</option>
				<option value="14">Ivan Rakitic</option>
				<option value="15">Paulinho</option>
				<option value="16">Andres Iniesta</option>
				<option value="17">Sergi Roberto</option>
				<option value="18">Denis Suarez</option>
				<option value="19">Andre Gomes</option>	
				<option value="20">Carles Alena</option>
				<option value="21">Jose Arnaiz</option>
				<option value="22">Arda Turan</option>
				<option value="23">Rafinha</option>	
				<option value="24">Lionel Messi</option>
				<option value="25">Luis Suarez</option>
				<option value="26">Gerard Deulofeu</option>
				<option value="27">	Paco Alcacer</option>	
				<option value="28">Ousmane Dembele</option>
				<option value="29">Marc Cardona</option>
				<input type="SUBMIT" value="GO!">
				
			</select>
		</form>
	"""
	return htmlify("Player", butons)





route('/', 'GET', index)
route('/table' , 'GET', table)
route('/details/select','POST',selecteddetail)
route('/feedback','POST', feedback)
route('/details','GET', details)
route('/details/detail','GET', tabloson)
route('/details','POST', secilmis)
##################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()