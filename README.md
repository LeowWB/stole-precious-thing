# Comparison of translation services

## Introduction

Long story short, my task is to compare different translation services' quality of translation
between English, Mandarin, Malay, and Tamil. The domain will be job descriptions on a particular
Singaporean careers site.

The code here just represents an investigative probe. It's not meant to be used as an application
or a service. Don't use it as an application or a service.

## Dependencies

* python 3.8
* spacy
* requests
* ibm-watson

spacy and requests are available on conda, but ibm-watson needs pip. Suggest you use venv.

Also this spacy model, which can be installed by:
`python -m spacy download en_core_web_lg`

## APIs

We will interface with all the translation services through rapidapi. This offers us convenience
and (hopefully) low prices.

You're gonna need a json file, `keys.json`, in the repo's main directory. It should be a plain-old-
javascript-object, with the keys being the names of the various translation services (i.e. the
names of the python wrapper files). The values will be your own API key values - I'm
obviously not committing mine to this repo for the world to see.
