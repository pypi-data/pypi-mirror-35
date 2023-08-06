# python-package-sandbox

If pip can find a local version, it will not go and download latest release. Not sure where that local version is, because even after deleting the directory in site-packages the behaviour continued.

Cannot use `pip3 install animals-math`.  

Instead, use `pip3 install --no-cache-dir --upgrade animals-math`
