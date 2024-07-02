# `scrapy-playwright` sample project for Scrapy Cloud

Running [`scrapy-playwright`](https://github.com/elacuesta/scrapy-playwright)
on [Zyte Scrapy Cloud](https://www.zyte.com/scrapy-cloud/).


### Dockerfile

A [Dockerfile](Dockerfile) is provided to build a custom docker image. To keep the
resulting image small, only the `chromium` browser is installed by default.


### Build and deploy

* Make sure you have [`shub`](https://shub.readthedocs.io/en/stable/index.html) installed
* Replace the project id (`project: <project-id>`) in the `scrapinghub.yml` file with your own project id
* Run `shub image upload` to build the image and push it to the registry
* Run `shub schedule headers` to schedule a job for the "headers" spider

For more information, check out the [full documentation](https://shub.readthedocs.io/en/stable/deploy-custom-image.html)
on how to build and deploy Docker images to Scrapy Cloud.
