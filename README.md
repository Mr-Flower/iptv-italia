# IPTV Italia

[![Aggiorna playlist](https://github.com/Mr-Flower/iptv-italia/actions/workflows/update.yml/badge.svg)](https://github.com/Mr-Flower/iptv-italia/actions/workflows/update.yml)
[![Ultimo aggiornamento](https://img.shields.io/github/last-commit/Mr-Flower/iptv-italia?label=ultimo%20aggiornamento)](https://github.com/Mr-Flower/iptv-italia/commits/main)

Una playlist M3U con **solo i canali TV italiani gratuiti e i VOD italiani**,
aggiornata automaticamente ogni giorno.

```
https://raw.githubusercontent.com/Mr-Flower/iptv-italia/main/italia.m3u8
```

Copia il link qui sopra nel tuo player IPTV e hai finito.

## Da dove arriva la lista

I canali non sono raccolti da me: provengono tutti da
**[Free-TV/IPTV](https://github.com/Free-TV/IPTV)**, un progetto open source
che mantiene una playlist di canali gratuiti di tutto il mondo. Questo
repository ne estrae la sola parte italiana e la riorganizza.

In particolare vengono letti tre file del progetto originale:

| File di Free-TV/IPTV | Cosa contiene | Come viene usato qui |
|---|---|---|
| [`lists/italy.md`](https://github.com/Free-TV/IPTV/blob/master/lists/italy.md) | Canali italiani nazionali, satellitari e regionali | Gruppi `Italia - …` |
| [`lists/zz_vod_it.md`](https://github.com/Free-TV/IPTV/blob/master/lists/zz_vod_it.md) | Canali VOD/FAST in italiano | Gruppi `VOD Italia - …` |
| [`epglist.txt`](https://github.com/Free-TV/IPTV/blob/master/epglist.txt) | Sorgenti della guida TV (EPG) | Solo le sorgenti italiane |

Free-TV/IPTV accetta soltanto canali **offerti ufficialmente in modo
gratuito** (digitale terrestre, satellite in chiaro, servizi gratuiti su
Internet): niente canali a pagamento e niente canali per adulti. Le regole
complete sono nel
[README del progetto](https://github.com/Free-TV/IPTV#philosophy).

Se un canale non funziona o ne manca uno, la correzione va proposta lì con una
pull request: al giro successivo arriverà anche in questa playlist.

## Cosa c'è dentro

| Gruppo | Contenuto |
|---|---|
| `Italia - National DVB-T` | Canali nazionali del digitale terrestre (Rai, Mediaset, La7, TV8, Nove, …) |
| `Italia - Satellite` | Canali in chiaro via satellite |
| `Italia - Regional DVB-T` | TV locali e regionali |
| `Italia - YouTube Live` | Dirette YouTube |
| `Italia - Twitch Live` | Dirette Twitch |
| `VOD Italia - Misc` | Canali vari |
| `VOD Italia - Rakuten TV` | Canali tematici Rakuten TV |
| `VOD Italia - Samsung TV Plus` | Canali tematici Samsung TV Plus |
| `VOD Italia - Pluto TV` | Canali tematici Pluto TV |

In tutto sono circa 590 voci; il numero cambia man mano che la lista
originale viene aggiornata.

### Simboli accanto ai nomi

| Simbolo | Significato |
|:---:|---|
| Ⓖ | Geo-bloccato: funziona solo da un indirizzo IP italiano |
| Ⓢ | Non in HD |
| Ⓨ | Diretta YouTube |
| Ⓣ | Diretta Twitch |

## Differenze rispetto alla playlist originale

- **Solo Italia**: un unico link invece della playlist mondiale o di due
  playlist separate.
- **Gruppi per sezione**: l'originale mette tutto sotto `Italy` e `VOD Italy`,
  qui ogni sezione è un gruppo a sé.
- **EPG più leggero**: solo le guide TV italiane di
  [epgshare01](https://epgshare01.online) invece di quelle di tutto il mondo.
- **Niente canali morti**: le voci che l'originale segna come non funzionanti
  (`[x]` e sezione *Invalid*) sono escluse, così come gli indirizzi duplicati.

## Come si usa

| Player | Dove inserire il link |
|---|---|
| VLC | *Media → Apri flusso di rete* |
| Kodi | Add-on *PVR IPTV Simple Client* → *URL playlist M3U* |
| TiviMate, IPTV Smarters e simili | *Aggiungi playlist* → *Playlist M3U* |

Le dirette YouTube e Twitch sono link a pagine web: molti player IPTV non le
aprono.

## Come funziona

Lo script [`make_italia.py`](make_italia.py) scarica i file da Free-TV/IPTV,
converte le tabelle in formato M3U e scrive [`italia.m3u8`](italia.m3u8). Una
[GitHub Action](.github/workflows/update.yml) lo esegue ogni giorno e salva la
playlist solo se è cambiata.

Per generarla a mano serve solo Python 3, senza dipendenze:

```
python3 make_italia.py              # scrive italia.m3u8
python3 make_italia.py --no-geo     # senza canali geo-bloccati
python3 make_italia.py --no-web     # senza dirette YouTube/Twitch
python3 make_italia.py -o altro.m3u8
```

## Avvertenze

Questo repository non ospita né ritrasmette alcun contenuto audio o video:
contiene soltanto collegamenti a flussi pubblicamente accessibili di canali
gratuiti. I flussi restano dei rispettivi titolari, che possono modificarli o
disattivarli in qualsiasi momento.

Se sei titolare di un canale e vuoi che il collegamento venga rimosso, apri
una [issue](https://github.com/Mr-Flower/iptv-italia/issues).

## Crediti

Tutto il merito dell'elenco va a chi mantiene
[Free-TV/IPTV](https://github.com/Free-TV/IPTV). La guida TV è fornita da
[epgshare01](https://epgshare01.online).
