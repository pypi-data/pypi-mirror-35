[![Build Status](https://travis-ci.org/iranianpep/iautomate.svg?branch=master)](https://travis-ci.org/iranianpep/iautomate)
[![codecov](https://codecov.io/gh/iranianpep/iautomate/branch/master/graph/badge.svg)](https://codecov.io/gh/iranianpep/iautomate)

0. Change the user to sudo
```
sudo su
```

1. Run the following command to install `pip` and `iautomate`
```
sh bootstrap.sh
```

2. Upload `index.php` and `sample-configuration.json`

3. Finally run:
```
iautomate sample-config.json
```