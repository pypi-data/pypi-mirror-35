### Mastocount

Mastocount takes several [Mastodon](https://joinmastodon.org) accounts credentials, retrieve the number of followers of these accounts and print detailed numbers and the total number.
For the full documentation, [read it online](https://mastocount.readthedocs.org/en/latest/).

If you would like, you can [support the development of this project on Liberapay](https://liberapay.com/carlchenet/).
Alternatively you can donate cryptocurrencies:

- BTC: 1A7Uj24MpoEkzywPtmPffNvC7SfF4EiWEL
- XMR: 43GGv8KzVhxehv832FWPTF7FSVuWjuBarFd17QP163uxMaFyoqwmDf1aiRtS5jWgCiRsi73yqedNJJ6V1La2joznKHGAhDi

### Quick Install

* Install Mastocount from PyPI

        # pip3 install mastocount

* Install Mastocount from sources
  *(see the installation guide for full details)
  [Installation Guide](http://mastocount.readthedocs.org/en/latest/install.html)*


        # tar zxvf mastocount-0.3.tar.gz
        # cd mastocount
        # python3 setup.py install
        # # or
        # python3 setup.py install --install-scripts=/usr/bin

### Create the authorization for the Mastocount app

* Just launch the following command::

        $ register_mastocount_app

### Use Mastocount

* Create or modify mastocount.ini file in order to configure mastocount:

    [linuxjobsfr@linuxjobs.social]
    user_credentials=/etc/mastocount/credentials/linuxjobsfr_usercred.txt
    client_credentials=/etc/mastocount/credentials/linuxjobsfr_clientcred.txt
    
    [linuxjobsfr_dev@linuxjobs.social]
    user_credentials=/etc/mastocount/credentials/linuxjobsfr_dev_usercred.txt
    client_credentials=/etc/mastocount/credentials/linuxjobsfr_dev_clientcred.txt
    
    [linuxjobsfr_devops@linuxjobs.social]
    user_credentials=/etc/mastocount/credentials/linuxjobsfr_devops_usercred.txt
    client_credentials=/etc/mastocount/credentials/linuxjobsfr_devops_clientcred.txt

* Launch Mastocount

        $ mastocount -c /path/to/mastocount.ini

### Authors

* Carl Chenet <chaica@ohmytux.com>

### License

This software comes under the terms of the GPLv3+.
