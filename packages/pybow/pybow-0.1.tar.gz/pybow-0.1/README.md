# pybow

pybow is a Python library collecting calculation methods related to archery.

## Purpose

pybow aims to (eventually) be a comprehensive collection of tools for archaeologists, data scientists, and maths-headed archery and bowyery enthusiasts.

To this end, pybow provides the `pb.Bow` object as a convenient way to describe bows by their measurements and bundled metadata, as well as implementations of analysis methods from scientific literature for easy reuse.

Eventually, the collection of methods shall be expanded, and complemented by tools helping in bow construction.

### Implemented Methods and Tools

* Analysis method of Beckhoff, from Beckhoff, K 1964, ‘Der Eibenbogen von Vrees’, Die Kunde N.F. 15 pp. 113–125
* Analysis method of Junkmanns, from Junkmanns, J 2013, *Pfeil und Bogen*, Verlag Angelike Hörnig, Ludwigshafen.

## Code & Installation

pybow’s source code is hosted at this Gitlab repo:
https://gitlab.com/gekitsu/pybow

Installation from PyPi via pip:

```sh
$ pip install pybow
```

## Dependencies

pybow has the following dependencies:

* `numpy`
* `pandas`
* `ruamel.yaml`

## Documentation

pybow documentation is hosted on readthedocs:
https://pybow.readthedocs.io/

## Changelog

* 0.1.0: Initial release.
	* the `pb.Bow` object for describing bows in Python
	* analysis methods: `beckhoff1964()` & `junkmanns2013()`
