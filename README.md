# polymer-highlander

This is a helper-script making it possible to use js-polymer-elements in dart-polymer. The problem is that elements fetched as bower-dependencies depend on the javascript-version of polymer which doesn't plan well with the dart-version. The `highlander.py`-script searches for references to javascript-polymer and changes them to dart-polymer. If you use the `polymer_elements` pub-package, the script also searches for references to paper-, iron-, etc. elements and replaces the reference with the polymer-versions to prevent multiple registration of the same element.

## Usage

The easiest way to use this script is to embed it as a post-install script in your bower-configuration file `.bowerrc`:
```js
{
    "scripts": {
        "postinstall": "python web/bower_components/polymer-highlander/highlander.py"
    },
    "directory": "web/bower_components"
}
```

In your `bower.json`, `polymer-highlander` should be listed as dev-dependency:
```js
  //...
  "dependencies": {
    //...
  },
  "devDependencies": {
    "polymer-highlander": "0.0.1"
  }
}
```

Note: The directory-structure of your project is important for this to work. It should follow the standard pub-layout:
```
/
-packages
-web/
  bower_components/
  something.dart
  something.html
-.bowerrc
-bower.json
-pubspec.yaml
```