// script.js

var selectedOptionsList = [];

function addOption() {
    var dosageForm = document.getElementById('dosage_form').value;
    var dosageFrequency = document.getElementById('dosage_frequency').value;
    var additionalInstructions = document.getElementById('additional_instructions').value;

    var option = {
        dosageForm: dosageForm,
        dosageFrequency: dosageFrequency,
        additionalInstructions: additionalInstructions
    };

    selectedOptionsList.push(option);

    console.log(selectedOptionsList);
}

  