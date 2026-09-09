const fs = require('fs');

function parseDateString(dateStr) {
    if (!dateStr) return null;
    const parts = dateStr.trim().split('/');
    if (parts.length !== 3) return null;
    return new Date(parseInt(parts[2]), parseInt(parts[1]) - 1, parseInt(parts[0]));
}

const data = fs.readFileSync('sagre.csv', 'utf8').split('\n').slice(1);
const today = new Date();
// Assuming today is 2026-07-03T11:57:40
// We can just use new Date() because the environment is running right now

console.log("Current date:", today.toISOString());

data.forEach(line => {
    if (!line.trim()) return;
    const parts = line.split(',');
    if (parts.length < 3) return;
    const dataInizio = parts[0];
    const dataFine = parts[1];
    const nome = parts[2];
    
    const start = parseDateString(dataInizio);
    const end = parseDateString(dataFine);
    
    let badge = "";
    if (start && end) {
        if (today >= start && today <= end) {
            badge = "In Corso";
        } else if (today < start) {
            badge = "In Arrivo";
        } else {
            badge = "Conclusa";
        }
    }
    
    if (badge === "In Corso") {
        console.log(`[IN CORSO] ${nome} (${dataInizio} - ${dataFine})`);
    } else if (badge === "") {
        console.log(`[EMPTY BADGE] ${nome} (${dataInizio} - ${dataFine})`);
    }
});
