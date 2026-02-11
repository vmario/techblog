---
title: "Arduino bez Arduino IDE"
date: 2025-02-08
draft: false
tags: [arduino, embedded]

fortune: "Science is about knowing; engineering is about doing."
motto:
  quote: "As engineers, we were going to be in a position to change the world — not just study it."
  cite: "Henry Petroski"
---

## Po co to komu?

Gdy miałem zacząć prowadzić zajęcia ze studentami na [Arduino Uno Rev3](https://store.arduino.cc/products/arduino-uno-rev3)[^1], chciałem uniknąć stosowania [Arduino IDE](https://www.arduino.cc/en/software); zarówno ze względu na ograniczony zakres stosowania tego środowiska, jak i z powodu chęci pokazania niskopoziomowych aspektów programowania mikrokontrolerów. Nigdy wcześniej jednak nie używałem Arduino i, przeglądając zasoby Internetu, miałem problem, by jednoznacznie stwierdzić, czy można w prosty sposób wgrać własne oprogramowanie z użyciem fabrycznego bootloadera, a także czy ten bootloader można bez problemu usunąć i przywrócić. Postanowiłem więc zbadać ten temat, gdy tylko zdobyłem Arduino.

## Pierwsze spotkanie z Arduino

Zacząłem od sprawdzenia, czy płytka i połączenie z komputerm działają prawidłowo. Uruchomiłem webowe <abbr title="Integrated Development Environment">IDE</abbr> [Arduino Cloud Editor](https://create.arduino.cc/editor), bo nie przewidywałem potrzeby używania tego narzędzia lokalnie. Wybrałem typowe embeddedowe _Hello, world_, czyli _Examples -> BUILT IN -> BASICS -> Blink_. Tu IDE poinformowało mnie, że:

> To upload a sketch via USB port, make sure the Agent is installed and running on this computer.

Pobrałem więc `ArduinoCreateAgent-1.3.5-linux-amd64-installer.tar.gz`, rozpakowałem i uruchamiłem instalator:

```
tar xvf ArduinoCreateAgent-1.3.5-linux-amd64-installer.tar.gz
./ArduinoCreateAgent-1.3.5-linux-amd64-installer.run
```

poszło gładko i to z poziomu zwykłego użytkownika. W trayu pojawiła się ikona agenta.

Po podłączeniu Arduino do komputera `dmesg` wypluł:

```
[ 4933.114636] usb 1-2: new full-speed USB device number 6 using xhci_hcd
[ 4933.258237] usb 1-2: New USB device found, idVendor=2341, idProduct=0043, bcdDevice= 0.01
[ 4933.258255] usb 1-2: New USB device strings: Mfr=1, Product=2, SerialNumber=220
[ 4933.258263] usb 1-2: Manufacturer: Arduino (www.arduino.cc)
[ 4933.258268] usb 1-2: SerialNumber: 55736313438351C060D0
[ 4933.328895] cdc_acm 1-2:1.0: ttyACM0: USB ACM device
[ 4933.328919] usbcore: registered new interface driver cdc_acm
[ 4933.328921] cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
```

A jego przyjaciel `lsusb` potwierdził, że podłączyłem:

```
Bus 001 Device 006: ID 2341:0043 Arduino SA Uno R3 (CDC ACM)
```

Po sprawdzeniu uprawnień urządzenia `/dev/ttyACM0`:

```
Permissions  Size User Group Date Modified    Date Created     Name
crw-rw----  166,0 root uucp  2023-11-18 14:17 2023-11-18 14:17  /dev/ttyACM0
```

dodałem swojego użytkownika do grupy `uucp`, aby uzyskać prawo korzystania z urządzenia i&nbsp;móc wybrać w IDE `/dev/ttyACM0`. Po kliknięciu ptaszka _Verify_ przykład został skompilowany:

```
/usr/local/bin/arduino-cli  compile --fqbn arduino:avr:uno --build-cache-path /tmp --output-dir  /tmp/2473313307/build --build-path  /tmp/arduino-build-5946F7B4B9011FEF3B520D38FBC37C35   /tmp/2473313307/Blink
Sketch uses 924 bytes (2%) of program storage space. Maximum is 32256 bytes.
Global variables use 9 bytes (0%) of dynamic memory, leaving 2039 bytes for local variables. Maximum is 2048 bytes.
```

Po kliknięciu strzałki _Upload_ zamrugały diody na płytce, a po chwili dioda _L_ zaczęła migać z częstotliwością 0,5&nbsp;Hz (1&nbsp;s zgaszona, 1&nbsp;s zaświecona). W trakcie programowania został użyty _avrdude_:

```
Upload started
Programming with: Serial
Flashing  with  command:/home/vmario/.arduino-create/arduino/avrdude/6.3.0-arduino17/bin/avrdude   -C/home/vmario/.arduino-create/arduino/avrdude/6.3.0-arduino17/etc/avrdude.conf  -v -patmega328p -carduino -P/dev/ttyACM0 -b115200 -D  -Uflash:w:/tmp/arduino-create-agent2548950536/Blink.hex:i
```

## Własny przykład

Napisanie odpowiednika programu z Arduino IDE nie było skomplikowane. Ze [schematu ideowego](https://content.arduino.cc/assets/UNO-TH_Rev3e_sch.pdf), wynika, że dioda _L_ sterowana jest wzmacniaczem operacyjnym podłączonym do linii _SCK_, czyli pinu _PB5_. Procesor to ATmega328P taktowana rezonatorem 16&nbsp;MHz. Nic więcej wiedzieć nie potrzebowałem. Przygotowałem plik `main.cpp`:

```c++ {hl_lines=["19-22"]}
#include <avr/io.h>
#include <util/delay.h>

enum { PIN_LED = 5 };

/**
 * Inicjalizuje porty GPIO.
 */
void gpioInitialize()
{
    DDRB = _BV(PIN_LED);
}

/**
 * Pętla główna.
 */
void mainLoop()
{
    PORTB |= _BV(PIN_LED);
    _delay_ms(100);
    PORTB &= ~_BV(PIN_LED);
    _delay_ms(100);
}

/**
 * Funkcja główna.
 */
int main()
{
    gpioInitialize();

    while (true) {
        mainLoop();
    }
}
```

Pozostała kompilacja, utworzenie Intel Heksa i wgranie go za pośrednictwem agenta, czyli _de facto_ oryginalnego bootloadera tak, jak to robi Arduino IDE:

```
avr-g++ -mmcu=atmega328p -std=c++14 -Wall -Wextra -pedantic -Os -flto -DF_CPU=16000000 main.cpp -o arduino-without-ide.elf
avr-objcopy -O ihex arduino-without-ide.elf arduino-without-ide.hex
avrdude -v -p atmega328p -c arduino -P /dev/ttyACM0 -b115200 -U flash:w:arduino-without-ide.hex:i
```

## Uruchomienie programatora ISP

Po podłączeniu programatora <abbr title="In-System Programming">ISP</abbr>, a konkretnie _USBTinyISP_, Linux poinformował, że nowe urządzenie jest widoczne:

```
[18969.976197] usb 1-2: new low-speed USB device number 10 using xhci_hcd
[18970.120705] usb 1-2: New USB device found, idVendor=1781, idProduct=0c9f, bcdDevice= 1.07
[18970.120724] usb 1-2: New USB device strings: Mfr=0, Product=2, SerialNumber=0
[18970.120731] usb 1-2: Product: USBtinyISP
```

Potwierdził to `lsusb`:

```
Bus 001 Device 010: ID 1781:0c9f Multiple Vendors USBtiny
```

Oczywiście, _avrdude_ miał problem z uprawnieniami:

```
avrdude: usbdev_open(): found USBtinyISP, bus:device: 001:010
avrdude usbtiny_open() warning: cannot open USB device: Permission denied
avrdude usbtiny_open() error: cannot find USBtiny device (0x1781/0xc9f)
avrdude main() error: unable to open programmer usbtiny on port usb
```

Tym razem urządzenie nie było w grupie `uucp`, gdyż nie udaje modemu, jak bootloader Arduino:

```
Permissions  Size User Group Date Modified    Date Created     Name
crw-rw-r--  189,9 root root  2023-11-18 18:11 2023-11-18 18:11  /dev/bus/usb/001/010
```

Dodałem więc do katalogu `/etc/udev/rules.d` plik `99-avr.rules`:

```
# USBasp Programmer rules http://www.fischl.de/usbasp/
SUBSYSTEMS=="usb", ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="05dc", GROUP="uucp", MODE="0664"
# USBtinyISP Programmer rules
SUBSYSTEMS=="usb", ATTRS{idVendor}=="1781", ATTRS{idProduct}=="0c9f", GROUP="uucp", MODE="0664"
```

Programator nabrał ochoty do współpracy z użytkownikami grupy `uucp`:

```
Permissions   Size User Group Date Modified    Date Created     Name
crw-rw-r--  189,11 root uucp  2023-11-18 18:26 2023-11-18 18:26  /dev/bus/usb/001/012
```

## Backup oryginalnej zawartości

Mając uruchomiony programator ISP, zacząłem od odczytania _fuse bitów_:

```
avrdude -c usbtiny -p atmega328p -U lfuse:r:-:h -U hfuse:r:-:h -U efuse:r:-:h -U lock:r:-:h
```

które przedstawiały się następująco:

```
avrdude: processing -U lfuse:r:-:h
avrdude: reading lfuse memory ...
avrdude: writing output file <stdout>
0xff

avrdude: processing -U hfuse:r:-:h
avrdude: reading hfuse memory ...
avrdude: writing output file <stdout>
0xde

avrdude: processing -U efuse:r:-:h
avrdude: reading efuse memory ...
avrdude: writing output file <stdout>
0xfd

avrdude: processing -U lock:r:-:h
avrdude: reading lock memory ...
avrdude: writing output file <stdout>
0xcf
```

Wreszcie przyszedł czas na odczytanie zawartości pamięci flash:

```
avrdude -c usbtiny -p atmega328p -U flash:r:arduino.hex:i
```

Po obejrzeniu Intel Heksa widać, że początek pokrywa się ze skompilowanym własnym programem, a na końcu jest bootloader [Optiboot](https://github.com/Optiboot/optiboot), do którego wrócimy za chwilę.

## Usunięcie bootloadera

Zabezpieczywszy oryginalny bootloader, wgrałem skompilowany program przez ISP, tym samym usuwając bootloader:

```
avrdude -v -p atmega328p -c usbtiny -U flash:w:arduino-without-ide.hex:i
```

Dioda mrugała tak jak trzeba, tym samym wykazałem, że do Arduino Uno można wgrywać programy skompilowane samodzielnie za pomocą AVR GCC, zarówno przez wbudowany programator, jak i zewnętrzne urządzenie ISP.

## Przywrócenie bootloadera

Oczywiście po takim zabiegu podłączenie agenta i próba programowania przez Arduino IDE zakończyła się niepowodzeniem:

```
Upload started
Programming with: Serial
Flashing  with  command:/home/vmario/.arduino-create/arduino/avrdude/6.3.0-arduino17/bin/avrdude   -C/home/vmario/.arduino-create/arduino/avrdude/6.3.0-arduino17/etc/avrdude.conf  -v -patmega328p -carduino -P/dev/ttyACM0 -b115200 -D  -Uflash:w:/tmp/arduino-create-agent4050385497/Blink.hex:i
avrdude: Version 6.3-20190619
         Copyright (c) 2000-2005 Brian Dean, http://www.bdmicro.com/
         Copyright (c) 2007-2014 Joerg Wunsch
         System wide configuration file is "/home/vmario/.arduino-create/arduino/avrdude/6.3.0-arduino17/etc/avrdude.conf"
         User configuration file is "/home/vmario/.avrduderc"
         User configuration file does not exist or is not a regular file, skipping
         Using Port                    : /dev/ttyACM0
         Using Programmer              : arduino
         Overriding Baud Rate          : 115200
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 1 of 10: not in sync: resp=0x00
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 2 of 10: not in sync: resp=0x00
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 3 of 10: not in sync: resp=0x00
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 4 of 10: not in sync: resp=0x00
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 5 of 10: not in sync: resp=0x00
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 6 of 10: not in sync: resp=0x00
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 7 of 10: not in sync: resp=0x00
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 8 of 10: not in sync: resp=0x00
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 9 of 10: not in sync: resp=0x00
avrdude: stk500_recv(): programmer is not responding
avrdude: stk500_getsync() attempt 10 of 10: not in sync: resp=0x00
avrdude done.  Thank you.
```

Aby to naprawić, wystarczyło wgrać kopię zapasową wsadu z oryginalnym bootloaderem. Co jednak zrobić, gdy się takiej kopii nie wykonało zawczasu? Można pobrać bootloader ze strony projektu Arduino. Jest tam [skompilowany wsad](https://github.com/arduino/Arduino/blob/master/app/test/optiboot_atmega328.hex). Co ciekawe, nie jest to [aktualny Optiboot](https://github.com/Optiboot/optiboot/blob/master/optiboot/bootloaders/optiboot/optiboot_atmega328.hex), ale [wersja sprzed kilkunastu lat](https://github.com/Optiboot/optiboot/blob/c0bbc7d8a38cbc0382ded4f22e4fa4ab09fb77be/optiboot/bootloaders/optiboot/optiboot_atmega328.hex).

```
avrdude -v -p atmega328p -c usbtiny -U flash:w:optiboot_atmega328.hex:i
```

[^1]: Wybrałem tę platformę nie tylko z powodu wygody i łatwej dostępności, ale przede wszystkim dlatego, że studenci chcą uczyć się na tym, o czym słyszą w&nbsp;Internecie.
