## Uni Pad

> 🦄 Left pad a string with Unicorns

## Screenshot

<img src="https://gitlab.com/yoginth/unipad/raw/master/Screenshot.png" width="550">

## Install

```
$ pip install unipad
```

## Usage

```python
import unipad

unipad.pad('yoginth', 10)
#=> 🦄🦄🦄yoginth
```

## API

### unipad.pad(input, length)

Pads `input` with unicorns on the left side if it's shorter than `length`. Padding unicorns are truncated if they exceed `length`.

#### input

Type: `string`

String to pad.

#### length

Type: `number`<br>
Default: `0`

Padding length.

## Get Help

There are few ways to get help:

 1. Please [post questions on Stack Overflow](https://stackoverflow.com/questions/ask). You can open issues with questions, as long you add a link to your Stack Overflow question.

 2. For bug reports and feature requests, open issues.

 3. For direct and quick help, you can [email me](mailto://yoginth@zoho.com).

## How to contribute

Have an idea? Found a bug? See [how to contribute][contributing].

Thanks!

## License

[MIT][license]

[LICENSE]: https://yoginth.mit-license.org/
[contributing]: /CONTRIBUTING.md
