# Google Translate Plugin

## Usage

The plugin is used in a wider context to translate utterances/texts on demand (e.g. from [solvers](https://openvoiceos.github.io/ovos-technical-manual/solvers/) and [ovos-bidirectional-translation-plugin](https://github.com/OpenVoiceOS/ovos-bidirectional-translation-plugin))

add this to one of the configuration files (eg `~./config/mycroft/mycroft.conf`)

```javascript
"language": {
    "detection_module": "ovos-google-lang-detector-plugin",
    "translation_module": "ovos-google-translate-plugin "
}
```
