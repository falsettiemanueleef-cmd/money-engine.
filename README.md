# MONEY ENGINE

Progetto personale per monitorare opportunità di affiliazione e registrare ricavi reali.

## Stato attuale

- La web app esistente è una PWA utilizzabile da browser compatibile.
- Il registro dei ricavi è locale al browser: non è sincronizzato e richiede inserimento manuale.
- Non esiste un collegamento bancario, non vengono eseguiti pagamenti e non vengono generati ricavi automaticamente.
- La scansione settimanale raccoglie notizie pubbliche come **indizi**; non approva programmi, non crea account e non sostituisce la verifica dei termini ufficiali.
- Il report `reports/latest.md` contiene la shortlist iniziale di TradeTracker, Awin e Amazon PartnerNet. La scansione automatica aggiorna separatamente `reports/weekly-leads.md`, così non sovrascrive la shortlist. Nessun report equivale a un'approvazione o a una candidatura.

## Scansione settimanale

GitHub Actions esegue ogni lunedì alle 15:00 UTC (16:00 in Italia in inverno, 17:00 durante l'ora legale) e aggiorna `reports/weekly-leads.md`. L'orario è UTC e non segue automaticamente il cambio dell'ora italiana. È disponibile anche l'avvio manuale dalla scheda Actions.

Le notizie raccolte non sono offerte verificate. Prima di aderire a un programma occorre controllare sul sito ufficiale: requisiti per l'Italia, commissioni, soglie, calendario e metodo di pagamento, cookie, regole promozionali, privacy e fiscalità.

## Avvio da Android

La PWA può essere aperta con Chrome su Android e, se il sito è pubblicato via HTTPS e il manifest/service worker sono serviti correttamente, aggiunta alla schermata Home. Questo non equivale a un APK nativo.

## Regole di sicurezza e trasparenza

L'app non richiede né usa dati bancari. Il rapporto delle opportunità è raggiungibile dalla sezione dedicata nell'app.

- Nessuna password, PIN, OTP o credenziale bancaria nel repository.
- Nessun click, acquisto, account o vendita artificiale.
- Nessuna pubblicazione automatica senza autorizzazione e conformità alle regole del canale.
- Nessuna commissione o entrata simulata presentata come reale.
- Nessuna promessa di reddito: 2.000 €/mese è un obiettivo non garantito.

## Limiti del piano gratuito

GitHub Actions, hosting e servizi esterni hanno limiti, quote e condizioni che possono cambiare. Controllare le condizioni correnti prima di fare affidamento su un servizio.
## App Android

Nel repository è presente un progetto Android Java che incorpora la web app in una WebView locale. Il workflow `Build Android APK` genera un APK debug e lo carica come artefatto GitHub per 14 giorni. L'ultima build verificata è terminata con successo (run 42012989265); l'APK è stato scaricato e riconosciuto come pacchetto Android. L'utente ha confermato installazione e inserimento di ricavi. Non è una release firmata per Play Store.

L'app conserva il registro nel browser/WebView del dispositivo: disinstallazione, cancellazione dati o cambio telefono possono far perdere i dati. Esportare periodicamente il backup JSON e conservarlo in un luogo sicuro. La persistenza dopo chiusura forzata e riapertura non è ancora stata verificata.
