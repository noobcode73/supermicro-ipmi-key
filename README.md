# supermicro-ipmi-key

This is a script to easily generate keys for the supermicro IPMI interface, based on [the documentation published by Peter Kleissner](https://peterkleissner.com/2018/05/27/reverse-engineering-supermicro-ipmi/ "the documentation published by Peter Kleissner").


To generate a key, simply take the MAC address from the IPMI card (case doesn’t matter), pass it as argument to the script, and paste the resulting key piece by piece into the activation web form:

    # python3 supermicro-ipmi-key.py AA:BB:CC:DD:EE:FF
