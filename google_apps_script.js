// =========================================================================
// GOOGLE APPS SCRIPT PER RACCOGLITORE SEGNALAZIONI SAGRE GROSSETO
// =========================================================================
// ISTRUZIONI:
// 1. Nel tuo Google Sheet (https://docs.google.com/spreadsheets/d/1wMb6K1GmFs4VpjZan_E-J3S1DiNr_LNR3UVceV87GqY/edit)
//    fai clic su: Estensioni > Apps Script
// 2. Cancella tutto ciò che c'è nell'editor e incolla questo codice.
// 3. Fai clic su "Salva" (icona del dischetto).
// 4. In alto a destra clicca su "Distribuisci" > "Nuova distribuzione".
// 5. Clicca sull'icona dell'ingranaggio (Seleziona tipo) e scegli: "Applicazione web".
// 6. Configura così:
//    - Descrizione: Raccoglitore Segnalazioni Sagre
//    - Esegui come: Me (il tuo account)
//    - Chi ha accesso: Chiunque (Anyone)
// 7. Clicca su "Distribuisci", autorizza l'accesso con il tuo account Google.
// 8. Copia l'URL dell'applicazione web fornito da Google (termina con /exec)
//    e incollalo nella chat!
// =========================================================================

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Se il foglio è vuoto, imposta le intestazioni
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(["Data e Ora", "Nome Evento", "Tipo Segnalazione", "Dettagli Correzione", "Dispositivo"]);
      sheet.getRange(1, 1, 1, 5).setFontWeight("bold").setBackground("#f3f4f6");
    }
    
    var data = {};
    if (e && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (parseErr) {
        data = e.parameter || {};
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }
    
    var timestamp = Utilities.formatDate(new Date(), "Europe/Rome", "yyyy-MM-dd HH:mm:ss");
    var eventName = data.event_name || data.eventName || "Non specificato";
    var issueType = data.issue_type || data.issueType || "Altro";
    var details = data.details || data.message || "";
    var device = data.device || "Smartphone/Web";
    
    sheet.appendRow([timestamp, eventName, issueType, details, device]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ status: "success", message: "Segnalazione registrata con successo!" }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var values = sheet.getDataRange().getValues();
    
    if (values.length <= 1) {
      return ContentService.createTextOutput(JSON.stringify([])).setMimeType(ContentService.MimeType.JSON);
    }
    
    var list = [];
    for (var i = 1; i < values.length; i++) {
      var row = values[i];
      // Formatta la data se è un oggetto Date
      var dateStr = row[0];
      if (row[0] instanceof Date) {
        dateStr = Utilities.formatDate(row[0], "Europe/Rome", "yyyy-MM-dd HH:mm:ss");
      }
      
      list.push({
        id: i,
        timestamp: dateStr,
        eventName: row[1] || "",
        issueType: row[2] || "",
        details: row[3] || "",
        device: row[4] || ""
      });
    }
    
    return ContentService
      .createTextOutput(JSON.stringify(list))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
