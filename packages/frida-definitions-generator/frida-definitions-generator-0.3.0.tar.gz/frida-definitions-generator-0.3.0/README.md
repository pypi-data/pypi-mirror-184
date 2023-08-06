Frida Definitions Generator
===========================

Generate TypeScript definitions for a given APK file or unpacked APK directory.
The installation is simple through pip:

    $ python3 -m pip install frida-definitions-generator

After you've installed the program you should have an executable named
`frida-definitions-generator` that you can run like this:

    $ frida-definitions-generator --type java /path/to/apk > app.d.ts

This will output all the classes from the APK as Frida TypeScript definitions
into the piped file. You can also pass a directory of the unzipped APK instead
of the APK itself.
