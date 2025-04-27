# CLI Reference

**Usage**:

```console
$ brave-search-python-client [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

🦁 Brave Search Python Client v0.4.25 - built with love in Berlin 🐻

**Commands**:

* `web`: Search the web.
* `images`: Search images.
* `videos`: Search videos.
* `news`: Search news.
* `Command Line Interface of Brave Search Python Client`

## `brave-search-python-client web`

Search the web.

**Usage**:

```console
$ brave-search-python-client web [OPTIONS] Q
```

**Arguments**:

* `Q`: The search query to perform  [required]

**Options**:

* `--country [ALL|AR|AU|AT|BE|BR|CA|CL|DK|FI|FR|DE|HK|IN|ID|IT|JP|KR|MY|MX|NL|NZ|NO|CN|PL|PT|PH|RU|SA|ZA|ES|SE|CH|TW|TR|GB|US]`: The country to search from (2-letter country code or &quot;ALL&quot; for all regions, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: ALL]
* `--search-lang [ar|eu|bn|bg|ca|zh-hans|zh-hant|hr|cs|da|nl|en|en-gb|et|fi|fr|gl|de|gu|he|hi|hu|is|it|jp|kn|ko|lv|lt|ms|ml|mr|nb|pl|pt-br|pt-pt|pa|ro|ru|sr|sk|sl|es|sv|ta|te|th|tr|uk|vi]`: The language to search in (2 letter language code, see https://api.search.brave.com/app/documentation/image-search/codes).  [default: en]
* `--ui-lang [es-AR|en-AU|de-AT|nl-BE|fr-BE|pt-BR|en-CA|fr-CA|es-CL|da-DK|fi-FI|fr-FR|de-DE|zh-HK|en-IN|en-ID|it-IT|ja-JP|ko-KR|en-MY|es-MX|nl-NL|en-NZ|no-NO|zh-CN|pl-PL|en-PH|ru-RU|en-ZA|es-ES|sv-SE|fr-CH|de-CH|zh-TW|tr-TR|en-GB|en-US|es-US]`: The language to display (see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en-US]
* `--count INTEGER`: The number of results to return (max 20)  [default: 20]
* `--offset INTEGER`: The offset to start from (max 9)  [default: 0]
* `--safesearch [off|moderate|strict]`: Enable safe search (off, moderate, strict)  [default: moderate]
* `--freshness [pd|pw|pm|py]`: pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30
* `--text-decorations / --no-text-decorations`: Whether display strings (e.g. result snippets) should include decoration markers (e.g. highlighting characters).  [default: text-decorations]
* `--spellcheck / --no-spellcheck`: Enable spellcheck  [default: spellcheck]
* `--result-filter TEXT`: Comma delimited string of result types to include in the search response. Not specifying this parameter will return back all result types in search response where data is available and a plan with the corresponding option is subscribed. The response always includes query and type to identify any query modifications and response type respectively. Available result filter values are: - discussions - faq - infobox - news - query - summarizer - videos - web - locations. Example result filter param result_filter=discussions, videos returns only discussions, and videos responses. Another example where only location results are required, set the result_filter param to result_filter=locations
* `--googles-id TEXT`: Goggles act as a custom re-ranking on top of Brave&#x27;s search index. For more details, refer to the Goggles repository (https://github.com/brave/goggles-quickstart)
* `--units [metric|imperial]`: The measurement units. If not provided, units are derived from search country. Possible values are: - metric: The standardized measurement system - imperial: The British Imperial system of units.
* `--extra-snippets / --no-extra-snippets`: A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans  [default: no-extra-snippets]
* `--summary / --no-summary`: This parameter enables summary key generation in web search results. This is required for summarizer to be enabled.  [default: no-summary]
* `--dump-response / --no-dump-response`: Dump the raw response from the API into a file (response.json in current working directory)  [default: no-dump-response]
* `--help`: Show this message and exit.

## `brave-search-python-client images`

Search images.

**Usage**:

```console
$ brave-search-python-client images [OPTIONS] Q
```

**Arguments**:

* `Q`: The search query to perform  [required]

**Options**:

* `--country [ALL|AR|AU|AT|BE|BR|CA|CL|DK|FI|FR|DE|HK|IN|ID|IT|JP|KR|MY|MX|NL|NZ|NO|CN|PL|PT|PH|RU|SA|ZA|ES|SE|CH|TW|TR|GB|US]`: The country to search from (2-letter country code or &quot;ALL&quot; for all regions - see https://api.search.brave.com/app/documentation/image-search/codes)  [default: ALL]
* `--search-lang [ar|eu|bn|bg|ca|zh-hans|zh-hant|hr|cs|da|nl|en|en-gb|et|fi|fr|gl|de|gu|he|hi|hu|is|it|jp|kn|ko|lv|lt|ms|ml|mr|nb|pl|pt-br|pt-pt|pa|ro|ru|sr|sk|sl|es|sv|ta|te|th|tr|uk|vi]`: The language to search in (2 letter language code, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en]
* `--count INTEGER`: The number of results to return (max 20)  [default: 20]
* `--safesearch [off|strict]`: Enable safe search (off, strict)  [default: strict]
* `--spellcheck / --no-spellcheck`: Enable spellcheck  [default: spellcheck]
* `--dump-response / --no-dump-response`: Dump the raw response from the API into a file (response.json in current working directory)  [default: no-dump-response]
* `--help`: Show this message and exit.

## `brave-search-python-client videos`

Search videos.

**Usage**:

```console
$ brave-search-python-client videos [OPTIONS] Q
```

**Arguments**:

* `Q`: The search query to perform  [required]

**Options**:

* `--country [ALL|AR|AU|AT|BE|BR|CA|CL|DK|FI|FR|DE|HK|IN|ID|IT|JP|KR|MY|MX|NL|NZ|NO|CN|PL|PT|PH|RU|SA|ZA|ES|SE|CH|TW|TR|GB|US]`: The country to search from (2-letter country code or &quot;ALL&quot; for all regions, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: ALL]
* `--search-lang [ar|eu|bn|bg|ca|zh-hans|zh-hant|hr|cs|da|nl|en|en-gb|et|fi|fr|gl|de|gu|he|hi|hu|is|it|jp|kn|ko|lv|lt|ms|ml|mr|nb|pl|pt-br|pt-pt|pa|ro|ru|sr|sk|sl|es|sv|ta|te|th|tr|uk|vi]`: The language to search in (2 letter language code, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en]
* `--ui-lang [es-AR|en-AU|de-AT|nl-BE|fr-BE|pt-BR|en-CA|fr-CA|es-CL|da-DK|fi-FI|fr-FR|de-DE|zh-HK|en-IN|en-ID|it-IT|ja-JP|ko-KR|en-MY|es-MX|nl-NL|en-NZ|no-NO|zh-CN|pl-PL|en-PH|ru-RU|en-ZA|es-ES|sv-SE|fr-CH|de-CH|zh-TW|tr-TR|en-GB|en-US|es-US]`: The language to display (see https://api.search.brave.com/app/documentation/image-search/codes).  [default: en-US]
* `--count INTEGER`: The number of results to return (max 20)  [default: 20]
* `--offset INTEGER`: The offset to start from (max 9)  [default: 0]
* `--freshness [pd|pw|pm|py]`: pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30
* `--spellcheck / --no-spellcheck`: Enable spellcheck  [default: spellcheck]
* `--dump-response / --no-dump-response`: Dump the raw response from the API into a file (response.json in current working directory)  [default: no-dump-response]
* `--help`: Show this message and exit.

## `brave-search-python-client news`

Search news.

**Usage**:

```console
$ brave-search-python-client news [OPTIONS] Q
```

**Arguments**:

* `Q`: The search query to perform  [required]

**Options**:

* `--country [ALL|AR|AU|AT|BE|BR|CA|CL|DK|FI|FR|DE|HK|IN|ID|IT|JP|KR|MY|MX|NL|NZ|NO|CN|PL|PT|PH|RU|SA|ZA|ES|SE|CH|TW|TR|GB|US]`: The country to search from (2-letter country code or &quot;ALL&quot; for all regions, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: ALL]
* `--search-lang [ar|eu|bn|bg|ca|zh-hans|zh-hant|hr|cs|da|nl|en|en-gb|et|fi|fr|gl|de|gu|he|hi|hu|is|it|jp|kn|ko|lv|lt|ms|ml|mr|nb|pl|pt-br|pt-pt|pa|ro|ru|sr|sk|sl|es|sv|ta|te|th|tr|uk|vi]`: The language to search in (2 letter language code, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en]
* `--ui-lang [es-AR|en-AU|de-AT|nl-BE|fr-BE|pt-BR|en-CA|fr-CA|es-CL|da-DK|fi-FI|fr-FR|de-DE|zh-HK|en-IN|en-ID|it-IT|ja-JP|ko-KR|en-MY|es-MX|nl-NL|en-NZ|no-NO|zh-CN|pl-PL|en-PH|ru-RU|en-ZA|es-ES|sv-SE|fr-CH|de-CH|zh-TW|tr-TR|en-GB|en-US|es-US]`: The language to display (see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en-US]
* `--count INTEGER`: The number of results to return (max 20)  [default: 20]
* `--offset INTEGER`: The offset to start from (max 9)  [default: 0]
* `--safesearch [off|moderate|strict]`: Enable safe search (off, moderate, strict)  [default: moderate]
* `--freshness [pd|pw|pm|py]`: pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30
* `--spellcheck / --no-spellcheck`: Enable spellcheck  [default: spellcheck]
* `--extra-snippets / --no-extra-snippets`: A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans  [default: no-extra-snippets]
* `--dump-response / --no-dump-response`: Dump the raw response from the API into a file (response.json in current working directory)  [default: no-dump-response]
* `--help`: Show this message and exit.

## `brave-search-python-client Command Line Interface of Brave Search Python Client`

**Usage**:

```console
$ brave-search-python-client Command Line Interface of Brave Search Python Client [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

🦁 Brave Search Python Client v0.4.25 - built with love in Berlin 🐻

**Commands**:

* `web`: Search the web.
* `images`: Search images.
* `videos`: Search videos.
* `news`: Search news.

### `brave-search-python-client Command Line Interface of Brave Search Python Client web`

Search the web.

**Usage**:

```console
$ brave-search-python-client Command Line Interface of Brave Search Python Client web [OPTIONS] Q
```

**Arguments**:

* `Q`: The search query to perform  [required]

**Options**:

* `--country [ALL|AR|AU|AT|BE|BR|CA|CL|DK|FI|FR|DE|HK|IN|ID|IT|JP|KR|MY|MX|NL|NZ|NO|CN|PL|PT|PH|RU|SA|ZA|ES|SE|CH|TW|TR|GB|US]`: The country to search from (2-letter country code or &quot;ALL&quot; for all regions, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: ALL]
* `--search-lang [ar|eu|bn|bg|ca|zh-hans|zh-hant|hr|cs|da|nl|en|en-gb|et|fi|fr|gl|de|gu|he|hi|hu|is|it|jp|kn|ko|lv|lt|ms|ml|mr|nb|pl|pt-br|pt-pt|pa|ro|ru|sr|sk|sl|es|sv|ta|te|th|tr|uk|vi]`: The language to search in (2 letter language code, see https://api.search.brave.com/app/documentation/image-search/codes).  [default: en]
* `--ui-lang [es-AR|en-AU|de-AT|nl-BE|fr-BE|pt-BR|en-CA|fr-CA|es-CL|da-DK|fi-FI|fr-FR|de-DE|zh-HK|en-IN|en-ID|it-IT|ja-JP|ko-KR|en-MY|es-MX|nl-NL|en-NZ|no-NO|zh-CN|pl-PL|en-PH|ru-RU|en-ZA|es-ES|sv-SE|fr-CH|de-CH|zh-TW|tr-TR|en-GB|en-US|es-US]`: The language to display (see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en-US]
* `--count INTEGER`: The number of results to return (max 20)  [default: 20]
* `--offset INTEGER`: The offset to start from (max 9)  [default: 0]
* `--safesearch [off|moderate|strict]`: Enable safe search (off, moderate, strict)  [default: moderate]
* `--freshness [pd|pw|pm|py]`: pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30
* `--text-decorations / --no-text-decorations`: Whether display strings (e.g. result snippets) should include decoration markers (e.g. highlighting characters).  [default: text-decorations]
* `--spellcheck / --no-spellcheck`: Enable spellcheck  [default: spellcheck]
* `--result-filter TEXT`: Comma delimited string of result types to include in the search response. Not specifying this parameter will return back all result types in search response where data is available and a plan with the corresponding option is subscribed. The response always includes query and type to identify any query modifications and response type respectively. Available result filter values are: - discussions - faq - infobox - news - query - summarizer - videos - web - locations. Example result filter param result_filter=discussions, videos returns only discussions, and videos responses. Another example where only location results are required, set the result_filter param to result_filter=locations
* `--googles-id TEXT`: Goggles act as a custom re-ranking on top of Brave&#x27;s search index. For more details, refer to the Goggles repository (https://github.com/brave/goggles-quickstart)
* `--units [metric|imperial]`: The measurement units. If not provided, units are derived from search country. Possible values are: - metric: The standardized measurement system - imperial: The British Imperial system of units.
* `--extra-snippets / --no-extra-snippets`: A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans  [default: no-extra-snippets]
* `--summary / --no-summary`: This parameter enables summary key generation in web search results. This is required for summarizer to be enabled.  [default: no-summary]
* `--dump-response / --no-dump-response`: Dump the raw response from the API into a file (response.json in current working directory)  [default: no-dump-response]
* `--help`: Show this message and exit.

### `brave-search-python-client Command Line Interface of Brave Search Python Client images`

Search images.

**Usage**:

```console
$ brave-search-python-client Command Line Interface of Brave Search Python Client images [OPTIONS] Q
```

**Arguments**:

* `Q`: The search query to perform  [required]

**Options**:

* `--country [ALL|AR|AU|AT|BE|BR|CA|CL|DK|FI|FR|DE|HK|IN|ID|IT|JP|KR|MY|MX|NL|NZ|NO|CN|PL|PT|PH|RU|SA|ZA|ES|SE|CH|TW|TR|GB|US]`: The country to search from (2-letter country code or &quot;ALL&quot; for all regions - see https://api.search.brave.com/app/documentation/image-search/codes)  [default: ALL]
* `--search-lang [ar|eu|bn|bg|ca|zh-hans|zh-hant|hr|cs|da|nl|en|en-gb|et|fi|fr|gl|de|gu|he|hi|hu|is|it|jp|kn|ko|lv|lt|ms|ml|mr|nb|pl|pt-br|pt-pt|pa|ro|ru|sr|sk|sl|es|sv|ta|te|th|tr|uk|vi]`: The language to search in (2 letter language code, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en]
* `--count INTEGER`: The number of results to return (max 20)  [default: 20]
* `--safesearch [off|strict]`: Enable safe search (off, strict)  [default: strict]
* `--spellcheck / --no-spellcheck`: Enable spellcheck  [default: spellcheck]
* `--dump-response / --no-dump-response`: Dump the raw response from the API into a file (response.json in current working directory)  [default: no-dump-response]
* `--help`: Show this message and exit.

### `brave-search-python-client Command Line Interface of Brave Search Python Client videos`

Search videos.

**Usage**:

```console
$ brave-search-python-client Command Line Interface of Brave Search Python Client videos [OPTIONS] Q
```

**Arguments**:

* `Q`: The search query to perform  [required]

**Options**:

* `--country [ALL|AR|AU|AT|BE|BR|CA|CL|DK|FI|FR|DE|HK|IN|ID|IT|JP|KR|MY|MX|NL|NZ|NO|CN|PL|PT|PH|RU|SA|ZA|ES|SE|CH|TW|TR|GB|US]`: The country to search from (2-letter country code or &quot;ALL&quot; for all regions, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: ALL]
* `--search-lang [ar|eu|bn|bg|ca|zh-hans|zh-hant|hr|cs|da|nl|en|en-gb|et|fi|fr|gl|de|gu|he|hi|hu|is|it|jp|kn|ko|lv|lt|ms|ml|mr|nb|pl|pt-br|pt-pt|pa|ro|ru|sr|sk|sl|es|sv|ta|te|th|tr|uk|vi]`: The language to search in (2 letter language code, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en]
* `--ui-lang [es-AR|en-AU|de-AT|nl-BE|fr-BE|pt-BR|en-CA|fr-CA|es-CL|da-DK|fi-FI|fr-FR|de-DE|zh-HK|en-IN|en-ID|it-IT|ja-JP|ko-KR|en-MY|es-MX|nl-NL|en-NZ|no-NO|zh-CN|pl-PL|en-PH|ru-RU|en-ZA|es-ES|sv-SE|fr-CH|de-CH|zh-TW|tr-TR|en-GB|en-US|es-US]`: The language to display (see https://api.search.brave.com/app/documentation/image-search/codes).  [default: en-US]
* `--count INTEGER`: The number of results to return (max 20)  [default: 20]
* `--offset INTEGER`: The offset to start from (max 9)  [default: 0]
* `--freshness [pd|pw|pm|py]`: pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30
* `--spellcheck / --no-spellcheck`: Enable spellcheck  [default: spellcheck]
* `--dump-response / --no-dump-response`: Dump the raw response from the API into a file (response.json in current working directory)  [default: no-dump-response]
* `--help`: Show this message and exit.

### `brave-search-python-client Command Line Interface of Brave Search Python Client news`

Search news.

**Usage**:

```console
$ brave-search-python-client Command Line Interface of Brave Search Python Client news [OPTIONS] Q
```

**Arguments**:

* `Q`: The search query to perform  [required]

**Options**:

* `--country [ALL|AR|AU|AT|BE|BR|CA|CL|DK|FI|FR|DE|HK|IN|ID|IT|JP|KR|MY|MX|NL|NZ|NO|CN|PL|PT|PH|RU|SA|ZA|ES|SE|CH|TW|TR|GB|US]`: The country to search from (2-letter country code or &quot;ALL&quot; for all regions, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: ALL]
* `--search-lang [ar|eu|bn|bg|ca|zh-hans|zh-hant|hr|cs|da|nl|en|en-gb|et|fi|fr|gl|de|gu|he|hi|hu|is|it|jp|kn|ko|lv|lt|ms|ml|mr|nb|pl|pt-br|pt-pt|pa|ro|ru|sr|sk|sl|es|sv|ta|te|th|tr|uk|vi]`: The language to search in (2 letter language code, see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en]
* `--ui-lang [es-AR|en-AU|de-AT|nl-BE|fr-BE|pt-BR|en-CA|fr-CA|es-CL|da-DK|fi-FI|fr-FR|de-DE|zh-HK|en-IN|en-ID|it-IT|ja-JP|ko-KR|en-MY|es-MX|nl-NL|en-NZ|no-NO|zh-CN|pl-PL|en-PH|ru-RU|en-ZA|es-ES|sv-SE|fr-CH|de-CH|zh-TW|tr-TR|en-GB|en-US|es-US]`: The language to display (see https://api.search.brave.com/app/documentation/image-search/codes)  [default: en-US]
* `--count INTEGER`: The number of results to return (max 20)  [default: 20]
* `--offset INTEGER`: The offset to start from (max 9)  [default: 0]
* `--safesearch [off|moderate|strict]`: Enable safe search (off, moderate, strict)  [default: moderate]
* `--freshness [pd|pw|pm|py]`: pd: Discovered within the last 24 hours. - pw: Discovered within the last 7 Days. - pm: Discovered within the last 31 Days. - py: Discovered within the last 365 Days… - YYYY-MM-DDtoYYYY-MM-DD: timeframe is also supported by specifying the date range e.g. 2022-04-01to2022-07-30
* `--spellcheck / --no-spellcheck`: Enable spellcheck  [default: spellcheck]
* `--extra-snippets / --no-extra-snippets`: A snippet is an excerpt from a page you get as a result of the query, and extra_snippets allow you to get up to 5 additional, alternative excerpts. Only available under Free AI, Base AI, Pro AI, Base Data, Pro Data and Custom plans  [default: no-extra-snippets]
* `--dump-response / --no-dump-response`: Dump the raw response from the API into a file (response.json in current working directory)  [default: no-dump-response]
* `--help`: Show this message and exit.
