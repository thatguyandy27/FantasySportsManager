# -*- coding: utf-8 *-*
from yahoo.YahooAuth import yahooSessionManager


def main():
    sessionMgr = yahooSessionManager(
        'key',
        'secret',
        'yahoo')

    print sessionMgr


if __name__ == "__main__":
    main()
