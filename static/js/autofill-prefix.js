document.addEventListener('DOMContentLoaded', function () {
    const countrySelect = document.getElementById('id_location');
    const phoneInput = document.getElementById('id_phone_number');

    // Fetch the country code map from JSON
    fetch("/static/data/countryPhoneCodes.json")
        .then(response => response.json())
        .then(data => {
            const prefixMap = {};
            data.forEach(entry => {
                prefixMap[entry.iso] = "+" + entry.code;
            });

            countrySelect.addEventListener('change', function () {
                const selectedIso = countrySelect.value;
                const prefix = prefixMap[selectedIso];

                if (prefix && !phoneInput.value.startsWith(prefix)) {
                    phoneInput.value = prefix + ' ';
                }
            });
        })
        .catch(error => {
            console.error("Failed to load country code data:", error);
        });
});
