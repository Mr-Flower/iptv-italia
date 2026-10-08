# IPTV Italia

Playlist M3U con i soli canali italiani e i VOD italiani, ricavata da
[Free-TV/IPTV](https://github.com/Free-TV/IPTV).

Link da inserire nel player (VLC, Kodi, TiviMate, ...):

```
https://raw.githubusercontent.com/Mr-Flower/iptv-italia/main/italia.m3u8
```

La playlist viene rigenerata ogni giorno da una GitHub Action.

## Contenuto

- Canali nazionali, satellitari e regionali gratuiti (`lists/italy.md`)
- Canali FAST/VOD italiani: Pluto TV, Samsung TV Plus, Rakuten TV (`lists/zz_vod_it.md`)

Rispetto alla playlist originale: i gruppi seguono le sezioni delle liste,
l'EPG è limitato alle sorgenti italiane, i canali segnati come non funzionanti
e le ritrasmissioni di terzi sono esclusi.

I canali con `Ⓖ` funzionano solo da un indirizzo IP italiano.

## Generazione manuale

```
python3 make_italia.py            # scrive italia.m3u8
python3 make_italia.py --no-geo   # senza canali geo-bloccati
python3 make_italia.py --no-web   # senza dirette YouTube/Twitch
```

## Avvertenze

Questo repository non ospita né ritrasmette alcun contenuto audio/video:
contiene solo collegamenti a flussi pubblicamente accessibili di canali
gratuiti, raccolti dal progetto Free-TV/IPTV, a cui vanno i crediti per
l'elenco. Non sono inclusi canali a pagamento.

Se sei titolare di un canale e vuoi che il collegamento venga rimosso, apri
una issue.
