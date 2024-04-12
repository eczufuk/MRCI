// static/script.js

// İlave Et butonuna tıklandığında çalışacak fonksiyon
function addMedication() {
    // Seçilen ilacın bilgilerini al
    var dosageForm = document.getElementById("dosage_form").value;
    var dosageFrequency = document.getElementById("dosage_frequency").value;
    var additionalInstructions = document.getElementById("additional_instructions").value;

    // Toplam puanı hesapla
    var complexityIndex = calculateComplexityIndex(dosageForm, dosageFrequency, additionalInstructions);

    // Seçilen ilacın bilgilerini ekranda göstermek için bir div oluştur
    var medicationDiv = document.createElement("div");
    medicationDiv.innerHTML = "<p>" + dosageForm + ", " + dosageFrequency + ", " + additionalInstructions + ", Puan: " + complexityIndex + "</p>";

    // Seçilen ilacı ekranda göstermek için olan div'e ekle
    document.getElementById("medicationsList").appendChild(medicationDiv);

    // Toplam puanı güncelle
    updateTotalScore();
}
