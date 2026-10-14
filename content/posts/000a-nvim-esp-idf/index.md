---
title: "Neovim i ESP IDF z debuggerem"
date: 2026-10-14
draft: false
tags: [programowanie]

fortune: "Teraz panowie widzą, że nic nie widać. A dlaczego nie widać, to zaraz panowie zobaczą."
motto:
  quote: "Jesteśmy biedni. Musimy myśleć."
  cite: "Ernest Rutherford"
---

## Instalacja ESP IDF

Pobieramy.

```
cd ~/Apps
git clone --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh esp32c3
cd ~/Code
. ~/Apps/esp-idf/export.sh
idf.py --version
```

Sprawdzamy
