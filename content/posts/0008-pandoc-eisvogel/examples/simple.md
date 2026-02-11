---
title: "Lorem ipsum"
subtitle: "Dolor sit amet"
footer-left: "Consectetur adipiscing elit"
author: [Mariusz Chilmon <<vmario@vmario.org>>]
lang: "pl"
titlepage: yes
colorlinks: yes
...

> Talk is cheap. Show me the code.
>
> — _Linus Torvalds_

# Rozdział

## Podrozdział

,,Zażółć gęślą jaźń''.

Lorem ipsum dolor --- sit amet,
[consectetur](https://example.com) adipiscing elit[^1].
_Vestibulum_ **placerat** ***erat*** `quis` vulputate consequat.

Pellentesque dui turpis:

* tincidunt vel sapien eget,
* feugiat consequat nunc.

In ultricies augue ut arcu maximus dapibus:

1. In non eleifend sapien.
2. Nullam facilisis id nibh vitae rhoncus.

[^1]: Vestibulum ut mollis libero.

| Quisque in          | Varius lacus             |
|---------------------|--------------------------|
| proin semper        | lacus in massa           |
| tincidunt hendrerit | mauris quis tellus lorem |

```c++
#include <iostream>
#include <vector>

using namespace std;

// Example code.
int main() {
    const vector<int> NUMBERS{42, 43};

    for (const auto& number : NUMBERS) {
        [](int n){ cout << n << " "; }(number);
    }

    return EXIT_SUCCESS;
};
```
