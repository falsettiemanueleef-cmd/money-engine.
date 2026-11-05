# MONEY ENGINE

Progetto personale per monitorare opportunità di affiliazione e registrare ricavi reali.

## Stato attuale

- La web app esistente è una PWA utilizzabile da browser compatibile.
- Il registro dei ricavi è locale al browser: non è sincronizzato e richiede inserimento manuale.
- Non esiste un collegamento bancario, non vengono eseguiti pagamenti e non vengono generati ricavi automaticamente.
- La scansione settimanale raccoglie notizie pubbliche come **indizi**; non approva programmi, non crea account e non sostituisce la verifica dei termini ufficiali.

## Scansione settimanale

GitHub Actions esegue ogni lunedì alle 15:00 UTC (16:00 in Italia in inverno, 17:00 durante l'ora legale) e aggiorna `reports/latest.md`. L'orario è UTC e non segue automaticamente il cambio dell'ora italiana. È disponibile anche l'avvio manuale dalla scheda Actions.

Le notizie raccolte non sono offerte verificate. Prima di aderire a un programma occorre controllare sul sito ufficiale: requisiti per l'Italia, commissioni, soglie, calendario e metodo di pagamento, cookie, regole promozionali, privacy e fiscalità.

## Avvio da Android

La PWA può essere aperta con Chrome su Android e, se il sito è pubblicato via HTTPS e il manifest/service worker sono serviti correttamente, aggiunta alla schermata Home. Questo non equivale a un APK nativo.

## Regole di sicurezza e trasparenza

- Nessuna password, PIN, OTP o credenziale bancaria nel repository.
- Nessun click, acquisto, account o vendita artificiale.
- Nessuna pubblicazione automatica senza autorizzazione e conformità alle regole del canale.
- Nessuna commissione o entrata simulata presentata come reale.
- Nessuna promessa di reddito: 2.000 €/mese è un obiettivo non garantito.

## Limiti del piano gratuito

GitHub Actions, hosting e servizi esterni hanno limiti, quote e condizioni che possono cambiare. Controllare le condizioni correnti prima di fare affidamento su un servizio.
## App Android (prima build di prova)

Nel repository è presente un progetto Android Java che incorpora la web app in una WebView locale. Il workflow `Build Android APK` prova a generare un APK debug a ogni modifica dei file `app/**` e lo carica come artefatto GitHub per 14 giorni. L'APK debug è destinato a installazione e collaudo, non è una release firmata per Play Store.

**Stato:** sorgenti e workflow sono stati aggiunti, ma la compilazione remota e l'installazione su un telefono reale non sono ancora state verificate. Aprire la scheda Actions del repository, selezionare `Build Android APK` e controllare che il job termini con successo; l'artefatto si chiama `money-engine-debug-apk`. Se non compare una run, usare `Run workflow` nella pagina Actions.

L'app conserva il registro nel browser/WebView del dispositivo: disinstallazione, cancellazione dati o cambio telefono possono far perdere i dati. Esportare periodicamente il backup JSON e conservarlo in un luogo sicuro.
