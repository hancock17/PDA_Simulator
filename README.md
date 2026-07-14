# PDA Simulator — `a^n b^n`

Küçük ve bağımlılıksız bir Python projesi. Bir pushdown automaton (PDA)
kullanarak `L = {a^n b^n | n >= 0}` dilindeki kelimeleri tanır.

Örneğin `aabb` kabul edilir; `aab`, `abb` ve `aba` reddedilir. Boş dize de
tanımlı dilde (`n = 0`) olduğu için kabul edilir.

## Gereksinimler

- Python 3.9 veya üzeri
- Harici paket gerektirmez

## Kullanım

Tek bir dizeyi denemek için:

```bash
python pda.py aabb
```

Örnekleri çalıştırmak için:

```bash
python pda.py
```

Testleri çalıştırmak için:

```bash
python -m unittest -v
```

## Nasıl çalışır?

- Her `a` için yığına bir işaretçi eklenir.
- Her `b` için yığından bir işaretçi çıkarılır.
- İlk `b` sonrasında `a` görülürse veya eşleşmeyen sembol kalırsa girdi reddedilir.

## Proje yapısı

```text
pda.py       PDA uygulaması ve komut satırı arayüzü
test_pda.py  Otomatik testler
```

## Lisans

Bu proje eğitim amaçlıdır. GitHub'da paylaşmadan önce tercih ettiğiniz lisansı
ekleyin (örneğin MIT License).
