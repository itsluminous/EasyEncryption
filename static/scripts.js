function openTab(evt, tabName) {
    var tabContents = document.getElementsByClassName("tab-content");
    for (var i = 0; i < tabContents.length; i++) {
        tabContents[i].style.display = "none";
    }

    var tabs = document.getElementsByClassName("tabs")[0].getElementsByTagName("button");
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].className = tabs[i].className.replace(" active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

function generateKey() {
    fetch('/generate_key')
        .then(response => response.text())
        .then(key => document.getElementById("generatedKey").value = key);
}

function encryptText() {
    var text = document.getElementById("encryptionInput").value;
    var key = document.getElementById("encryptionKey").value;

    fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'text': text,
            'key': key
        })
    })
        .then(response => response.text())
        .then(encryptedText => document.getElementById("encryptedOutput").value = encryptedText);
}

function decryptText() {
    var text = document.getElementById("decryptionInput").value;
    var key = document.getElementById("decryptionKey").value;

    fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'text': text,
            'key': key
        })
    })
        .then(response => response.text())
        .then(decryptedText => document.getElementById("decryptedOutput").value = decryptedText);
}

function copyText(elementId) {
    const element = document.getElementById(elementId);
    const text = element.value || element.textContent;

    navigator.clipboard.writeText(text)
        .then(() => {
            const toast = document.getElementById('toast');
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 1300);
        })
        .catch((err) => {
            console.error('Unable to copy to clipboard:', err);
        });
}