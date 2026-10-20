# Vigenère-Verschlüsselung

Eine objektorientierte Implementierung der Vigenère-Verschlüsselung, die sowohl die Textverschlüsselung über die Befehlszeile als auch die dateibasierte Verschlüsselung mit Ausgabespeicherung unterstützt.

## Funktionen

- Verschlüsselung und Entschlüsselung von Text direkt über die Befehlszeile
- Verarbeitung von Dateien zur Verschlüsselung und Entschlüsselung
- Ergebnisse in Ausgabedateien speichern
- Beibehaltung von Groß-/Kleinschreibung und nicht-alphabetischen Zeichen
- Einfache und intuitive Befehlszeilenschnittstelle

### Grundlegende Befehlsstruktur

```bash
python main.py --encrypt/--decrypt --key YOUR_KEY [--text "Your text" | --file input.txt] [--out output.txt]
```

### Beispiele

#### Text direkt verschlüsseln

```bash
python main.py --encrypt --key SECRET --text "Hello World"
```

Dies gibt den verschlüsselten Text in der Konsole aus.

```bash
python main.py --decrypt --key SECRET --text "Zincs Jscnw"
```
Dadurch wird der bereits verschlüsselte Text entschlüsselt.

#### Text aus einer Datei verschlüsseln

```bash
python main.py --encrypt --key SECRET --file input.txt --out encrypted.txt
```

Dies liest aus 'input.txt', verschlüsselt den Inhalt und speichert ihn in 'encrypted.txt'.

#### Text aus einer Datei entschlüsseln

```bash
python main.py --decrypt --key SECRET --file encrypted.txt --out decrypted.txt
```

Dies liest aus `encrypted.txt`, entschlüsselt  den Inhalt und speichert ihn in `decrypted.txt`.