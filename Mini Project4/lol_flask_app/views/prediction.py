from flask import Blueprint, render_template, request, redirect, url_for
import pickle
import os

with open(f"{os.getcwd()}\model.pkl", 'rb') as file:
    model = pickle.load(file)
prediction_bp = Blueprint('prediction', __name__)

@prediction_bp.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        form_params = list(request.form.keys())
        expected_params = [
            'blue-kill-score', 'blue-assist-score', 'blue-death-score', 'blue-first-blood',
            'blue-first-dragon', 'blue-dragon-kill', 'blue-first-riftherald', 'blue-riftherald-kill',
            'blue-first-baron', 'blue-baron-kill', 'blue-first-tower', 'blue-tower-destroyed',
            'blue-first-inhibitor', 'blue-inhibitor-destroyed', 'blue-total-level', 'blue-total-gold',
            'red-kill-score', 'red-assist-score', 'red-death-score', 'red-first-blood',
            'red-first-dragon', 'red-dragon-kill', 'red-first-riftherald', 'red-riftherald-kill',
            'red-first-baron', 'red-baron-kill', 'red-first-tower', 'red-tower-destroyed',
            'red-first-inhibitor', 'red-inhibitor-destroyed', 'red-total-level', 'red-total-gold'
        ]
        print(form_params)
        if set(form_params) != set(expected_params):
            print('Form parameter names do not match expected parameters.')
        else:
            print('No problem')
        # Blue Team 입력값 받아오기
        Blue_kill_score = int(request.form['blue-kill-score'])
        Blue_assist_score = int(request.form['blue-assist-score'])
        Blue_death_score = int(request.form['blue-death-score'])
        Blue_first_blood = int(request.form['blue-first-blood'])
        Blue_first_dragon = int(request.form['blue-first-dragon'])
        Blue_dragon_kill = int(request.form['blue-dragon-kill'])
        Blue_first_riftherald = int(request.form['blue-first-riftherald'])
        Blue_riftherald_kill = int(request.form['blue-riftherald-kill'])
        Blue_first_baron = int(request.form['blue-first-baron'])
        Blue_baron_kill = int(request.form['blue-baron-kill'])
        Blue_first_tower = int(request.form['blue-first-tower'])
        Blue_tower_destroyed = int(request.form['blue-tower-destroyed'])
        Blue_first_inhibitor = int(request.form['blue-first-inhibitor'])
        Blue_inhibitor_destroyed = int(request.form['blue-inhibitor-destroyed'])
        Blue_total_level = int(request.form['blue-total-level'])
        Blue_total_gold = int(request.form['blue-total-gold'])

        # Red Team 입력값 받아오기
        Red_kill_score = int(request.form['red-kill-score'])
        Red_assist_score = int(request.form['red-assist-score'])
        Red_death_score = int(request.form['red-death-score'])
        Red_first_blood = int(request.form['red-first-blood'])
        Red_first_dragon = int(request.form['red-first-dragon'])
        Red_dragon_kill = int(request.form['red-dragon-kill'])
        Red_first_riftherald = int(request.form['red-first-riftherald'])
        Red_riftherald_kill = int(request.form['red-riftherald-kill'])
        Red_first_baron = int(request.form['red-first-baron'])
        Red_baron_kill = int(request.form['red-baron-kill'])
        Red_first_tower = int(request.form['red-first-tower'])
        Red_tower_destroyed = int(request.form['red-tower-destroyed'])
        Red_first_inhibitor = int(request.form['red-first-inhibitor'])
        Red_inhibitor_destroyed = int(request.form['red-inhibitor-destroyed'])
        Red_total_level = int(request.form['red-total-level'])
        Red_total_gold = int(request.form['red-total-gold'])

        input_data = [[Blue_kill_score, Blue_assist_score, Blue_death_score, Blue_total_level,Blue_total_gold,Blue_first_blood,Blue_first_dragon,Blue_dragon_kill,Blue_first_riftherald,Blue_riftherald_kill, Blue_first_baron,Blue_baron_kill,Blue_first_tower,Blue_tower_destroyed,Blue_first_inhibitor,Blue_inhibitor_destroyed,Red_kill_score, Red_assist_score, Red_death_score, Red_total_level,Red_total_gold,Red_first_blood,Red_first_dragon,Red_dragon_kill,Red_first_riftherald,Red_riftherald_kill, Red_first_baron,Red_baron_kill,Red_first_tower,Red_tower_destroyed,Red_first_inhibitor,Red_inhibitor_destroyed]]
        
        result = model.predict_proba(input_data)[0]
        
        return redirect(url_for('result.show_result', result_blue = round(result[1],3), result_red = round(result[0],3)))
    
    return render_template('dashboard.html')
        