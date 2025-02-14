from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from Assessments import AssessmentFactory
from Strategies import CalculationStrategyFactory
from utils.number_utils import generateRandomNumbersPairs

app = Flask(__name__, template_folder='dist', static_folder='dist', static_url_path='/')
socketio = SocketIO(app, debug=True, cors_allowed_origins='*', async_mode='eventlet')

assessment = None
assessmentIterator = None
assessmentItem = None


def start_assessment(quantity: int):
    numbersPairs = generateRandomNumbersPairs(maxNumber=10, count=quantity)
    strategies = CalculationStrategyFactory.createAdditionStrategies(numbersPairs)

    assessment = AssessmentFactory.createResponseAssessment(strategies)
    assessmentIterator = iter(assessment)

    return assessment, assessmentIterator


@socketio.on('start')
def handle_start(quantity: int):
    global assessment, assessmentIterator

    assessment, assessmentIterator = start_assessment(quantity)


@socketio.on('question')
def handle_question(args):
    global assessmentItem

    try:
        assessmentItem = next(assessmentIterator)

        return str(assessmentItem), assessmentItem.goal
    except StopIteration:
        emit('end', {'assessment': str(assessment), 'results': assessment.results, 'isPassed': assessment.result})
        return ''


@socketio.on('answer')
def handle_answer(answer: int):
    result = assessmentItem.pipe(lambda item: item.setAnswer(lambda: answer)).assess()

    return result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ping')
def pong_hello_world():
    return 'pong hello world'


@app.route('/image/<int:digit>')
def fetch_image(digit: int):
    return f'{digit}'


if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
