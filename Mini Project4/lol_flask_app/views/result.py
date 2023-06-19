from flask import Blueprint, render_template, request

result_bp = Blueprint('result', __name__)

@result_bp.route('/result')
def show_result():
    result_blue = request.args.get('result_blue')
    result_red = request.args.get('result_red')
    return render_template('result.html', result_blue=result_blue, result_red=result_red)