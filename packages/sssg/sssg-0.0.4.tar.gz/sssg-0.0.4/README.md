# Simple SSG

This is a very simple static site generator. It was made for one purpose alone: to decouple a static sites content from its document structure.

## Install 
To install the package run the following command:

```
pip install sssg
```

## Use
Before running, you should create a ```pages.json``` file, and all template and content files references in it. Below is an example of how a directory structure might look.

```
├── pages.json
├── templates
|   ├── home.html
|   ├── ...
└── content
    ├── title.txt
    ├── ...
```
By default the path of the ```pages.json``` is named as such and located in the root directory. The base template and content directory are also as above, but all three can be configured with command line arguments. To see the list of arguments run the following command.

```
python -m sssg -h
```

Your ```pages.json``` file contents may look something like this:
```
[
    {
        "template": "./home.html",
        "target": "./index.html",
        "content": {
            "title": "./title.txt"
        }
    }
]
```
For the example lets say your ```/templates/home.html``` file contents looks like this:

```html

<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
</body>
</html>
```

And lets say your ```/content/title.txt``` looks like this:
```
Test Title
```

Now run the following command:

```
python -m sssg
```
This will generate your static files, which will look like this:

```
...
└── static
    ├── index.html
    ├── ...
```

Where the contents of ```index.html``` is:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Test Title</title>
</head>
<body>
    <h1>Test Title</h1>
</body>
</html>
```

I hope this explains the basics of how to use ```sssg```.