# Google Translate Plugin

This plugin is an [OVOS](https://openvoiceos.github.io/ovos-technical-manual/) language plugin for [OpenVoiceOS](https://github.com/OpenVoiceOS). It provides text translation and language detection through Google Translate, without an API key.

The package registers two plugins:

- `ovos-google-translate-plugin`: translates text between languages.
- `ovos-google-lang-detector-plugin`: detects the language of a text.

## Install

```bash
pip install ovos-google-translate-plugin
```

## Usage

Other components use this plugin to translate utterances and texts, for example [solvers](https://openvoiceos.github.io/ovos-technical-manual/solvers/) and [ovos-bidirectional-translation-plugin](https://github.com/OpenVoiceOS/ovos-bidirectional-translation-plugin).

Add this to one of the configuration files (for example `~/.config/mycroft/mycroft.conf`):

```javascript
"language": {
    "detection_module": "ovos-google-lang-detector-plugin",
    "translation_module": "ovos-google-translate-plugin"
}
```

## Related projects

- [ovos-bidirectional-translation-plugin](https://github.com/OpenVoiceOS/ovos-bidirectional-translation-plugin): translates utterances in both directions around a pipeline that only understands one language.
- [ovos-plugin-manager](https://github.com/OpenVoiceOS/ovos-plugin-manager): loads and manages OVOS plugins, including this one.

## License

Apache-2.0
