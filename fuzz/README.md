# Fuzzing of CredSweeper API

The directory is used for dynamic analysis with using [atheris](https://github.com/google/atheris),
based on [LibFuzzer](https://llvm.org/docs/LibFuzzer.html#options)


## Preparation

- The same interpreter packages as for the project + atheris.
Working dir is project root - to be sure current source of the project is used for coverage.

```bash
pip install atheris
```


## Fuzzing

Launch fuzzing script to collect corpus files.
```bash
./fuzzing.sh
```
Then after productive fuzzing there will be new seed files in fuzz/corpus or crashes in projects root.
Crashes look like "crash-{{sha1sum of content}}"
```bash
crash-61cec917cdcf9494178a9ef3655a41560ee73686
```
