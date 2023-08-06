# Usage

`unid` is a Python module for unique ID generation. We always make sure that `unid` stays Pythonic and true to the Python language. Below are a few examples to learn how to generate IDs.

```
>>> import unid
>>> manager = unid.IDGenerator()
>>> manager.new
0
>>> manager.new
1
>>> manager.new
2
```

For more information and usage for ID generation, visit the [documentation](https://unid.readthedocs.io/en/latest/index.html), hosted by [Read The Docs](https://readthedocs.io).

As of this release, we have not yet compiled a full API. This will hopefully come out in the next few days after the first stable release. Thank your for your patience.

# Bugs and Issue Reports

If you experience an issue or bug while using `unid`, feel free to report it on [Github](https://github.com/jcov28/unid/issues). We will try to get the issue fixed soon and in a future version.

# Compatibility

Although this has only been tested on MacOSX (Monterey 12.6), we can assume it will work on other operating systems. Below is a compatibility chart for `unid`.

|      | Windows | MacOSX   | Linux |
| :--: |  :---:  | :------: | :---: |
| 3.11 | ?       | Verified | ?     |
| 3.10 | ?       | ?        | ?     |
| 3.9  | ?       | ?        | ?     |
| 3.8  | ?       | ?        | ?     |
| 3.7  | ?       | ?        | ?     |
