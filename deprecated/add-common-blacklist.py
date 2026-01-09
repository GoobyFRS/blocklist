#!/usr/bin/env python3
"""
Script to add all domains from a blacklist to Pi-Hole.
Blacklist source: https://discourse.pi-hole.net/t/commonly-blacklisted-domains/305
"""

import subprocess

# Define the blacklist domains
BLACKLIST_DOMAINS = [
    "adsassets.waze.com", "api.mixpanel.com", "spade.twitch.com", 
    "pubads.g.doubleclick.net", "sb.scorecardresearch.com", 
    "ad.pandora.tv", "ads.pandora.tv.net", "stats.pandora.com", 
    "adserver.pandora.com", "wsp.mgid.com", "s0.2mdn.net", 
    "vsp-alexa-eu.amazon.com", "api.ad.xiaomi.com", 
    "api.admob.xiaomi.com", "api.d.xiaomi.com", 
    "a.stat.xiaomi.com", "tracking.miui.com", "cdn.ad.xiaomi.com", 
    "data.mistat.xiaomi.com", "e.ad.xiaomi.com", 
    "globalapi.ad.xiaomi.com", "new.api.ad.xiaomi.com", 
    "sdkconfig.ad.xiaomi.com", "ssp.ad.xiaomi.com", 
    "test.ad.xiaomi.com", "test.e.ad.xiaomi.com", 
    "test.new.api.ad.xiaomi.com", "cc.sys.intl.xiaomi.com", 
    "cc.sys.miui.com", "ccc.sys.miui.com", 
    "ccc.sys.intl.xiaomi.com", "adv.sec.miui.com", 
    "geofence.sys.miui.com", "abtest.mistat.xiaomi.com", 
    "logupdate.avlyun.sec.miui.com", "mazu.sec.miui.com", 
    "feedback.miui.com", "data.sec.miui.com", 
    "data.mistat.intl.xiaomi.com", "tyler.logs.roku.com", 
    "giga.logs.roku.com", "cooper.logs.roku.com", 
    "msmetrics.ws.sonos.com", "coin-hive.com", 
    "www.coin-hive.com", "cdn.m-pathy.com", 
    "click-de.plista.com", "farm-de.plista.com", 
    "static-de.plista.com", "www.plista.com", "plista.com", 
    "click.plista.com"
]

def add_to_blacklist(domains):
    """Add domains to Pi-hole blacklist."""
    print("*** Adding Common Blacklists to Pi-Hole Now ***")
    for domain in domains:
        try:
            result = subprocess.run(
                ["pihole", "-b", domain], 
                capture_output=True, 
                text=True,
                check=True
            )
            print(f"Blacklisted: {domain}")
        except subprocess.CalledProcessError as e:
            print(f"Error adding {domain}: {e.stderr.strip()}")

def update_gravity():
    """Update Pi-hole's gravity."""
    print("*** Updating Gravity Now ***")
    try:
        result = subprocess.run(
            ["pihole", "-g"], 
            capture_output=True, 
            text=True, 
            check=True
        )
        print("*** Gravity Updated - Blacklists are applied ***")
    except subprocess.CalledProcessError as e:
        print(f"Error updating gravity: {e.stderr.strip()}")

if __name__ == "__main__":
    add_to_blacklist(BLACKLIST_DOMAINS)
    update_gravity()
