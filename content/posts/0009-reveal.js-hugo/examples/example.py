#!/usr/bin/env python3

import argparse
import logging

def configureLogging():
    """Konfiguruje log."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log', default='INFO')
    args = parser.parse_args()
    debugLevel = getattr(logging, args.log.upper(), None)
    if not isinstance(debugLevel, int):
        raise ValueError(f'Invalid log level: {debugLevel}')
    logging.basicConfig(
            format='%(asctime)s %(name)s:%(levelname)s:%(message)s',
            datefmt='%H:%M:%S',
            level=debugLevel)

def main():
    """Uruchamia przykład logowania."""
    configureLogging()
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')

if __name__ == "__main__":
    main()
