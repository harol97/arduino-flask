from flask import Flask,render_template
from flask_socketio import SocketIO
from flask_serial import Serial
from eventlet import monkey_patch

monkey_patch()

app = Flask(__name__)
app.config['SERIAL_TIMEOUT'] = 0.2
app.config['SERIAL_PORT'] = 'COM1'
app.config['SERIAL_BAUDRATE'] = 9600
app.config['SERIAL_BYTESIZE'] = 8
app.config['SERIAL_PARITY'] = 'N'
app.config['SERIAL_STOPBITS'] = 1
app.config['SECRET_KEY'] = 'secret!'

ser =Serial(app)
socketio = SocketIO(app)

@app.route('/')
def index(): 
    return render_template('index.html')

@ser.on_message()
def handle_message(medida):
    medida = medida.decode().replace('\r','').replace('\n','')
    socketio.emit('data',str(medida))

if __name__ == '__main__':
    socketio.run(app,debug = False)