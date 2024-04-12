from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

medications = []

def clear_form():
    global medications
    medications = []
    
def calculate_complexity_index(dosage_form, dosage_frequency, additional_instructions):
    form_puanlama = {
        'capsule_tablet': 1,
        'gargle': 2,
        'pastil_chewing_gum': 2,
        'liquid': 2,
        'powder': 2,
        'sublingual': 2,
        'cream_gel_ointment': 2,
        'solution': 2,
        'resin_paste': 3,
        'patch': 2,
        'spray': 1,
        'ear_drops_cream_ointment': 3,
        'eye_drops': 3,
        'eye_gel_ointment': 3,
        'nose_drops_cream_ointment': 3,
        'nasal_spray': 2,
        'aerosol': 3,
        'metered_dose_inhaler': 4,
        'nebulizer': 5,
        'oxygen': 3,
        'others': 3,
        'dialysis': 5,
        'enema': 2,
        'injection_ready': 3,
        'injection_ampoule': 4,
        'pessary': 3,
        'suppository': 2,
        'vaginal_cream': 2,
        'patient_controlled_analgesia': 2
    }
    frequency_puanlama = {
        'once_daily': 1,
        'as_needed_once_daily': 0.5,
        'twice_daily': 2,
        'as_needed_twice_daily': 1,
        'three_times_daily': 3,
        'as_needed_three_times_daily': 1.5,
        'four_times_daily': 4,
        'as_needed_four_times_daily': 2,
        'every_12_hours': 2.5,
        'as_needed_every_12_hours': 1.5,
        'every_8_hours': 3.5,
        'as_needed_every_8_hours': 2,
        'every_6_hours': 4.5,
        'as_needed_every_6_hours': 2.5,
        'every_4_hours': 6.5,
        'as_needed_every_4_hours': 3.5,
        'every_2_hours': 12.5,
        'as_needed_every_2_hours': 6.5,
        'as_needed_oxygen': 1,
        'oxygen_less_than_15_hours': 2,
        'oxygen_greater_than_15_hours': 3
    }
    additional_instructions_puanlama = {
        'crush': 1,
        'dissolve': 1,
        'two_tablets_or_puffs_same_time': 1,
        'various_doses': 1,
        'specific_time': 1,
        'with_meal': 1,
        'with_specific_liquid': 1,
        'as_prescribed': 2,
        'increased_dosing': 2,
        'alternative_dosing': 2
    }

    # Seçilen formun puanını alın
    form_puan = form_puanlama.get(dosage_form, 0)
    frequency_puan = frequency_puanlama.get(dosage_frequency, 0)
    additional_instructions_puan = additional_instructions_puanlama.get(additional_instructions, 0)

    total_puan = form_puan + frequency_puan + additional_instructions_puan

    return total_puan

# Bu kısmı ekleyin
additional_instructions_puanlama = {
    'no-needed':0,
    'crush': 1,
    'dissolve': 1,
    'two_tablets_or_puffs_same_time': 1,
    'various_doses': 1,
    'specific_time': 1,
    'with_meal': 1,
    'with_specific_liquid': 1,
    'as_prescribed': 2,
    'increased_dosing': 2,
    'alternative_dosing': 2
}

form_puanlama = {
    'capsule_tablet': 1,
    'gargle': 2,
    'pastil_chewing_gum': 2,
    'liquid': 2,
    'powder': 2,
    'sublingual': 2,
    'cream_gel_ointment': 2,
    'solution': 2,
    'resin_paste': 3,
    'patch': 2,
    'spray': 1,
    'ear_drops_cream_ointment': 3,
    'eye_drops': 3,
    'eye_gel_ointment': 3,
    'nose_drops_cream_ointment': 3,
    'nasal_spray': 2,
    'aerosol': 3,
    'metered_dose_inhaler': 4,
    'nebulizer': 5,
    'oxygen': 3,
    'others': 3,
    'dialysis': 5,
    'enema': 2,
    'injection_ready': 3,
    'injection_ampoule': 4,
    'pessary': 3,
    'suppository': 2,
    'vaginal_cream': 2,
    'patient_controlled_analgesia': 2
}

frequency_puanlama = {
    'once_daily': 1,
    'as_needed_once_daily': 0.5,
    'twice_daily': 2,
    'as_needed_twice_daily': 1,
    'three_times_daily': 3,
    'as_needed_three_times_daily': 1.5,
    'four_times_daily': 4,
    'as_needed_four_times_daily': 2,
    'every_12_hours': 2.5,
    'as_needed_every_12_hours': 1.5,
    'every_8_hours': 3.5,
    'as_needed_every_8_hours': 2,
    'every_6_hours': 4.5,
    'as_needed_every_6_hours': 2.5,
    'every_4_hours': 6.5,
    'as_needed_every_4_hours': 3.5,
    'every_2_hours': 12.5,
    'as_needed_every_2_hours': 6.5,
    'as_needed_oxygen': 1,
    'oxygen_less_than_15_hours': 2,
    'oxygen_greater_than_15_hours': 3
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/medicationregimen', methods=['GET', 'POST'])
def medication_regimen():
    if request.method == 'POST':
        dosage_form = request.form.get('dosage_form', '')
        dosage_frequency = request.form.get('dosage_frequency', '')
        additional_instructions = request.form.get('additional_instructions', '')

        # İndeks hesaplama formülüne göre indeksi hesaplayın
        complexity_index = calculate_complexity_index(dosage_form, dosage_frequency, additional_instructions)

        # İlaç bilgilerini liste içine ekle
        medications.append({
            'dosage_form': dosage_form,
            'dosage_frequency': dosage_frequency,
            'additional_instructions': additional_instructions,
            'complexity_index': complexity_index
        })

        # Toplam puanı güncelle
        total_score = calculate_total_score()

        return render_template('medicationregimen.html', medications=medications, total_score=total_score)

    return render_template('medicationregimen.html')

def calculate_total_score():
    total_score = 0
    for med in medications:
        total_score += med['complexity_index']
    return total_score

# Diğer importları buraya ekleyin

@app.route('/add-medication', methods=['POST'])
def add_medication():
    dosage_form = request.form.get('dosage_form', '')
    dosage_frequency = request.form.get('dosage_frequency', '')
    additional_instructions = request.form.get('additional_instructions', '')

    # İndeks hesaplama formülüne göre indeksi hesaplayın
    complexity_index = calculate_complexity_index(dosage_form, dosage_frequency, additional_instructions)

    medications.append({
        'dosage_form': dosage_form,
        'dosage_frequency': dosage_frequency,
        'additional_instructions': additional_instructions,
        'complexity_index': complexity_index
    })

    total_score = calculate_total_score()

    return jsonify({'success': True, 'total_score': total_score})

@app.route('/clear-form', methods=['POST'])
def clear_form_route():
    clear_form()
    return jsonify({'status': 'success'})
    
if __name__ == '__main__':
    app.run(debug=True)






