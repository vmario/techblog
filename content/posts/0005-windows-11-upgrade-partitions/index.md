---
title: "Naprawa GRUB-a po aktualizacji do Windows 11"
date: 2023-10-28
draft: false
tags: [linux, windows]

fortune: "Linux jest bardziej uczciwy, bo po aktualizacji psuje sam siebie."
motto:
  quote: "Never trust a computer you can't throw out a window."
  cite: "Steve Wozniak"
---

Długo mnie namawiał Windows 10 na aktualizację do wersji 11, niczym bot od fotowoltaiki na położenie paneli na północnej połaci dachu. Wprawdzie rzadko używam tego systemu, ale zwlekałem, bo spodziewałem się bliżej nieokreślonych problemów, z którymi będę się później bujał przez kilka dni. Podświadomie może czułem się też oszukany, bo przecież miało nie być kolejnych Windowsów. To miało się już skończyć.

Z drugiej strony wydanie jedenastki oznacza przynajmniej tymczasową porażkę koncepcji _Windows as a service_, zapoczątkowanej w 2015 roku:

> Right now we’re releasing Windows 10, and because Windows 10 is the last version of Windows, we’re all still working on Windows 10.
>
> --- <cite>Jerry Nixon</cite>

W końcu się zgodziłem. Windows 11 wystartował bez problemu, ale gdy spróbowałem uruchomić Linuksa, okazało się, że dostałem jednak kopa w tyłek:

```
Welcome to GRUB!

error: unknown filesystem.
Entering rescue mode...
grub rescue>
```

Mogłem powiedzieć z satysfakcją, &bdquo;a nie mówiłem!&rdquo;, ale potrzebowałem przecież działającego komputera. Domyśliłem się, że Microsoft stwierdził, że to nic nie szkodzi nagrzebać w tablicy partycji, więc ściągnąłem na pendrive'a instalator Arch Linuksa i odpaliłem `fdisk -l`. Otrzymałem taki układ partycji:

Urządzenie|Rozmiar|Rodzaj
----------|------:|------
/dev/sda1 |   499M|Windows recovery environment
/dev/sda2 |   100M|EFI System
/dev/sda3 |    16M|Microsoft reserved
/dev/sda4 | 171.4G|Microsoft basic data
/dev/sda5 |   772M|Windows recovery environment
/dev/sda6 |   273G|Linux filesystem
/dev/sda7 |    20G|Linux swap

Zamontowałem partycję linuksową `/dev/sda6` i wyświetliłem `/etc/fstab`:

```
mkdir /mnt/root
mount /dev/sda6 /mnt/root
cat /mnt/root/etc/fstab
```

Zawartość `/etc/fstab` wskazywała, że coś rzeczywiście nie gra:

```
# Static information about the filesystems.
# See fstab(5) for details.

# <file system> <dir> <type> <options> <dump> <pass>
# /dev/sda5
UUID=5610dcc4-9301-4b94-87e1-d1e574f81780       /               ext4            rw,noatime,discard      0 1

/dev/sda4                                       /mnt/win-unlock fuse.dislocker
/mnt/win-unlock/dislocker-file                  /mnt/win        ntfs-3g         rw,fmask=0112,dmask=0002,gid=disk      0 0
```

Wyglądało na to, że pojawiła się dodatkowa partycja między główną partycją windowsową a linuksową. Potwierdziła to też zawartość konfiguracji GRUB-a w `/mnt/root/boot/grub/grub.cfg`, gdzie znalazłem odwołania do partycji `gpt5`, a nie `gpt6`.

Mój GRUB jednak najwyraźniej nie docierał w ogóle do etapu wczytania konfiguracji, więc wyjściowym problemem był sam plik bootloadera na partycji <abbr title="Unified Extensible Firmware Interface">UEFI</abbr> (<abbr title="EFI System Partition">ESP</abbr> — _EFI System Partition_). Wtedy na to nie wpadłem, ale gdybym wówczas przeszukał binarkę bootloadera pod kątem położenia katalogu GRUB-a:

```
mkdir /mnt/esp
mount /dev/sda2 /mnt/esp
strings /mnt/esp/EFI/GRUB/grubx64.efi | grep boot/grub
```

otrzymałbym zapewne:

```
(,gpt5)/boot/grub
```

Tak, czy inaczej, sprawa była dosyć jasna: należy przeinstalować GRUB-a i wygenerować na nowo jego konfigurację. W tym celu z systemu instalacyjno-ratunkowego należy chrootować się na nasz dysk (`grub-install` zakłada, że działa w docelowym systemie) i zamontować <abbr title="EFI System Partition">ESP</abbr>:

```
mkdir /mnt/root
mount /dev/sda6 /mnt/root
arch-chroot /mnt/root
mkdir /tmp/esp
mount /dev/sda2 /tmp/esp
```

Następnie instalujemy GRUB-a:

```
grub-install --target=x86_64-efi --efi-directory=/tmp/esp --bootloader-id=GRUB
```

i regenerujemy konfigurację, uprzednio zrobiwszy kopię zapasową:

```
cd /boot/grub
cp grub.cfg grub.cfg.bak
grub-mkconfig -o grub.cfg
```

Po restarcie system powinien wstać poprawnie. Można wówczas jeszcze poprawić w&nbsp;`/etc/fstab` komentarz z numerem partycji, żeby nie wprowadzał nas w błąd.
