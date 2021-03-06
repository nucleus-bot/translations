# NucleusBot

[NucleusBot](https://www.nucleus.bot/bot) is a cross-platform cloud-hosted stream bot. This repository serves as the home for its translations. One of our missions for NucleusBot is to provide the opportunity for streamers to entertain their audiences in their native language. This is done by providing the option for various translations within the bot.

# Translating

If you believe that translation is invalid, or does not make sense in the context that was provided, feel free to [open a new Issue](https://github.com/nucleus-bot/translations/issues). If you would like to make a contribution, feel free to [make a new Pull Request](https://github.com/nucleus-bot/translations/pulls).

# Translations

| Icon | Status |
| :---: | :--- |
| ![Check](https://cdn.nucleus.bot/translations/status/check.png?) | Completed
| ![Exclamation](https://cdn.nucleus.bot/translations/status/notice.png?) | Needs to be updated, or may need revision |
| ![Unknown](https://cdn.nucleus.bot/translations/status/unknown.png?) | May not need to be included |
| ![Times](https://cdn.nucleus.bot/translations/status/times.png?) | Missing |

| Language | Status |
| :--- | :---: |
| Arabic - العربية | ![Arabic](https://api.nucleus.bot/translations/status/ar_sa.png) |
| Bulgarian - български език | ![Bulgarian](https://api.nucleus.bot/translations/status/bg_bg.png) |
| Catalan - Català | ![Catalan](https://api.nucleus.bot/translations/status/ca_es.png) |
| Czech - Český | ![Czech](https://api.nucleus.bot/translations/status/cs_cz.png) |
| Chinese (Traditional) | ![Chinese_Traditional](https://api.nucleus.bot/translations/status/zh_tw.png) |
| Chinese (Simplified) | ![Chinese_Simplified](https://api.nucleus.bot/translations/status/zh_cn.png) |
| Danish - Dansk | ![Danish](https://api.nucleus.bot/translations/status/da_dk.png) |
| Dutch - Nederlands | ![Dutch](https://api.nucleus.bot/translations/status/nl_nl.png) |
| English (US) | ![English_US](https://api.nucleus.bot/translations/status/en_us.png) |
| English (GB) | ![English_GB](https://api.nucleus.bot/translations/status/en_gb.png) |
| Farsi / Persian - فارسی | ![Persian](https://api.nucleus.bot/translations/status/fa_ir.png) |
| Finnish - Suomi | ![Finnish](https://api.nucleus.bot/translations/status/fi_fi.png) |
| French - Français | ![French](https://api.nucleus.bot/translations/status/fr_fr.png) |
| German - Deutsch | ![German](https://api.nucleus.bot/translations/status/de_de.png) |
| Greek - Ελληνικά | ![Greek](https://api.nucleus.bot/translations/status/el_gr.png) |
| Hebrew - עברית | ![Hebrew](https://api.nucleus.bot/translations/status/he_il.png) |
| Hindi - हिन्दी | ![Hindi](https://api.nucleus.bot/translations/status/hi_in.png) |
| Hungarian - Magyar | ![Hungarian](https://api.nucleus.bot/translations/status/hu_hu.png) |
| Indonesian - Bahasa Indonesia | ![Indonesian](https://api.nucleus.bot/translations/status/in_id.png) |
| Italian - Italiano | ![Italian](https://api.nucleus.bot/translations/status/it_it.png) |
| Japanese - 日本語 | ![Japanese](https://api.nucleus.bot/translations/status/ja_jp.png) |
| Korean - 한국어 | ![Korean](https://api.nucleus.bot/translations/status/ko_kr.png) |
| Malay - Melayu | ![Malay](https://api.nucleus.bot/translations/status/ms_my.png) |
| Norwegian - Norsk | ![Norwegian](https://api.nucleus.bot/translations/status/nb_no.png) |
| Polish - Polski | ![Polish](https://api.nucleus.bot/translations/status/pl_pl.png) |
| Portugese - Português | ![Portugese](https://api.nucleus.bot/translations/status/pt_br.png) |
| Romanian - Română | ![Romanian](https://api.nucleus.bot/translations/status/ro_ro.png) |
| Russian - Русский | ![Russian](https://api.nucleus.bot/translations/status/ru_ru.png) |
| Slovak - Slovenčina | ![Slovak](https://api.nucleus.bot/translations/status/sk_sk.png) |
| Spanish - Español | ![Spanish](https://api.nucleus.bot/translations/status/es_es.png) |
| Swedish - Svenska | ![Swedish](https://api.nucleus.bot/translations/status/sv_se.png) |
| Turkish - Türkçe | ![Turkish](https://api.nucleus.bot/translations/status/tr_tr.png) |
| Ukranian - Українська | ![Ukranian](https://api.nucleus.bot/translations/status/uk_ua.png) |
| Vietnamese - Tiếng Việt | ![Vietnamese](https://api.nucleus.bot/translations/status/vi_vn.png) |

# Translation Guide

### INTRODUCTION

NucleusBot uses ".properties" files to parse and store text at startup.
Each property is stored with a defined "key", which is used to fetch the necessary value when needed, as so:

### KEYS

```
key = Value
```

Each key is provided in lowercase-snakecase. Values can be provided in any casing needed. Please refer to the "English" files provided for examples.

In some cases a key may contain one of more period "`.`" in the case of subsets.

```
parent.keyA = ValueA
parent.keyB = ValueB
```

### ARRAYS

Keys that end with a "`[]`" are ARRAYs. These keys support multiple Values that are separated by a semi-colon "`;`"

```
key[] = Value1;Value2
```

ArrayValues can be split into multiple lines by escaping the newline using a backslash "`\`"

*New lines may also be indented to avoid being confused with new keys. Values are trimmed of any preceding or succeeding spaces.*

```
key[] = Value1;\
  Value2;\
  Value3
```

### EMBEDDING

A "Value" may also contain other Keys within them by using curly brackets `{}` like so `{key2}`.
This is called "Embedding" which includes another language value in the current one.

```
key1 = World
key2 = Hello {key1}
```

"key2" as shown above would display "Hello World".

Keys from a separate language file may be used by including that files name within the brackets, separated by a colon ":", `{file_name:key}`.

```
key = {example:key}
```

Embedded keys may also include a value from an array.
Including an ArrayValue will pick one of the values from the array at RANDOM when ran.

```
key1 = {key_array[]}
key2 = {example:key_array[]}
```

### REFERENCES

The "Website" section of the translations may make use of inline-links, where links may occur in the middle of sections of text.

To handle inline-links the translation properties makes use of embedded "references" within *Values*. A reference is surrounded with square brackets "[]" and consists of a reference and text separated by a colon ":", `[reference:The Translation]`

The left-side of the reference will always be the same across all files as this is the actual reference to the link to use, the right-side will be the translation to be contained within the link.

`[tos:Terms of Service]` may become `<a href="/terms">Terms of Service</a>`, or `[tos:Your Text Here]` to `<a href="/terms">Your Text Here</a>`

### VARIABLES

The "Value" for each key may contain a "Variable" which will be added to the Value at runtime, and may include usernames, numeric values, or otherwise.

Variables are set as follows

`%s` - Represents a string, Can be a username, rank, or parsed numeric value (1,000)  
`%d` - Represents an integer/digit. Can be a representative length of time, or other value  
`%1$` - The n^th provided variable, "%n$", if order of variables needs to be repeated or changed.  
`%n$s` - Represents the n^th variable as a string. Replace "n" with a digit  
`%n$d` - Represents the n^th variable as an integer/digit. Replace "n" with a digit  

The number of Variables in the "Value" MUST be equal to the number of Variables as provided in the "English" examples. Failure to do so may cause errors while the bot is running.
The "Empty" folder provided may be copied or overwritten to compensate for a new set of Language files.
