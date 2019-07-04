# NucleusBot

[NucleusBot](https://www.bossnation.tv/bot) is a cross-platform cloud-hosted stream bot developed by **Boss Nation LLC**. This repository serves as the home for its translations. One of our missions for NucleusBot is to provide the opportunity for streamers to entertain their audiences in their native language. This is done by providing the option for various translations within the bot.

# Translating

If you believe that translation is invalid, or does not make sense in the context that was provided, feel free to [open a new Issue](https://github.com/boss-nation-llc/NucleusBot-Translations/issues). If you would like to make a contribution, feel free to [make a new Pull Request](https://github.com/boss-nation-llc/NucleusBot-Translations/pulls).

# Translations

| Icon | Status |
| :---: | :--- |
| :heavy_check_mark: | Completed
| :heavy_exclamation_mark: | Needs to be updated, or may need revision |
| :question: | May not need to be included |
| :heavy_multiplication_x: | Missing |

| Language | Status |
| :--- | :---: |
| English (US) | :heavy_check_mark: |
| Arabic - العربية | :heavy_multiplication_x: |
| Bulgarian - български език | :heavy_multiplication_x: |
| Catalan - Català | :heavy_multiplication_x: |
| Czech - Český | :heavy_multiplication_x: |
| Chinese (Traditional) | :heavy_multiplication_x: |
| Chinese (Simplified) | :heavy_multiplication_x: |
| Danish - Dansk | :heavy_multiplication_x: |
| Dutch - Nederlands | :heavy_multiplication_x: |
| English (GB) | :question: |
| Finnish - Suomi | :heavy_multiplication_x: |
| French - Français | :heavy_multiplication_x: |
| German - Deutsch | :heavy_multiplication_x: |
| Greek - Ελληνικά | :heavy_multiplication_x: |
| Hebrew - עברית | :heavy_multiplication_x: |
| Hindi - हिन्दी | :heavy_multiplication_x: |
| Hungarian - Magyar | :heavy_multiplication_x: |
| Indonesian - Bahasa Indonesia | :heavy_multiplication_x: |
| Italian - Italiano | :heavy_multiplication_x: |
| Japanese - 日本語 | :heavy_multiplication_x: |
| Korean - 한국어 | :heavy_multiplication_x: |
| Malay | :heavy_multiplication_x: |
| Norwegian - Norsk | :heavy_exclamation_mark: |
| Polish - Polski | :heavy_multiplication_x: |
| Portugese - Português | :heavy_multiplication_x: |
| Romanian - Română | :heavy_multiplication_x: |
| Russian - Русский | :heavy_multiplication_x: |
| Slovak - Slovenčina | :heavy_multiplication_x: |
| Spanish - Español | :heavy_multiplication_x: |
| Swedish - Svenska | :heavy_multiplication_x: |
| Turkish - Türkçe | :heavy_multiplication_x: |
| Ukranian - Українська | :heavy_multiplication_x: |
| Vietnamese - Tiếng Việt | :heavy_multiplication_x: |


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

`[tos:Terms of Service]` may become `<a href="/terms">Terms of Service</a>`.

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