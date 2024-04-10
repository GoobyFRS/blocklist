#!/usr/bin/env python3
"""
Run this script to add all domains from Pi-Hole Common Blacklist. Found here: https://discourse.pi-hole.net/t/commonly-blacklisted-domains/305
"""
import os
print("*** Adding Common Blacklists to Pi-Hole Now ***")

domains = ["adsassets.waze.com", "api.mixpanel.com", "spade.twitch.com", "pubads.g.doubleclick.net", "sb.scorecardresearch.com", "ad.pandora.tv", "ads.pandora.tv.net", "stats.pandora.com", "adserver.pandora.com", "wsp.mgid.com", "s0.2mdn.net", "vsp-alexa-eu.amazon.com", "api.ad.xiaomi.com", "api.admob.xiaomi.com", "api.d.xiaomi.com", "a.stat.xiaomi.com", "tracking.miui.com", "cdn.ad.xiaomi.com", "data.mistat.xiaomi.com", "e.ad.xiaomi.com", "globalapi.ad.xiaomi.com", "new.api.ad.xiaomi.com", "sdkconfig.ad.xiaomi.com", "ssp.ad.xiaomi.com", "test.ad.xiaomi.com", "test.e.ad.xiaomi.com", "test.new.api.ad.xiaomi.com", "cc.sys.intl.xiaomi.com", "cc.sys.miui.com", "ccc.sys.miui.com", "ccc.sys.intl.xiaomi.com", "adv.sec.miui.com", "geofence.sys.miui.com", "abtest.mistat.xiaomi.com", "logupdate.avlyun.sec.miui.com", "mazu.sec.miui.com", "feedback.miui.com", "data.sec.miui.com", "data.mistat.intl.xiaomi.com", "tyler.logs.roku.com", "giga.logs.roku.com", "cooper.logs.roku.com", "msmetrics.ws.sonos.com", "coin-hive.com", "www.coin-hive.com", "cdn.m-pathy.com", "click-de.plista.com", "farm-de.plista.com", "static-de.plista.com", "www.plista.com", "plista.com", "click.plista.com"]

for domain in domains:
	os.system("pihole -b " + domain)
	#
print("*** Blacklisting Completed - Updating Gravity Now ***")
os.system("pihole -g")
print("*** Gravity Updated - Blacklists are applied ***")