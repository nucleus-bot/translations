# Elgato Stream Deck Plugin

The [Elgato Stream Deck](https://www.elgato.com/en/gaming/stream-deck) is an LCD button display. Each button can be linked to an action using the Stream Decks software. NucleusBot has a plugin for integrating with the stream deck, allowing users that have both NucleusBot and a Stream Deck to log into their NucleusBot account and link various bot actions to their Stream Deck buttons.

# Translating

If you believe that translation is invalid, or does not make sense in the context that was provided, feel free to [open a new Issue](https://github.com/boss-nation-llc/NucleusBot-Translations/issues). If you would like to make a contribution, feel free to [make a new Pull Request](https://github.com/boss-nation-llc/NucleusBot-Translations/pulls).

# Translations

| Icon | Status |
| :---: | :--- |
| :heavy_check_mark: | Completed
| :heavy_exclamation_mark: | Needs to be updated, or may need revision |
| :heavy_multiplication_x: | Missing |

| Language | Status |
| :--- | :---: |
| English (US) | :heavy_multiplication_x: |
| Chinese (Simplified) | :heavy_multiplication_x: |
| French - Français | :heavy_multiplication_x: |
| German - Deutsch | :heavy_multiplication_x: |
| Japanese - 日本語 | :heavy_multiplication_x: |
| Korean - 한국어 | :heavy_multiplication_x: |
| Spanish - Español | :heavy_multiplication_x: |

# Translation Guide

### INTRODUCTION

Currently the Elgato Stream Deck only supports 7 languages: `English`, `Chinese (Simplified)`, `French`, `German`, `Japanese`, `Korean`, and `Spanish`. If you would like to request a language be added, this must be brought up with Elgato who is *not* an Affiliate of NucleusBot.

Stream Deck makes use of *json* (JavaScript Object Notation) files for handling it's translations and as such these file types will be used here out of the norm of NucleusBots *properties* files.

### TRANSLATIONS

Each JSON file will look similar to the following example.

```
{
  "Description": "",
  "Name": "NucleusBot",
  "tv.bossnation.plugin.button": {
    "Name": "Button",
    "Tooltip": ""
  }
}
```

The `Name` and `Description` fields are the Name and Description, relatively, of the Plugin itself. Fields such as `tv.bossnation.plugin.button` are references to actions that exist that have been created by this plugin.

Each reference will begin with `tv.bossnation.plugin` as is required by Elgato. `tv.bossnation` is Reverse-DNS format, and this is our *plugin*. `button` refers to the actual name of the action to be performed.

Each reference will also be an object that looks like the following example:

```
{
  "Name": "Button",
  "Tooltip": ""
}
```

`Name` is the name of the action that can be linked to a button, and `Tooltip` is a description of the action when it is moused over.
