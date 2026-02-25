document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('opacity');
    const valDisplay = document.getElementById('opacity-val');

    // Load current value
    chrome.storage.sync.get('overlayOpacity', data => {
        if (data.overlayOpacity) {
            input.value = data.overlayOpacity;
            if (valDisplay) valDisplay.textContent = Number(data.overlayOpacity).toFixed(2);
        }
    });

    input.addEventListener('input', () => {
        let val = parseFloat(input.value);
        if (isNaN(val) || val < 0.1 || val > 1) val = 0.75;
        if (valDisplay) valDisplay.textContent = val.toFixed(2);
        chrome.storage.sync.set({ overlayOpacity: val });
    });
});