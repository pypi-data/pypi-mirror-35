## TORO KBD Markdown Extension

The toro-mkdocs-kbd wraps your keyboard shortcut into a KBD tag. The tag will contain three
attributes; linux, macos, and windows. The values in the attributes will be the keyboard shortcut based
on the OS.


#### Installation

```
pip install toro-mkdocs-kbd
```

#### Usage

The markdown syntax will be the keyboard shortcut between two questions marks. A plus sign will be used
to separate the keys. __MOD__ will be used as a generic symbol for both the __ctrl__ and __command__ key.

```
??MOD+A??
```

The produced HTML of the markdown syntax will be:

```
<p><kbd linux="Ctrl + A" macos="⌘A" winodws="Ctrl + A"></kbd></p>
```

#### Conversion

| Markdown        | Windows/Linux | macOS |
|:---------------:|:-------------:|:-----:|
| ??mod??         | Ctrl          | ⌘     |
| ??alt??         | Alt           | ⌥     |
| ??enter??       | Enter         | ↩     |
| ??shift??       | Shift         | ⇧     |
| ??ctrl??        | Ctrl          | ⌃     |
| ??left??        | Left          | ←     |
| ??right??       | Right         | →     |
| ??up??          | Up            | ↑     |
| ??down??        | Down          | ↓     |
| ??tab??         | Tab           | ⇥     |
| ??esc??         | Esc           | ⎋     |
| ??space??       | Space         | Space |
